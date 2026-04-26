"""Canonical CSV -> Parquet normalization snippet for the data-analysis skill."""

from pathlib import Path

import polars as pl

input_path = Path("input.csv")
output_path = Path("input.cleaned.parquet")

lazy_frame = pl.scan_csv(input_path)

(
    lazy_frame
    .sink_parquet(
        output_path,
        compression="zstd",
        compression_level=3,
        row_group_size=100_000,
    )
)

print(output_path)

