---
id: 06.measures_columns_variables
title: Measures, calculated columns, and variables
domain: dax
type: how-to
level: beginner
tags: [dax, measure, best-practice]
summary: Decision guide for measure versus calculated column versus calculated table, plus how to use VAR and RETURN for readable, faster formulas.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S652, S653, S660, S661]
references: []
related: [06.dax_basics, 06.best_practices, 06.errors_troubleshooting]
---

# Measures, calculated columns, and variables

## Purpose
Pick the right calculation type and write it in a clear, efficient way.

## Key facts
- Fact: A measure is computed at query time in filter context and stores no values. A calculated column is computed at refresh in row context and stores values in the model (S652, S653).
- Fact: Calculated tables are computed at refresh and are Import tables.
- Fact: Quick measures generate DAX for common cases such as rank and difference from baseline (S653).
- Fact: Report measures can be added to a live connection report to a Power BI or Analysis Services model, and are stored in the report (S653).

## Decision guide
| Need | Use |
|---|---|
| Summarize, ratio, change with slicers | Measure |
| Slice, group, or filter by the result | Calculated column (or better, shape upstream) |
| Row-level text or flag that never aggregates | Calculated column |
| A lookup, date, or bridge table | Calculated table, or load from source |
| Rank or running total shown in one visual | Visual calculation |

Inference: Prefer to compute columns in Power Query or the source. This keeps columns compressed well and refresh logic in one place. Calculated columns on DirectQuery tables are limited (see [storage modes](../05_data_modeling/05_storage_modes.md)).

## Implicit versus explicit measures
An implicit measure is a column dropped into a visual and summed by the field well. An explicit measure is a named DAX formula. Explicit measures can be reused, formatted once, and used in calculation groups. Desktop's calculation group setup asks you to discourage implicit measures (S616 via [calculation groups](../05_data_modeling/05_calculation_groups.md)).

## Variables
```dax
Sales vs Prior Year % =
VAR Current = [Total Sales]
VAR Prior   = CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
RETURN
    DIVIDE ( Current - Prior, Prior )
```
- Fact: A variable can hold any scalar type, including a table (S652).
- Fact: A variable is evaluated once, where it is defined, in the context where it is defined. That is the main trap: it does not see later CALCULATE filter changes. Inference from DAX semantics; test when mixing VAR with CALCULATE.
- Benefits: readability, one evaluation instead of repeated ones, easier debugging by returning a variable.

## Steps to debug a measure
1. Return each variable in turn with RETURN.
2. Test in DAX query view with EVALUATE.
3. Put the measure in a table with the fields that give the suspect context.
4. Use EVALUATEANDLOG when you need to log intermediate values (see [catalog](../references/dax/06_functions_aggregation_logical.md)).

## Common mistakes
- Using a calculated column that references a measure. It triggers context transition for every row (S660).
- Repeating the same subexpression many times instead of using VAR (S661 shows repeated evaluation can cost extra storage engine requests).
- Naming measures like columns. Use clear names and a display folder.

## See also
- [DAX best practices](06_best_practices.md)
- [CALCULATE](06_calculate_context_transition.md)
