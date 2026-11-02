---
id: 10.paginated_overview
title: Paginated reports overview
domain: paginated_reports
type: concept
level: beginner
tags: [paginated-report, report, service]
summary: What paginated reports and RDL are, when to choose them over interactive reports, and which tools author them.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1224, S1231, S1237]
references: []
related: [10.paginated_licensing_capacity, 10.paginated_data_sources, 10.paginated_parameters]
---
## Purpose

Paginated reports are print-ready, fixed-layout documents. They are built on Report Definition Language (RDL), the same format as SQL Server Reporting Services (SSRS). Think invoices, statements, and inventory lists.

## Key facts

- Fact: Interactive Power BI reports suit exploration. Paginated reports suit operational output meant for print or PDF. [S1224]
- Fact: A paginated table prints every row across as many pages as needed. An interactive table prints only the rows visible on screen. [S1231]
- Fact: Files use the `.rdl` extension. Interactive reports use `.pbix`. [S1231]
- Fact: Paginated reports use the SSRS rendering engine, not the Analysis Services engine. [S1228]
- Fact: Power BI Report Builder is the primary authoring tool. It is free to download. [S1224, S1231]

## How it works

You design a layout of tables, matrices, and lists (called tablix regions). Each region binds to a dataset. A dataset is a query against a data source. Parameters filter the query. Expressions compute values and formatting. When a user opens the report, the service runs the queries and renders pages.

Example: An invoice report takes a parameter InvoiceID. The dataset query is `SELECT ... WHERE InvoiceID = @InvoiceID`. The page header shows `="Page " & Globals!PageNumber`.

## Authoring options

| Tool | Notes |
|---|---|
| Power BI Report Builder | Desktop app. Full feature set. Publishes straight to the service. |
| Web authoring in the service | Preview. Simple formatted tables. Not full Report Builder parity. No hierarchies. Cannot use live-connection models. [S1237] |
| SQL Server Data Tools (SSDT) | Works, but the service uploads one item at a time, so many project scenarios are unsupported. [S1224] |

Web authoring has a preview toggle. If a report renders oddly, try Disable preview features on the File menu. Preview features re-enable after 30 days. [S1224]

## When to choose which

| Need | Choose |
|---|---|
| Slice and explore | Power BI report |
| Pixel-fixed, multi-page, print or PDF | Paginated report |
| Email PDF or Excel on a schedule | Paginated report with a subscription |
| Export every row of a large table | Paginated report |

## Common mistakes

- Using a paginated report for exploration. It has no cross-filtering.
- Expecting every SSRS feature. See [Limits and unsupported features](10_paginated_limits_unsupported.md).
- Moving SSRS reports without checking data sources. See [Data sources](10_paginated_data_sources.md).

## See also

- [Licensing and capacity](10_paginated_licensing_capacity.md)
- [Parameters](10_paginated_parameters.md)
- [Expressions](10_paginated_expressions.md)
- [Export and subscriptions](10_paginated_export_subscriptions.md)
