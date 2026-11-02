---
id: 23.dataflow_vs_semantic_model
title: Dataflow or semantic model - where to put the transformation
domain: patterns_recipes
type: decision
level: intermediate
tags: [dataflow, semantic-model, power-query, decision-guide]
summary: Guidance on when to prepare data in a dataflow, a lakehouse, or inside the semantic model, including the Gen1 versus Gen2 status.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1833, S1834, S1827, S2937, S2938]
references: []
related: [23.import_vs_directquery_vs_direct_lake, 23.workspace_design]
---
## Purpose

Power Query logic can live in a semantic model or in a dataflow. The choice decides whether transformation is reused or copied, and who maintains it.

## Key facts

- Fact: Dataflows let many models share one set of cleaned tables. Without them, extract-transform-load (ETL) logic is copied between models and tied to each model's refresh settings [S1834].
- Fact: Dataflow Gen1 is in a legacy state and gets no new feature investment. Microsoft recommends Dataflow Gen2 for Premium customers with Fabric access. Pro and PPU customers can keep using Gen1, because Gen2 guidance for them is still evolving [S1834].
- Fact: Gen2 adds multiple output destinations (lakehouse, warehouse, SQL, and others), pipeline orchestration, autosave, and better monitoring [S1833].
- Fact: Gen1 supports DirectQuery through the dataflow connector. Gen2 does not list it [S1833].
- Fact: Direct Lake needs upstream preparation in the lake, using Spark, T-SQL, dataflows, or pipelines [S1827].

## Decision table

| Situation | Put the logic in |
|---|---|
| One model, one author, light shaping | The semantic model (Power Query) |
| Same cleaned table needed by several models | A dataflow, or a lakehouse table |
| Slow or gateway-bound source hit by many queries | Ingestion dataflow, then transformation on top [S1834] |
| Direct Lake model | Lakehouse or warehouse pipeline; dataflow Gen2 can write there [S1827, S1833] |
| Author cannot write to the lake | Import tables in the model [S1827] |
| Pro-only tenant with no Fabric capacity | Gen1 dataflow, or the model [S1834] |
| Heavy business calculations | DAX measures, not either layer (Inference) |

## Layering pattern

Microsoft's reuse guidance: split extraction (staging) from transformation. Staging dataflows copy source data as is. Transformation dataflows build the shared tables. Models read the final layer [S1834].

Benefit: a slow on-premises source is queried once. Later layers read from storage and do not call the gateway again.

## Common mistakes

- One giant dataflow that does everything, so no one can reuse its pieces.
- Building a new Gen1 dataflow in a Fabric tenant out of habit.
- Duplicating the same query in five models.
- Putting row-level business rules in a dataflow when they belong in the model.

## Limits and version notes

Gen1 to Gen2 upgrade guidance exists on Learn. An in-place Dataflows Upgrade Wizard, which keeps each dataflow's ID, name, schedule, and connections, is in preview as of 2026-10-09 [S2938]. The destination list for Gen2 grows; confirm before design [S1833]. Compare also the semantic-model domain pages when written.

## See also

- [Import vs DirectQuery vs Direct Lake](23_import_vs_directquery_vs_direct_lake.md)
- [Workspace design](23_workspace_design.md)
