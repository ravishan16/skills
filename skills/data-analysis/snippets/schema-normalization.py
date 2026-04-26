"""Schema normalization snippet with a simple transformation record."""

from __future__ import annotations

import json
from pathlib import Path

import polars as pl


def normalize_name(name: str) -> str:
    return "_".join(name.strip().lower().split())


input_path = Path("input.cleaned.parquet")
output_path = Path("input.normalized.parquet")
record_path = Path("input.transformation-record.json")

frame = pl.read_parquet(input_path)

mapping = {column: normalize_name(column) for column in frame.columns}
normalized = frame.rename(mapping)

normalized.write_parquet(
    output_path,
    compression="zstd",
    compression_level=3,
    row_group_size=100_000,
)

record_path.write_text(json.dumps({"renamed_columns": mapping}, indent=2))
print({"output": str(output_path), "record": str(record_path)})

