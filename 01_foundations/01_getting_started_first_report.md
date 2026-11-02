---
id: 01.getting_started_first_report
title: Getting started - your first report
domain: foundations
type: how-to
level: beginner
tags: [power-bi, desktop, tutorial, how-to, report]
summary: Seven-step path from installing Desktop to publishing a first report built from an Excel file.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S001, S006, S002]
references: []
related: [01.product_family_and_components, 02.install_and_requirements, 02.ui_tour]
---
## Purpose

Build and share a first report with the shortest path. Example: a workbook called Sales.xlsx with one table named Orders.

## Before you start

- Windows 10 or later PC (Desktop is Windows only; S002).
- Power BI Desktop installed. See [install](../02_desktop/02_install_and_requirements.md).
- A work or school account to publish. Fact: publishing needs a license that allows sharing; see [licenses](01_licenses_and_capacity.md).

## Steps

Source: S006 unless noted.
1. Open Desktop.
2. Select Home, Get Data, Excel. Pick Sales.xlsx. In the Navigator, tick Orders and select Load.
3. Optional cleaning: select Transform Data to open Power Query Editor. Remove unneeded columns, filter rows, set data types. Select Close and Apply.
4. In the Fields (Data) pane, tick fields such as Region and Amount. Desktop creates a visual. Change the type in the Visualizations pane.
5. Add more visuals. Arrange them on the canvas.
6. Select File, Save.
7. Select Publish on the Home ribbon. Sign in and choose a workspace.

After publishing, you can share the report, pin visuals to a dashboard, and schedule refresh (S006). An on-premises file source needs a gateway for scheduled refresh (see the data sources domain).

## Go the other way: Excel from Power BI

In the service, open the report or semantic model, select More options, then Analyze in Excel. Excel opens with a live connection and PivotTables (S006).

## Common mistakes

- Publishing with no plan for refresh. The published model keeps the data from the last load until a refresh runs.
- Skipping the cleaning step and getting text-typed numbers. Check data types in Power Query.
- Expecting to build a dashboard in Desktop. Create it in the service (S003).
- Running an old Desktop. Only the latest version is supported (S002).

## See also

- [Key concepts](01_key_concepts_terminology.md)
- [UI tour](../02_desktop/02_ui_tour.md)
- [Desktop vs service](../02_desktop/02_desktop_vs_service.md)
