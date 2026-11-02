---
id: 20.tableau_to_power_bi
title: Migrating from Tableau to Power BI
domain: migration
type: comparison
level: intermediate
tags: [migration, tableau, dax]
summary: Concept mapping from Tableau to Power BI, covering LOD expressions, parameters, extracts, Prep and common pitfalls, with source tiers labeled.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: low
sources: [S1535, S1542]
references: []
related: [20.migration_process, 20.migration_checklist]
---
## Purpose

Use this page to translate Tableau ideas into Power BI parts. No Microsoft Learn page gave an official Tableau mapping, so rows are community practice or labeled inference.

## Key facts

- Fact (community): Tableau calculates per worksheet. Power BI uses a model-based engine with filter and row context. One team said this difference explained most migration issues [S1542].
- Fact (community): Tableau calculated fields and LOD expressions usually become DAX measures or calculated columns. This is the steepest learning step [S1542].
- Fact (community): Automatic converters exist but need manual rework and validation [S1542].
- Fact: Microsoft advises rebuilding around the business question, not the old layout [S1535].

## Concept map

| Tableau | Power BI | Basis |
|---|---|---|
| Workbook | Report (PBIX or PBIP) plus semantic model | Inference |
| Data source / extract (Hyper) | Semantic model in Import mode | Inference; DirectQuery replaces live connection |
| Live connection | DirectQuery or Direct Lake | Inference |
| Prep flow | Power Query, Dataflow Gen2 or pipeline | Community [S1542] |
| Calculated field (row level) | Calculated column or Power Query step | Inference |
| Aggregated calculation | DAX measure | Community [S1542] |
| LOD FIXED / INCLUDE / EXCLUDE | CALCULATE with ALL, ALLEXCEPT, VALUES | Community [S1542] |
| Table calculations | Visual calculations, window functions, measures | Inference |
| Parameter | What-if parameter, slicer or disconnected table | Community [S1542] |
| Set / group | Group, calculated column or filter table | Inference |
| Filter shelf | Visual, page or report filter | Inference |
| Dashboard actions | Cross-filtering, drillthrough, bookmarks | Inference |
| Tableau Server / Cloud project | Workspace and app | Inference |
| Row-level security (user filters) | RLS roles | Inference |

Inference rows come from general product knowledge, not a fetched source. Verify before relying on them.

## LOD to DAX

A common pattern is `{ FIXED [Customer] : MIN([Order Date]) }` as a calculated column using CALCULATE plus ALLEXCEPT [S1542]. Fixed ignores the view's dimensions. In DAX you remove filters with ALL or ALLEXCEPT and keep the ones you need. Include and exclude mean adding or removing a grouping column inside the measure.

## Steps

1. Inventory workbooks, data sources and calculations. Rank by use.
2. Design one star-schema model per subject area. Do not copy each workbook's data shape.
3. Rebuild calculations as measures in the model, once.
4. Rebuild visuals around questions. Use a small proof of concept.
5. Reconcile numbers side by side with Tableau output.
6. Train authors on filter context. Plan capacity and licenses.

## Common mistakes

- Porting each workbook's calculations into each report, which makes KPIs drift [S1542].
- Copying visuals pixel for pixel. Performance can suffer if the model is poor [S1542].
- Underestimating calculation work, which slips timelines [S1542].
- Assuming licensing maps like for like. Map Server or Cloud to workspaces and capacity first [S1542].

## Limits and version notes

All Tableau-specific content here is tier 3 or inference. A Microsoft-published Tableau mapping was not found (see gaps). Check current Power BI features such as visual calculations that may reduce rework.

## See also

- [Migration process](20_migration_process.md)
- [Migration checklist](20_migration_checklist.md)
