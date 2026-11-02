---
id: 01.architecture
title: Architecture - how the pieces fit
domain: foundations
type: concept
level: beginner
tags: [power-bi, service, desktop, semantic-model, workspace, onelake]
summary: Explains the flow from data source to semantic model to report to workspace to consumer, and where tenant and capacity sit.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S001, S003, S008, S009, S017]
references: []
related: [01.product_family_and_components, 01.key_concepts_terminology, 01.licenses_and_capacity]
---
## Purpose

Give a mental map. Data starts in sources, is shaped into a model, is shown in a report, is stored in a workspace, and is read by people. The map explains most Power BI terms.

## The flow in one example

A sales analyst has an Excel file and a SQL database.
1. In Power BI Desktop she connects to both and cleans them in Power Query.
2. She relates the tables and writes measures in DAX (Data Analysis Expressions). The result is a semantic model.
3. She builds report pages on that model.
4. She publishes to a workspace in the Power BI service.
5. The service refreshes the model on a schedule. Colleagues open the report in a browser or the mobile app.

## Layers

| Layer | Holds | Notes |
|---|---|---|
| Data sources | Files, databases, web, cloud services | Over 100 connectors in Desktop (S001) |
| Power Query | Extract and transform steps | Runs in Desktop and in the service |
| Semantic model | Tables, relationships, measures, security roles | Formerly called dataset (S003) |
| Report | Pages of visuals bound to one semantic model (S003) | Can be many reports per model |
| Dashboard | Single page of tiles pinned from reports (S003) | Service only |
| Workspace | Container for items and roles | Admin, Member, Contributor, Viewer (S003) |
| Capacity | Compute pool a workspace runs on | Shared, Premium P, or Fabric F (S009) |
| Tenant | The Microsoft Entra organisation | Holds all capacities and settings (S009) |

## How it works

- Fact: every Fabric user has a personal workspace, My workspace. Shared capacity hosts My workspaces and Pro or PPU workspaces by default (S009).
- Fact: workspaces live inside capacities. A workspace can be reassigned to another capacity in the same tenant (S009).
- Fact: a report is based on a single semantic model, but one model can feed many reports (S003).
- Inference: the split between model and report is why a fix to a measure in one model updates every report that uses it.
- Fact: storage for Fabric items is OneLake, built on Azure Data Lake Storage Gen2 (S008). Import-mode Power BI models keep their own compressed in-memory copy.

## Common mistakes

- Treating the report file as the model. In the service they are two items after publish.
- Thinking a dashboard can be authored in Desktop. Dashboards are built in the service (S003).
- Forgetting that an on-premises source needs a gateway for refresh. See the data sources domain.

## See also

- [Product family](01_product_family_and_components.md)
- [Key concepts and terminology](01_key_concepts_terminology.md)
- [Licenses and capacity concepts](01_licenses_and_capacity.md)
- [Desktop vs service](../02_desktop/02_desktop_vs_service.md)
