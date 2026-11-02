---
id: 16.directquery_tuning
title: DirectQuery performance tuning
domain: performance
type: how-to
level: advanced
tags: [performance, storage-mode, optimization, limits]
summary: Checklist for DirectQuery models covering source tuning, model design, query reduction, composite fixes, diagnostics, and known limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S622, S623, S608, S615, S678, S2834, S2835]
references: []
related: [05.storage_modes, 05.aggregations, 16.performance_analyzer]
---

# DirectQuery performance tuning

## Purpose
In DirectQuery, every visual sends a query to the source. Report speed equals source speed plus overhead. Tune the source first, then the model, then the report.

## Key facts
- Fact: Import queries are faster than native queries sent to DirectQuery sources, because imported data is cached in memory and optimized for analytic queries (S622 via Power Platform guidance).
- Fact: A query or intermediate result over 1,000,000 rows fails; Premium can raise the limit (S622, S2835).
- Fact: a DirectQuery query running longer than about four minutes (225 seconds) times out in the service (S2834).
- Fact: Default maximum connections per source is 10 in Desktop; Pro and Report Server cap at 10 active; Premium depends on SKU (S622).
- Fact: Measure filters and Top N filters can cause two queries; the first for Top N returns all categories, which can hit the row limit (S623).

## Source (S622)
1. Check baseline query speed in the source.
2. Add indexes, statistics, and columnstore where applicable.
3. Favor integer keys for joins; avoid joins on uniqueidentifier or calculated expressions.

## Model design (S622)
1. Keep Power Query steps simple and foldable; check View Native Query.
2. Start with simple measures, then iterate.
3. Hide surrogate keys.
4. Limit bi-directional filters and test their cost.
5. Consider the Assume referential integrity setting so joins can be INNER JOIN.
6. Avoid relative date filters in Power Query; they become fixed literals in the native query. Implement them in the model or report.
7. Review calculated columns and tables that cannot fold.

## Composite fixes (S623, S608, S615)
- Set shared dimensions to Dual.
- Add Import aggregation tables, or automatic aggregations on Premium ([aggregations](../05_data_modeling/05_aggregations.md)).
- Use hybrid tables for recent live data plus cached history.
- Keep visuals within one source group where possible; consider sync slicers rather than cross source group relationships (S608).
- Other options listed by Microsoft: aggregation-aware measures, dynamic M parameters, query caching in capacity settings (S622).

## Report design (S623, S678)
1. Apply the Query reduction preset: Apply button on slicers and filters, cross-highlighting and cross-filtering off.
2. Apply filters before adding fields while authoring, so intermediate queries stay small.
3. Limit visuals per page; queries beyond the connection limit run in series.
4. Turn off interactions that trigger expensive queries.
5. Replace many card visuals with one multi-row card.

## Diagnostics (S622)
1. Use Performance Analyzer for one visual at a time ([guide](16_performance_analyzer.md)).
2. For SQL, open the Desktop trace file FlightRecorderCurrent.trc in SQL Server Profiler (File, Options and settings, Options, Diagnostics, open traces folder). Keep captures near 10 seconds.
3. Events show DAX and native SQL, durations, and an ActivityID that groups related events.

## Common mistakes
- Using DirectQuery to avoid refresh without testing source load.
- Case-insensitive engine against a case-sensitive source gives undefined results; normalize casing (S622).
- Many unfiltered visuals on one page.
- Complex DAX in measures that translate into heavy SQL.

## Limits and version notes
Connection counts and row limits are volatile. Verify before sizing.

## See also
- [Storage modes](../05_data_modeling/05_storage_modes.md)
- [Optimization checklist](16_optimization_checklist.md)
