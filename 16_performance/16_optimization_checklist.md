---
id: 16.optimization_checklist
title: Power BI optimization checklist
domain: performance
type: how-to
level: intermediate
tags: [performance, optimization, best-practice, cheatsheet]
summary: A layered checklist to diagnose and fix slow Power BI reports, from capacity and source through model, DAX, and report layers.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S670, S671, S675, S677, S674, S622, S661]
references: []
related: [16.performance_analyzer, 16.dax_studio_vertipaq, 16.model_size_reduction, 16.directquery_tuning, 16.capacity_metrics_app, 16.report_design_performance]
---

# Power BI optimization checklist

## Purpose
Work from the biggest cause to the smallest. Measure before and after each change.

## Step 0: Define the problem
1. Which report, page, visual, and user action is slow?
2. Is it slow for everyone, or at certain times? Time-of-day patterns suggest capacity load.
3. Record a baseline in [Performance Analyzer](16_performance_analyzer.md).

## Step 1: Capacity (if slow at peak times)
- [ ] Check throttling and heavy items in the [Capacity Metrics app](16_capacity_metrics_app.md).
- [ ] Move heavy scheduled refreshes away from peak use.
- [ ] Scale the SKU only after item tuning (S674).

## Step 2: Source and refresh
- [ ] Power Query steps fold (View Native Query).
- [ ] Incremental refresh on large facts ([basics](../05_data_modeling/05_incremental_refresh_basics.md)).
- [ ] Source has indexes and statistics (DirectQuery) (S622).

## Step 3: Model
- [ ] Star schema with one-to-many relationships ([star schema](../05_data_modeling/05_star_schema.md)).
- [ ] Single-direction filters unless justified ([filter direction](../05_data_modeling/05_filter_direction_ambiguity.md)).
- [ ] Unneeded columns and rows removed; keys are integers (S671).
- [ ] Auto date/time off; one proper date table.
- [ ] Right storage modes: Dual dimensions beside DirectQuery facts ([storage modes](../05_data_modeling/05_storage_modes.md)).
- [ ] Aggregations for large DirectQuery facts ([aggregations](../05_data_modeling/05_aggregations.md)).
- [ ] Direct Lake: Delta tables optimized, no fallback ([Direct Lake](../05_data_modeling/05_direct_lake.md)).
- [ ] Check size with [View Metrics](16_dax_studio_vertipaq.md).

## Step 4: DAX
- [ ] Capture the visual query; run in DAX Studio with Server Timings (S677).
- [ ] Use VAR to avoid repeated evaluation; merge alternatives into one CALCULATE (S661).
- [ ] Avoid calling measures in wide calculated columns.
- [ ] Use DIVIDE and SELECTEDVALUE.
- [ ] See [DAX best practices](../06_dax/06_best_practices.md).

## Step 5: Report
- [ ] Fewer visuals per page; bounded tables; drillthrough for detail (S675).
- [ ] Interactions edited; query reduction for DirectQuery.
- [ ] Custom visuals tested.
- [ ] See [report design](16_report_design_performance.md).

## Step 6: Verify
1. Re-run the baseline on a cold cache, then warm.
2. Test in the service with realistic user counts and RLS.
3. Document the change and the measured gain.

## Decision table: where is the time?
| Symptom | Likely layer | First tool |
|---|---|---|
| Visual display or Other is large | Report design | Performance Analyzer |
| DAX query is large, SE dominant | Model size or cardinality | DAX Studio |
| DAX query is large, FE dominant | DAX logic | DAX Studio |
| Direct query is large | Source | Source tools, SQL Profiler |
| Slow only at peak, errors on load | Capacity | Capacity Metrics app |
| Slow refresh | Source and model size | Refresh history, Power Query diagnostics |
