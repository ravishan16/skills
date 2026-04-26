# Metadata pass snippet

Use this before committing to an execution strategy.

## Inspect

- file path and format
- file size on disk
- rough row and column footprint
- header quality
- likely date, identifier, measure, and category columns
- workbook sheet names and used ranges for Excel
- whether the task needs only previewing or full analysis

## Decision framing

- If the input is already Parquet, prefer direct scan.
- If CSV or Excel is large relative to available memory, normalize to Parquet first.
- If the schema is ambiguous, do a bounded sample pass before deeper processing.

## Example command sketch

```bash
ls -lh "$INPUT"
python - <<'PY'
from pathlib import Path

path = Path("$INPUT")
print({"path": str(path), "suffix": path.suffix.lower(), "size_bytes": path.stat().st_size})
PY
```

