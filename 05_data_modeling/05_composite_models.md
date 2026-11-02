---
id: 05.composite_models
title: Composite models
domain: data_modeling
type: concept
level: advanced
tags: [data-modeling, composite-model, storage-mode, relationship]
summary: Explains composite models, source groups, cross source group relationships, and Microsoft's design recommendations and risks.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S603, S607, S608, S609, S610, S623]
references: []
related: [05.storage_modes, 05.relationships_cardinality, 05.aggregations, 05.direct_lake]
---

# Composite models

## Purpose
A composite model mixes storage modes or data sources in one semantic model. It can combine fast cached dimensions with live facts, or join several DirectQuery sources.

## Key facts
- Fact: Set storage mode per table, except calculated tables, which are always Import (S608).
- Fact: Composite models can integrate multiple DirectQuery sources and can include aggregations (S610, S623).
- Fact: You can also build a composite model on top of another published semantic model: connect, then choose Make changes to this model. The connection becomes DirectQuery to the remote model, you can add tables, and you can override some column properties such as format and display name (S607, S609).
- Fact: Models with Direct Lake tables are live edited in Desktop; adding Import tables is done in web modeling, and adding DirectQuery tables uses XMLA tools (S609).

## How queries are routed (S608)
1. Only Import or Dual tables: answered from cache. Fastest.
2. Dual plus DirectQuery tables from one source: one or more native queries to the source. Relationships are regular.
3. Dual or hybrid tables from one source: cache for import partitions, native queries for the rest.
4. Anything else, including an Import table related to a DirectQuery table: cross source group, limited relationships. Groupings from non-DirectQuery tables are sent to the source as materialized subqueries, which can be slow for large sets.

## Recommended table roles (S608)
| Role | Mode | Reason |
|---|---|---|
| Large or live fact | DirectQuery | Never imported |
| Dimension beside DirectQuery fact | Dual | Fast slicers, regular relationships |
| Dimension not used with DirectQuery facts | Import | Cache speed |
| Fact needing live tail plus fast history | Hybrid | Import partitions plus DirectQuery partition |

## Cross source group relationships (S608)
- Use low-cardinality relationship columns, under about 50,000 unique values.
- Avoid long text columns; keep cardinality times average text length under 1,000,000 characters.
- Relate at a coarser grain, such as month key instead of date.
- Keep paths short; Desktop does not fully validate these, so ambiguity can slip in.
- These relationships are limited (see [relationships](05_relationships_cardinality.md)), so unmatched rows drop and RELATED cannot read the one side (S603).

## Risks
- Security: data from several sources meets in one model, so review credentials, privacy levels, and RLS design before publishing. Unverified here; check Microsoft guidance.
- Complexity: more refresh paths, more failure modes, harder tuning.
- Results can be valid yet different when relationships cross source groups (S608).

## Common mistakes
- Using composite as the default instead of a single clean Import model.
- Leaving shared dimensions in Import with DirectQuery facts.
- Building wide many-to-many joins across sources.

## See also
- [Storage modes](05_storage_modes.md)
- [Aggregations](05_aggregations.md)
- [Direct Lake](05_direct_lake.md)
