---
id: ref.m_functions_table_part2
title: M functions: Table (part 2)
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Table-category M functions, second half, for shaping, filtering, joining and aggregating tables.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---
# M functions: Table (part 2)

Purpose: a lookup list of M functions from the official function reference. 57 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Table functions N to Z

- `Table.PrefixColumns`: Returns a table where the columns have all been prefixed with the given text.
- `Table.PromoteHeaders`: Promotes the first row of values as the new column headers (that is, as column names).
- `Table.RemoveColumns`: Removes the specified columns.
- `Table.ReorderColumns`: Returns a table with the columns in the specified order.
- `Table.RenameColumns`: Returns a table with the columns renamed as specified.
- `Table.SelectColumns`: Returns a table with only the specified columns.
- `Table.TransformColumnNames`: Transforms column names by using the given function.
- `Table.Unpivot`: Translates a set of columns in a table into attribute-value pairs.
- `Table.UnpivotOtherColumns`: Translates all columns other than a specified set into attribute-value pairs.
- `Table.AddColumn`: Adds a column with the specified name. The value is computed using the specified selection function with each row t
- `Table.AddFuzzyClusterColumn`: Adds a new column with representative values obtained by fuzzy grouping values of the specified column in the table
- `Table.AddIndexColumn`: Appends a column with explicit position values.
- `Table.AddJoinColumn`: Performs a join between tables on supplied columns and produces the join result in a new column.
- `Table.AddKey`: Adds a key to a table.
- `Table.AggregateTableColumn`: Aggregates a column of tables into multiple columns in the containing table.
- `Table.CombineColumns`: Combines the specified columns into a new column using the specified combiner function.
- `Table.CombineColumnsToRecord`: Combines the specified columns into a new record-valued column where each record has field names and values corresp
- `Table.ExpandListColumn`: Given a column of lists in a table, create a copy of a row for each value in its list.
- `Table.ExpandRecordColumn`: Expands a column of records into columns with each of the values.
- `Table.ExpandTableColumn`: Expands a column of records or a column of tables into multiple columns in the containing table.
- `Table.FillDown`: Propagates the value of a previous cell to the null-valued cells below in the column.
- `Table.FillUp`: Propagates the value of a cell to the null-valued cells above in the column.
- `Table.FuzzyGroup`: Groups rows in the table based on fuzzy matching of keys.
- `Table.FuzzyJoin`: Joins the rows from the two tables that fuzzy match based on the given keys.
- `Table.FuzzyNestedJoin`: Performs a fuzzy join between tables on supplied columns and produces the join result in a new column.
- `Table.Group`: Groups rows in the table that have the same key.
- `Table.Join`: Joins the rows from the two tables that match based on the given keys.
- `Table.Keys`: Returns the keys of the specified table.
- `Table.NestedJoin`: Performs a join between tables on supplied columns and produces the join result in a new column.
- `Table.PartitionKey`: Returns the partition key of the specified table.
- `Table.ReplaceErrorValues`: Replaces the error values in the specified columns with the corresponding specified value.
- `Table.ReplaceKeys`: Replaces the keys of the specified table.
- `Table.ReplacePartitionKey`: Replaces the partition key of the specified table.
- `Table.ReplaceValue`: Replaces one value with another in the specified columns.
- `Table.Split`: Splits the specified table into a list of tables using the specified page size.
- `Table.SplitColumn`: Splits the specified column into a set of additional columns using the specified splitter function.
- `Table.TransformColumns`: Transforms the values of one or more columns.
- `Table.TransformColumnTypes`: Applies type transformation(s) of the form { column, type } using a specific culture.
- `Table.TransformRows`: Transforms the rows of the table using the specified transform function.
- `Table.Transpose`: Makes columns into rows and rows into columns.
- `Table.Contains`: Indicates whether the specified record appears as a row in the table.
- `Table.ContainsAll`: Indicates whether all of the specified records appear as rows in the table.
- `Table.ContainsAny`: Indicates whether any of the specified records appear as rows in the table.
- `Table.Distinct`: Removes duplicate rows from the table.
- `Table.IsDistinct`: Indicates whether the table contains only distinct rows (no duplicates).
- `Table.PositionOf`: Returns the position or positions of the row within the table.
- `Table.PositionOfAny`: Returns the position or positions of any of the specified rows within the table.
- `Table.RemoveMatchingRows`: Removes all occurrences of the specified rows from the table.
- `Table.ReplaceMatchingRows`: Replaces all the specified rows with the provided row or rows.
- `Table.AddRankColumn`: Appends a column with the ranking of one or more other columns.
- `Table.Max`: Returns the largest row or default value using the given criteria.
- `Table.MaxN`: Returns the largest row or rows using the given criteria.
- `Table.Min`: Returns the smallest row or a default value using the given criteria.
- `Table.MinN`: Returns the smallest row or rows using the given criteria.
- `Table.Sort`: Sorts the table using one or more column names and comparison criteria.
- `Table.Buffer`: Buffers a table in memory, isolating it from external changes during evaluation.
- `Table.StopFolding`: Prevents any downstream operations from being run against the original source of the data.

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
