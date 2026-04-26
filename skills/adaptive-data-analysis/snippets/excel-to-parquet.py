"""Canonical Excel -> Parquet normalization snippet for the adaptive-data-analysis skill."""

from pathlib import Path

import fastexcel
import polars as pl

input_path = Path("input.xlsx")
sheet_name = "Sheet1"
output_path = Path("input.cleaned.parquet")

# Inspect workbook metadata first so tab selection is explicit.
reader = fastexcel.read_excel(input_path)
available_sheets = [sheet.name for sheet in reader.sheets]
if sheet_name not in available_sheets:
    raise ValueError(f"Sheet {sheet_name!r} not found. Available sheets: {available_sheets}")

frame = pl.read_excel(input_path, sheet_name=sheet_name)

frame.write_parquet(
    output_path,
    compression="zstd",
    compression_level=3,
    row_group_size=100_000,
)

print({"sheet": sheet_name, "available_sheets": available_sheets, "output": str(output_path)})
