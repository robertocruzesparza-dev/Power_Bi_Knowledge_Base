---
id: 11.direct_lake
title: Direct Lake storage mode
domain: fabric_onelake
type: concept
level: intermediate
tags: [direct-lake, semantic-model, onelake, storage-mode, limits]
summary: How Direct Lake loads Delta columns into memory, framing, the two variants, licensing, and key limitations.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1203, S1238, S2600]
references: [../references/fabric_onelake/11_direct_lake_guardrails.md]
related: [11.direct_lake_fallback, 11.onelake, 09.semantic_model_refresh]
---
## Purpose

Direct Lake gives near-Import speed over very large Delta tables without copying them into the model. The VertiPaq engine loads needed columns from OneLake when queries ask for them.

## Key facts

- Fact: Import and Direct Lake queries run on VertiPaq. DirectQuery sends queries to the source instead. [S1203]
- Fact: A Direct Lake refresh copies metadata only, called framing. It often takes seconds. [S1203, S1238]
- Fact: Direct Lake needs a Fabric capacity (F SKU). Import and DirectQuery work with any license. [S1203]
- Fact: The docs say P SKUs are being retired and new deployments should use F SKUs. [S1203]
- Fact: Direct Lake tables cannot use a gateway. Only cloud connections work. [S1203]

## How it works

1. Transcoding: the first query that needs a column loads that whole column from Parquet into memory. It stays resident until evicted. [S1238]
2. Framing: a refresh reads the Delta log and points the model at the latest Parquet files. Queries then see data as of the last frame, not the live table. [S1238]
3. Eviction: framing, idle time, or memory pressure can drop columns. Incremental framing usually keeps dictionaries and adds new values. [S1238]
4. Automatic updates: the setting Keep your Direct Lake data up to date is on by default. It frames a table when its Delta data changes. It suspends after a non-recoverable error and resumes after a clean manual refresh. [S1238]

Turn automatic updates off when you need to finish an ETL job first. Then refresh by hand, on schedule, or by REST or TOM. [S1238]

## Two variants

| | Direct Lake on OneLake | Direct Lake on SQL analytics endpoint |
|---|---|---|
| Data sources | One or more Fabric items with Delta tables | One Fabric item |
| DirectQuery fallback | None (DirectLakeOnly) | Yes, controlled by a property |
| Composite with Import | Yes | No, in the same model |
| Calculated columns | Preview, user context only | No |
| SQL-level RLS or OLS | Not applied | Applied via fallback |
| Recommended for new models | Yes, per Microsoft | Existing models |

Source: S1203, S1238. Microsoft says Direct Lake on OneLake is the recommended option for new models. [S1238]

## Limits

Table guardrails scale by SKU. See [guardrails reference](../references/fabric_onelake/11_direct_lake_guardrails.md). Key points:

- Max model size on disk is a model-level guardrail. Other guardrails are per query. [S1203]
- Complex Delta types, binary, GUID, and NaN values are unsupported. String values cap at 32,764 characters. [S1203]
- One-side relationship columns must hold unique values or queries fail. [S1203]
- Cannot create Direct Lake models in My workspace. [S1203]
- Embedding needs a V2 embed token. Service principal use needs a fixed identity cloud connection. [S1203]
- XMLA tools need compatibility level 1604 or higher. [S1203]
- Source and model must be in the same region. [S1203]
- Semantic model RLS works, but Microsoft strongly recommends a fixed identity connection. [S1203]

Performance depends on tidy Delta tables: fewer, larger Parquet files and V-Order. [S1203]

## Common mistakes

- Expecting live data. Queries see the last frame.
- Skipping a refresh after creating tables with XMLA tools. They start unprocessed. [S1203]
- Mixing DirectQuery tables in a Direct Lake on SQL model.

## See also

- [Direct Lake fallback](11_direct_lake_fallback.md)
- [Semantic model refresh](../09_semantic_models_dataflows/09_semantic_model_refresh.md)
- [OneLake](11_onelake.md)
