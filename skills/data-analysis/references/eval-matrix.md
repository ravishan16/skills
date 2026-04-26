# Eval matrix

Use this reference when adding evals or checking whether the skill still reflects its intended behavior.

## Core cases

1. small CSV that should stay in memory after metadata inspection
2. large CSV that should normalize to Parquet before deep analysis
3. existing Parquet that should be scanned directly without rewrite
4. multi-sheet Excel workbook where the correct sheet must be selected
5. dirty Excel headers that require schema normalization
6. low-memory scenario that should force chunked or out-of-core execution

## Assertions to check

- the skill explains **why** it chose the execution strategy
- Parquet is not rewritten without a reason
- Excel sheet selection is justified
- schema cleanup is recorded in the transformation output
- ambiguous data is surfaced explicitly instead of hidden
- the report distinguishes observed structure from inferred business meaning
- the report names answerable questions and important unanswered questions
