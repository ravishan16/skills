# Lean data platform blueprint

Use this reference when you need the default component map for the small-platform design.

## Baseline architecture

1. **Data lake**
   - Store raw and curated objects in **Cloudflare R2**.
   - Keep Parquet as the physical file format for analytical scans.
2. **Table contract**
   - Use **Apache Iceberg** for ACID table metadata, partition evolution, and schema changes.
   - Use **R2 Data Catalog** as the default metadata service when the goal is to avoid operating a separate catalog server.
3. **Edge control plane**
   - Use **Cloudflare Workers** for trusted request handling, JWT verification, tenant routing, signed access decisions, and lightweight API endpoints.
   - Use **KV** for low-friction control-plane data such as hostname-to-tenant mappings, theme settings, and feature flags.
4. **Write plane**
   - Run ingestion and table mutation outside the edge runtime on a VM or instance such as EC2, Google Cloud, Hetzner, or another host the team controls.
   - Let that runtime own Parquet generation, Iceberg commits, scheduled maintenance, and data backfills.
5. **Report delivery**
   - Host the frontend on **Cloudflare Pages**.
   - Use **Evidence.dev** in SPA mode for report UX when browser-delivered live queries are acceptable.
6. **Identity**
   - Use **Supabase Auth** for user identity, enterprise login support, and JWT issuance.

## Why this stack stays lean

- no dedicated warehouse is required for the first version
- no dedicated BI backend is required for read-heavy report delivery
- no dedicated metastore server is required when a managed catalog is available
- edge compute scales toward zero when requests are idle

## Recommended boundaries

- Keep **governed datasets** in Iceberg-backed storage.
- Expose **report-safe Parquet surfaces** to browser-driven analytics instead of giving the browser unrestricted access to internal tables.
- Put **auth and tenant enforcement** in Workers or another trusted layer.
- Make the **write plane** explicit so ingestion, maintenance, and secrets ownership are not left implicit.

## Minimal control-plane data

- tenant ID
- tenant hostname list
- brand settings such as logo URL and colors
- allowed dataset or report identifiers
- auth audience or project settings

## Deliverable language

When summarizing the design, separate:

- the **default architecture**
- the **operational assumptions**
- the **upgrade path**
