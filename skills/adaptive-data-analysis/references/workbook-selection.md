# Workbook selection reference

Use this reference when an Excel workbook contains multiple tabs and the correct analysis target is not obvious.

## Goals

1. inspect all plausible tabs before deep processing
2. classify each tab as likely raw data, summary/dashboard, lookup/reference, or ambiguous
3. choose a primary analysis tab and explain why
4. report ignored tabs explicitly

## Heuristics

- Prefer rectangular tabs with consistent headers and row-wise records.
- Treat tabs with charts, merged cells, subtotal blocks, or dashboard-style layouts as summary views unless the user explicitly asks for them.
- Treat small dimension-like tabs with codes, labels, or mappings as lookups.
- Treat multiple similarly structured tabs as candidates for comparison or union only when their schemas align and the user asks for combined analysis.

## Reporting

For workbook inputs, report:

- the tabs inspected
- the likely role of each tab
- the selected primary tab
- ignored tabs and why they were not chosen
- any ambiguity that still needs confirmation
