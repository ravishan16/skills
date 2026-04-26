"""Canonical Excel -> Parquet normalization snippet for the data-analysis skill."""

from pathlib import Path

import polars as pl

# Replace with the repo's tested Excel ingest path once runtime helpers are bundled.
input_path = Path("input.xlsx")
sheet_name = "Sheet1"
output_path = Path("input.cleaned.parquet")

frame = pl.read_excel(input_path, sheet_name=sheet_name)

frame.write_parquet(
    output_path,
    compression="zstd",
    compression_level=3,
    row_group_size=100_000,
)

print({"sheet": sheet_name, "output": str(output_path)})

