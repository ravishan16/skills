# Runtime evolution reference

Use this reference when the user asks whether the platform should stay lean or move to a larger runtime.

## Stay on the lean stack when

- report traffic is moderate
- scans are mostly bounded, cacheable, or Parquet-friendly
- most workloads are read-heavy dashboards or customer reports
- governance and freshness needs fit an edge-first model
- the team values low fixed cost and minimal operations over warehouse-style breadth

## Consider MotherDuck or BigQuery when

- concurrent interactive workloads rise beyond what browser- and edge-friendly scans can comfortably handle
- joins, window functions, or ad hoc exploration grow substantially more complex
- data freshness or orchestration demands exceed the simple ingestion pipeline
- governance, auditing, or access policy needs become warehouse-centric
- teams need a more centralized query surface for many internal consumers

## Upgrade signals to name explicitly

- browser-delivered scans are too large or too frequent to stay predictable
- report latency becomes unacceptable under concurrent tenant load
- per-tenant materialization becomes harder to manage than a centralized query runtime
- operational toil around refreshes, compaction, or query isolation starts dominating engineering time

## Migration discipline

- keep Parquet as the interchange format
- keep Iceberg or equivalent open metadata at the storage layer where feasible
- isolate report-facing contracts from backend query-engine choices
- upgrade selected workloads first instead of rewriting the whole platform

## Recommendation style

When advising on runtime evolution:

1. preserve the lean stack as the starting point unless the workload already disproves it
2. name the concrete upgrade trigger
3. describe what stays the same and what changes
