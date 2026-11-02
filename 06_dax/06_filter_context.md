---
id: 06.filter_context
title: Row context, filter context, and query context
domain: dax
type: concept
level: beginner
tags: [dax, filter-context, measure]
summary: Explains the three DAX contexts, how visuals and slicers create filter context, and how relationships carry it between tables.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S652, S653, S656, S660]
references: []
related: [06.calculate_context_transition, 05.filter_direction_ambiguity, 06.dax_basics]
---

# Row context, filter context, and query context

## Purpose
Every DAX result depends on the context it is evaluated in. Learn the contexts and most formulas become predictable.

## Key facts
- Fact: Row context means "the current row". It exists in a calculated column and inside iterator functions (S652, S653).
- Fact: Filter context is the set of values allowed in each column, including filters propagated through relationships. It is used to evaluate measures (S653).
- Fact: Query context is the subset of data a cell implicitly gets from row and column headers, slicers, and report filters (S652).
- Fact: Filter context applies in addition to row context; it does not replace it (S656).
- Fact: A row context iterates rows but filters nothing. Only a context transition turns it into a filter (S660).

## Example
A matrix shows Sales by Year and Region. For the cell (2025, West), the measure `SUM ( Sales[Amount] )` sees Year = 2025 and Region = West. The grand total cell has no filters on those columns, so it sums everything.

## How filters get there
1. Visual fields on rows, columns, legend.
2. Slicers, visual, page, and report filters.
3. Cross-filtering from other visuals.
4. CALCULATE filter arguments inside the formula (see [CALCULATE](06_calculate_context_transition.md)).
5. Relationships: a filter on Product flows to Sales along a one-to-many link (see [filter direction](../05_data_modeling/05_filter_direction_ambiguity.md)).

## Row context details
- A calculated column `= [Freight] + [Tax]` reads the current row's values (S652).
- RELATED follows a relationship from the current row to the one side (S652).
- Nested iterators have several row contexts, one per loop. EARLIER and EARLIEST read an outer loop; variables are the modern alternative (S652).

## Checking context in a formula
| Need | Function |
|---|---|
| One value selected? | HASONEVALUE, SELECTEDVALUE |
| Column filtered directly? | ISFILTERED |
| Filtered through relationships too? | ISCROSSFILTERED |
| At which hierarchy level? | ISINSCOPE |
See the [information functions](../references/dax/06_functions_information.md).

## Common mistakes
- Using a column reference in a measure without an aggregation. A bare column needs row context.
- Expecting a slicer on one fact table to filter an unrelated one.
- Forgetting that totals evaluate the same formula with fewer filters, not a sum of the rows.

## See also
- [CALCULATE and context transition](06_calculate_context_transition.md)
- [Relationships and cardinality](../05_data_modeling/05_relationships_cardinality.md)
