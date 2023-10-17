"""
Subsample daq.csv file from ~1000 Hz to frame rate.
Then add stim info to get a table with one row per imaging frame.
"""

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import tifffile
from tqdm import tqdm


class DaqFrameConverter:
    """Implements combination of daq and stim info to frame info."""
    def __init__(
            self,
            source_folder: Path,
            tif_file: Path,
            main_daq_trigger: str,
            start_offset: int = -1,
            end_offset: int = 0,
            flip_trigger: str = "counter",
            flip_columns_to_rename: dict | None = None,
            extra_daq_triggers: list | None = None,
    ) -> None:
        self.source_folder = source_folder
        self.tif_file = tif_file
        self.main_daq_trigger = main_daq_trigger
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.flip_trigger = flip_trigger
        self.flip_columns_to_rename = flip_columns_to_rename
        self.extra_daq_triggers = extra_daq_triggers

        self.daq_file = self.source_folder / "daq.csv"
        self.flip_file = self.source_folder / "flip_info.csv"
        assert self.daq_file.is_file()
        assert self.flip_file.is_file()
        assert self.tif_file.is_file()

        self.n_tif_frames: int | None = None

    def run(self) -> pd.DataFrame:
        """Main method to call."""
        self.n_tif_frames = self.read_n_tif_frames()

        daq_table = pd.read_csv(self.daq_file)
        flip_table = pd.read_csv(self.flip_file)

        if isinstance(self.flip_columns_to_rename, dict):
            flip_table = flip_table.rename(columns=self.flip_columns_to_rename)

        flip_table[self.flip_trigger] += self.start_offset
        daq_table[self.main_daq_trigger] += self.start_offset

        daq_table = self.subsample_daq(daq_table)
        self.check_triggers(daq_table)
        self.check_intervals(daq_table)
        frames = self.combine_triggers_and_stim(daq_table, flip_table)
        frames = self.clean_up(frames)
        n_frame_triggers = frames.shape[0]
        if n_frame_triggers == self.n_tif_frames:
            print(f"As many frame triggers as tif frames: {n_frame_triggers}")
        else:
            warnings.warn(f"{n_frame_triggers=} != {self.n_tif_frames}")
        return frames

    def combine_triggers_and_stim(self, daq_table: pd.DataFrame, flip_table: pd.DataFrame) -> pd.DataFrame:
        """Combine daq triggers and stim info."""
        last_trigger = daq_table[self.main_daq_trigger].max()
        frames = []
        for i_row, row in tqdm(daq_table.iterrows()):
            trigger_count = row[self.main_daq_trigger]
            if trigger_count < 0:
                print(f"Skipping {trigger_count}")
                continue
            elif (last_trigger - trigger_count) < self.end_offset:
                print(f"Skipping {trigger_count}")
                continue

            is_trigger = flip_table[self.flip_trigger] == trigger_count
            n_trigger = np.sum(is_trigger)

            this_frame = {
                "i_widefield_frame": trigger_count,
                "datetime": row["datetime"],
                "widefield_frame_interval": row[f"interval_{self.main_daq_trigger}"],
                "flip_info_available": n_trigger > 0,
            }
            if isinstance(self.extra_daq_triggers, list):
                for col in self.extra_daq_triggers:
                    this_frame[f"i_{col}"] = row[col]
            if n_trigger > 0:
                all_flips = flip_table.loc[is_trigger, :].to_dict(orient="records")
                first_flip = all_flips[0]
                this_frame.update(first_flip)
            frames.append(this_frame)
        frames = pd.DataFrame(frames)
        return frames

    def read_n_tif_frames(self) -> int:
        """Read number of frames from tif."""
        with tifffile.TiffFile(self.tif_file) as file:
            n_frames = len(file.pages)
        print(f"{n_frames} tif frames in {self.tif_file}")
        return n_frames

    def subsample_daq(self, daq_table: pd.DataFrame) -> pd.DataFrame:
        """Subsample daq """
        is_selected = daq_table[f"interval_{self.main_daq_trigger}"].notna()
        daq_table = daq_table.loc[is_selected, :].reset_index(drop=True)
        n_triggers = daq_table.shape[0]
        print(f"{n_triggers} triggers in daq table.")
        return daq_table

    def check_triggers(self, daq_table: pd.DataFrame) -> None:
        triggers = daq_table[self.main_daq_trigger].values
        possible = np.arange(np.min(triggers), np.max(triggers))
        is_registered = np.isin(possible, triggers)
        is_missed = np.logical_not(is_registered)
        missed = possible[is_missed]
        n_missed = missed.size
        if n_missed > 0:
            print(f"{n_missed} triggers not registered: {missed}")
        else:
            print("All triggers registered.")

    def check_intervals(self, daq_table: pd.DataFrame):
        all_intervals = daq_table[f"interval_{self.main_daq_trigger}"].values
        median_interval = np.median(all_intervals)
        min_interval = np.min(all_intervals)
        max_interval = np.max(all_intervals)
        frame_rate = 1 / median_interval
        print(f"Intervals: min={min_interval * 1000:.1f}ms, median={median_interval * 1000:.1f}ms, max={max_interval * 1000:.1f}ms")
        print(f"Frame rate: {frame_rate:.1f} Hz")

        for direction in [1, -1]:
            for i in range(5):
                if direction == -1 and i == 0:
                    continue
                row = daq_table.iloc[direction * i, :]
                trigger = row[self.main_daq_trigger]
                interval = row[f"interval_{self.main_daq_trigger}"]
                print(f"{trigger} -> {trigger + 1}: {interval * 1000:.1f} ms")

    def clean_up(self, frames: pd.DataFrame) -> pd.DataFrame:
        for col in frames.columns:
            if "Unnamed" in col:
                del frames[col]
        return frames