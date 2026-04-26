# lean-data-platform

Architecture guidance for a **lean analytics SaaS** built around **Cloudflare R2**, **Apache Iceberg**, **Workers**, **Pages**, **Supabase Auth**, and **Evidence.dev**.

## What this skill is for

Use this skill when you want an agent to:

- design a cost-optimized analytics platform with no always-on servers
- define a multi-tenant reporting architecture on Cloudflare
- separate governed Iceberg storage from browser-facing report delivery
- map a future path to MotherDuck or BigQuery without abandoning Parquet and Iceberg discipline

## Default platform shape

- **Storage:** Cloudflare R2
- **Table format:** Apache Iceberg on Parquet
- **Catalog:** R2 Data Catalog
- **Edge control plane:** Cloudflare Workers + KV
- **Ingestion/write plane:** external VM or instance running the data pipeline
- **Frontend/report delivery:** Cloudflare Pages hosting Evidence.dev in SPA mode
- **Identity:** Supabase Auth with JWT verification at the edge
- **White-labeling:** Cloudflare for SaaS plus Worker-driven tenant branding

## Design principles

1. **No-nonsense infrastructure**: prefer scale-to-zero services and avoid dedicated metadata or app servers when managed edge products suffice.
2. **Open storage contract**: keep data in Parquet and Iceberg so the platform can evolve without a lock-in rewrite.
3. **Zero-copy discipline**: move Excel and CSV inputs through Arrow-compatible tooling into Parquet with predictable write settings.
4. **Trusted tenant enforcement**: use Workers or another trusted execution layer for tenant-aware access decisions.
5. **Explicit exposure model**: define exactly how report-safe data reaches the browser instead of hand-waving "direct access."
6. **Graduated runtime strategy**: stay edge-first by default, then introduce MotherDuck or BigQuery only when workload shape demands it.

## Good prompt patterns

- `Design a white-labeled analytics SaaS on Cloudflare with Supabase Auth, R2, and Evidence.dev.`
- `Show me how to isolate tenants in an Iceberg lakehouse backed by R2 without adding a heavy control plane.`
- `Explain when this Cloudflare + DuckDB + Parquet stack should stay lean versus move to MotherDuck or BigQuery.`

## Where to look next

- Core behavior: `SKILL.md`
- Architecture details: `references/`
- Reusable handoff format: `assets/blueprint-template.md`
- Implementation patterns: `snippets/`
