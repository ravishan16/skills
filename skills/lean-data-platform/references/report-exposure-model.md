# Report exposure model reference

Use this reference when the user asks how reports safely access data from R2 or whether the browser can read Parquet directly.

## Rule

Do not leave the report-exposure model implied. Every answer should name exactly how report data becomes browser-visible.

## Preferred patterns

1. **Signed object access**
   - a trusted runtime issues time-bound access to tenant-scoped report artifacts
   - use when the browser should read static or semi-static outputs directly
2. **Worker-mediated data API**
   - the browser calls a Worker that authorizes the request and returns only approved report data
   - use when the platform needs tighter request-time control
3. **Tenant-scoped materialized artifacts**
   - the write plane precomputes report-ready Parquet or JSON outputs for each tenant
   - use when the UI should stay simple and predictable

## Non-goals

- do not expose raw internal prefixes directly to the browser
- do not treat "the frontend filters it" as a valid security pattern
- do not assume browser access to governed Iceberg tables is the safe default

## What to return

- which exposure pattern is used
- which datasets or prefixes are browser-visible
- which datasets are never exposed directly
- where authorization happens
