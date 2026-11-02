---
id: 04.m_function_categories
title: M function categories and how to find a function
domain: power_query_m
type: reference
level: intermediate
tags: [m-language, power-query, catalog, reference]
summary: The main M function categories with approximate counts, naming conventions, and links to the catalog files that list each function.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332]
references: [../references/power_query_m/04_m_functions_table_part1.md, ../references/power_query_m/04_m_functions_table_part2.md, ../references/power_query_m/04_m_functions_list.md, ../references/power_query_m/04_m_functions_text_number.md, ../references/power_query_m/04_m_functions_date_time.md, ../references/power_query_m/04_m_functions_record_value_type.md, ../references/power_query_m/04_m_functions_binary_other.md]
related: [04.m_language_basics, 04.common_transformations]
---

# M function categories and how to find a function

Purpose: find the right M function fast. M function names follow `Category.Action`, so the prefix tells you what the function works on.

## Key facts

- The official function reference groups functions by category pages, such as Table functions, List functions and Text functions (Fact, S332).
- Counts below are approximate. They come from links parsed on 2026-10-07 and include some helper types and constants (Inference).
- Shaping data usually means Table functions. Row-level logic uses Text, Number and Date functions. Column values inside a row use Record and List functions.

## Categories

| Prefix | What it works on | Approx. count | Catalog |
|---|---|---|---|
| `Table.` | Tables: select, add, group, join, pivot | 120 | [part 1](../references/power_query_m/04_m_functions_table_part1.md), [part 2](../references/power_query_m/04_m_functions_table_part2.md) |
| `List.` | Lists: sort, filter, aggregate, generate | 70 to 77 | [list](../references/power_query_m/04_m_functions_list.md) |
| `Text.` | Text: split, trim, replace, pad | 45 | [text and number](../references/power_query_m/04_m_functions_text_number.md) |
| `Number.`, `Int64.`, `Decimal.` | Numbers and math | 53 | same |
| `Date.`, `DateTime.`, `DateTimeZone.`, `Time.`, `Duration.` | Dates, times and spans | 57, 25, 15, 9, 12 | [date and time](../references/power_query_m/04_m_functions_date_time.md) |
| `Record.` | Records | about 24 | [record, value, type](../references/power_query_m/04_m_functions_record_value_type.md) |
| `Value.`, `Type.` | Values, types, metadata, folding hooks | 36, 24 | same |
| `Binary.`, `Combiner.`, `Splitter.`, `Uri.`, `Lines.`, `Comparer.` | Files, combine and split rules | 40, 7, 10, 4, 4, 4 | [binary and other](../references/power_query_m/04_m_functions_binary_other.md) |
| Source functions | `Sql.Database`, `Excel.Workbook`, `Web.Contents`, `OData.Feed`, `Csv.Document`, `Json.Document` and more | many | connector pages |

## How to find a function

1. Decide the object: table, list, text, date. Use that prefix.
2. Scan the catalog file for the verb, for example Remove, Select, Transform, Replace.
3. Open the official page for the signature and examples.
4. In the editor, type the prefix in the formula bar to see suggestions. Use `#shared` in a blank query to list all functions available in your build (Assumption; verify in your build).

## Common mistakes

- Using a Table function on a column. Use `Table.Column(table, "Name")` or `table[Name]` to get a list first.
- Using `List.` aggregate functions when a `Table.Group` step would fold to the source.
- Assuming every function folds. Folding is connector-specific; see [query folding](04_query_folding.md).

## Limits

Descriptions are shortened from the official pages. Cube, accessing-data, error-handling and expression function pages were not cataloged here; use the official reference for those.

## See also

- [M language basics](04_m_language_basics.md)
- [Common transformations](04_common_transformations.md)
