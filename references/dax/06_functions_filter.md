---
id: 06.ref_functions_filter
title: DAX filter functions catalog
domain: dax
type: reference
level: intermediate
tags: [dax, dax-function, filter-context, catalog]
summary: Catalog of DAX filter and window functions, with one-line purposes, verified against the Microsoft Learn category page.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S641, S640, S2830]
references: []
related: [06.calculate_context_transition, 06.filter_context]
---

## Table of Contents

- [Context-changing functions](#context-changing-functions)
- [Lookup and selection](#lookup-and-selection)
- [Window functions](#window-functions)
- [Visual calculation functions](#visual-calculation-functions)
- [Notes](#notes)

# DAX filter functions catalog

Fact: Names and purposes below come from the Microsoft Learn "Filter functions" page, read on 2026-10-07 (S641). The set grows with each release, so check the live page for new entries.

## Context-changing functions
| Function | Purpose |
|---|---|
| CALCULATE | Evaluates an expression in a modified filter context |
| CALCULATETABLE | Same, but the expression returns a table |
| FILTER | Returns the rows of a table that satisfy a condition |
| ALL | All rows of a table or all values of a column; ignores existing filters |
| ALLEXCEPT | Removes filters on a table except on the listed columns |
| ALLNOBLANKROW | Like ALL on a parent table, but excludes the blank row |
| ALLSELECTED | Removes filters from the current query's rows and columns but keeps outer slicer or page filters |
| ALLCROSSFILTERED | Clears all filters applied to a table |
| REMOVEFILTERS | Clears filters from tables or columns; cannot return a table (unverified detail: check the function page) |
| KEEPFILTERS | Intersects a new filter with the existing one instead of replacing it |
| EARLIER | Value of a column from an outer row context |
| EARLIEST | Value from the outermost row context |

## Lookup and selection
| Function | Purpose |
|---|---|
| LOOKUPVALUE | Returns a value from the row matching all search conditions |
| SELECTEDVALUE | Returns the single value in context, else an alternate result |

## Window functions
These return rows relative to the current row inside partitions. They power running totals, ranks, and moving averages in measures and calculated columns (S641).
| Function | Purpose |
|---|---|
| WINDOW | Rows inside a given interval |
| OFFSET | One row before or after the current row by a given offset |
| INDEX | Row at an absolute position in a partition |
| RANK | Rank of a row within an interval |
| ROWNUMBER | Unique rank of a row within an interval |
| ORDERBY | Sort columns for a window function |
| PARTITIONBY | Partition columns for a window function |
| MATCHBY | Columns that identify the current row |

## Visual calculation functions
Fact: These are marked for visual calculations only (S641). Visual calculations are a Desktop feature that works on the visual matrix, not on model tables.
- FIRST, LAST, NEXT, PREVIOUS: read a value from another row of an axis.
- LOOKUP and LOOKUPWITHTOTALS: look up a value under given filters.
- RANGE: interval of rows relative to the current row; a shortcut for WINDOW.
- MOVINGAVERAGE and RUNNINGSUM: moving average and running sum along an axis.

## Notes
- Fact: GROUPBY is discouraged in visual calculations because it likely returns meaningless results (S630).
- Inference: Prefer REMOVEFILTERS over ALL when the goal is only to clear filters, because the name states the intent. ALL also works as a table function.
- See [CALCULATE and context transition](../../06_dax/06_calculate_context_transition.md) for how modifiers combine.
