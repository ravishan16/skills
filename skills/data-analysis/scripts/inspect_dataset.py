#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect a local dataset path and emit structured metadata.",
        epilog=(
            "Examples:\n"
            "  python3 scripts/inspect_dataset.py data.csv\n"
            "  python3 scripts/inspect_dataset.py --sample-rows 3 input.csv\n"
            "  python3 scripts/inspect_dataset.py --format markdown report.parquet"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("input_path", help="Path to a local CSV, Parquet, or XLSX file")
    parser.add_argument(
        "--sample-rows",
        type=int,
        default=5,
        help="Number of CSV sample rows to include (default: 5)",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format for stdout (default: json)",
    )
    return parser


def inspect_csv(path: Path, sample_rows: int) -> dict[str, object]:
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        header = next(reader, [])
        rows = []
        for index, row in enumerate(reader):
            if index >= sample_rows:
                break
            rows.append(row)
    return {
        "header": header,
        "sample_rows": rows,
        "column_count": len(header),
    }


def inspect_path(path: Path, sample_rows: int) -> dict[str, object]:
    payload: dict[str, object] = {
        "path": str(path),
        "suffix": path.suffix.lower(),
        "size_bytes": path.stat().st_size,
        "exists": path.exists(),
    }

    suffix = path.suffix.lower()
    if suffix == ".csv":
        payload["csv"] = inspect_csv(path, sample_rows)
    elif suffix in {".parquet", ".pq"}:
        payload["note"] = "Parquet file detected; use Polars or DuckDB for deep schema inspection."
    elif suffix == ".xlsx":
        payload["note"] = "Excel file detected; inspect workbook metadata before deeper analysis."
    else:
        payload["note"] = "Unsupported extension for deep inspection; file-level metadata only."
    return payload


def render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Dataset inspection",
        "",
        f"- Path: `{payload['path']}`",
        f"- Suffix: `{payload['suffix']}`",
        f"- Size bytes: `{payload['size_bytes']}`",
    ]
    note = payload.get("note")
    if note:
        lines.append(f"- Note: {note}")
    csv_section = payload.get("csv")
    if isinstance(csv_section, dict):
        lines.extend(
            [
                "",
                "## CSV sample",
                "",
                f"- Column count: `{csv_section.get('column_count', 0)}`",
                f"- Header: `{csv_section.get('header', [])}`",
                f"- Sample rows: `{csv_section.get('sample_rows', [])}`",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    path = Path(args.input_path)

    if not path.exists():
        print(f"Error: input path not found: {path}", file=sys.stderr)
        return 3

    if not path.is_file():
        print(f"Error: input path is not a file: {path}", file=sys.stderr)
        return 4

    payload = inspect_path(path, args.sample_rows)

    if args.format == "markdown":
        print(render_markdown(payload))
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

