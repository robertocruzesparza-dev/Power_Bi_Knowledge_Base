---
id: 05.storage_modes
title: Storage modes compared (Import, DirectQuery, Dual, Hybrid, Live connection)
domain: data_modeling
type: comparison
level: intermediate
tags: [data-modeling, storage-mode, semantic-model, limits]
summary: Compares table storage modes in Power BI semantic models, how Dual and Hybrid work, and the rules for changing a mode.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S607, S610, S622, S623, S2510, S2502]
references: []
related: [05.composite_models, 05.direct_lake, 05.aggregations, 05.incremental_refresh_basics]
---

# Storage modes: Import, DirectQuery, Dual, Hybrid, Live connection

## Purpose
Storage mode is a property of each table. It decides where data lives and which engine answers a query.

## Key facts
| Mode | Where data lives | Best for |
|---|---|---|
| Import | In the model cache (Vertipaq) | Speed, most sources, full DAX |
| DirectQuery | At the source; queried at view time | Very large or near-real-time facts |
| Dual | Both; engine picks per query | Dimensions beside DirectQuery facts |
| Hybrid | Import partitions plus one DirectQuery partition | Recent data live, history cached |
| Direct Lake | Delta tables in OneLake, loaded on demand | Large Fabric lake data; see [Direct Lake](05_direct_lake.md) |
| Live connection | A remote model; no local model | Thin reports over shared models |

- Fact: A model with more than one storage mode is a composite model (S607, S610).
- Fact: DirectQuery translates DAX to the native query language of the source, such as SQL (S607).
- Fact: Dual tables share the functional limits of DirectQuery tables, including limited M and restricted DAX in calculated columns (S607).
- Fact: Hybrid is created by an incremental refresh policy with real-time data; the latest partition is DirectQuery (S607, S620).
- Fact: A Live connect report holds no local model and is sometimes called a thin report. Measures you add are stored in the report (S607).

## How Dual helps
In a source group, relationships between Import and DirectQuery tables are limited, so joins cannot be pushed to the source. Setting the dimensions to Dual keeps relationships regular (S607). When you convert a DirectQuery table to Import, Desktop offers to set related one-side tables to Dual and walks only toward the one side of one-to-many links (S607).

## Changing a mode
- Fact: For most tables you set the mode only when you add the table (S607).
- Fact: A DirectQuery table can change to Import or Dual. After that you cannot change it back to DirectQuery, except in web modeling and live edit in Desktop, which have version control (S607).
- Fact: You cannot flip a whole Import model to DirectQuery. Add DirectQuery tables, build a composite model, or rebuild with fold-friendly steps (S622).
- Fact: Direct Lake on OneLake tables can convert to Import with semantic link labs in a Fabric notebook (S607).

## DirectQuery implications (S622)
- Visuals can show cached results until Refresh is used, and different visuals can query at slightly different times.
- A query or intermediate result over 1,000,000 rows fails. Premium capacities can raise this (Max Intermediate Row Set Count).
- Case-insensitive engine against a case-sensitive source can yield undefined results; normalize casing.
- The per-file DirectQuery connection limit defaults to 10 per source; service limits depend on SKU.
- Mitigations listed by Microsoft: aggregations, hybrid tables, Dual dimensions, dynamic M parameters, query caching.

## Choosing
1. Can the data fit and refresh in time? Use Import.
2. Is data huge or must be live? Use DirectQuery for facts, Dual for dimensions.
3. Is the data in a Fabric lake? Consider Direct Lake.
4. Need both? Build a composite model, with care (see [composite models](05_composite_models.md)).

## Common mistakes
- Setting dimensions to Import beside DirectQuery facts, creating limited relationships.
- Choosing DirectQuery because "real time sounds good" without testing source speed.
- Expecting to revert a table to DirectQuery after switching.

## Limits and version notes
DirectQuery limits and defaults above come from current docs and can change (S622).

## See also
- [Composite models](05_composite_models.md)
- [Aggregations](05_aggregations.md)
- [Incremental refresh basics](05_incremental_refresh_basics.md)
