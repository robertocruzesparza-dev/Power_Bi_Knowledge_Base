---
id: 06.ref_functions_table
title: DAX table manipulation functions catalog
domain: dax
type: reference
level: intermediate
tags: [dax, dax-function, catalog]
summary: Catalog of DAX functions that return or reshape tables, grouped by job, verified against the Microsoft Learn category page.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S643]
references: []
related: [06.patterns, 06.calculate_context_transition]
---

# DAX table manipulation functions catalog

Fact: Names come from the Microsoft Learn "Table manipulation functions" page, read 2026-10-07 (S643).

## Build or reshape a table
| Function | Purpose |
|---|---|
| ADDCOLUMNS | Adds calculated columns to a table or expression |
| SELECTCOLUMNS | Returns chosen or computed columns only |
| ROW | One-row table from named expressions |
| DATATABLE | Inline table with typed columns and fixed rows |
| Table Constructor | Curly-brace syntax for an inline table, such as { 1, 2, 3 } |
| GENERATESERIES | One-column table holding an arithmetic series |
| ADDMISSINGITEMS | Adds missing combinations of items to a table |

## Group and summarize
| Function | Purpose |
|---|---|
| SUMMARIZE | Summary table over groups; use mainly to list groups |
| SUMMARIZECOLUMNS | Summary table over groups with filters; used by report queries |
| GROUPBY | Groups rows; no implicit CALCULATE; pairs with CURRENTGROUP |
| CURRENTGROUP | The rows of the current group inside GROUPBY |
| ROLLUP, ROLLUPGROUP, ROLLUPADDISSUBTOTAL, ROLLUPISSUBTOTAL | Add subtotal rows to SUMMARIZE or SUMMARIZECOLUMNS |
| IGNORE | Omits expressions from the blank check in SUMMARIZECOLUMNS |
| TOPN | Top N rows by an expression |

## Distinct, set, and join
| Function | Purpose |
|---|---|
| DISTINCT (column) | One-column table of distinct values |
| DISTINCT (table) | Table with duplicate rows removed |
| VALUES | Distinct values of a column or table, including the blank row if one is added by a relationship |
| UNION | Combines two tables |
| INTERSECT | Rows in both tables, keeping duplicates |
| EXCEPT | Rows in the first table not in the second |
| CROSSJOIN | Cartesian product |
| GENERATE, GENERATEALL | For each row of table 1, evaluate table 2 and combine; GENERATEALL keeps rows with empty results |
| NATURALINNERJOIN, NATURALLEFTOUTERJOIN | Joins on columns with matching names and lineage |
| SUBSTITUTEWITHINDEX | Left semijoin that replaces values with an index |

## Other
- FILTERS: values applied directly as filters to a column.
- TREATAS: applies a table as filters to columns of an unrelated table (virtual relationship).
- DETAILROWS: runs a measure's Detail Rows Expression.

## Notes
- Inference: ADDCOLUMNS plus SUMMARIZE or VALUES is the safer pattern than adding extension columns inside SUMMARIZE, because GROUPBY and SUMMARIZE treat context differently (S630).
- Fact: Calculated tables are always Import and cannot change storage mode (see [composite models](../../05_data_modeling/05_composite_models.md)).
