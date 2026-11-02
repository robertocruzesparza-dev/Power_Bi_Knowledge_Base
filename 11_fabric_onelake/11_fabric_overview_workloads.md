---
id: 11.fabric_overview_workloads
title: Microsoft Fabric overview and where Power BI fits
domain: fabric_onelake
type: concept
level: beginner
tags: [fabric, power-bi, onelake, workspace]
summary: Fabric workloads and items, how they share OneLake and capacity, and Power BI's place inside the platform.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1244, S1241, S1243, S1203, S1208, S2917]
references: []
related: [11.onelake, 11.fabric_capacity_and_licensing, 11.lakehouse_vs_warehouse]
---
## Purpose

Microsoft Fabric is one software-as-a-service (SaaS) analytics platform. Power BI is one of its workloads. All workloads store data in OneLake and spend one shared pool of compute, called capacity.

## Key facts

- Fact: Fabric covers data ingestion, transformation, real-time processing, analytics, and reporting in one platform. [S1244]
- Fact: Workloads listed by Microsoft: Power BI, Databases, Data Factory, Industry Solutions, Real-Time Intelligence, Data Engineering, Data Science, Data Warehouse, and Fabric IQ (preview). [S1244]
- Fact: Every Fabric tenant gets one OneLake automatically. [S1243]
- Fact: Fabric items are created in workspaces. Each workspace belongs to a capacity. [S1241]

## Workloads and main items

| Workload | Main items |
|---|---|
| Power BI | Semantic models, reports, paginated reports, dashboards, dataflows (Gen1), scorecards |
| Data Factory | Pipelines, Dataflow Gen2, copy jobs |
| Data Engineering | Lakehouse, notebooks, Spark job definitions |
| Data Warehouse | Warehouse, SQL analytics endpoint |
| Real-Time Intelligence | Eventhouse, KQL database, eventstreams, Real-Time hub |
| Data Science | Machine learning experiments and models |
| Databases | SQL database in Fabric, mirrored databases |
| Fabric IQ (preview) | Ontology, planning, graph, data agent, operations agent |

Sources: S1244, S1241. The table groups items by Microsoft's workload names; item lists are not exhaustive.

## How Power BI fits

1. Power BI items (reports, semantic models, dashboards, paginated reports, Gen1 dataflows) work with Pro, PPU, or Fabric capacity. [S1241]
2. Non-Power BI items (lakehouses, warehouses, notebooks, pipelines) need an F, P with Fabric enabled, or trial capacity. Pro and PPU alone do not enable them. [S1241]
3. Semantic models read Fabric data in three ways: Import, DirectQuery, or [Direct Lake](11_direct_lake.md).
4. Import tables can also write Delta copies into OneLake through OneLake integration. [S1203]
5. Governance, sensitivity labels, endorsement, and the OneLake catalog span all items. [S1244]

Example flow: Data Factory loads CSVs into a lakehouse. Spark cleans them into Delta tables. A Direct Lake semantic model reads those tables. A Power BI report shows them. One copy of data serves every step.

## Common mistakes

- Thinking a PPU license lets you create a lakehouse. It does not. [S1241]
- Assuming Premium P capacity has Fabric items on. An admin must enable Fabric. [S1241]
- Treating the workload list as fixed. Fabric adds items often; check the Learn overview.

## Limits and version notes

Fabric IQ is a preview workload. Fabric is not available in sovereign clouds per the P-to-F migration page. [S1208]

## See also

- [OneLake](11_onelake.md)
- [Fabric capacity and licensing](11_fabric_capacity_and_licensing.md)
- [Lakehouse versus warehouse](11_lakehouse_vs_warehouse.md)
