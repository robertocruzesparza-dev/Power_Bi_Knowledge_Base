---
id: 01.licenses_and_capacity
title: Licenses and capacity - concept level
domain: foundations
type: concept
level: beginner
tags: [licensing, capacity, power-bi, fabric]
summary: Explains Free, Pro, Premium Per User, and capacity licensing at concept level, with no prices; prices live in the licensing domain.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S007, S009, S017, S026, S2503, S2526, S2527, S2528]
references: [../references/foundations/01_fabric_sku_table.md]
related: [01.power_bi_and_fabric, 01.architecture]
---
## Purpose

You need two things to share Power BI content: a per-user license and, sometimes, a capacity. This file explains how they combine. Prices and exact quotas belong to the licensing domain.

## Key facts

- Fact: there are three per-user licenses: Fabric (Free), Power BI Pro, and Premium Per User (PPU) (S007).
- Fact: capacity licenses are Fabric F SKUs or Power BI Premium P SKUs (S007, S009).
- Fact: Premium Per User gives most Premium features to each licensed user. It does not provision a Fabric capacity (S009).
- Fact: the Power BI Premium per-capacity (P) SKUs are being retired at the end of each customer's agreement term. Pro and PPU are not affected (S026).

## Per-user licenses

| License | What it allows | Constraint |
|---|---|---|
| Free | Build for yourself in My workspace; view content shared in a capacity | Cannot share or publish to others' workspaces (S007) |
| Pro | Publish, share, subscribe, collaborate with other Pro users | Needed to create Power BI items outside My workspace (S009) |
| PPU | All Pro features plus most Premium features | Shares only with other PPU users unless content sits in a capacity (S007) |

## Capacity licenses

- Fact: F SKUs are bought in Azure. Billing is per second with a one-minute minimum, with an optional yearly reservation (S009).
- Fact: the F SKU names run F2 to F8192. F64 equals 64 capacity units and maps to Premium P1 (S009). See the [SKU table](../references/foundations/01_fabric_sku_table.md).
- Fact: a workspace type of PPU is not a Fabric capacity (S009).

## Who can view what

| Content location | Free viewer can view? | Source |
|---|---|---|
| Shared capacity (Pro workspace) | No, unless it is their own My workspace | S007 |
| F SKU below F64 | No; viewers need Pro, PPU, or trial | S009 |
| F64 or larger, or P SKU | Yes, with the Viewer role | S009 |
| PPU workspace | No; needs a PPU license | S007 |

## Common mistakes

- Assuming a Pro license lets you create lakehouses. Fabric items need an F or trial capacity (S009).
- Assuming F32 lets free users view reports. The threshold is F64 (S009).
- Buying PPU for a Fabric-wide rollout. PPU does not enable non-Power BI Fabric items (S009).

## Limits and version notes

- Volatile. Verify against the licensing domain and Microsoft Learn before buying. Prices vary by region (S009).
- Fact: the service description lists model size limit as 1 GB for Pro, 100 GB for PPU, and varies by capacity; refresh as 8 per day for Pro and 48 per day for PPU and Premium (S017). Re-verify before relying on these.
- Fact: Power BI Report Server is included with P SKUs and with F64 or larger reserved instances, not with smaller F SKUs (S013).

## See also

- [Power BI and Fabric](01_power_bi_and_fabric.md)
- [Report Server and deployment options](01_report_server_and_deployment_options.md)
- Licensing domain: ../13_licensing_pricing/
