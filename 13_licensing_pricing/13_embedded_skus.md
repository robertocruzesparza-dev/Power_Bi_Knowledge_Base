---
id: 13.embedded_skus
title: Embedded capacity SKUs (A, EM, F, P)
domain: licensing_pricing
type: comparison
level: intermediate
tags: [embedding, licensing, capacity]
summary: Compares A, EM, P and F SKUs for embedding, with billing terms, user license rules and A SKU hourly prices.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S1501, S1506, S1508, S1512, S2700, S2704]
references: []
related: [13.fabric_capacity_f_skus, 13.who_needs_which_license, 13.pricing_reference]
---
## Purpose

Embedding needs a capacity in production. This page shows which SKU families can embed and what each costs to run.

## Key facts

- Fact: Production embedding requires a capacity (A, EM, P or F). Free trial tokens are for development only [S1512].
- Fact: A SKUs bill hourly with no commitment and can be paused or scaled. EM bills monthly with a yearly commitment [S1512].
- Fact: EM1 and EM2 are sold only through volume licensing [S1508].
- Fact: F SKUs are not supported in the GCC environment. Only EM and P are available there. F SKUs work in GCC High and DoD [S1512].
- Fact: Embedded A SKUs and F SKUs below F64 need Pro or PPU for each viewer in the "for your organization" case [S1501].

## Comparison

| Family | Offer | Billing | Commitment | Secure URL embed |
|---|---|---|---|---|
| F | Azure | per second | none, reservation optional | yes |
| A | Azure | hourly | none | no |
| EM | Microsoft 365 | monthly | yearly | yes (per doc table) |
| P | Microsoft 365 | monthly | monthly or yearly | yes |

Source: S1512. P SKUs are being retired; see [P SKU retirement](13_premium_p_sku_retirement.md).

## A SKU hourly prices

West US 2, USD per hour, from the retail API on 2026-10-07 [S1506]:

| SKU | USD per hour | Equivalent F SKU |
|---|---|---|
| A1 | 1.0081 | F8 |
| A2 | 2.0081 | F16 |
| A3 | 4.0242 | F32 |
| A4 | 8.0565 | F64 |
| A5 | 16.121 | F128 |
| A6 | 32.2506 | F256 |

West Europe and Brazil South returned the same A SKU figures in USD [S1506]. A7 and A8 rows did not appear in the API for West US 2 on 2026-10-08, although Learn lists A7 and A8 as equivalents of F512 and F1024 (Unknown whether they are sold) [S2700, S2704]. Compare with F SKU hourly rates in [Pricing reference](13_pricing_reference.md): F8 at 0.18 USD per CU is 1.44 USD per hour, higher than A1 at list price (Inference from two sources).

## Steps to choose

1. App owns data for external customers: any of A, F, P or EM works. End users need no license [S1512].
2. Internal users in Teams or SharePoint: F64 or larger lets Free users view. Smaller SKUs need Pro or PPU per viewer [S1512].
3. Spiky or demo workloads: A SKU or F SKU with pause.
4. Need Fabric items too: F SKU only. EM and A support Power BI items only [S1501].

## Common mistakes

- Leaving an A SKU running overnight. Billing is hourly until paused [S1512].
- Assuming A SKUs change location after creation. Embedded capacity location cannot be changed; create a new one and reassign workspaces [S1526].

## Limits and version notes

Memory limits per SKU are in [Limits and quotas](13_limits_and_quotas.md). Service principals need Pro or PPU only for publishing through the UI; the import REST API works without them [S1512].

## See also

- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
