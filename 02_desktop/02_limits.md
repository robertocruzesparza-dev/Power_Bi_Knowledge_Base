---
id: 02.limits
title: Desktop and publishing limits
domain: desktop
type: reference
level: intermediate
tags: [desktop, limits, semantic-model, troubleshooting]
summary: Verified size, row, column, query and refresh limits that affect Desktop files and what happens when you publish them.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S014, S015, S016, S017, S018, S019, S020, S034, S038, S039, S2500, S2501, S2502, S2504, S2505, S2507, S2508, S2509, S2557]
references: []
related: [02.file_formats, 02.desktop_vs_service]
---
## Purpose

Know the ceilings before you build. Limits differ by license and capacity. All values were read on 2026-10-07 and can change.

## Limits table

| Limit | Value | Source |
|---|---|---|
| Model size, shared capacity or Pro | 1 GB (compressed) | S015, S020 |
| Model size, PPU (service description) | 100 GB | S017 |
| Desktop upload of a model | 10 GB; large-format models can grow beyond on refresh in the service | S018 |
| Uncompressed data processed per refresh, shared capacity | 10 GB | S016 |
| Scheduled refresh timeout | 2 hours shared; 5 hours Premium | S016 |
| Scheduled refreshes before auto-disable | 4 consecutive failures | S016 |
| Refreshes per day | 8 Pro; 48 PPU and Premium | S017 |
| Distinct values per column (Import) | 1,999,999,997 | S015 |
| Columns per model (all tables) | 16,000 minus one per table | S015 |
| DirectQuery result rows | 1 million per query | S015 |
| Data sources per user (service) | 1,000 | S015 |
| Visual query timeout | 225 s shared and Premium; 600 s SSAS and AAS | S014 |
| Visual query memory | 1 GB shared; 10 GB Premium | S014 |
| Model view table display | Warning above 75 tables | S023 |
| Excel workbook upload | Under 1 GB | S038 |
| OneDrive and SharePoint file viewing | 1 GB | S039 |

Resolved 2026-10-08 (S2500, S2501, S2502, S2504): S017 and S018 do not conflict. The 1 GB default applies to the small storage format and to Pro workspaces. PPU lists 100 GB, and large storage format can be enabled for PPU. Per-capacity limits are 25 to 400 GB by SKU (F64 25 GB, F1024 400 GB). With the small format, a hard ceiling applies per SKU: F2 1 GB, F4 2 GB, F8 3 GB, F16 5 GB, F32 6 GB, F64 and larger 10 GB. Desktop upload stays at 10 GB. Queries on a workspace outside Premium have a 1 GB limit; DirectQuery in the service times out at 4 minutes.

## Publish problems and fixes

| Symptom | Likely cause | Fix (S020) |
|---|---|---|
| Error 400 Bad Request on publish | Pro user, model over 1 GB | Use PPU or Premium capacity, or shrink the model |
| Connection forcibly closed | Network | Try another network or VM; upload via OneDrive; shrink PBIX |
| Cannot publish to other workspace | Tenant setting "Use semantic models across workspaces" off | Ask admin |
| Cannot republish or replace | Tenant setting "Block republish and disable package refresh" on, or same-name live-connected report | Ask admin; rename |

Also: Import cannot be overwritten by DirectQuery or live-connect on republish, and the reverse for live connections (search result, S034).

## Download limits

Fact (S019): downloading a PBIX needs at least Contributor. Not downloadable: Direct Lake models, models with incremental refresh, models with automatic aggregations, and models migrated from Azure Analysis Services. Model size over 50 GB is not supported. Oversize items can be downloaded only as a live-connected report.

## Common mistakes

- Testing only in Desktop. Desktop applies no query limits unless simulated (S014).
- Relying on one table row-count: the DirectQuery cap is on query results, not table size (S015).

## Limits and version notes

- Volatile. Check Microsoft Learn limits pages and the licensing domain before capacity decisions.
- Fact: scheduled refresh limits are owned by the service domain.

## See also

- [Options and settings](02_options_and_settings.md)
- [File formats](02_file_formats.md)
- Licensing domain: ../13_licensing_pricing/
