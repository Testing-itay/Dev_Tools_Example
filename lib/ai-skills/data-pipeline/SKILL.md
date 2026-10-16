
---
name: Data Pipeline Designer
description: Designs ETL pipelines and data transformation workflows
---

# Data Pipeline Designer

## Purpose

Design robust ETL/ELT pipelines that reliably extract, transform, and load data across systems.

## Instructions

When designing data pipelines:

1. **Source Connectors** — Define extractors for databases (Postgres, MySQL), APIs (REST, GraphQL), and file systems (S3, GCS)
2. **Transformations** — Apply schema mapping, data type coercion, deduplication, and business rule validation
3. **Load Strategy** — Choose between full refresh, incremental (CDC), and append-only based on data volume and freshness needs
4. **Error Handling** — Implement dead-letter queues, retry policies, and data quality alerts
5. **Orchestration** — Use Airflow, Prefect, or Dagster DAGs with proper dependency management and SLAs

## Data Quality Gates

- Row count validation (expected vs actual)
- Schema drift detection
- Null percentage thresholds per column
- Freshness checks (max allowed staleness)
