# Reporting and white-label reference

Use this reference when the user asks about live report delivery, Evidence.dev, custom domains, or tenant branding.

## Evidence.dev SPA mode

- Treat Evidence.dev as the report UI layer, not the governance layer.
- In SPA mode, the browser can run DuckDB-Wasm queries over explicitly exposed Parquet files.
- Optimize those Parquet objects for range-friendly scans and predictable access paths.

## Important boundary

- **Iceberg** is the governed table contract.
- **Browser-facing Parquet** is the report-serving surface.

Keep that distinction explicit so report delivery stays simple without weakening data governance.

## Allowed exposure patterns

Choose one pattern explicitly in the answer:

1. **Signed object access**
   - a trusted service issues scoped, time-bound access to report artifacts
2. **Worker-mediated data API**
   - the browser calls a Worker that authorizes and serves only approved report data
3. **Tenant-scoped materialized artifacts**
   - curated report outputs are generated ahead of time for specific tenants and routes

If no explicit exposure pattern is chosen, the design is incomplete.

## White-label flow

1. Customer points `reports.customer.com` or similar to the platform.
2. Cloudflare for SaaS terminates TLS and routes the hostname.
3. A Worker maps hostname to tenant context.
4. The Worker injects or selects tenant-specific branding such as logo and colors.
5. The same trusted layer decides which report routes or artifacts the tenant can access.

## Branding inputs

- logo URL
- primary and secondary colors
- tenant display name
- optional theme tokens or CSS variables

## Report-surface guidance

- prefer curated, report-oriented datasets over raw tables
- avoid exposing internal-only tables directly to the browser
- call out when signed URLs, narrow prefixes, or a report API are needed
