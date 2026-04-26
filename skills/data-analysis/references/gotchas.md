# Data-analysis gotchas

Use this reference when the input is messy, especially for Excel and schema cleanup.

## Excel gotchas

- The visible first row is often not the true header row.
- Workbooks may contain title rows, notes, merged cells, subtotal rows, or blank spacer columns.
- Formula cells may not reflect the values a user expects if the workbook was not recalculated before export.
- A workbook can contain multiple candidate tables; do not assume the first non-empty sheet is the right one.

## CSV gotchas

- CSV files with large text fields or mixed numeric/text columns can look smaller on disk than their in-memory footprint.
- Delimiters, quoting, and null-like tokens can change type inference substantially.
- Duplicate headers and trailing delimiters should be surfaced explicitly.

## Parquet gotchas

- Existing Parquet is often already the optimal interchange format; avoid pointless rewrites.
- Rewriting Parquet can destroy helpful physical properties if partitioning, ordering, or row group sizing was already intentional.

## Analysis gotchas

- A quick preview is not enough to justify a full in-memory load.
- Schema normalization should be logged so the user can trace renamed or coerced columns.
- If the data is ambiguous, prefer a conservative answer over a confident but lossy transformation.

