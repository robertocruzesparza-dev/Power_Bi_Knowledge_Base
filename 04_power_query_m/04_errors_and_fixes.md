---
id: 04.errors_and_fixes
title: Power Query errors and fixes
domain: power_query_m
type: troubleshooting
level: intermediate
tags: [power-query, troubleshooting, error-message, m-language]
summary: Step-level and cell-level errors, the common error reasons, how to remove or replace errors, and known gotchas such as type inference and sort order.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S326, S329, S315]
references: []
related: [04.data_privacy_firewall, 04.common_transformations, 04.m_language_basics]
---

# Power Query errors and fixes

Purpose: read an error, decide whether it is step-level or cell-level, and fix it.

## Key facts

- Two error kinds exist: step-level errors stop the query and show a yellow pane; cell-level errors let the query load and show Error in cells (Fact, S326).
- An error has three parts: reason (for example Expression.Error), message and detail. Power Query Online also shows an error code (Fact, S326).
- The Show details button reveals more where available.

## Step-level errors

| Error | Likely cause | Fix |
|---|---|---|
| `DataSource.NotFound` | Source moved, no access, or path exists only on another machine | Point to a path both users can reach, or fix credentials |
| `Expression.Error`: column of the table wasn't found | A step names a column the source no longer has | Remove or change the step; avoid hard-coding changing names |
| `Formula.Firewall` | Privacy levels or the way sources are combined | See [Data Privacy Firewall](04_data_privacy_firewall.md) |

(Fact, S326.)

## Cell-level errors (Fact, S326)

A common cause is a conversion error, for example the text NA changed to a whole number. Use the column quality tool to spot them. Then use the right-click or ribbon options: Remove Errors, Replace Errors, or Keep Errors to inspect them.

In M you can handle an error inline:

```
= Table.AddColumn(Typed, "Safe", each try Number.From([Sales]) otherwise 0)
```

## Gotchas from Microsoft's common issues page (Fact, S329)

- Sort is not guaranteed to be preserved by later operations. Sort after the operation, buffer with `Table.Buffer`, or use ranking instead of Remove Duplicates.
- Type inference reads the first 200 rows only. Integers in the first 200 rows and decimals after row 200 lead to truncated decimals. Fix by setting the type explicitly or checking with data profiling over the whole set.
- Connections forcibly closed by the remote host can appear when calling APIs; the page explains this warning.

## Steps: debug a failing refresh

1. Reproduce in Power Query: refresh the preview and read the first red step.
2. Check credentials and privacy levels for each source.
3. Check that the column names and types still match the source.
4. Compare Desktop with the service: a gateway or credential problem fails only in the service.
5. Review the gateway data source (names must match; see [gateway data sources](../03_data_sources/03_gateway_sso_and_data_sources.md)).

## Common mistakes

- Removing errors and silently losing rows. Count rows before and after.
- Replacing errors with 0 where a null would be more honest.
- Fixing a type change by editing the type in the last step only, instead of at the source of the problem.

## See also

- [Common transformations](04_common_transformations.md)
- [Privacy levels](../03_data_sources/03_privacy_levels.md)
