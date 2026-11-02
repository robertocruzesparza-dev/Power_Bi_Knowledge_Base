---
id: 13.fabric_capacity_f_skus
title: Fabric capacity F SKUs
domain: licensing_pricing
type: reference
level: intermediate
tags: [licensing, capacity, fabric]
summary: Lists all F SKUs with capacity units and Premium equivalents, and explains billing, pause, resize, reservation and purchase routes.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1501, S1508, S1514, S1515, S1516, S2705]
references: []
related: [13.pricing_reference, 13.limits_and_quotas, 13.premium_p_sku_retirement]
---
## Purpose

An F SKU is an Azure-billed Fabric capacity. It is the recommended capacity for Power BI and all Fabric workloads [S1501].

## Key facts

- Fact: F SKUs are bought in Azure and billed per second with a one-minute minimum. No commitment is needed [S1501].
- Fact: A yearly reservation lowers the rate. The reservation does not cover storage or networking [S1516].
- Fact: Capacity overage is an opt-in safety net, enabled by default on new F capacities. It bills excess CU hours at three times pay-as-you-go, up to a rolling 24-hour threshold, and is available only for F SKUs [S2705].
- Fact: Pricing is regional [S1501]. See [Pricing reference](13_pricing_reference.md).
- Fact: A capacity unit (CU) measures compute. One Premium v-core equals 8 CUs [S1509].

## SKU table

| SKU | CUs | Premium or A equivalent | v-cores |
|---|---|---|---|
| F2 | 2 | none | 0.25 |
| F4 | 4 | none | 0.5 |
| F8 | 8 | EM1 / A1 | 1 |
| F16 | 16 | EM2 / A2 | 2 |
| F32 | 32 | EM3 / A3 | 4 |
| F64 | 64 | P1 / A4 | 8 |
| F128 | 128 | P2 / A5 | 16 |
| F256 | 256 | P3 / A6 | 32 |
| F512 | 512 | P4 / A7 | 64 |
| F1024 | 1,024 | P5 / A8 | 128 |
| F2048 | 2,048 | none | 256 |
| F4096 | 4,096 | none | 512 |
| F8192 | 8,192 | none | 1,024 |

Source: S1501. The table compares compute, not features or licensing. F512 and larger are not available in every region [S1508].

## How it works

- Scale: resize manually in the Azure portal. There is no autoscale for F SKUs [S1509].
- Pause: pausing stops compute billing. OneLake storage billing continues [S1515]. Pausing also adds any remaining overage and smoothed usage to the bill [S1515].
- Governance: F SKUs add surge protection and capacity overage protection [S1509].
- Azure features: managed private endpoints, trusted workspace access, Azure Monitor and Cost Management [S1509].
- Report Server: included with an F64 or larger reservation [S1509].

## Steps to buy

1. Register the `Microsoft.Fabric` resource provider in the Azure subscription.
2. Check available CU quota for the SKU and region [S1514].
3. In the Azure portal, open Microsoft Fabric and select Create Fabric Capacity.
4. Choose subscription, resource group, name, region, size and a capacity admin from your tenant. B2B guests cannot be capacity admins [S1514].
5. Enable Fabric in the tenant, then assign workspaces to the capacity.

A Cloud Solution Provider (CSP) can also provision the capacity [S1514].

## Common mistakes

- Picking a region only for price. Data residency and latency matter too.
- Expecting a reservation to renew itself. Reservations do not renew automatically unless you set renewal [S1516].
- Believing pause removes all cost. Storage still bills [S1515].

## Limits and version notes

Cross-region workspace moves delete Fabric items and large-format models, so plan before you pick a region [S1509]. Per-SKU memory limits are in [Limits and quotas](13_limits_and_quotas.md).

## See also

- [Embedded A SKUs](13_embedded_skus.md)
- [Fabric trial](13_fabric_trial.md)
