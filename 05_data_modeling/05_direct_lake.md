---
id: 05.direct_lake
title: Direct Lake storage mode
domain: data_modeling
type: concept
level: intermediate
tags: [direct-lake, fabric, onelake, storage-mode, limits]
summary: Explains Direct Lake on OneLake versus on SQL analytics endpoints, framing, column loading, fallback, and the main limitations.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S611, S612, S613, S614, S2540, S2541, S2518]
references: [../references/data_modeling/05_direct_lake_guardrails.md]
related: [05.storage_modes, 05.composite_models]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [Two Direct Lake options](#two-direct-lake-options)
- [How it works](#how-it-works)
- [Fallback to DirectQuery](#fallback-to-directquery)
- [Limitations](#limitations)
- [Steps to keep a model healthy](#steps-to-keep-a-model-healthy)
- [See also](#see-also)

# Direct Lake storage mode

## Purpose
Direct Lake lets a semantic model read Delta tables in OneLake straight into memory, so it queries like Import without copying the whole data set.

## Key facts
- Fact: Direct Lake needs a Fabric capacity (F SKU or Premium). Import and DirectQuery work with any license (S611).
- Fact: The VertiPaq engine answers Direct Lake and Import queries. DirectQuery sends queries to the source (S611).
- Fact: A Direct Lake refresh is "framing". It reads Delta metadata and takes seconds. An Import refresh copies data (S611, S612).
- Fact: Only columns a query needs are loaded, so data volume can exceed the capacity memory limit (S611).
- Inference: It suits IT-built, lake-centric designs. Import often suits self-service analysts who cannot write to the lake (S611).

## Two Direct Lake options
| Aspect | Direct Lake on OneLake | Direct Lake on SQL endpoint |
|---|---|---|
| Sources | One or more Fabric items with Delta tables | One Fabric item with a SQL analytics endpoint |
| DirectQuery fallback | None | Yes, controlled by DirectLakeBehavior |
| Mix with Import tables | Yes (web modeling) | Not in the same model |
| Calculated columns | Supported, user context only (preview; calculated tables also preview) | No |
| SQL endpoint RLS | Not applied | Triggers fallback |
| Recommended for new models | Yes (S612) | Existing models |

Source support differs by item type. For example KQL databases and Cosmos DB in Fabric work only with Direct Lake on OneLake, and Snowflake only with the SQL endpoint option (S611).

## How it works
1. Column loading (transcoding): the first query that needs a column loads it from OneLake, merges dictionaries, and may build join indexes for relationships (S612, S613).
2. Resident columns stay in memory until evicted by refresh, inactivity, or memory pressure.
3. Framing: refresh sets a point-in-time baseline. Queries see Delta data as of the last successful framing, not necessarily the latest (S612).
4. Incremental framing drops only affected segments and usually keeps dictionaries (S612).
5. Temperature: cold (nothing loaded), semiwarm, warm, hot. Aim to warm up quickly (S613).

Performance drivers (S613): V-Order compression, correct data types (no integers stored as strings), large segments (about 1 to 16 million rows), low column cardinality, and no DirectQuery fallback.

## Fallback to DirectQuery
Applies only to the SQL endpoint option. Queries stay in Direct Lake mode only if all hold (S612):
1. No SQL RLS, dynamic data masking, or object-level security on the endpoint tables used.
2. No tables based on unmaterialized SQL views.
3. No table over guardrails (see [guardrail table](../references/data_modeling/05_direct_lake_guardrails.md)).
4. The model was framed after Delta tables changed.

Causes and fixes (S612): not framed, refresh; view, materialize it; guardrails, OPTIMIZE and VACUUM; memory pressure, reduce load or scale.

## Limitations (as of 2026-10-07)
- No complex Delta column types, binary, or GUID semantic types (S611).
- One-side relationship columns must be unique; queries fail on duplicates (S611).
- String values capped at 32,764 Unicode characters; NaN not supported (S611).
- No gateways; cloud connections only (S611).
- User-defined hierarchies on Direct Lake tables are not supported in Excel and other MDX clients (S611).
- Models cannot be created in My Workspace; cross-region creation is not supported (S611).
- No user-defined aggregations, hybrid tables, or model table partitions. Partition the Delta table instead (S611).
- Semantic model RLS works; a fixed-identity cloud connection is strongly recommended (S611).
- The doc says capabilities evolve rapidly. Re-check it before design decisions.

## Steps to keep a model healthy
1. Write gold tables with V-Order and compact files (S611 tip, S613).
2. Run OPTIMIZE and VACUUM after heavy loads.
3. Frame after each pipeline run, or enable automatic updates.
4. Test with Performance Analyzer for fallback and cold-load cost.

## See also
- [Storage modes](05_storage_modes.md)
- [Guardrails reference](../references/data_modeling/05_direct_lake_guardrails.md)
