---
id: 09.semantic_model_refresh
title: Semantic model refresh, limits, and failures
domain: semantic_models_dataflows
type: reference
level: intermediate
tags: [semantic-model, refresh, limits, troubleshooting]
summary: Refresh types, daily schedule and time-out limits, failure rules, notifications, and the enhanced refresh REST API for semantic models.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1204, S1205, S1206, S1212, S1226, S2604]
references: [../references/semantic_models_dataflows/09_enhanced_refresh_parameters.md]
related: [09.large_semantic_models, 11.direct_lake]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [Refresh types](#refresh-types)
- [Limits table](#limits-table)
- [When refresh fails](#when-refresh-fails)
- [Enhanced refresh](#enhanced-refresh)
- [Common mistakes](#common-mistakes)
- [See also](#see-also)

## Purpose

Import models hold a copy of source data. Refresh reloads that copy. This file lists what Power BI allows, what stops a refresh, and how to control it.

## Key facts

- Fact: Shared capacity allows 8 scheduled refreshes per day. Premium, PPU, and Fabric capacity allow up to 48. The 8-count resets at 12:01 AM local time. [S1204]
- Fact: Manual Refresh now in the UI does not count toward the 8. [S1204]
- Fact: DirectQuery and live connections need no data refresh. Dashboard tiles refresh about hourly. [S1204]
- Fact: Refresh history shows two operations per attempt: Data, then Query Cache. If Data fails, Query Cache does not run. [S1204]
- Fact: Failure emails go to the owner by default. You can add more recipients, but they must be in your Microsoft Entra tenant. [S1204]

## Refresh types

| Type | What it does |
|---|---|
| Scheduled refresh | Runs at set times. Needs credentials and, for on-premises data, a gateway. |
| On-demand | Refresh now, API call, or Power Automate. API and Automate refreshes send no failure email. |
| OneDrive refresh | Syncs a PBIX, XLSX, or CSV from OneDrive or SharePoint Online. Not a source pull. |
| Query cache refresh | Premium only. Rebuilds cached results after data refresh. |
| Visual refresh | Reloads visuals in a report view. |

A data refresh in the service fails if a source column or table was renamed or removed. The service has no schema refresh for Import models. Fix it in Desktop and republish. [S1204]

## Limits table

| Limit | Value | Source |
|---|---|---|
| Scheduled refreshes per day, shared capacity | 8 | S1204 |
| Scheduled refreshes per day, Premium/PPU/Fabric | 48 | S1204 |
| Refresh time-out, shared capacity | 2 hours | S1204, S1206 |
| Refresh time-out, Premium workspace | 5 hours (XMLA can exceed) | S1204, S1206 |
| Uncompressed data per refresh, shared capacity | 10 GB | S1206 |
| Imported model size, Pro | 1 GB | S1206 |
| Consecutive failures before schedule is disabled | 4 (not configurable) | S1205, S1206 |
| Inactivity before schedule is paused | 2 months with no visits | S1204 |
| Enhanced refresh: total time incl. retries | 24 hours | S1212 |
| Enhanced refresh: default per-attempt time-out | 5 hours | S1212 |

## When refresh fails

1. Open Refresh, then Refresh history. Read the error and each retry.
2. Check the gateway status and Data source credentials.
3. If the schedule shows disabled, fix the cause, set the schedule slider On, and Apply. [S1205]
4. If paused for inactivity, open any report on the model or run Refresh now. [S1204]
5. A model with a scheduled subscription is not paused for inactivity. [S1226]

Expired cached credentials give "Access to the resource is forbidden". Clear the browser cache and sign in with the alwaysPromptForContentProviderCreds query option described in the Learn page. [S1206]

An Embedded capacity that is switched off fails the first refresh and disables the schedule at once. [S1206]

## Enhanced refresh

Enhanced refresh is a REST API mode for Premium, PPU, and Embedded models. It adds table and partition targets, batch commits, status polling, cancellation, and timeouts. It is async, so no long HTTP connection is needed. [S1212]

- Only one refresh runs per model at a time. A second request returns 400. [S1212]
- Scheduled or UI-started refreshes cannot be canceled or polled with this API. [S1212]
- Enhanced refresh does not refresh tile caches. They refresh when a user opens a report. [S1212]
- `partialBatch` commits objects one by one. A failure can leave the model empty or partial. Use `transactional` to keep prior data. [S1212]

Parameter details: [Enhanced refresh parameters](../references/semantic_models_dataflows/09_enhanced_refresh_parameters.md).

Direct Lake models use a different, light refresh called framing. See [Direct Lake](../11_fabric_onelake/11_direct_lake.md).

## Common mistakes

- Scheduling 48 refreshes with query caching on. Each refresh discards the cache.
- Expecting email when a refresh is started by API.
- Adding a failure-email recipient outside the tenant. External recipients are not supported. [S1204]

## See also

- [Large semantic models](09_large_semantic_models.md)
- [Dataflow Gen2 refresh and limits](09_dataflow_gen2_refresh_limits.md)
