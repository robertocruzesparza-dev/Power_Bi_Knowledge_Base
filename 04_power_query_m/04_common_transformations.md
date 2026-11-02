---
id: 04.common_transformations
title: Common transformations and their M functions
domain: power_query_m
type: how-to
level: beginner
tags: [power-query, m-language, how-to, cheatsheet]
summary: The transformations used most often (filter, split, group, merge, append, pivot, unpivot, fill, replace, change type) with the M function each one generates.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S322, S325, S331, S332]
references: [../references/power_query_m/04_m_functions_table_part1.md, ../references/power_query_m/04_m_functions_table_part2.md]
related: [04.m_function_categories, 04.query_folding, 04.errors_and_fixes]
---

# Common transformations and their M functions

Purpose: map a ribbon command to the M it writes, so you can read, debug and edit generated code. Function names were checked against the official catalog on 2026-10-07 (Fact, S332).

## Cheat sheet

| Task | Ribbon path | M function |
|---|---|---|
| Use first row as headers | Home > Use First Row as Headers | `Table.PromoteHeaders` |
| Set data type | Column header type icon, or Transform > Data Type | `Table.TransformColumnTypes` |
| Keep rows by condition | Column filter menu | `Table.SelectRows` |
| Remove columns | Home > Remove Columns | `Table.RemoveColumns` |
| Remove duplicates | Home > Remove Rows > Remove Duplicates | `Table.Distinct` |
| Sort | Column menu | `Table.Sort` |
| Replace values | Transform > Replace Values | `Table.ReplaceValue` |
| Split column | Transform > Split Column | `Table.SplitColumn` |
| Add custom column | Add Column > Custom Column | `Table.AddColumn` |
| Fill down | Transform > Fill > Down | `Table.FillDown` |
| Group by | Transform > Group By | `Table.Group` |
| Pivot | Transform > Pivot Column | `Table.Pivot` |
| Unpivot other columns | Transform > Unpivot Columns > Unpivot Other Columns | `Table.UnpivotOtherColumns` |
| Merge queries (join) | Home > Merge Queries | `Table.NestedJoin` then `Table.ExpandTableColumn` |
| Append queries | Home > Append Queries | `Table.Combine` |

## Worked example: clean and summarize

```
let
    Source = Csv.Document(File.Contents("C:\data\sales.csv")),
    Headers = Table.PromoteHeaders(Source),
    Typed = Table.TransformColumnTypes(Headers, {{"Amount", type number}, {"Date", type date}}),
    Recent = Table.SelectRows(Typed, each [Date] >= #date(2026, 1, 1)),
    Grouped = Table.Group(Recent, {"Region"}, {{"Total", each List.Sum([Amount]), type number}})
in
    Grouped
```

## Tips

- Merge types (left outer, inner, full outer, left anti and so on) are options of the join kind argument. Pick the kind in the Merge dialog.
- Unpivot other columns is safer than unpivoting selected columns when new columns appear later.
- Group By on a foldable source can fold to a SQL GROUP BY; check View Native Query (see [query folding](04_query_folding.md)).
- Operations that need all rows, such as sort, are slow in preview; do them last (Fact, S325).
- Use Keep First Rows while developing, then remove that step (Fact, S325).

## Common mistakes

- Merging on columns of different types; set both to the same type first.
- Hard-coding column names that change in the source, which causes "column not found" errors (see [errors and fixes](04_errors_and_fixes.md)).
- Appending queries with different column names and getting null columns.
- Expecting sort order to survive a later Remove Duplicates or Group (Fact, S329).

## See also

- [Function categories](04_m_function_categories.md)
- [Table function catalog, part 2](../references/power_query_m/04_m_functions_table_part2.md)
