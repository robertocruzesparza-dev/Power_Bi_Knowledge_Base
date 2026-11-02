---
id: 09.semantic_model_basics
title: Semantic models basics and sharing
domain: semantic_models_dataflows
type: concept
level: beginner
tags: [semantic-model, service, workspace, governance]
summary: What a semantic model is, how it is shared across workspaces with Build permission, and what changed for default models in Fabric.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1213, S1220, S1221, S1207, S2921]
references: []
related: [09.large_semantic_models, 09.semantic_model_refresh, 09.endorsement_and_discovery]
---
## Purpose

A semantic model is the data model behind Power BI reports. It holds tables, relationships, measures, and security roles. Many reports can share one model, so numbers stay consistent.

## Key facts

- Fact: "Semantic model" is the current name for what Power BI called a "dataset". Older docs, APIs, and URLs still use "dataset". [S1220]
- Fact: Publishing a report from Desktop publishes its data model as a semantic model at the same time. [S1221]
- Fact: A report in one workspace can use a semantic model from another workspace through a live connection. No copy is made. [S1213]
- Fact: Row-level security (RLS) on the shared model still applies to the report author and viewers. [S1213]
- Fact: Contributor, Member, and Admin roles carry Build permission on models in that workspace. [S1221]

## How sharing works

Build permission lets a person create new content on a model: reports, dashboards, paginated reports, Analyze in Excel, and XMLA (XML for Analysis) endpoint access. It also allows export of underlying data. [S1221]

Ways to grant Build permission:

1. Workspace role of Contributor or higher.
2. The model owner assigns Build to users or groups on the Manage permissions page.
3. An app audience setting that also grants Build on the underlying models.
4. A user with Reshare plus Build shares a report and passes Build on.

Read permission alone lets a person view reports but not edit them. If Build is removed, people still see existing reports but lose edit and export of underlying data. [S1221]

Example: A finance team publishes "Finance Core" in a Premium workspace. Sales analysts get Build through an app audience. They build their own reports in their own workspace. Finance changes the model once, and all reports update.

Free-license users with Build can create a report on a model stored on Fabric F64 or larger, or Premium capacity. They must save it to My workspace. Sharing it needs Pro or Premium Per User (PPU). Their queries use the host capacity's capacity units (CUs). [S1221]

## Default semantic models in Fabric

Fact: Since 2025-09-05, a default semantic model is no longer created automatically when a warehouse, lakehouse, or mirrored item is created. [S1220, S1207]

Fact: By 2025-11-30, existing default models were scheduled to become independent items. Keep them if reports use them, or delete them if unused. [S1220]

Inference: Treat any semantic model in a Fabric workspace as a normal item. Manage it with the REST API, lineage, and endorsement like any other.

Fabric does not sync tables to a warehouse model automatically. You add tables and views by hand. Data types that cannot map to Power BI types are dropped during sync. [S1220]

## Common mistakes

- Assuming a viewer of a report can build on its model. They need Build.
- Deleting a model that reports in other workspaces still use. Power BI blocks this with an error. [S1221]
- Expecting a Pro license to be enough to view shared content in Premium or F SKUs below F64. See [Fabric capacity and licensing](../11_fabric_onelake/11_fabric_capacity_and_licensing.md).

## See also

- [Large semantic models](09_large_semantic_models.md)
- [Semantic model refresh](09_semantic_model_refresh.md)
- [Endorsement and discovery](09_endorsement_and_discovery.md)
