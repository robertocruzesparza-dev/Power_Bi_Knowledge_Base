---
id: ref.m_functions_table_part1
title: M functions: Table (part 1)
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Table-category M functions, first half, for shaping, filtering, joining and aggregating tables.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---
# M functions: Table (part 1)

Purpose: a lookup list of M functions from the official function reference. 56 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Table functions A to M

- `ItemExpression.From`: Returns the abstract syntax tree (AST) for the body of a function.
- `RowExpression.Column`: Returns an abstract syntax tree (AST) that represents access to a column within a row expression.
- `RowExpression.From`: Returns the abstract syntax tree (AST) for the body of a function.
- `Table.FromColumns`: Creates a table from a list of columns and specified values.
- `Table.FromList`: Converts a list into a table by applying the specified splitting function to each item in the list.
- `Table.FromRecords`: Converts a list of records into a table.
- `Table.FromRows`: Creates a table from a list of row values and optional columns.
- `Table.FromValue`: Creates a table with a column from the provided value or values.
- `Table.View`: Creates or extends a table with user-defined handlers for query and action operations.
- `Table.ViewError`: Creates a modified error record that won't trigger a fallback when raised by a handler defined on a view (via Table
- `Table.ViewFunction`: Creates a function that can be intercepted by a handler defined on a view (via Table.View).
- `Table.ToColumns`: Creates a list of nested lists of column values from a table.
- `Table.ToList`: Converts a table into a list by applying the specified combining function to each row of values in the table.
- `Table.ToRecords`: Converts a table to a list of records.
- `Table.ToRows`: Creates a list of nested lists of row values from a table.
- `Table.ApproximateRowCount`: Returns the approximate number of rows in the table.
- `Table.ColumnCount`: Returns the number of columns in the table.
- `Table.IsEmpty`: Indicates whether the table contains any rows.
- `Table.PartitionValues`: Returns information about how a table is partitioned.
- `Table.Profile`: Returns a profile of the columns of a table.
- `Table.RowCount`: Returns the number of rows in the table.
- `Table.Schema`: Returns a table containing a description of the columns (that is, the schema) of the specified table.
- `Tables.GetRelationships`: Gets the relationships among a set of tables.
- `Table.AlternateRows`: Keeps the initial offset then alternates taking and skipping the following rows.
- `Table.Combine`: Returns a table that is the result of merging a list of tables.
- `Table.FindText`: Returns all the rows that contain the given text in the table.
- `Table.First`: Returns the first row or a specified default value.
- `Table.FirstN`: Returns the first count rows specified.
- `Table.FirstValue`: Returns the first column of the first row of the table or a specified default value.
- `Table.FromPartitions`: Returns a table that is the result of combining a set of partitioned tables.
- `Table.InsertRows`: Inserts a list of rows into the table at the specified position.
- `Table.Last`: Returns the last row or a specified default value.
- `Table.LastN`: Returns the last specified number of rows.
- `Table.MatchesAllRows`: Indicates whether all the rows in the table meet the given condition.
- `Table.MatchesAnyRows`: Indicates whether any the rows in the table meet the given condition.
- `Table.Partition`: Partitions the table into a list of tables based on the number of groups and column specified.
- `Table.Range`: Returns the rows beginning at the specified offset.
- `Table.RemoveFirstN`: Returns a table with the specified number of rows removed from the table starting at the first row.
- `Table.RemoveLastN`: Returns a table with the specified number of rows removed from the table starting at the last row.
- `Table.RemoveRows`: Removes the specified number of rows.
- `Table.RemoveRowsWithErrors`: Returns a table with the rows removed from the input table that contain an error in at least one of the cells. If a
- `Table.Repeat`: Repeats the rows of the tables a specified number of times.
- `Table.ReplaceRows`: Replaces the specified range of rows with the provided row or rows.
- `Table.ReverseRows`: Returns a table with the rows in reverse order.
- `Table.SelectRows`: Selects the rows that meet the condition function.
- `Table.SelectRowsWithErrors`: Returns a table with only those rows of the input table that contain an error in at least one of the cells. If a co
- `Table.SingleRow`: Returns a single row in the table.
- `Table.Skip`: Returns a table with the first specified number of rows skipped.
- `Table.SplitAt`: Returns a list containing the first count rows specified and the remaining rows.
- `Table.Column`: Returns a specified column of data from the table as a list.
- `Table.ColumnNames`: Returns the column names as a list.
- `Table.ColumnsOfType`: Returns a list with the names of the columns that match the specified types.
- `Table.DemoteHeaders`: Demotes the column headers to the first row of values.
- `Table.DuplicateColumn`: Duplicates a column with the specified name. Values and type are copied from the source column.
- `Table.HasColumns`: Indicates whether the table contains the specified column or columns.
- `Table.Pivot`: Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a column 

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
