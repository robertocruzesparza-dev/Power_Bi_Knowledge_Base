---
id: 09.datamarts_status
title: Power BI datamarts status and migration
domain: semantic_models_dataflows
type: decision
level: intermediate
tags: [datamart, warehouse, migration, fabric, deprecated]
summary: Datamarts are no longer supported. Learn the dates, what to check, and how to move a datamart to a Fabric warehouse.
status: retired
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1207, S1220, S2613]
references: []
related: [11.lakehouse_vs_warehouse, 09.dataflows_gen1_vs_gen2]
---
## Purpose

A Power BI datamart was a self-service, managed SQL database with a built-in semantic model. Microsoft replaced it with the Fabric Data Warehouse. If you still hold datamarts, act now.

## Key facts

- Fact: Since 2025-06-01, creating a new datamart redirects to creating a Fabric warehouse. [S1207]
- Fact: Since 2025-11-01, Microsoft says datamarts are no longer supported and are not accessible from workspaces. [S1207]
- Fact: Since 2025-09-05, default semantic models are no longer created automatically for new warehouses, lakehouses, or mirrored items. By 2025-11-30 existing default models were decoupled into independent models. [S2613]
- Fact: The page still calls datamarts "a preview feature" in one sentence. Treat the retirement notice as the stronger statement. Inference: wording is inconsistent inside one article. [S1207]
- Fact: You need a P or F SKU to create a warehouse. [S1207]

Because the Learn page says datamarts are inaccessible, assume any datamart you still see is at risk. Verify its state in your tenant before relying on it. Unknown: whether any tenant retains read-only access.

## Find your datamarts

Options named by Microsoft: [S1207]

1. Feature Usage and Adoption report.
2. Purview hub.
3. Datamarts administration page.
4. Power BI admin REST APIs.

## Manual upgrade steps

1. In the datamart, choose Transform data, then Export template (Power Query template).
2. In the Fabric portal, create a blank warehouse.
3. In the warehouse, choose Get data, then New Dataflow Gen2.
4. Import from a Power Query template.
5. Save and run to publish and load data into the warehouse.
6. Point reports at the warehouse through a semantic model. [S1207]

Microsoft also publishes accelerator scripts for datamart modernization in the fabric-toolbox GitHub repo. [S1207]

## What to rebuild

- Row-level security (RLS): recreate with warehouse role-based access and T-SQL row-level security. Datamarts exposed tables through views in a `model` schema; recreate that schema with views. [S1207]
- Relationships and measures: script the TMSL from SSMS over the XMLA endpoint, or rebuild in the new semantic model. [S1207]
- Incremental refresh: use Dataflow Gen2 incremental refresh. See [Dataflow Gen2 limits](09_dataflow_gen2_refresh_limits.md).

## Common mistakes

- Waiting for a forced migration. The notice says to migrate to avoid breaking reports.
- Forgetting that default semantic models were decoupled. See [Semantic model basics](09_semantic_model_basics.md).

## See also

- [Lakehouse versus warehouse](../11_fabric_onelake/11_lakehouse_vs_warehouse.md)
