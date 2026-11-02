---
id: 06.errors_troubleshooting
title: Common DAX errors and fixes
domain: dax
type: troubleshooting
level: intermediate
tags: [dax, troubleshooting, error-message]
summary: Explains frequent DAX errors, including single-value, multiple-value table, circular dependency, ambiguous path, and wrong-total problems, with fixes.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S652, S662, S663, S664, S603, S660]
references: []
related: [06.calculate_context_transition, 05.filter_direction_ambiguity]
---

# Common DAX errors and fixes

## Purpose
Match a symptom to a cause and a fix.

## Error classes (S652)
Microsoft groups errors as syntactic (missing parenthesis or comma), semantic, and calculation errors. Semantic and calculation causes include: a missing column, table, or function; a type mismatch found at fetch time; wrong number or type of arguments; a reference to a column that has its own error; and a reference to an unprocessed column.

## Symptom table
| Symptom | Likely cause | Fix |
|---|---|---|
| "A single value for column 'X' in table 'Y' cannot be determined" | Measure uses a column with no aggregation and no row context (S664) | Aggregate (MAX, SELECTEDVALUE) or use an iterator |
| "A table of multiple values was supplied where a single value was expected" | VALUES returned several rows and was compared to a scalar (S662) | Use SELECTEDVALUE, or guard with HASONEVALUE |
| Circular dependency detected | Two objects reference each other, often through hidden context transition in calculated columns (S663) | Break the loop, move logic to a measure or Power Query |
| Ambiguous path error | Equal-priority filter paths (S603) | Remove a relationship or use USERELATIONSHIP |
| Total does not equal sum of rows | Measure is non-additive; the total is evaluated with fewer filters | Iterate over the grain with SUMX, or accept |
| Same value on every row | Missing relationship, or filter not reaching the table; or inlined measure lost transition (S660) | Check relationships; call the measure instead of its body |
| Blank where zero expected | No rows in the filter context | Add `+ 0` or COALESCE deliberately, and test performance |
| Visual shows "(Blank)" group | Many-side keys with no match (S603) | Fix the source data |
| Name not found | Typo, deleted object, or unquoted table name with spaces | Quote 'Table Name'; check names |

## Worked example: single value error
Wrong measure: `Line Total = Sales[Qty] * Sales[Price]`. A measure has no row context, so the column is ambiguous.
Fix with an iterator: `Line Total = SUMX ( Sales, Sales[Qty] * Sales[Price] )`.
SQLBI notes the message wording is misleading: the error appears even if the table has one row (S664).

## Circular dependency tips (S663)
1. Two calculated columns that reference each other are the simple case.
2. CALCULATE in a calculated column makes the column depend on all columns of its table, so two such columns can loop.
3. A relationship that involves a calculated column or table can also create a loop.
4. The engine's detection is reliable; find the loop rather than doubting the error.
5. Premium refreshes can surface cycles that were previously missed; for a calculated table using SUMMARIZECOLUMNS an explicit nonempty filter may help (S603).

## Steps for any wrong-number problem
1. Show the measure in a table with its filter fields.
2. Test each VAR by returning it.
3. Check relationships and filter direction.
4. Check for BLANK keys and duplicate dimension keys.
5. Simplify to the smallest failing formula in DAX query view.

## Common mistakes
- Wrapping errors in IFERROR to hide bugs.
- Using / instead of DIVIDE.
- Pasting formulas with curly quotes; DAX may not recognize them (S652 syntax page).

## See also
- [CALCULATE and context transition](06_calculate_context_transition.md)
- [Filter direction and ambiguity](../05_data_modeling/05_filter_direction_ambiguity.md)
