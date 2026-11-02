---
id: 04.parameters_and_custom_functions
title: Parameters and custom functions
domain: power_query_m
type: how-to
level: intermediate
tags: [power-query, m-language, how-to, best-practice]
summary: How to create and use Power Query parameters, build reusable custom functions, and avoid injection risks with dynamic values.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S327, S328, S334]
references: []
related: [04.m_language_basics, 04.common_transformations, 04.performance_best_practices]
---

# Parameters and custom functions

Purpose: reuse values and logic instead of copying steps. Parameters store one value; custom functions package a set of steps.

## Parameters (Fact, S327)

A parameter stores a value you can reuse to change arguments of transforms or data source functions, or as input to custom functions.

Properties: Name, Description, Required, Type, Suggested values and Current value. Always set the type. Suggested values can be Any value, a List of values (with a default), or a Query.

Create one in either way:
1. Right-click a query that returns a simple constant (date, text, number) and choose Convert to Parameter.
2. Home > Manage Parameters > New Parameter, then fill in the form.

You can convert a parameter back with Convert To Query. Typical uses: server and database names, a folder path, a start date, a row limit while developing.

## Custom functions (Fact, S328)

A custom function applies the same transformations to many tables or values. Create one by code:

1. Right-click an empty area in the Queries pane and choose Blank Query.
2. Home > Advanced editor, then replace the template with the function.
3. Select Done.

```
let
    AddTax = (price as number, rate as number) as number => price * (1 + rate)
in
    AddTax
```

A function in a query is invoked like `AddTax(100, 0.2)`. The editor can also convert an existing query into a function (Assumption: via a right-click Create Function command, not re-verified here). You then invoke it for each row of a table of inputs, such as a list of file names.

## Worked example: combine many files

1. Build a query that cleans one file.
2. Turn it into a function with the file content as its parameter.
3. Add a column in the file list table that calls the function for each row.
4. Expand the resulting column.

## Security note (Fact, S334)

When you use dynamic M query parameters, avoid building queries by string concatenation. Prefer M operations that fold to the source. Use the source's own parameter passing where available.

## Common mistakes

- Using a parameter in a data source step and forgetting to update it on the gateway data source. The names must match (see [gateway data sources](../03_data_sources/03_gateway_sso_and_data_sources.md)).
- Untyped parameters, which remove type-specific filter menus.
- Wrapping every step in a function, which hides folding. Check View Native Query after invoking.

## Limits and notes

- After publishing, test refresh: the data source the parameter produces must be reachable and, for gateways, registered with matching names.
- The service can show parameter values in semantic model settings (Assumption; verify in your tenant).

## See also

- [M language basics](04_m_language_basics.md)
- [Query folding](04_query_folding.md)
