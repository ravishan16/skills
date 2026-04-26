# Lean data platform gotchas

Use this reference when the user's request risks collapsing governance, tenancy, and report delivery into one vague layer.

## Architecture gotchas

- A browser query engine is not a substitute for trusted authorization.
- A managed catalog removes one class of server management, but it does not remove the need for careful data exposure boundaries.
- Custom domains and branding are part of the control plane; keep them out of raw dataset metadata.
- The write plane is separate from the edge control plane; do not leave ingestion ownership implied.

## Data gotchas

- Iceberg is excellent for governed tables, but browser-friendly report access may still need curated Parquet outputs or narrow exposure rules.
- Spreadsheet ingestion should be normalized early; do not build customer reporting on top of raw Excel semantics.
- Stable file naming and write settings help both caching and repeatable report behavior.

## Product gotchas

- White-labeling affects auth, routing, branding, and support workflows together; do not treat it as a CSS-only task.
- Zero egress and scale-to-zero are strong defaults, but they are not excuses to ignore governance, observability, or failure isolation.
- A component diagram is not production-ready if it omits tenant lifecycle, audit logs, or fallback behavior.
- Pricing and limits change; re-check current product docs before making cost promises.
