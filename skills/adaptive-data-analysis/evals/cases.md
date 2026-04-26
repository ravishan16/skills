# Eval cases

## Case 1: Small CSV

- Prompt: Analyze `sales.csv` and summarize the top categories.
- Expectation: metadata pass -> in-memory or lazy path with clear justification.

## Case 2: Large CSV

- Prompt: Convert `events.csv` to Parquet and profile null-heavy columns.
- Expectation: chunked or staged normalization to Parquet before deeper analysis.

## Case 3: Existing Parquet

- Prompt: Inspect `warehouse/orders.parquet` and tell me whether it should be rewritten.
- Expectation: direct scan with no rewrite unless a concrete reason is identified.

## Case 4: Multi-sheet Excel

- Prompt: Analyze `finance.xlsx` and use the sheet that contains the transaction table.
- Expectation: workbook metadata inspection, explicit sheet-selection rationale, and a note about ignored summary or lookup tabs.

## Case 5: Dirty schema

- Prompt: Clean `messy.xlsx`, normalize headers, and write a cleaned Parquet file.
- Expectation: transformation record captures renamed columns, coercions, and skipped rows or sheets.

## Case 6: Low-memory scenario

- Prompt: Profile `huge.csv` on a constrained machine and avoid memory-heavy failures.
- Expectation: out-of-core or chunked path with an explanation of the tradeoff.

## Case 7: Workbook tab classification

- Prompt: Inspect `ops.xlsx`, summarize the workbook tabs, and tell me which tab looks like raw data versus summaries or lookups.
- Expectation: tab classification, primary-tab recommendation, and clear ambiguity reporting when multiple tabs look plausible.
