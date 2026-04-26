# Tenant isolation reference

Use this reference when the user asks how to keep multiple customers isolated in the same lean analytics platform.

## Preferred isolation model

1. **Logical storage separation**
   - Organize datasets by tenant-oriented namespaces, prefixes, or table boundaries.
   - Keep object paths predictable so data access policies and cleanup jobs stay simple.
2. **Trusted request context**
   - Extract tenant identity from a verified JWT or from a trusted hostname-to-tenant mapping.
   - Normalize tenant context in Workers before any data access decision is made.
3. **Report exposure**
   - Only expose report-specific Parquet or derived artifacts that match the requesting tenant's scope.
   - Do not assume the browser can safely enforce tenant filtering on its own.

## Shared-table caution

If a shared-table design uses a `tenant_id` column:

- require a trusted execution layer to apply tenant predicates
- keep the predicate logic consistent and auditable
- treat missing tenant filters as security issues, not convenience bugs

## Storage layout examples

- `r2://analytics/tenants/<tenant-id>/raw/...`
- `r2://analytics/tenants/<tenant-id>/curated/...`
- `r2://analytics/tenants/<tenant-id>/reports/...`

Or, when Iceberg namespaces are the main abstraction:

- `<tenant-id>.events`
- `<tenant-id>.orders`
- `<tenant-id>.finance`

## What to return

For tenant-isolation answers, name:

- where tenant boundaries live
- how tenant identity is derived
- where enforcement happens
- what happens for shared or cross-tenant data
