# Ingestion and write-plane reference

Use this reference when the user asks where ingestion runs, who owns Iceberg writes, or how raw files become curated datasets.

## Default stance

Keep ingestion outside the edge runtime unless the user explicitly wants something else.

## Default write plane

- a VM or instance
- possible homes include EC2, Google Cloud, Hetzner, or another host the team controls
- it runs the batch or event-driven pipeline that reads uploads, normalizes data, writes Parquet, and commits Iceberg metadata

## Responsibilities

- ingest Excel, CSV, or upstream Parquet feeds
- normalize schemas and write curated Parquet outputs
- commit Iceberg metadata changes
- run compaction, retention, and cleanup workflows
- emit job status and failure signals

## Ownership questions to answer

- which runtime performs writes
- where its credentials live
- how it is triggered
- what happens on partial failure
- who can rerun or backfill jobs

## Recommendation style

- keep the ingestion story pragmatic
- do not over-design orchestration if the user has not asked for it
- do not pretend the write plane is optional
