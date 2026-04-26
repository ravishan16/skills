# Schema normalization reference

Use this reference when the task requires cleanup, reconciliation, or artifact writing.

## Column naming

- Trim whitespace around column names.
- Collapse repeated separators.
- Prefer stable, machine-friendly names.
- Disambiguate duplicates deterministically, and record the mapping.

## Types

- Parse timestamps and dates explicitly.
- Keep mixed numeric/text columns as string unless there is strong evidence the coercion is safe.
- Normalize null-like values consistently.

## Logging changes

When normalization occurs, record:

- original column name
- normalized column name
- type coercions
- dropped columns or skipped sheets
- any ambiguity that required a conservative choice

## Multi-source reconciliation

If multiple files or sheets are combined:

- describe which schema was treated as canonical
- document any widening or unioning of types
- surface conflicts instead of silently hiding them

