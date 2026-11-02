---
id: 13.fabric_trial
title: Fabric trial and individual trials
domain: licensing_pricing
type: how-to
level: beginner
tags: [licensing, fabric, capacity]
summary: How the 60-day Fabric trial capacity works, its size, restrictions, what happens when it ends, and how it differs from a Power BI individual trial.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: high
sources: [S1510, S1511, S2706, S3023]
references: []
related: [13.fabric_capacity_f_skus, 13.license_types_overview]
---
## Purpose

A trial lets you test Fabric without buying capacity. It is for evaluation, not production.

## Key facts

- Fact: The trial lasts 60 days. It is an F4 (4 CUs) or F64 (64 CUs) capacity. Eligible admins can switch between 4 and 64 CUs; this does not extend the 60 days [S1511].
- Fact (rechecked 2026-11-02): Learn still says the trial capacity lasts 60 days, and non-Power BI Fabric items need a paid F or P capacity within seven days after expiry [S3023].
- Fact: Storage is up to 1 TB in OneLake [S1511].
- Fact: Users without a PPU receive a Power BI individual trial with the Fabric trial [S1511].
- Fact: Copilot, Trusted Workspace Access, AI experiences (data agent, AI functions) and Private Link are not supported on trial [S1511].
- Fact: A trial capacity supports at most three SQL databases and has no autoscale [S1511].
- Fact: Microsoft limits the number of trial capacities per tenant [S1511].
- Fact: A separate Power BI Pro trial lasts 30 days and includes up to 25 licenses. After it ends you are charged [S1510].

## Steps

1. Open the Fabric portal and select the account manager (profile picture).
2. Select Start trial. If it is missing, trials may be disabled or your tenant hit the limit.
3. Pick a region. Default is the tenant home region, but sometimes a nearby region.
4. Create a workspace with workspace type Fabric Trial.
5. Share by turning on Contributor permissions for the trial, or assign workspaces to it.

Admin setting: Users can try Microsoft Fabric paid features (Help and support settings). Also enable Users can create Fabric items [S1511].

## When the trial ends

- Workspaces fall back to Pro type. Non-Power BI Fabric items become inactive [S1511].
- Content stays in OneLake for 7 days. Assign the workspace to a paid F or P capacity to recover it [S1511].
- Power BI items stay available [S1511].

## Common mistakes

- Using the trial for production. Microsoft states it is for evaluation only [S1511].
- Starting the trial in the wrong region. Moving a workspace with Fabric items to another region requires deleting them first [S1511].
- Letting unmanaged trials pile up when the admin leaves. They consume the tenant limit; cancel them [S1511].

## Limits and version notes

An individual trial gives PPU-like rights but is not a Fabric capacity. A Fabric capacity is required for non-Power BI items [S1511]. Trial availability depends on tenant settings and region.

## See also

- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
- [License types overview](13_license_types_overview.md)
