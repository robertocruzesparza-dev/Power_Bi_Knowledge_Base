---
id: 02.desktop_vs_service
title: Desktop versus the Power BI service
domain: desktop
type: comparison
level: beginner
tags: [desktop, service, comparison, decision-guide]
summary: Side-by-side view of what you can do in Desktop, in the service, or in both, and how to move content between them.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S001, S003, S017, S019, S034, S021, S022, S2840, S2841, S2839]
references: []
related: [01.product_family_and_components, 02.limits, 02.file_formats]
---
## Purpose

Decide where to do each task. Desktop is best for modeling and report creation. The service is best for sharing and collaboration (S001).

## Comparison

| Task | Desktop | Service |
|---|---|---|
| Connect to 100+ sources and use Power Query | Yes (S001) | Via dataflows and web editing (S001) |
| Full data modeling with DAX | Yes | Partial; web modeling exists |
| Build reports | Yes | Yes, in the browser editor (S003) |
| Dashboards | No | Yes (S003) |
| Workspaces, apps, sharing | No | Yes (S001) |
| Scheduled refresh, subscriptions, alerts | No | Yes (S001) |
| Security: RLS definition | Define roles | Assign members, manage (S001) |
| Performance Analyzer, external tools | Yes (S001) | No |
| DAX query view | Yes | Yes, "Write DAX queries" (S021) |
| TMDL view | GA | Preview (S022) |
| Hardware | Windows only | Any browser |

Row-level security (RLS) details belong to the security domain.

## Moving content

- Desktop to service: Publish on the Home ribbon, pick a workspace (S034). Directly publishing a protected file is unsupported for guest users (S034).
- Service to Desktop: download the PBIX if you are at least Contributor, subject to limits (S019). Direct Lake, incremental refresh, and automatic aggregation models cannot be downloaded as a copy.
- Live connection: connect Desktop to a published semantic model so reports reuse it without a copy of data.

## Decision rules

- Need Git, code editing, or heavy modeling: Desktop.
- Need quick edit by someone without Windows: service editor.
- Need audience sharing, refresh, or monitoring: service.
- Inference: build the model once in Desktop, publish, then let many reports connect live.

## Common mistakes

- Treating the published copy as the source of truth while the PBIX diverges. Decide where the master lives.
- Overwriting a semantic model by republishing a live-connected report with the same name; Desktop blocks this and asks you to rename (S020).
- Changing storage mode between publishes; unsupported (S034).

## Limits and version notes

- Volatile. Fact: the service description lists Pro model size as 1 GB, PPU as 100 GB, and refresh rate as 8 or 48 per day (S017).
- Features move between Desktop and web monthly; check the monthly update page.

## See also

- [Product family](../01_foundations/01_product_family_and_components.md)
- [Limits](02_limits.md)
- Service domain: ../08_service/
