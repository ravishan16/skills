# Semantic interpretation reference

Use this reference when the user wants to understand what a dataset represents, what the fields likely mean, or what business questions it can answer.

## Interpretation layers

Separate your explanation into three layers:

1. **Observed structure**
   - columns, types, null rates, uniqueness, date ranges, value distributions
2. **Probable meaning**
   - what the table likely represents
   - which columns look like identifiers, measures, dimensions, statuses, or timestamps
3. **Unknowns**
   - places where domain context is required before making a confident business claim

## Heuristics

- Treat columns ending in `_id`, `id`, `uuid`, or similar patterns as likely identifiers.
- Treat low-cardinality text columns as likely dimensions, categories, or statuses.
- Treat numeric columns with additive behavior as likely measures, but do not assume whether they represent revenue, quantity, cost, or score without evidence.
- Treat date or timestamp columns as analysis anchors for trends, recency, cohorts, or operational timing.
- Look for likely grain: one row per order, customer, event, invoice line, or daily aggregate.

## Questions the data can answer

When possible, identify likely answerable questions such as:

- trend over time
- top or bottom entities by a measure
- breakdown by region, segment, category, or status
- data quality questions like null concentration or duplicates
- joinability based on identifier-like fields

## Questions the data cannot answer yet

Call out missing pieces explicitly, for example:

- no clear time column for trend analysis
- no entity key for deduplication or joins
- no business definition for ambiguous measures
- no geography or category field for segmentation

## Tone

- Be pragmatic and specific.
- Prefer "this appears to be" over overconfident language.
- When unsure, ask for domain context instead of inventing meaning.

