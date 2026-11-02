---
id: 05.calculation_groups
title: Calculation groups
domain: data_modeling
type: how-to
level: advanced
tags: [calculation-group, dax, measure, semantic-model]
summary: Explains calculation groups and items, SELECTEDMEASURE, precedence, sideways recursion, and typical time intelligence and currency patterns.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S616, S617, S611]
references: []
related: [06.time_intelligence, 06.calculate_context_transition, 05.direct_lake]
---

# Calculation groups

## Purpose
A calculation group applies one DAX pattern to many measures. Instead of writing Sales PY, Orders PY, and Margin PY, you write one "PY" calculation item that wraps any measure.

## Key facts
- Fact: Calculation groups need tabular compatibility level 1500 or higher. All Power BI semantic models meet this (S617).
- Fact: A group is a table with one text column. Each row is a calculation item holding a DAX expression (S616, S617).
- Fact: The item is applied when it is selected in a slicer or filter, or used to group a visual (S617).
- Fact: Creating one in Desktop's Model view asks you to enable "discourage implicit measures". Calculation groups can also be authored in TMDL view or with XMLA tools such as Tabular Editor (S616).
- Fact: A calculation group applies only when exactly one of its items is in filter context (S617).

## Helper functions (S617)
| Function | Returns |
|---|---|
| SELECTEDMEASURE | The measure currently being evaluated |
| SELECTEDMEASURENAME | Its name as text |
| ISSELECTEDMEASURE | TRUE if it is in a list of measures |
| SELECTEDMEASUREFORMATSTRING | Its format string |

These work only inside calculation item expressions. Prefer ISSELECTEDMEASURE over name comparison, because name text is not updated if you rename the measure (S617 via the SELECTEDMEASURENAME page).

## Example
Group "Time Intelligence", column "Time Calculation", precedence 20 (S617):

```dax
-- Current
SELECTEDMEASURE ()
-- YTD
CALCULATE ( SELECTEDMEASURE (), DATESYTD ( DimDate[Date] ) )
-- PY
CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( DimDate[Date] ) )
-- YOY
SELECTEDMEASURE ()
    - CALCULATE ( SELECTEDMEASURE (), 'Time Intelligence'[Time Calculation] = "PY" )
```

Call one item from a measure:

```dax
Orders YOY% =
CALCULATE ( [Orders], 'Time Intelligence'[Time Calculation] = "YOY%" )
```

Items can reference sibling items by filtering the group column. This is called sideways recursion; other recursion is not supported (S617).

## Precedence
When a model has two groups and both have a selected item, the higher precedence is applied first (outermost) (S617).
- Group A precedence 200, item SELECTEDMEASURE() * 2. Group B precedence 100, item SELECTEDMEASURE() + 2. Measure = 10.
- Result: ( (10) + 2 ) * 2 = 24, not 14.
- With CALCULATE inside items, the higher precedence group can change the filters the lower one sees. Example: YTD (20) with Daily Average (10) divides the YTD value by the count of YTD days (S617).
- Only the highest precedence group's dynamic format string is applied; a measure's own dynamic format string ranks below any group (S617).

## Steps to build one in Desktop
1. Model view, Calculation group, accept the implicit measure prompt (S616).
2. Rename the group and its column. Add items; use SELECTEDMEASURE in each.
3. Set precedence in Properties if you have several groups.
4. Test in a matrix with the column on Columns, or in DAX query view.
5. Optionally add selection expressions to control multi-select behavior (S616).

## Common mistakes
- Relying on implicit measures (a summed column). Desktop asks you to discourage them when you add a group (S616); inference: create explicit measures instead.
- Expecting two items from the same group to apply at once.
- Ignoring precedence when mixing time and currency groups.
- Applying a time item to a ratio measure without checking the result makes sense.

## Limits and version notes
- Fact: Models using Direct Lake tables can include calculation groups, which implicitly create calculated tables (S611).

## See also
- [Time intelligence](../06_dax/06_time_intelligence.md)
- [CALCULATE and context transition](../06_dax/06_calculate_context_transition.md)
