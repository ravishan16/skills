-- Canonical DuckDB analysis snippet for normalized Parquet data.
-- Replace column names and predicates to match the actual dataset.

WITH base AS (
    SELECT *
    FROM read_parquet('input.cleaned.parquet')
),
scoped AS (
    SELECT *
    FROM base
    WHERE 1 = 1
)
SELECT
    category,
    COUNT(*) AS row_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM scoped
GROUP BY 1
ORDER BY total_amount DESC
LIMIT 20;

