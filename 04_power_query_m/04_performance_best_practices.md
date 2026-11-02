---
id: 04.performance_best_practices
title: Power Query performance and best practices
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, performance, optimization, best-practice]
summary: Practical rules for fast, maintainable Power Query: connector choice, early filtering, ordering expensive steps, types, naming, modules and future-proofing.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S322, S325, S329, S334]
references: []
related: [04.query_folding, 04.parameters_and_custom_functions, 04.errors_and_fixes]
---

# Power Query performance and best practices

Purpose: a short checklist drawn from Microsoft's Power Query best practices, with the reason for each rule.

## Rules (Fact, S325 unless noted)

1. Choose the purpose-built connector. The SQL Server connector beats generic ODBC because it supports features such as query folding.
2. Filter early. Fewer rows reach later steps, and on folding sources the filter runs at the source.
3. Do expensive operations last. Sorts and similar steps must read the whole source before returning rows, so preview slows down. Streaming operations such as filters return rows as they pass.
4. Develop on a subset. Add Keep First Rows while building, then remove it.
5. Set correct data types. Type-specific filters and column menus depend on them.
6. Profile before you transform: column quality, distribution and profile.
7. Document: rename steps and add descriptions.
8. Split long queries into smaller referenced queries (Extract Previous on a step) and group queries in folders.
9. Use parameters and custom functions for repeated logic (see [parameters and functions](04_parameters_and_custom_functions.md)).
10. Future-proof: avoid steps tied to column positions or exact names that may change.

## Folding and speed (Fact, S322)

Folding pushes work to the source, which often loads faster than pulling all data and transforming locally. Check View Native Query after each risky step. See [query folding](04_query_folding.md).

## Load and refresh habits

- Disable load for staging queries that only feed other queries (Assumption; standard practice, verify the menu label in your build).
- Avoid many queries that each read the same large file. Reference one base query instead. A reference does not always avoid a second read; the data source may be queried more than once by design (Fact, S302).
- Power BI Desktop and the service may send multiple queries to get schema or data, depending on caching (Fact, S302).

## Security habits (Fact, S334)

Set privacy levels per source, do not enable Fast Combine, use encrypted connections, and keep certificate revocation checks on.

## Common mistakes

- Sorting at the start, then relying on that order after a join or distinct (Fact, S329).
- Leaving auto-detected types for CSV columns that change beyond row 200 (Fact, S329).
- Combining a huge file and many small steps in one 40-step query that nobody can read.

## Measuring

Use the status bar's execution time for a rough check. For deeper analysis Microsoft documents query diagnostics (not covered here; see the gaps list).

## See also

- [Power Query editor](04_power_query_editor.md)
- [Common transformations](04_common_transformations.md)
