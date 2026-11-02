---
id: 06.dax_basics
title: DAX basics and calculation types
domain: dax
type: concept
level: beginner
tags: [dax, measure, semantic-model]
summary: Introduces Data Analysis Expressions (DAX), the five places you write it, basic syntax, and how to choose between them.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S652, S653, S656]
references: []
related: [06.filter_context, 06.measures_columns_variables, 06.function_catalog]
---

# DAX basics and calculation types

## Purpose
DAX is the formula language of Power BI semantic models, Analysis Services, and Power Pivot. It defines calculations and row-level security rules (S653).

## Key facts
- Fact: A formula is built from model objects (tables, columns, measures), functions, operators, and constants (S653).
- Fact: A scalar is one value of any data type. Functions can also return tables (S653).
- Fact: Column references look like Sales[Amount]; table names with spaces use quotes, 'Sales Order'[Amount]. Measure references use square brackets only, [Total Sales].
- Fact: VAR is a keyword, not a function. It stores an expression result under a name, and RETURN outputs the final expression (S652, S653).

## Where you write DAX
| Place | Evaluated | Stored |
|---|---|---|
| Measure | At query time, in filter context | Formula only |
| Calculated column | At refresh, row by row | Values in the model |
| Calculated table | At refresh | Values in the model (Import) |
| Visual calculation | On the visual's data | In the report visual |
| DAX query (EVALUATE) | When run, in DAX query view | Not stored |
Row-level security rules and user-defined functions are also DAX. See [measures, columns, and variables](06_measures_columns_variables.md).

## Example
```dax
Total Sales = SUM ( Sales[SalesAmount] )
Store Sales = CALCULATE ( [Total Sales], Channel[ChannelName] = "Store" )
```
The second measure evaluates the first with a filter on channel. This is the pattern from Microsoft's DAX basics tutorial (S656).

## Syntax tips
1. Name, equals sign, expression.
2. Separate arguments with commas (locale settings can change list separators in some clients; unverified here).
3. Format the code: one argument per line for long formulas.
4. Use comments: // line, -- line, /* block */.

## Common mistakes
- Treating DAX like Excel cell formulas. DAX works on columns and tables, and context decides the result (S652).
- Writing everything as calculated columns when a measure is enough.
- Missing the filter context idea. Read [filter context](06_filter_context.md) first.

## See also
- [Filter context and row context](06_filter_context.md)
- [CALCULATE and context transition](06_calculate_context_transition.md)
- [Function catalog](06_function_catalog.md)
