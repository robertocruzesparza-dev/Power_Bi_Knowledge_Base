---
id: 09.dataflows_gen1_vs_gen2
title: Dataflows Gen1 versus Gen2
domain: semantic_models_dataflows
type: comparison
level: intermediate
tags: [dataflow, power-query, fabric, comparison, licensing]
summary: Compare Power BI dataflows Gen1 (legacy) and Fabric Dataflow Gen2, with licensing needs and migration paths.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1202, S1214, S1215, S1216, S1219, S1222, S2618]
references: []
related: [09.dataflow_gen2_refresh_limits, 09.datamarts_status]
---
## Purpose

Dataflows are cloud Power Query jobs that prepare data. Gen1 lives in Power BI workspaces. Gen2 lives in Fabric. Choose Gen2 for new work unless your license blocks it.

## Key facts

- Fact: Microsoft calls Power BI Dataflow Gen1 "legacy" and says it gets no new feature investment. [S1216]
- Fact: For Premium customers with Fabric access, Gen2 is the recommended path. Pro and PPU customers can keep using Gen1. [S1216]
- Fact: As of April 2026, new Dataflow Gen2 items are created only with CI/CD and Git integration. The older "Classic" Gen2 type can no longer be created. Existing ones still run. [S1202]
- Fact: Gen2 needs a Fabric capacity, a Fabric trial capacity, or a Power BI Premium capacity. [S1202]

## Comparison

| Feature | Gen1 | Gen2 |
|---|---|---|
| Home | Power BI workspace | Fabric workspace |
| Output | Internal storage only (or bring your own lake) | Internal storage or destinations such as lakehouse, warehouse, Azure SQL, SharePoint |
| DirectQuery over dataflow | Yes (Premium, enhanced compute) | No. Load to a destination and connect there |
| Linked and computed tables | Premium only | Not used. Use destinations and pipelines |
| Enhanced compute engine | Premium, A3 or larger | Not applicable. Uses Fabric SQL engines |
| Incremental refresh | Premium only, set after publish | Built into the editor, needs fixed-schema destination |
| AutoSave and background publish | No | Yes |
| Pipeline activity | No | Yes |
| Monitoring hub integration | No | Yes |
| Endorsement | Yes | Not copied by Save As [S1219] |

Sources for the table: S1202, S1214, S1219, S1222.

Gen2 creates hidden staging items (DataflowsStagingLakehouse and DataflowsStagingWarehouse). Do not edit them. [S1202]

## Licensing

- Gen1 on Pro: refresh, Power Query Online, and the Dataflows connector work. Computed tables, linked tables, DirectQuery, AI features, and incremental refresh need Premium or PPU. [S1215]
- Gen1 PPU content cannot be consumed outside the PPU environment. [S1214]
- Gen1 enhanced compute: Premium P1 or A3 and above. [S1214]
- Gen2: needs capacity as above. Free users cannot create it. See [Fabric capacity and licensing](../11_fabric_onelake/11_fabric_capacity_and_licensing.md).

Power Platform dataflows: creating new referenced linked entities was disabled 2026-09-01, and existing ones stop working 2026-10-31 (claimed on a Learn page; this is Power Apps, not Power BI). [S1215]

## Migration

Three routes from Gen1 to Gen2: [S1202]

1. Export queries to a PQT template file, then import into Gen2.
2. Copy and paste queries in Power Query.
3. Save As: on the dataflow's menu choose Save as Dataflow Gen2. A REST API supports bulk moves. [S1219]

Save As does not copy scheduled refresh or incremental refresh settings. Set them again. [S1219]

## Common mistakes

- Planning DirectQuery on a Gen2 dataflow. Use a lakehouse or warehouse destination instead.
- Forgetting to recreate schedules after Save As.
- Letting downstream refreshes read Gen2 through the Dataflows connector. See the workaround in [Dataflow Gen2 refresh and limits](09_dataflow_gen2_refresh_limits.md).

## See also

- [Dataflow Gen2 refresh and limits](09_dataflow_gen2_refresh_limits.md)
- [Datamarts status](09_datamarts_status.md)
