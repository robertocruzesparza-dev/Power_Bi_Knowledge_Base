---
id: 11.fabric_capacity_and_licensing
title: Fabric capacity versus Power BI Premium
domain: fabric_onelake
type: reference
level: intermediate
tags: [fabric, capacity, licensing, comparison, limits]
summary: Fabric F SKUs, capacity units, Power BI Premium P SKU retirement, who needs which license, and the F64 viewer rule.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1241, S1208, S1209, S1203, S2619]
references: []
related: [11.capacity_throttling, 10.paginated_licensing_capacity, 09.large_semantic_models]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [SKU table](#sku-table)
- [License rules](#license-rules)
- [P SKU retirement](#p-sku-retirement)
- [Common mistakes](#common-mistakes)
- [See also](#see-also)

## Purpose

A capacity is a pool of compute for a tenant. Capacity units (CUs) measure it. Fabric sells it as F SKUs through Azure. Power BI Premium sold it as P SKUs, which are being retired.

## Key facts

- Fact: F SKUs are billed by Azure per second with a one-minute minimum, with optional yearly reservation. Pricing is regional. [S1241]
- Fact: P SKUs were available only to customers with an active Enterprise Agreement (EA). EM SKUs do not support Fabric. [S1241]
- Fact: You can pause an F capacity to stop billing and resize it. [S1208]
- Fact: Embedded scenarios work with any F SKU, so separate EM or A SKUs are not needed. [S1208]
- Unverified here: current prices. Check the Azure Fabric pricing page.

## SKU table

| SKU | CUs | Power BI equivalent | v-cores |
|---|---|---|---|
| F2 | 2 | none | 0.25 |
| F4 | 4 | none | 0.5 |
| F8 | 8 | EM/A1 | 1 |
| F16 | 16 | EM2/A2 | 2 |
| F32 | 32 | EM3/A3 | 4 |
| F64 | 64 | P1/A4 | 8 |
| Trial | 64 | none | 8 |
| F128 | 128 | P2/A5 | 16 |
| F256 | 256 | P3/A6 | 32 |
| F512 | 512 | P4/A7 | 64 |
| F1024 | 1,024 | P5/A8 | 128 |
| F2048 | 2,048 | none | 256 |

F4096 and F8192 also exist (4,096 and 8,192 CUs). Source: S1241. The table compares compute, not features or licensing.

## License rules

| Situation | Rule |
|---|---|
| View Power BI content with a Free license | Workspace on F64 or larger, or Premium P, with Viewer role |
| F SKU smaller than F64 | Each viewer needs Pro, Premium Per User (PPU), or an individual trial |
| Create Power BI items outside My workspace | Pro or PPU |
| Create non-Power BI Fabric items | F or trial capacity (or P with Fabric enabled); a Free license is enough |
| PPU alone | Does not give Fabric capacity or lakehouses |
| Fabric trial | 60 days, equal to F64 compute |
| Embed for customers (app owns data) | Any F, A/EM, or P; end users need no license |

Source: S1241. PPU suits fewer than 250 users needing Premium features (Microsoft guidance). [S1241]

## P SKU retirement

Fact: Microsoft is retiring Power BI Premium per-capacity (P) SKUs at the end of each customer's agreement term and no longer sells new ones. [S1208]

After a P subscription ends: [S1209]

1. Days 1 to 30: grace period, same size.
2. From day 31: interactive operations are throttled.
3. From day 91: all operations are rejected. Data is kept but inaccessible until workspaces move to an F capacity or the capacity is deleted.

EA customers with an active EA can renew existing P capacity annually until the EA ends. Expiring EA and Microsoft Cloud Agreement customers cannot add new P capacity. [S1208]

Not retired: Pro, PPU, and EM/A embedded SKUs. Sovereign clouds keep P SKUs for now. [S1208]

Large-format models and any Fabric item do not survive a cross-region workspace reassignment as is. Plan migrations in the same region. [S1209]

Direct Lake pages also tell new deployments to choose F SKUs. [S1203]

## Common mistakes

- Buying F32 and expecting Free viewers to work. They need F64.
- Treating a Premium P capacity as Fabric-enabled by default.
- Counting on P renewals without checking the agreement.

## See also

- [Capacity throttling](11_capacity_throttling.md)
- [Paginated licensing](../10_paginated_reports/10_paginated_licensing_capacity.md)
- [Large semantic models](../09_semantic_models_dataflows/09_large_semantic_models.md)
