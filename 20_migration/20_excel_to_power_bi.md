---
id: 20.excel_to_power_bi
title: Migrating Excel workbooks to Power BI
domain: migration
type: how-to
level: beginner
tags: [migration, excel, semantic-model]
summary: How to move Excel data, Power Query queries and Power Pivot models into Power BI, and what changed for uploaded local workbooks.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1540, S1541, S2724]
references: []
related: [20.migration_process, 20.migration_checklist]
---
## Purpose

Many Power BI projects start from Excel. Choose the right path: connect to a simple table, or import the whole data model.

## Key facts

- Fact: For simple data, use Get Data, then Excel in Desktop. For workbooks with Power Query or Power Pivot, use File, Import, Power Query, Power Pivot, Power View [S1540].
- Fact: The import is a one-time conversion to a PBIX file. The result no longer depends on the workbook [S1540].
- Fact: Imported objects: Power Query queries (with groups), Power Pivot external connections (become queries), calculated columns, measures, KPIs, relationships and most data categories. Some categories, such as Image, reset [S1540].
- Fact: Worksheet tables linked to the data model can be imported as a snapshot (limit 1 million characters) or kept as a connection to the workbook [S1540].
- Fact: Power BI no longer supports uploading local Excel workbooks to workspaces with scheduled refresh. Republish the model or import from OneDrive or SharePoint [S1541].
- Fact: Workbooks must be .xlsx or .xlsm and smaller than 1 GB [S1541].
- Fact: Workbooks with data models cannot be shared across Power BI tenants [S1541].

## Concept map

| Excel | Power BI | Basis |
|---|---|---|
| Worksheet range / table | Table in Power Query | Source [S1541] |
| Get and Transform / Power Query | Power Query (same engine, M) | Source [S1540] |
| Power Pivot model | Semantic model | Source [S1540] |
| DAX measure | DAX measure | Source [S1540] |
| PivotTable | Matrix visual | Inference |
| Chart | Visual | Inference |
| Formula in a cell | Measure or calculated column | Inference |
| Shared workbook on a drive | Workspace and app | Inference |

## Steps

1. In Desktop choose File, Import, Power Query, Power Pivot, Power View.
2. Select the workbook and Start. Read the summary page for items not imported.
3. Fix data categories and review auto-built visuals.
4. Publish to a workspace. Configure refresh and a gateway if needed.
5. Optionally, use Analyze in Excel so users keep PivotTables on the governed model.
6. Admins: call the workbooks admin REST API to list affected local workbooks [S1541].

## Worked example

A finance workbook has five Power Query queries and a Power Pivot model with 12 measures. Import gives one PBIX with all queries and measures. The team publishes it, sets daily refresh, and replaces the file's PivotTables with Analyze in Excel connections.

## Common mistakes

- Uploading the workbook itself and expecting refresh. Publish the model instead [S1541].
- Leaving hard-coded cell logic that has no equivalent. Move rules into Power Query or measures.
- Ignoring spreadsheet sprawl. Inventory who uses which file first.

## Limits and version notes

The Publish to Power BI command in Excel for Microsoft 365 is deprecated and is absent from Excel 2024 perpetual; use Power BI Desktop import or OneDrive and SharePoint instead [S2724]. Sovereign cloud customers cannot upload Excel workbooks to workspaces. On-premises SSAS tabular connections through a gateway cannot use scheduled refresh in uploaded workbooks [S1541].

## See also

- [Migration process](20_migration_process.md)
