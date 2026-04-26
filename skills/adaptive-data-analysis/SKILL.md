---
name: adaptive-data-analysis
description: >
  Analyze structured local data files with a metadata-first, Parquet-first workflow.
  Use when the user wants to inspect, profile, clean, summarize, optimize, or convert
  CSV, Parquet, or Excel data. Prefer this skill when the dataset may require an
  explicit choice between in-memory, lazy, chunked, or out-of-core execution,
  especially for multi-sheet workbooks or large row-oriented files.
license: MIT
compatibility: Requires Python 3.11+ for bundled scripts and local file access for CSV, Parquet, and XLSX files.
metadata:
  author: Ravishankar Sivasubramaniam
  version: "0.2.0"
argument-hint: <file-or-directory> [analysis request]
allowed-tools: Bash
---

## When to use this skill

- Use for **structured local data** in **CSV**, **Parquet**, or **Excel (`.xlsx`)** form.
- Use when the user wants profiling, schema inspection, conversion to Parquet, aggregation, cleanup, or a concise analysis report.
- Do **not** use for PDFs, image-based tables, or general document extraction.

## Runtime and defaults

- Python 3.11+
- `pyarrow`
- `polars`
- `duckdb`
- `fastexcel`
- Default Parquet compression: **ZSTD level 3**
- Default Parquet row group size: **100,000**

## Supported inputs

### v1 supported

- `.csv`
- `.parquet`
- `.pq`
- `.xlsx`

### v1 deferred

- `.pdf`
- `.xls`
- `.xlsb`
- image-based tables
- semi-structured document extraction

## Progress checklist

- [ ] Resolve the input path and requested analysis
- [ ] Inspect metadata before expensive reads
- [ ] Choose the execution strategy explicitly
- [ ] Normalize to Parquet when appropriate
- [ ] Run the requested analysis
- [ ] Report findings, artifacts, and tradeoffs

## Core policy

1. **Inspect metadata first**
   - file format
   - file size
   - schema or sample rows
   - workbook sheet list and target sheet dimensions for Excel
   - estimated memory footprint
   - available RAM headroom when it can be determined safely
2. **Prefer Parquet-first normalization**
   - convert CSV and Excel inputs to Parquet early when the task goes beyond a trivial preview
3. **Keep the workflow Arrow-compatible**
   - use `pyarrow` as the interchange layer
4. **Use Polars for transform-heavy work**
   - schema cleanup
   - expression-heavy transforms
   - lazy scans
5. **Use DuckDB for SQL-heavy work**
   - joins
   - window functions
   - multi-file queries
   - out-of-core analytical SQL
6. **Avoid Pandas in the happy path**

## Gotchas

- Excel workbooks often contain decorative top rows; do not assume row 1 is the real header.
- Do not rewrite Parquet unless there is a concrete reason.
- Mixed numeric/text columns should stay conservative rather than forcing lossy casts.
- Formula-heavy spreadsheets may not behave like clean tabular exports.
- Duplicate headers and ragged rows must be surfaced, not silently normalized away.
- Multi-sheet workbooks often mix raw data tabs, summary tabs, and lookup tabs; do not assume the first non-empty sheet is the right analysis target.

## Available scripts

- `scripts/inspect_dataset.py` — emits structured metadata about a local dataset path, with CSV sampling support and JSON output.
- `scripts/render_report.py` — renders a Markdown analysis report from structured JSON fields.

## Execution strategy

### Parquet input

- Prefer direct lazy scans with Polars or direct DuckDB queries.
- Avoid rewriting Parquet unless the user requests repartitioning, recompression, cleanup, or schema normalization.

### CSV input

- If the estimated working set fits comfortably in memory, use Polars with projection and filtering before collection.
- If the file is large relative to RAM headroom, convert to Parquet first, then analyze the normalized output.

### Excel input

- Use `fastexcel` to inspect workbook metadata first.
- Summarize candidate sheets before choosing one for deeper processing.
- Prefer a raw, rectangular data tab over dashboard, chart, or summary tabs when the user asks for analysis.
- If multiple tabs look relevant, explain the candidate choices and either select the strongest one or ask for confirmation when ambiguity is material.
- Normalize the selected sheet to Parquet once and avoid repeated workbook reads.
- Only combine or join sheets when schemas align, a clear join key exists, or the user explicitly asks for cross-sheet analysis.
- Report which sheets were used, which were ignored, and why.
- Surface workbook limitations explicitly when formulas, merged cells, or irregular layouts affect reliability.

### Fallback behavior

- If metadata is insufficient to choose safely, begin with a bounded sample pass.
- Escalate to chunked or out-of-core execution instead of risking memory-heavy eager loads.

## Output contract

Each run should produce or report:

1. **Analysis summary**
   - dataset overview
   - chosen strategy and why it was selected
   - schema and data-quality observations
   - requested findings or aggregates
2. **Dataset meaning**
   - probable entity or business object represented by the file
   - likely meaning of key columns, measures, dimensions, and time fields
   - confidence level for semantic interpretation when meaning is inferred rather than explicit
3. **Questions this data can answer**
   - concrete examples of analyses supported by the detected schema
   - relevant cuts such as trend, segment, ranking, distribution, or join-ready identifiers
4. **Questions this data cannot answer yet**
   - important missing fields
   - ambiguities that block confident business interpretation
   - cases where the user must provide domain context
5. **Artifacts when requested**
   - normalized or cleaned Parquet output
   - optional schema report
   - optional profiling summary
6. **Transformation record**
    - renamed columns
    - coercions
    - dropped rows or skipped sheets
    - selected and ignored workbook tabs, when applicable
7. **Failure surface**
   - explicit unsupported-format or parse-error reporting

## Semantic interpretation policy

- Distinguish clearly between **observed structure**, **probable meaning**, and **unknowns**.
- Infer semantics from column names, value patterns, cardinality, temporal fields, and identifier-like columns, but do not present guesses as confirmed facts.
- Use confidence-oriented language such as "likely", "appears to", or "probably" when meaning is inferred.
- Call out where domain confirmation is needed, especially for measures like revenue, margin, status, or event semantics.
- Suggest useful next questions based on the schema that is actually present.
- Be explicit when the file is structurally understandable but semantically under-specified.

## Suggested workflow

1. Resolve the input path. If given a bare filename, resolve it from the working tree before processing.
2. Perform a metadata pass before expensive reads.
   - When useful, run:
     ```bash
     python3 scripts/inspect_dataset.py "$INPUT_PATH"
     ```
3. Choose one strategy explicitly:
   - in-memory
   - lazy
   - chunked conversion
   - DuckDB out-of-core SQL
4. For Excel, inspect all visible candidate sheets, summarize their likely role, and choose the primary analysis tab explicitly.
5. Normalize to Parquet when the input is CSV or Excel and the task is more than a quick preview.
6. Run analysis with Polars or DuckDB based on the requested work.
7. Add a semantic interpretation layer:
   - what the dataset appears to represent
   - what important fields likely mean
   - what questions are answerable from the available columns
   - what requires user confirmation
8. Report the strategy, findings, semantic interpretation, and any written artifacts.

When needed, load supporting material selectively:

- Read `references/gotchas.md` for Excel and schema edge cases.
- Read `references/schema-normalization.md` when cleaning or reconciling columns.
- Read `references/semantic-interpretation.md` when summarizing what the data likely means.
- Read `references/eval-matrix.md` when adding or checking eval coverage.
- Read `references/workbook-selection.md` when the input workbook has multiple candidate tabs.
- Use `assets/report-template.md` when the user wants a written analysis report.
- Use `snippets/metadata-pass.md` when inspecting files before choosing a strategy.
- Use `snippets/csv-to-parquet.py` or `snippets/excel-to-parquet.py` when normalizing row-oriented inputs.
- Use `snippets/duckdb-analysis.sql` for SQL-heavy aggregation patterns.
- Use `snippets/schema-normalization.py` when recording stable cleanup behavior.
- Use `snippets/semantic-summary.md` when writing the interpretation layer.
- Use `snippets/artifact-naming.md` when choosing output file names.
- Use `scripts/render_report.py` when you have structured output fields and need to write a Markdown report file consistently.

## Failure modes

- If required Python packages are missing, stop and instruct the user to install the documented runtime dependencies.
- If the workbook is unsupported or ambiguous, report the exact limitation.
- If schema inference is unreliable, say so explicitly and prefer a conservative conversion strategy.
- If output paths would overwrite meaningful data, require explicit confirmation first.
