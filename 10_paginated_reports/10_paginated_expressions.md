---
id: 10.paginated_expressions
title: Expressions in paginated reports
domain: paginated_reports
type: reference
level: intermediate
tags: [paginated-report, reference, cheatsheet]
summary: Expression syntax, built-in collections, common patterns, and custom code options for Power BI Report Builder.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1233, S1234, S1224]
references: []
related: [10.paginated_parameters, 10.paginated_limits_unsupported]
---
## Purpose

Expressions control content and appearance in a paginated report. They start with an equal sign and use Microsoft Visual Basic. [S1233]

## Key facts

- Fact: Expressions can call Visual Basic runtime functions and members of System.Convert and System.Math. They can also use custom code and .NET classes such as RegularExpressions. [S1233]
- Fact: Built-in collections are Fields, Parameters, Variables, Globals, and User. [S1234]
- Fact: Display text uses brackets, such as `[Sales]`. The stored expression is `=Fields!Sales.Value`. [S1234]

## Syntax cheat sheet

| Task | Expression |
|---|---|
| Field value | `=Fields!Sales.Value` |
| Sum of a field | `=Sum(Fields!Sales.Value)` |
| Parameter value or label | `=Parameters!Store.Value`, `=Parameters!Store.Label` |
| Report variable | `=Variables!MyCalculation.Value` |
| User running report | `=User!UserID` |
| Page X of Y (header or footer only) | `="Page " & Globals!PageNumber & " of " & Globals!TotalPages` |
| Run time | `="The report ran at: " & Globals!ExecutionTime` |
| Previous row aggregate | `=Previous(Sum(Fields!Sales.Value))` |
| Conditional | `=IIF(Fields!Qty.Value > 10, "High", "Low")` |
| Percent text | `="Growth: " & Format(Fields!Growth.Value, "p2")` |
| Hide by Boolean parameter | `=Not Parameters!Show.Value` |
| Page break every 20 rows | `=Ceiling(RowNumber(Nothing)/20)` |
| Join multivalue parameter | `=Join(Parameters!MyMulti.Value, ", ")` |
| Dynamic connection string | `="Data Source=" & Parameters!ServerName.Value & ";initial catalog=AdventureWorks2022"` |

Sources: S1233, S1234 for all rows.

## Where expressions go

Text box values, filters, group expressions, visibility (Hidden property), colors and fonts, connection strings, parameter defaults, and page headers. [S1233]

## Page-scope rules

PageNumber, TotalPages, PageName, OverallPageNumber, and OverallTotalPages work only in a page header or footer. OverallPageNumber ignores page-number resets; PageNumber respects them. [S1233]

Members of Globals return a variant. Cast when a typed value is needed, such as `=CDate(Globals!ExecutionTime)`. [S1233]

## Custom code

- Embedded code blocks in the report work in the Power BI service. [S1224]
- Custom assemblies (DLL references) are not supported. Use embedded code or Azure Functions instead. [S1224]
- Microsoft suggests building complex or custom-code expressions in SQL Server Data Tools. [S1234]

## Common mistakes

- Using PageNumber in the body. It fails outside headers and footers.
- Writing DAX in an expression. These are Visual Basic. DAX belongs in the dataset query for semantic model sources.
- Using a custom assembly, which the service rejects at upload.

## See also

- [Parameters](10_paginated_parameters.md)
- [Limits and unsupported features](10_paginated_limits_unsupported.md)
