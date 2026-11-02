---
id: 10.paginated_parameters
title: Create parameters in paginated reports
domain: paginated_reports
type: how-to
level: beginner
tags: [paginated-report, how-to, example]
summary: Step-by-step creation of report parameters in Power BI Report Builder, with available values, defaults, and dataset binding.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1228, S1226, S1224, S1230, S1233]
references: []
related: [10.paginated_expressions, 10.paginated_export_subscriptions]
---
## Purpose

A parameter lets the reader choose values that filter data or change layout. Four steps make it work: define, set available values, set defaults, bind to the dataset.

## Steps

1. In the Report Data pane, right-click Parameters and choose Add Parameter.
2. Name it. It must start with a letter and hold only letters, numbers, or underscores. No spaces. [S1228]
3. Set Prompt text and Data type: Text, Integer, DateTime (calendar), or Boolean (radio buttons).
4. Optional flags: Allow blank value, Allow null value, Allow multiple values (check boxes).
5. Set visibility: Visible (on toolbar), Hidden (set only through URL), or Internal (hidden and not editable after publish). [S1228]
6. On Available Values, add values by hand (value plus label) or Get values from a query.
7. On Default Values, choose none, specified values, or a query. With defaults the report runs on open. Without them the reader picks and selects View Report.
8. Bind to the dataset. Put `@ProductCategory` in the query's WHERE clause. Report Builder then links the dataset parameter automatically. Or link by hand on the dataset's Parameters page. [S1228]

Example query:

```sql
SELECT ProductID, ProductName, Price
FROM Products
WHERE CategoryID = @ProductCategory
```

Preview with F5 and check the filter.

## Multivalue parameters

Use `=Join(Parameters!MyMultivalue.Value, ", ")` to show chosen values in a text box. In a query, use an IN clause with the parameter. Behavior depends on the data source. [S1233]

## Using parameters elsewhere

- Subscriptions: pick current or default parameter values per subscription. Different subscriptions can use different values. [S1226]
- To change values on an existing subscription, re-render with new values, open Subscriptions, and choose Use current (rendered report) values. [S1226]
- Query-bound parameters must return valid values or the subscription fails with an rsParametersNotSpecified email. [S1226]
- REST export accepts parameterValues, including repeated names for multiple values. [S1230]
- Drill-through from a Power BI report to a paginated report uses URL parameters. [S1224]

## Common mistakes

- Spaces in the name.
- Forgetting to bind the parameter, so the report shows all data.
- Relying on locale. The service passes DateTime parameters in US format. [S1224]

## See also

- [Expressions](10_paginated_expressions.md)
- [Export and subscriptions](10_paginated_export_subscriptions.md)
