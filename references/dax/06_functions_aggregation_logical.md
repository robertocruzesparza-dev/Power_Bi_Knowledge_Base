---
id: 06.ref_functions_aggregation_logical
title: DAX aggregation and logical functions catalog
domain: dax
type: reference
level: beginner
tags: [dax, dax-function, catalog]
summary: Catalog of DAX aggregation (SUM, COUNT, X-iterators) and logical (IF, SWITCH, COALESCE) functions with distinctions that trip people up.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S644, S645, S647, S648]
references: []
related: [06.measures_columns_variables, 06.errors_troubleshooting]
---

# DAX aggregation and logical functions catalog

Fact: Names come from the Microsoft Learn category pages read on 2026-10-07 (S644, S645, S647).

## Aggregation: column versions
| Function | Purpose |
|---|---|
| SUM, AVERAGE, MIN, MAX | Aggregate numbers in a column; MIN and MAX also compare two scalars |
| AVERAGEA, MAXA, MINA | Include logical values and numbers stored as text |
| COUNT | Count non-blank values; does not support Boolean |
| COUNTA | Count non-blank values; supports Boolean |
| COUNTBLANK | Count blank cells in a column |
| COUNTROWS | Count rows in a table or table expression |
| DISTINCTCOUNT | Count distinct values (counts the blank as one value) |
| DISTINCTCOUNTNOBLANK | Count distinct values without the blank |
| APPROXIMATEDISTINCTCOUNT | Estimated distinct count, for large DirectQuery sources |
| PRODUCT | Product of the numbers in a column |

## Aggregation: iterator (X) versions
Iterators evaluate an expression per row of a table, then aggregate. They create row context.
- SUMX, AVERAGEX, MAXX, MINX, PRODUCTX: aggregate a per-row expression.
- COUNTX: counts rows where the expression yields a number.
- COUNTAX: counts non-blank results of the expression.

Example: revenue where price and quantity are in different columns.
```dax
Revenue = SUMX ( Sales, Sales[Quantity] * Sales[UnitPrice] )
```

## Logical
| Function | Purpose |
|---|---|
| IF | Returns one value if TRUE, else another |
| IF.EAGER | Same, but always runs both branches (eager plan) |
| SWITCH | Compares an expression to a list of values; SWITCH ( TRUE (), ... ) tests conditions in order |
| IFERROR | Returns an alternate value if the expression errors |
| COALESCE | First argument that is not BLANK |
| AND, OR, NOT | Boolean operators as functions (AND and OR take two arguments only) |
| TRUE, FALSE | Boolean constants |
| BITAND, BITOR, BITXOR, BITLSHIFT, BITRSHIFT | Bitwise operations on numbers |

## Other
- BLANK: returns a blank.
- ERROR: raises an error with a message.
- EVALUATEANDLOG: returns the first argument and writes it to a DAX Evaluation Log event for debugging.
- EXTERNALMEASURE: invokes a measure from a remote model.
- TOCSV, TOJSON: return a table as text.

## Distinctions that matter
- Fact: COUNT ignores Boolean; use COUNTA when a column holds TRUE and FALSE (S644).
- Fact: DIVIDE returns BLANK or an alternate value on division by zero (S648). Prefer it to the / operator when the denominator can be zero.
- Inference: IF.EAGER can help speed in some plans but costs work in both branches; test with Performance Analyzer before use.
- Inference: Avoid IFERROR in hot measures; fix the cause or use DIVIDE and COALESCE.
