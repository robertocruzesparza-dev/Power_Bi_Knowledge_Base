---
id: 04.m_language_basics
title: M language basics: syntax and evaluation
domain: power_query_m
type: concept
level: intermediate
tags: [m-language, power-query, cheatsheet]
summary: Core M syntax: values, let and in, records, lists, tables, functions, operators, comments, errors, and the lazy evaluation model.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S322, S333]
references: [../references/power_query_m/04_m_functions_table_part1.md]
related: [04.m_function_categories, 04.power_query_editor, 04.parameters_and_custom_functions]
---

# M language basics: syntax and evaluation

Purpose: read and write simple M by hand. M is the formula language behind every Power Query query.

## Key facts

- M is a mostly pure, higher-order, dynamically typed, partially lazy functional language (Fact, S333).
- Evaluation resembles a spreadsheet: expressions refer to others by name, and the engine works out the order from dependencies (Fact, S333).
- A value is the result of an expression. Expressions are recipes; values are results (Fact, S333).
- M is case sensitive: `Table.SelectRows` works, `table.selectrows` does not (Assumption from widely documented behavior; not re-read in the specification this pass).

## Values and literals (Fact, S333)

| Kind | Example |
|---|---|
| Number | `123` |
| Logical | `true` |
| Text | `"abc"` |
| Null | `null` |
| List | `{1, 2, 3}` |
| Record | `[A = 1, B = 2]` |
| Table | `#table({"A","B"}, {{1,2},{3,4}})` (no literal; built by functions) |
| Function | `(x, y) => (x + y) / 2` |

Lists may be infinite, but a list literal has fixed length. Record fields can refer to each other, for example `[A1 = A2 * 2, A2 = A3 + 1, A3 = 1]`.

## The let expression

```
let
    Source = Sql.Database("server", "db"),
    Filtered = Table.SelectRows(Source, each [Amount] > 100)
in
    Filtered
```

Each line is a named step. The result after `in` is the query's output. Quoted identifiers use `#"My step"`. Steps are not run top to bottom; only what the output needs is evaluated (Fact, S322).

## Other syntax

- Comments: `//` to end of line, `/* ... */` for blocks (Fact, S333).
- `each _` is shorthand for a function with one parameter named underscore; `[Col]` reads a field of the current row.
- Conditionals: `if a then b else c`. `else` is required.
- Error handling: `try expr otherwise fallback`. See [errors and fixes](04_errors_and_fixes.md).
- Item access: `Table{0}` row by position, `Table[Column]` column as list, `Record[Field]`.
- Types: `type text`, `type number`, `Int64.Type`.

## How lazy evaluation matters

Unused steps are never run. That enables query folding, where the engine pushes work to the source. It also means a step can look fine yet never execute until output needs it (Fact, S322).

## Common mistakes

- Forgetting a comma between steps, or adding one after the last step.
- Using `=` for comparison inside `if`; M uses `=` for equality and `<>` for not equal.
- Treating step order as run order.

## See also

- [Function categories](04_m_function_categories.md)
- [Parameters and custom functions](04_parameters_and_custom_functions.md)
- [Common transformations](04_common_transformations.md)
