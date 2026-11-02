---
id: 16.capacity_metrics_app
title: Fabric Capacity Metrics app and throttling
domain: performance
type: how-to
level: intermediate
tags: [monitoring, capacity, performance, limits]
summary: Explains the Capacity Metrics app pages, smoothing, the four throttling policies, and how to tell capacity throttling from a slow design.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S672, S673, S674, S680, S2536, S2537, S2525]
references: []
related: [16.optimization_checklist, 16.performance_analyzer]
---

# Fabric Capacity Metrics app and throttling

## Purpose
The Capacity Metrics app shows how much compute each item uses on a capacity and whether the capacity is throttling. Capacity admins use it to find heavy items and plan scale.

## App pages (S672)
| Page | Shows |
|---|---|
| Health | High-level view of all capacities you administer; throttling or rejections |
| Compute | 14-day view: utilization, throttling, overages, operations matrix |
| Storage | 30-day storage by workspace, billable storage, soft-deleted data |
| Timepoint | A 30-second timepoint: which interactive and background operations used compute |
| Timepoint summary | Operation types that used capacity at that timepoint |
| Timepoint item detail | Operation-level detail with filters for operation ID, user, and capacity unit (CU) thresholds |

## Smoothing and throttling (S674, S673, S680)
- Fact: Overages are computed after smoothing. Overages beyond the allowed 10-minute window become carryforward CUs. Unused CUs burn them down. Throttling continues until carryforward is paid off (S674).
- Fact: Policies (S673):
| Policy | Future use consumed | Effect |
|---|---|---|
| Overage protection | up to 10 minutes | No throttling |
| Interactive delay | 10 to 60 minutes | User-requested interactive jobs are delayed (20-second delay per S680) |
| Interactive rejection | 60 minutes to 24 hours | Interactive jobs are rejected |
| Background rejection | over 24 hours | Scheduled background jobs are rejected |
- Fact: If you see 75% of future consumption at a timepoint, you have 15 minutes before interactive rejection begins (S673, for the 60-minute window).
- Fact: With capacity overage enabled, the capacity does not enter throttling until the overage limit is exceeded; the charts then say "capacity overage billed" (S673).
- Fact: Background rejection of 250% means 2.5 times the daily resources for the SKU were used (S680).

## How to recognize throttling (S674)
Error code CapacityLimitExceeded; messages such as "Your organization's Fabric compute capacity has exceeded its limits. Try again later" or "Cannot load model due to reaching capacity limits". Microsoft notes slow performance is often item design, only sometimes throttling. Confirm in the Compute page's System events and Throttling charts.

## Steps to find a heavy item
1. Compute page: find the peak utilization window.
2. Select a timepoint and drill to Timepoint.
3. Sort operations by CU; separate interactive from background.
4. Open Timepoint item detail; filter by user or operation.
5. Take the item to [Performance Analyzer](16_performance_analyzer.md) or [DAX Studio](16_dax_studio_vertipaq.md).
6. If load is legitimate and constant, scale the SKU or split workloads (S674).

## Related notes
- Scaling between SKUs across the F256 and F512 boundary might give a slower experience (S674).
- Pausing a capacity converts accumulated smoothed usage to billed utilization, which shows as a spike.
- Capacity admins can set email alerts through Capacity Overview Events (S674).

## Common mistakes
- Tuning a model when the real issue is a background refresh storm.
- Reading one timepoint as the cause; smoothed usage from earlier jobs can be included (S680).
- Using the app without being a capacity admin (access is for capacity admins; verify tenant setup).

## Limits and version notes
Thresholds and page names change; confirm on the live page.
- Re-verified 2026-10-08: the Fabric what's-new page lists Capacity Metrics app enhancements as generally available in September 2026 (health-state duration, capacity-units-per-second views, heatmaps, contributor drilldowns, chargeback integration) (S2525). Details not read.
