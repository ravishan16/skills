# Operations and observability reference

Use this reference when the user asks whether the design is production-ready or how the platform should be operated safely.

## Minimum operational controls

1. **Tenant-aware request logging**
   - auth failures
   - hostname mismatches
   - forbidden report access attempts
2. **Ingestion job tracking**
   - start, success, failure, and retry status
   - dataset or table affected
3. **Iceberg maintenance**
   - snapshot retention
   - orphan cleanup
   - compaction or file-size hygiene
4. **Schema-change handling**
   - document how report breakage is detected
   - define who approves breaking schema changes
5. **Failure fallback**
   - what happens when catalog, domain mapping, or auth dependencies fail

## Rule

If the answer lacks observability and maintenance guidance, say the platform is not yet production-ready.

## What to return

- logs and audit events to keep
- maintenance jobs to schedule
- degraded modes and escalation points
