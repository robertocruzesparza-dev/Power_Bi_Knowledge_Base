---
id: 23.storage_mode_choice
title: Choosing a table storage mode
domain: patterns_recipes
type: decision
level: intermediate
tags: [storage-mode, composite-model, decision-guide, data-modeling]
summary: A decision guide for choosing Import, DirectQuery, Dual, or hybrid storage per table, with the reasoning behind each recommendation.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1828, S1829, S1838, S1827, S1846]
references: []
related: [23.import_vs_directquery_vs_direct_lake, 23.rls_pattern_choice]
---
## Purpose

Storage mode is set per table. It decides where data lives and who runs the query. Pick it deliberately, because changing it later is not a toggle.

## Key facts

- Fact: Import copies data into the model. DirectQuery sends queries to the source at view time. Dual acts as both and lets the engine choose per query [S1829].
- Fact: Hybrid means an Import table with a DirectQuery partition for the newest data, set up through incremental refresh with real-time data [S1829].
- Fact: Microsoft's Dataverse guidance says to import data whenever possible, because DirectQuery reports are usually slower [S1846]. Read it as general advice, not a rule.
- Fact: A model with mixed storage modes is a composite model [S1829].
- Fact: You cannot flip a whole Import model to DirectQuery. Add DirectQuery tables, build a composite model, or rebuild with fold-friendly steps [S1838].

## Decision flow

1. Does the source support DirectQuery? If not, use Import. Check the connector's Capabilities section [S1838].
2. Must users see data newer than your refresh allows, or is the data too large to import? If no, use Import.
3. If yes: use DirectQuery for the large or near real-time fact tables [S1828].
4. Set dimension tables to Dual when they sit in the same source as the DirectQuery fact. Slicers then render from memory and joins stay regular [S1828].
5. Need fast history plus fresh recent rows? Use hybrid tables on the fact [S1828].
6. Lakehouse or warehouse data in Fabric at scale? Consider Direct Lake; see [the three-way comparison](23_import_vs_directquery_vs_direct_lake.md).
7. Need a speedup for DirectQuery visuals that ask for high-level totals? Add Import aggregation tables [S1828].

## Table roles

| Table role | Recommended mode | Why |
|---|---|---|
| Large fact, live data | DirectQuery | Data never imported |
| Dimension joined to a DirectQuery fact | Dual | Avoids limited relationships |
| Dimension from a different source | Import | Cross-source relationships are limited anyway |
| Calculated table | Import | Always import |
| Fact with recent-only freshness need | Hybrid | Import history, live latest |

Source: [S1828].

## Worked example

A retailer has a 4-billion-row Sales fact in Azure SQL and small Product and Date tables. Set Sales to DirectQuery, Product and Date to Dual, add an Import aggregation table at month and category level. Month charts hit memory. Row-level drill reaches SQL. (Pattern from [S1828]; the numbers are illustrative.)

## Common mistakes

- Choosing DirectQuery because "it is always current" without testing source speed.
- Leaving dimensions as Import beside a DirectQuery fact. Relationships become limited, and groupings are pushed to the source as subqueries [S1828].
- Ignoring the 1,000,000-row intermediate result limit in DirectQuery. Premium capacities can raise it [S1838].
- Not educating users that visuals can differ in time and need Refresh [S1838].

## Limits

DirectQuery caches visuals, so a visual may show earlier results until refresh. Visuals are not always time-consistent [S1838]. Case-insensitive engine plus case-sensitive source can produce undefined results; normalize casing [S1838].

## See also

- [Import vs DirectQuery vs Direct Lake](23_import_vs_directquery_vs_direct_lake.md)
- [RLS pattern choice](23_rls_pattern_choice.md)
