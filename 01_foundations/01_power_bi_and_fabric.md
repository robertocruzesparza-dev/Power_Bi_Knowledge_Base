---
id: 01.power_bi_and_fabric
title: Power BI and Microsoft Fabric
domain: foundations
type: concept
level: beginner
tags: [power-bi, fabric, onelake, direct-lake]
summary: Describes how Power BI sits inside Microsoft Fabric, what is shared, what is Power BI only, and what does not change.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S001, S008, S009, S010, S2808, S2801]
references: []
related: [01.architecture, 01.licenses_and_capacity]
---
## Purpose

Fabric is Microsoft's all-in-one analytics platform. Power BI is one of its workloads. This file states what that means for a Power BI user.

## Key facts

- Fact: Fabric is software as a service (SaaS) and stores data in OneLake, a logical data lake built on Azure Data Lake Storage Gen2 (S008).
- Fact: no migration is needed for Power BI content. You sign in with the same account (S001).
- Fact: Fabric adds capabilities such as lakehouses, warehouses, notebooks, pipelines, real-time analytics. Power BI keeps its familiar interface (S001, S008).
- Fact: the Fabric overview lists these workloads: Power BI, Databases, Data Factory, Industry Solutions, Real-Time Intelligence, Data Engineering, Data Science, Data Warehouse, and Fabric IQ (preview) (S008).
- Fact: a Fabric free licence is auto-assigned at first Fabric sign-in if the tenant has Fabric enabled (S009).

## Shared versus Power BI only

| Feature | Shared across Fabric | Power BI only (per S001) |
|---|---|---|
| OneLake integration | Yes | |
| Direct Lake storage mode | Yes | |
| Dataflows Gen2 and notebooks | Yes | |
| Copilot | Yes | |
| Security and governance via Microsoft Purview | Yes | |
| Power BI Desktop | | Yes |
| Power BI service reports and dashboards | | Yes |
| Paginated reports | | Yes |
| Custom visuals marketplace | | Yes |
| Goals (scorecards) | | Yes |

## Fabric workloads at a glance

- Power BI: reports, dashboards, semantic models.
- Data Factory: data integration with more than 200 connectors (S008).
- Data Engineering: Apache Spark, notebooks, lakehouses (S008).
- Data Warehouse: SQL engine storing data as Delta Lake (S008).
- Real-Time Intelligence: streaming data analytics (S008).

## Limits and version notes

- Status is mixed: most listed items are generally available. Fabric IQ is labelled preview (S008). Treat the "Power BI only" column as a point-in-time table from the 2026 overview, not as permanent.
- Fact: the August 2026 Desktop update lists Direct Lake calculated columns as preview, showing that Direct Lake modeling keeps evolving (S010).
- Fact: Fabric is not yet available in sovereign clouds, per the P SKU migration guidance (S026).
- Prices belong to the licensing domain. See [licenses and capacity concepts](01_licenses_and_capacity.md).

## See also

- [Architecture](01_architecture_how_pieces_fit.md)
- [Licenses and capacity concepts](01_licenses_and_capacity.md)
- Fabric and OneLake domain: ../11_fabric_onelake/
