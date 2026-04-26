# Artifact naming snippet

Use predictable output names so reruns stay understandable.

## Recommended suffixes

- cleaned parquet: `<stem>.cleaned.parquet`
- normalized parquet: `<stem>.normalized.parquet`
- profile summary: `<stem>.profile.json`
- analysis report: `<stem>.analysis.md`
- transformation log: `<stem>.transformation-record.json`

## Rules

- Do not overwrite the raw source unless explicitly asked.
- Keep derived outputs next to the source unless the user requests a dedicated artifacts directory.
- Reuse the same naming scheme across CSV, Parquet, and Excel workflows.
