---
id: 13.limits_and_quotas
title: Limits and quotas by license and SKU
domain: licensing_pricing
type: reference
level: intermediate
tags: [limits, capacity, licensing]
summary: Tables of per-user limits and per-SKU semantic model memory, refresh parallelism, DirectQuery and Direct Lake guardrails as of 2026-10-07.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1502, S1503, S1507, S1508, S1514, S2707, S2731]
references: []
related: [13.fabric_capacity_f_skus, 13.license_types_overview, 13.pricing_reference]
---
## Purpose

Limits decide whether a model fits and how many refreshes can run at once. All values below are from Microsoft Learn on 2026-10-07 unless marked.

## Per-user limits

| Limit | Pro | PPU |
|---|---|---|
| Model size | 1 GB | 100 GB |
| Scheduled refreshes per model per day | 8 | 48 |
| Native storage | 10 GB per license | 100 TB tenant total |
| Model refresh parallelism | n/a | 40 to 160 by license count |

Sources: S1502, S1503. Per-capacity limits follow.

## Per-SKU limits

Semantic model limits for F SKUs [S1508]. Max memory is per model, not cumulative.

| SKU | Max memory GB | Max DirectQuery connections | Model refresh parallelism | Max memory per query GB |
|---|---|---|---|---|
| F2 | 3 | 5 | 1 | 1 |
| F4 | 3 | 5 | 2 | 1 |
| F8 | 3 | 10 | 5 | 1 |
| F16 | 5 | 10 | 10 | 2 |
| F32 | 10 | 10 | 20 | 5 |
| F64 | 25 | 50 | 40 | 10 |
| F128 | 50 | 75 | 80 | 10 |
| F256 | 100 | 100 | 160 | 10 |
| F512 | 200 | 200 | 320 | 20 |
| F1024 | 400 | 200 | 640 | 40 |
| F2048 and up | 400 | 200 | 1,280 | 40 |

Direct Lake guardrails [S1508]: F2 to F32 allow 300 million rows per table; F64 allows 1,500 million; F128 3,000; F256 6,000; F512 12,000; F1024 and up 24,000 million. Maximum Direct Lake model size on OneLake is 10 GB (F2 to F8), 20 GB (F16), 40 GB (F32), and unlimited from F64.

## Dataflow tasks

Gen1 parallel tasks: 2 (F2, F4), 4 (F8), 8 (F16), 16 (F32), 32 (F64), 64 (F128 and up). Gen2: 96 up to F32, 384 for F64 to F256, 1,536 for F512 and up [S1508].

## PPU specifics

- Fact: PPU follows P3-equivalent size limits, with a 100 GB model cap [S1502].
- Fact: Export to file REST API is not supported for PPU. The paginated-report export call is limited to one per 5 minutes per user [S1502].
- Fact: Multi-Geo, unlimited distribution and Report Server rights are not in PPU [S1502].
- Fact: Moving a workspace from PPU to a non-PPU capacity needs a full refresh before use [S1502].

## Notes and caveats

- Memory must also cover refresh and queries, so the usable model size is below the cap [S1508].
- A visual that takes more than 225 seconds to render times out [S1508].
- F2048 and up are not in all regions [S1508].
- Azure CU quota per subscription and region applies when you create a capacity. An F64 needs 64 free CUs [S1514].
- Throttling and smoothing rules are covered in the performance domain.

## See also

- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
- [License types overview](13_license_types_overview.md)
