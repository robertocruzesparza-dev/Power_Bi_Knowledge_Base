---
id: 06.patterns
title: Common DAX patterns
domain: dax
type: how-to
level: intermediate
tags: [dax, dax-pattern, measure, example]
summary: Reusable DAX recipes for percent of total, ranking, top N, running totals, virtual relationships, distinct counts, and parameter tables.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S641, S643, S651, S660, S604]
references: [../references/dax/06_functions_table.md]
related: [06.calculate_context_transition, 06.time_intelligence]
---

## Table of Contents

- [Percent of total](#percent-of-total)
- [Ranking and top N](#ranking-and-top-n)
- [Running total](#running-total)
- [Virtual relationship](#virtual-relationship)
- [Distinct count across a bridge](#distinct-count-across-a-bridge)
- [Parameter table](#parameter-table)
- [Show only when one item selected](#show-only-when-one-item-selected)
- [Notes](#notes)

# Common DAX patterns

Model assumed: Sales fact; Product, Customer, Date dimensions with one-to-many relationships. Test each pattern on your model; these are standard recipes, not guarantees.

## Percent of total
```dax
% of All Products =
DIVIDE ( [Total Sales], CALCULATE ( [Total Sales], REMOVEFILTERS ( Product ) ) )
```
Use ALLSELECTED instead of REMOVEFILTERS to keep slicer filters and compare with the visible total (S641).

## Ranking and top N
```dax
Product Rank = RANKX ( ALLSELECTED ( Product[Name] ), [Total Sales] )
Top 5 Sales =
CALCULATE ( [Total Sales], TOPN ( 5, ALLSELECTED ( Product ), [Total Sales] ) )
```
- RANKX ranks a value against a table (see [statistical catalog](../references/dax/06_functions_statistical_relationship.md)). TOPN returns the top rows (S643).
- Ties: TOPN can return more than N rows when values tie. Add a tie-breaker expression.
- For a visual-only ranking, a Top N visual filter is simpler.

## Running total
```dax
Running Sales =
CALCULATE ( [Total Sales], FILTER ( ALL ( 'Date'[Date] ), 'Date'[Date] <= MAX ( 'Date'[Date] ) ) )
```
MAX reads the outer date; calling a measure in an iterator over dates would give each row only its own date (S660). Alternatives: DATESYTD for year-to-date, or the WINDOW family and visual calculations (see [window functions](06_window_visual_calcs.md)).

## Virtual relationship
```dax
Sales for Selected Region =
CALCULATE ( [Total Sales], TREATAS ( VALUES ( RegionSlicer[Region] ), Customer[Region] ) )
```
TREATAS applies one table's values as filters on columns of another, with no relationship (S643). Good for disconnected slicers.

## Distinct count across a bridge
Avoid permanent bi-directional filtering. Switch it per measure (S604):
```dax
Countries Sold =
CALCULATE ( DISTINCTCOUNT ( Customer[Country] ), CROSSFILTER ( Customer[CustomerKey], Sales[CustomerKey], BOTH ) )
```

## Parameter table
Create a one-column table with an inline constructor, then read the choice:
```dax
Metric Choice = { "Sales", "Margin", "Orders" }
Selected Metric =
SWITCH ( SELECTEDVALUE ( 'Metric Choice'[Value], "Sales" ),
    "Sales", [Total Sales], "Margin", [Total Margin], "Orders", [Order Count] )
```
Field parameters and calculation groups are the built-in alternatives.

## Show only when one item selected
```dax
Product Detail = IF ( HASONEVALUE ( Product[Name] ), [Total Sales], BLANK () )
```

## Notes
- Fact: Disconnected tables never filter facts on their own; the measure does the work.
- Inference: Replace FILTER ( ALL ( table ), ... ) with a column-level filter when only one column is tested; it reduces the rows scanned.
- Semi-additive measures (balances): use LASTDATE or CLOSINGBALANCE* ([time intelligence](06_time_intelligence.md)).
- Avoid IFERROR-wrapped divides; use DIVIDE.
