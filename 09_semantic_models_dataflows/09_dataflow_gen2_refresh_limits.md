---
id: 09.dataflow_gen2_refresh_limits
title: Dataflow Gen2 refresh, incremental refresh, and limits
domain: semantic_models_dataflows
type: reference
level: intermediate
tags: [dataflow, refresh, incremental-refresh, limits, fabric]
summary: Refresh quotas, time limits, schedule pausing, incremental refresh rules, fast copy, and known issues for Dataflow Gen2.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1217, S1218, S1223, S1202, S1222, S1247, S2618]
references: []
related: [09.dataflows_gen1_vs_gen2, 11.lakehouse_vs_warehouse]
---
## Purpose

Use this page to size and troubleshoot Dataflow Gen2. All values are from Microsoft Learn on the retrieval date.

## Limits table

| Limit | Value |
|---|---|
| Refreshes per dataflow per 24-hour rolling window (CI/CD) | 300 |
| Same, non-CI/CD Gen2 | 150 |
| One query evaluation | 8 hours |
| Total time of one dataflow refresh | 24 hours |
| Staged queries plus queries with a destination, per dataflow | 50 |
| Incremental refresh buckets per query | 50 |
| Incremental refresh buckets per dataflow | 150 |
| Concurrent bucket evaluations, lakehouse destination | 10 |

Source: S1217, S1218. Burst traffic can also hit system throttling even below 300 per day. [S1218]

## Schedule pausing

Fact: If scheduled refreshes fail repeatedly, Gen2 pauses the schedule and emails the owner. Two rules apply: [S1218]

1. 100 percent failure over 72 hours with at least 6 refreshes.
2. 100 percent failure over 168 hours with at least 5 refreshes.

Gen1 and semantic models differ: they disable after 4 consecutive failures. See [Semantic model refresh](09_semantic_model_refresh.md).

## Incremental refresh

Incremental refresh reloads only recent buckets. In Gen2 it is set inside the editor. [S1217]

Requirements and rules:

- The destination must use a fixed schema, not dynamic. [S1217]
- The only update method is replace, applied per bucket. Older data outside the buckets is untouched. [S1217]
- You do not set a historical range. The dataflow adds filters and parameters as the last query step. [S1217]
- Other writers (such as Spark) on the same lakehouse table can break it. Table maintenance like OPTIMIZE or REORG is not supported on such tables. [S1217]
- Switching from non-incremental to incremental fails if destination data overlaps the buckets. Filter the first load to data older than the first bucket. [S1217]
- Gateways need version 3000.270 (May 2025) or newer for lakehouse destinations. [S1217]
- If it runs slower, enlarge the bucket size or switch to full refresh. [S1217]

Gen1 incremental refresh needs Premium, a DateTime filter column, and a partition cap of 50 per query and 150 per dataflow (stated on a Power Platform page). [S1222]

## Fast copy

Fast copy ingests large data in parallel on several cores. Billing uses total core time, not wall-clock time, so a quick run can still use meaningful compute. Limits: gateway 3000.214.2 or newer; fixed schema and schema-based destinations are not supported. [S1223]

## Known issues

- Intermittent timeouts through the Dataflows connector can surface as "The key didn't match any rows in the table". Data is not missing. Workaround: set a lakehouse or warehouse destination and read from it directly. [S1218]
- Refresh failing with "insufficient permissions for accessing staging artifacts" means the first dataflow creator has not signed in for 90 days or left. That person signs in, or open a support ticket. [S1218]
- After Git sync or a deployment pipeline, open and save the dataflow so it publishes, or call the on-demand publish job API. The Power Automate connector does not work with CI/CD Gen2. [S1247]
- Canceling a refresh keeps the last good staging data, but destination data written so far stays. [S1218]

## See also

- [Dataflows Gen1 versus Gen2](09_dataflows_gen1_vs_gen2.md)
- [Lakehouse versus warehouse](../11_fabric_onelake/11_lakehouse_vs_warehouse.md)
