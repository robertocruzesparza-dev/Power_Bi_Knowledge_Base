---
id: 04.query_folding
title: Query folding
domain: power_query_m
type: concept
level: intermediate
tags: [query-folding, power-query, performance, optimization]
summary: What query folding is, how to check it, what usually breaks it, and how native queries keep it alive.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S322, S323, S324, S325, S314]
references: []
related: [04.performance_best_practices, 04.data_privacy_firewall, 03.privacy_levels, 03.import_directquery_support]
---

# Query folding

Purpose: understand when Power Query pushes work to the source, so refresh is fast and DirectQuery works.

## Key facts

- Folding translates supported M steps into a source query (for example SQL), so the source does the work (Fact, S322).
- Three outcomes: full folding (source does it all), partial folding (source does what it can, the Power Query engine does the rest), and no folding (all work in the engine) (Fact, S322).
- Connectors for structured sources with a query engine, such as SQL Server and OData Feed, commonly fold. File sources such as CSV and Excel do not (Fact, S322).
- The engine may reorder steps during optimization (Fact, S322).
- Privacy levels can block or prevent folding when sources of different levels are combined (Fact, S314, S322).

## How to check folding

1. Right-click a step and choose View Native Query. If it is greyed out, the step likely does not fold. Availability depends on the connector (Fact, S322).
2. In Power Query Online, read the folding indicators next to steps. They also show a query plan. These tools exist only in Online (Fact, S322, S323).

Indicator meanings (Fact, S323): Folding means the source evaluates the query up to this step. Not folding means some part runs outside the source. Might fold means it is decided at run time, mostly with ODBC or OData. Opaque means the plan is inconclusive. Unknown means no plan exists, for example for a record or list.

A not-folding indicator does not mean nothing folds. Everything up to the last folding step usually folds. The first Source or Navigation steps are often inconclusive and later steps still fold (Fact, S323).

## Worked example

```
let
    Source = Sql.Database("ServerName", "AdventureWorks"),
    Navigation = Source{[Schema = "Production", Item = "Product"]}[Data],
    Capitalized = Table.TransformColumns(Navigation, {{"Name", each Text.Proper(_), type text}})
in
    Capitalized
```

The first steps run at the source. The Capitalized step never folds, so it runs locally, and any later step that depends on it also does not fold (Fact, S323).

## Native queries without losing folding

`Value.NativeQuery` runs your own SQL and can keep folding for later steps on these connectors: Amazon Redshift, Dataverse (with enhanced compute), Google BigQuery, PostgreSQL, SAP HANA, Snowflake and SQL Server. Navigate to the database node, choose Transform Data on that node, then write the native query against it. If folding fails, test your steps as a subquery of the native query (Fact, S324).

## Habits that protect folding

- Put filters, column removal and joins early, before steps that cannot fold.
- Do steps that never fold (text case changes such as Text.Proper, custom functions, index columns, buffering) after all foldable steps. (Inference from S323 example; list is not exhaustive.)
- Use the purpose-built connector rather than ODBC when one exists (Fact, S325).
- `Table.Buffer` forces data into memory and stops further folding (Inference; the firewall source says buffering prevents later folding, S315).
- Do not reorder steps without rechecking View Native Query.

## Common mistakes

- Assuming a greyed View Native Query is a bug; it is the folding signal.
- Mixing a Private source with another source, which forces buffering.
- Sorting early and expecting downstream steps to keep the order (Fact, S329).

## Limits

- Incremental refresh and DirectQuery generally need the date filter to fold (Inference, widely reported; verify in the incremental refresh topic of the service domain).
- Indicators and query plan are Online only (Fact, S323).

## See also

- [Performance and best practices](04_performance_best_practices.md)
- [Privacy levels](../03_data_sources/03_privacy_levels.md)
