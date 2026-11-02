---
id: 06.calculate_context_transition
title: CALCULATE and context transition
domain: dax
type: concept
level: intermediate
tags: [dax, filter-context, dax-function, measure]
summary: Shows how CALCULATE changes filter context, how filter arguments and modifiers combine, and how context transition works in iterators and columns.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S651, S660, S641]
references: [../references/dax/06_functions_filter.md]
related: [06.filter_context, 06.errors_troubleshooting, 05.calculation_groups]
---

# CALCULATE and context transition

## Purpose
CALCULATE evaluates an expression in a modified filter context. It is the most important DAX function (S651).

## Key facts
- Fact: Each filter argument either adds a filter (column not yet filtered) or overwrites the existing filter on those columns (S651).
- Fact: KEEPFILTERS wraps a filter so it intersects with the existing one instead of overwriting (S651).
- Fact: CALCULATE without filter arguments still does one job: it transitions row context to filter context (S651).
- Fact: Referencing a model measure inside row context transitions automatically, because a measure reference is wrapped in a hidden CALCULATE (S651, S660).
- Fact: CALCULATE is not supported in calculated columns or RLS rules in DirectQuery mode (S651).
- Fact: CALCULATETABLE does the same for table expressions (S651).

## Filter modifiers (S651)
| Modifier | Effect |
|---|---|
| REMOVEFILTERS | Clear filters on columns or tables |
| ALL, ALLEXCEPT, ALLNOBLANKROW | Clear filters; also return tables |
| KEEPFILTERS | Add without overwriting |
| USERELATIONSHIP | Use an inactive relationship; the active one is switched off for the call |
| CROSSFILTER | Change direction or disable a relationship |
Microsoft advises REMOVEFILTERS where the tool supports it (S651).

## Example: percent of channel total
```dax
Share of All Channels =
DIVIDE (
    [Total Sales],
    CALCULATE ( [Total Sales], REMOVEFILTERS ( 'Sales Order'[Channel] ) )
)
```
The denominator clears the channel filter only. Other filters stay (S651).

## Example: context transition in a calculated column
```dax
Customer Segment =
IF (
    CALCULATE ( SUM ( Sales[Sales Amount] ), ALLEXCEPT ( Customer, Customer[CustomerKey] ) ) < 2500,
    "Low", "High"
)
```
For each customer row, the row context becomes a filter on that customer, so the sum is that customer's revenue (S651).

## How transition behaves (S660)
1. It takes the current row and filters all columns of the iterated table to that row's values.
2. In a calculated column the row context covers the whole table, so a measure call filters every column. Cost grows with table width.
3. Replacing a measure reference by its inline expression removes the hidden CALCULATE, so no transition occurs and the result is the unfiltered total.
4. In a running total, calling a measure inside an iterator over dates restricts each row to its own date. Read the outer context with MAX of the date instead (S660).

## Evaluation order (inference from S651)
Filter arguments evaluate in the outer context first. Then all filters combine and the expression evaluates once.

## Common mistakes
- Boolean filters like Sales[Qty] > 5 are shorthand for filtering all values of one column. They replace existing filters on that column.
- Using FILTER over a whole table where a column filter works. It is slower and can hold more rows than needed.
- Assuming a measure and a copied expression behave the same in a row context.
- Nested CALCULATE calls with conflicting filters; the inner one wins on its own columns.

## See also
- [Filter functions catalog](../references/dax/06_functions_filter.md)
- [Common errors](06_errors_troubleshooting.md)
- [Calculation groups](../05_data_modeling/05_calculation_groups.md)
