---
id: 18.analyze_in_excel
title: Excel with Power BI data
domain: ecosystem_tools
type: how-to
level: intermediate
tags: [excel, semantic-model, tenant-setting, limits, ecosystem]
summary: How to use Analyze in Excel, export with live connection and the Power BI Excel add-in, with prerequisites, security behavior and limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S2115, S2139, S2825]
references: []
related: [18.external_tools_overview, 18.teams_integration]
---

## Table of Contents

- [Purpose](#purpose)
- [Three ways in](#three-ways-in)
- [Prerequisites](#prerequisites)
- [Limits](#limits)
- [Troubleshooting](#troubleshooting)

# Excel with Power BI data

## Purpose
Build refreshable PivotTables and tables in Excel from a governed Power BI semantic model. Example: a finance analyst validates a report total with a PivotTable on the same model.

## Three ways in
1. Analyze in Excel: from a report (Export > Analyze in Excel), a workspace item menu, or the model details page. Power BI saves a workbook to OneDrive or SharePoint, or downloads it [S2115].
2. Export with live connection: from a visual, Export data > Summarized data > .xlsx with live connection, max 500,000 rows [S2115].
3. Excel add-in: Insert > PivotTable > From Power BI, or Data > Get Data > From Power Platform > From Power BI. It inserts connected PivotTables and connected tables [S2115].

## Prerequisites
- Tenant setting "Users can work with Power BI semantic models in Excel using a live connection" on [S2115].
- For on-premises models, the "Allow XMLA endpoints and Analyze in Excel with on-premises datasets" setting [S2115].
- Build permission on the model, or Contributor or higher in the workspace [S2115].
- Fabric Free, Pro or PPU licence. Free users only for My workspace or models on Premium or F64+ capacity [S2115].
- The add-in is visible for Pro users; Excel Trust Center must allow add-ins and web add-ins [S2115].

## Security
- Fact: row-level security (RLS) and object-level security (OLS) apply [S2115].
- Fact: the model's sensitivity label is applied to the workbook; the stricter label wins [S2115].

## Limits
- Hierarchies survive only for Import models, not Direct Lake, DirectQuery or composite [S2115].
- Errors above about 2 GB of data; filter or use the XMLA endpoint [S2115].
- External users cannot connect. Not available for Report Server, Embedded app-owns-data, or live connections to Analysis Services [S2115].
- Mac users can only use Excel for the web [S2115].
- Field parameters may not work as expected [S2115].
- Measures added only in a live-connected report are missing from an export [S2115].

## Troubleshooting
- Forbidden: Excel used a different account. Sign in with the account that has access [S2139].
- Cannot drag anything to Values: PivotTables need explicit measures in the model, because calculation is server side [S2139].
- Analysis Services live connection: user also needs read access in Analysis Services [S2139].

## Unverified
Excel cube functions (CUBEVALUE and similar) over Power BI models: no page was verified this pass. See gaps.

## See also
- [External tools overview](18_external_tools_overview.md)
