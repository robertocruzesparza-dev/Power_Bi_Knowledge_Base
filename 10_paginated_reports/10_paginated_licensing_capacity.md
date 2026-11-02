---
id: 10.paginated_licensing_capacity
title: Paginated reports licensing and capacity sizing
domain: paginated_reports
type: reference
level: intermediate
tags: [paginated-report, licensing, capacity, limits]
summary: Who needs which license to author, publish, and view paginated reports, and how to estimate capacity load.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1224, S1231, S1227, S1232, S1235, S1236, S1242, S2610]
references: []
related: [10.paginated_overview, 11.fabric_capacity_and_licensing]
---
## Purpose

Paginated reports have the same license rules as .pbix reports. Premium or Fabric capacity is not required to publish, but it helps scale and widens who can view.

## License rules

| Action | Requirement |
|---|---|
| Download Power BI Report Builder | No license |
| Author, and publish to My workspace | Free license is enough |
| Publish to other workspaces | Pro or Premium Per User (PPU), plus at least Contributor role |
| Use a Power BI semantic model as source | Build permission on it |
| View in a workspace not on Premium or Fabric | Pro or PPU |
| View with a Free license | Workspace on Fabric F64 or larger, or Premium P1 or larger, with Viewer role |

Sources: S1224, S1231, S1236. Fact: "Pro required to publish elsewhere" and "F64 for free viewers" were stated on Learn on the retrieval date.

## Capacity planning

Fact: Paginated reports use the capacity's paginated workload. Capacity use depends on design complexity, data volume, data retrieval method, and export of large files. [S1227]

Microsoft's tests with one concurrent report render workload: [S1227]

| Workload | F64 or P1 users | F128 or P2 users |
|---|---|---|
| Small (100 rows) | 2,500 | 5,000 |
| Medium (100,000 rows) | 1,900 | 3,800 |
| Large (250,000 rows) | 1,300 | 2,600 |

The numbers assume a 5 percent concurrency ratio and a capacity with no other load. [S1227]

Formulas from the same page: [S1227]

- Max concurrent renders = capacity units x 3.75 / report CPU seconds. Worked example: F64 has 64 units, so 64 x 3.75 = 240. A 4-second report gives 60 concurrent renders and 1,200 users. (The page writes the same value as 8 cores x 30.)
- Max users = max concurrent renders / 0.05.

Each workload on a capacity allows at most 500 concurrent report renders. Over that you get HTTP 429 Too Many Requests. [S1227]

Measure real CPU seconds with the Fabric Capacity Metrics app on a clean test capacity. Sum render operations, since long renders appear as several rows. [S1227]

DAX queries from paginated reports to semantic models get compound throttling protection. See [Capacity throttling](../11_fabric_onelake/11_capacity_throttling.md). [S1242]

## Embedding rules

- Embed for customers: service principal required; no master user; no PPU. [S1232]
- Embedding with a semantic model: both items must be in Premium or Embedded workspaces, and the token creator needs Write on both. [S1232]
- Embed for your organization with PPU: only PPU users can view. [S1232]
- Paginated reports do not support client-side events or setAccessToken. [S1232]

## Report Server

Power BI Report Server hosts paginated reports on premises. It needs SQL Server Enterprise with Software Assurance or SQL Server 2025 core licenses, or Fabric F64+ reserved instances. Publishing paginated reports to it with an F64+ reservation needs a Pro license. [S1235]

## See also

- [Paginated overview](10_paginated_overview.md)
- [Fabric capacity and licensing](../11_fabric_onelake/11_fabric_capacity_and_licensing.md)
