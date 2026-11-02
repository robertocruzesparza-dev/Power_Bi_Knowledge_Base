---
id: 13.premium_p_sku_retirement
title: Premium P SKU retirement and migration status
domain: licensing_pricing
type: reference
level: intermediate
tags: [licensing, capacity, migration]
summary: States the Power BI Premium per-capacity retirement rules, grace periods, P to F mapping and the safe migration order, as of 2026-10-07.
status: deprecated
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S1501, S1509, S1510, S1518, S2702, S2703, S2704, S3008, S3021]
references: []
related: [13.fabric_capacity_f_skus, 13.pricing_reference, 20.ssrs_rdl_to_power_bi]
---
## Purpose

Power BI Premium per-capacity SKUs (P1 to P5) are being retired. This page gives the rules so you can plan a move to F SKUs.

## Key facts

- Fact: Microsoft is retiring P SKUs at the end of each customer's current agreement term. Microsoft no longer sells new P SKUs [S1509].
- Fact: Customers with an active Enterprise Agreement (EA) can renew existing P capacity yearly until the EA term ends. Customers with expiring EAs or Microsoft Cloud Agreements cannot add or renew P capacity through the agreement. Migration is manual, not automatic at renewal [S1509, S2702, S2703].
- Fact: Pro and PPU are not affected. Only per-capacity SKUs retire [S1509].
- Fact (rechecked 2026-11-02): the Learn migration overview, decision guide and questions page still state the same rules: retirement at each agreement's end, 30-day grace, throttling from day 31, blocked from day 91, no automatic migration, no single final date, and sovereign clouds not yet affected [S3021].
- Fact: Sovereign clouds are not affected yet because Fabric is not available there [S1509].
- Unknown: a single final date for EA customers. Microsoft pages give no fixed date; rechecked 2026-10-09, and they tell customers to confirm terms with their account representative [S3008]. One consultancy cites 1 January 2028; this is unverified and third-party [S1518].
- History (2024 announcements, not repeated on current Learn pages): the non-EA renewal cutoff was reported as 2025-01-01, later 2025-02-01, and new purchases left the purchase flow on 2024-07-01. Current Learn pages no longer give separate EA and non-EA dates; they say each term ends at its agreement end [S1518, S2702]. A third-party site cites 2026-01-01 (non-EA) and 2028-01-01 (EA); neither is on Microsoft pages, so treat as unverified.

## Timeline after a P subscription ends

| Phase | Days after end | Effect |
|---|---|---|
| Grace | 1 to 30 | Capacity runs at current size at no charge |
| Throttled | 31 to 90 | Interactive operations are delayed; export still possible |
| Blocked | 91 onward | All operations rejected; data kept but inaccessible until moved or deleted |

Source: S1509. Microsoft says the grace period is a safety net, not a migration window [S1509].

## Mapping

| P SKU | F SKU | CUs |
|---|---|---|
| P1 | F64 | 64 |
| P2 | F128 | 128 |
| P3 | F256 | 256 |
| P4 | F512 | 512 |
| P5 | F1024 | 1,024 |

Source: S1509. This compares compute only. Right-size from Capacity Metrics app data and the Fabric SKU Estimator [S1509].

## Steps (safe order)

1. Buy the F SKU in the same Azure region as the P SKU.
2. Reassign all workspaces to the F SKU.
3. Validate reports, refreshes and subscriptions.
4. Cancel the P SKU last [S1509].

## What changes

- Purchase moves from the Microsoft 365 admin center to the Azure portal. Pricing moves from global to regional [S1509].
- Autoscale does not exist on F SKUs. Use manual resize and overage protection [S1509].
- Free users keep viewing on F64+ with a Viewer role, the same as on P [S1509].
- Report Server rights come with an F64+ reservation or SQL Server Enterprise with Software Assurance. Check before canceling P [S1509].

## Common mistakes

- Cancelling P before reassigning workspaces.
- Moving across regions without a backup plan. Large-format models and Fabric items do not survive a cross-region reassignment [S1509].

## See also

- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
- [Pricing reference](13_pricing_reference.md)
