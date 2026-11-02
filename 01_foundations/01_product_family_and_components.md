---
id: 01.product_family_and_components
title: Power BI product family and components
domain: foundations
type: concept
level: beginner
tags: [power-bi, desktop, service, mobile, report-server, paginated-report]
summary: Lists each Power BI component, what it does, who uses it, and which one to pick for a given job.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S001, S002, S003, S013]
references: []
related: [01.architecture, 01.power_bi_and_fabric, 01.key_concepts_terminology]
---
## Purpose

Power BI is Microsoft's business analytics platform. It turns data into reports and dashboards. This file names the parts so later files can refer to them without re-explaining.

## Key facts

- Fact: Microsoft describes Power BI as a core workload of Microsoft Fabric. Existing Power BI content and workspaces stay as they are (S001).
- Fact: Power BI has two main components, Power BI Desktop and the Power BI service. A mobile app views reports on phones and tablets (S001).
- Fact: Desktop is for modeling and building reports. The service is for sharing and collaboration (S001).
- Fact: Paginated reports and Power BI Report Server are specialised parts of the family (S001, S013).

## Component table

| Component | What it is | Typical user | Runs where |
|---|---|---|---|
| Power BI Desktop | Free Windows authoring app: connect, transform, model, build reports | Report creator, modeler | Local Windows PC |
| Power BI service | Cloud site at app.powerbi.com: workspaces, apps, dashboards, refresh, sharing | Creators and consumers | Microsoft cloud |
| Power BI mobile apps | View and interact with reports and dashboards on phones and tablets | Consumer | iOS, Android |
| Paginated reports (Report Builder) | Pixel-perfect, printable documents such as invoices | Report author | Report Builder app, then service |
| Power BI Report Server | On-premises server hosting Power BI reports, paginated reports, KPIs | IT-managed teams | Customer servers |
| Dataflows (legacy label in service docs) | Reusable data-preparation steps stored in the service | Data preparer | Service |
| Custom visuals marketplace | Extra visuals from AppSource | Report creator | Desktop and service |

Fact: the 2026 overview lists "Dataflow (legacy)" for Gen1 style dataflows and points to Dataflows Gen2 in Fabric for new work (S001, S003).

## Which component for which job

| Need | Use | Why |
|---|---|---|
| Build a report and data model | Desktop | Full modeling, Power Query, DAX tools (S001) |
| Share with a team, schedule refresh | Service | Collaboration and refresh features (S001) |
| Look at a report on a phone | Mobile app | Optimised layouts (S001) |
| Printable multi-page output | Paginated report | Tables flow across pages (S013) |
| Keep reports on premises | Report Server | On-premises hosting (S013) |

## Common mistakes

- Assuming Desktop is the only authoring tool. Fact: the service also lets you create and edit reports in a browser (S003).
- Mixing up Power BI Report Server with the cloud service. They have different feature sets and release cadences (see [Report Server and deployment options](01_report_server_and_deployment_options.md)).
- Believing Power BI and Fabric are separate products that need migration. Fact: no migration is needed (S001).

## See also

- [Architecture: how the pieces fit](01_architecture_how_pieces_fit.md)
- [Power BI and Microsoft Fabric](01_power_bi_and_fabric.md)
- [Key concepts and terminology](01_key_concepts_terminology.md)
- [Desktop install](../02_desktop/02_install_and_requirements.md)
