#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <csv-file>" >&2
  exit 1
fi

CSV_FILE="$1"

if [[ ! -f "$CSV_FILE" ]]; then
  echo "CSV file not found: $CSV_FILE" >&2
  exit 1
fi

cat <<EOF
Benchmark scaffold for adaptive-data-analysis

Input: $CSV_FILE

Suggested comparisons:
1. template-style Pandas CSV load + summary
2. Polars lazy CSV scan + Parquet normalization
3. DuckDB scan over normalized Parquet

Track:
- wall-clock runtime
- peak memory
- output artifact size

This scaffold is intentionally lightweight until the repo grows a tested benchmark harness.
EOF
