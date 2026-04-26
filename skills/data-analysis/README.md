# data-analysis

High-performance structured-data analysis for **CSV**, **Parquet**, and **Excel (`.xlsx`)** using a metadata-first workflow.

## What this skill is for

Use this skill when you want an agent to:

- inspect a dataset before loading it deeply
- explain what the file contains
- infer what the data likely means, carefully
- convert CSV or Excel to optimized Parquet
- choose between in-memory, lazy, chunked, and out-of-core processing
- produce a concise analysis report plus machine-friendly outputs

## Supported inputs

- CSV
- Parquet
- Excel (`.xlsx`)

## Core stack

- `pyarrow`
- `polars`
- `duckdb`
- `fastexcel`

Default Parquet write settings:

- **ZSTD level 3**
- **row group size 100,000**

## Tips and tricks

1. **Ask for intent, not just mechanics**
   - Better: “Profile `sales.csv`, tell me what it represents, and what questions it can answer.”
   - Weaker: “Open this CSV.”

2. **Be explicit when you want outputs written**
   - Example: “Write a cleaned Parquet file and a Markdown analysis report.”

3. **Use it for semantic understanding too**
   - Example: “What does this dataset appear to represent, and what fields are likely identifiers vs measures?”

4. **Call out constraints**
   - Example: “I’m on a low-memory machine, avoid eager in-memory processing.”

5. **Ask for decision transparency**
   - Example: “Explain why you chose Polars vs DuckDB and whether the file should be normalized first.”

6. **Use the right file type expectation**
   - If the source is already good Parquet, ask whether it should stay as-is before rewriting it.

7. **Ask what the data cannot answer**
   - Example: “Tell me what business questions this file can answer and what still needs domain context.”

## Good prompt patterns

- `Analyze orders.xlsx, pick the correct sheet, and summarize what this data means.`
- `Convert events.csv to Parquet, profile null-heavy columns, and explain the chosen execution strategy.`
- `Inspect warehouse/orders.parquet and tell me if it should be rewritten or queried directly.`
- `Clean messy.xlsx, normalize headers, and write a cleaned Parquet plus a transformation record.`

## Practical guidance

- Prefer this skill for **structured local data**.
- Do **not** use it for PDFs or image-based table extraction.
- If the data is semantically ambiguous, the skill should infer carefully and say what needs confirmation.

## Where to look next

- Core behavior: `SKILL.md`
- Deep guidance: `references/`
- Report template: `assets/report-template.md`
- Reusable command/code patterns: `snippets/`
- Helper scripts: `scripts/`
