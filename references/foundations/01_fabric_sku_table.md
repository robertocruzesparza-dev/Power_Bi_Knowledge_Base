---
id: 01.ref_fabric_sku_table
title: Fabric SKU to Power BI SKU comparison table
domain: foundations
type: reference
level: intermediate
tags: [licensing, capacity, reference, fabric, limits]
summary: Capacity units and Power BI v-core equivalents for each Fabric F SKU, with the P and A SKU mapping and the F64 viewing threshold.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S009, S026, S2526, S2502]
references: []
related: [01.licenses_and_capacity]
---
# Fabric SKU comparison (reference)

Fact (S009): capacity units (CU) measure compute. The table compares compute only, not functional or licensing equivalence.

| SKU | Capacity units | Power BI SKU | Power BI v-cores |
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
| F1024 | 1024 | P5/A8 | 128 |
| F2048 | 2048 | none | 256 |
| F4096 | 4096 | none | 512 |
| F8192 | 8192 | none | 1024 |

## Rules attached to the table

- Fact (S009): with F64 or larger, users with a Free license and the Viewer role can view Power BI content. Below F64, viewers need Pro, PPU, or an individual trial.
- Fact (S009): EM and A SKUs support only Power BI items. Power BI EM SKUs do not support Fabric.
- Fact (S009): the Fabric trial lasts 60 days and is sized like F64.
- Fact (S026): P SKUs retire at the end of the agreement term. After the term: 30 days grace, days 31 to 90 throttled, day 91 onward all operations rejected, data retained.
- Fact (S026): Enterprise Agreement customers can renew existing P capacity annually until the EA term ends; new P SKUs are not sold.
