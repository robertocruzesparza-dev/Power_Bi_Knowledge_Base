---
id: 06.window_visual_calcs
title: Window functions and visual calculations
domain: dax
type: concept
level: advanced
tags: [dax, dax-function, dax-pattern, desktop]
summary: Introduces DAX window functions (WINDOW, OFFSET, INDEX, RANK, ROWNUMBER) and the visual-calculation-only functions that work on a visual's matrix.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S641, S651, S630, S2830, S2844]
references: [../references/dax/06_functions_filter.md]
related: [06.patterns, 06.function_catalog]
---

# Window functions and visual calculations

## Purpose
Window functions return rows positioned relative to the current row. They replace older EARLIER and FILTER-over-ALL patterns for running totals, moving averages, and ranks.

## Key facts
- Fact: The window family is WINDOW, OFFSET, INDEX, RANK, and ROWNUMBER, helped by ORDERBY, PARTITIONBY, and MATCHBY (S641).
- Fact: WINDOW returns multiple rows in an interval. OFFSET returns one row before or after the current row. INDEX returns the row at an absolute position (S641).
- Fact: Visual calculations are DAX that run on the visual's own data. Functions marked as visual-calculation-only are FIRST, LAST, NEXT, PREVIOUS, LOOKUP, LOOKUPWITHTOTALS, RANGE, MOVINGAVERAGE, RUNNINGSUM (S641).
- Fact: CALCULATE lists visual calculations as a supported place; GROUPBY is discouraged there (S651, S630).

## How the parts fit
1. relation: the table of rows to look across (often ALLSELECTED of the visual's columns).
2. ORDERBY: sort within each partition.
3. PARTITIONBY: restart the window for each value of these columns.
4. MATCHBY: columns that identify the current row when order alone is ambiguous.

## Example (model measure style)
Previous month's sales shown beside the current one:
```dax
Prev Month Sales =
CALCULATE ( [Total Sales], OFFSET ( -1, ALLSELECTED ( 'Date'[Year], 'Date'[Month] ), ORDERBY ( 'Date'[Year], ASC, 'Date'[Month], ASC ) ) )
```
Check argument order against the function page; signatures are detailed and unverified here beyond names.

## Visual calculation example (inside a visual)
```dax
Running = RUNNINGSUM ( [Sales Amount] )
Delta   = [Sales Amount] - PREVIOUS ( [Sales Amount] )
```
These refer to visual fields, not model columns. Inference: they suit presentation logic; keep shared business logic in model measures.

## Common mistakes
- Using a window function with a sort order that is not unique, producing arbitrary results. Add MATCHBY or more ORDERBY columns.
- Expecting visual calculations to be available to other visuals. They live in one visual.
- Rebuilding what time intelligence functions already do.

## Limits and version notes
Fact: visual calculations reached general availability in the May 2026 update (S2844). Window functions are older. Availability still depends on your Desktop version.

## See also
- [Filter functions catalog](../references/dax/06_functions_filter.md)
- [Patterns](06_patterns.md)
