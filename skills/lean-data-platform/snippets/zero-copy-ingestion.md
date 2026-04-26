# Zero-copy ingestion snippet

Use this pattern when describing the path from Excel or CSV into the lakehouse.

## Workflow

1. Read spreadsheet or CSV inputs with **Polars** using Arrow-friendly paths.
2. For Excel, prefer the **fastexcel** engine so sheet data reaches Arrow memory without unnecessary copies.
3. Normalize column names and basic schema issues before publishing derived artifacts.
4. Write **Parquet** with:
   - compression: **ZSTD level 3**
   - row group size: **100,000**
5. Register the resulting Parquet files in the Iceberg catalog with **PyIceberg** or another Iceberg-aware writer.
6. Use **DuckDB** for validation, joins, and analytical SQL over the curated data.
7. Expose only the report-safe read surface needed by downstream Evidence or tenant APIs.

## Why this matters

- Arrow-compatible flow reduces unnecessary copies
- Parquet keeps scans cheap and range-friendly
- Iceberg adds governed table semantics without abandoning open files
