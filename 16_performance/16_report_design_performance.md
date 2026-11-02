---
id: 16.report_design_performance
title: Report design for performance
domain: performance
type: how-to
level: beginner
tags: [performance, report, visual, best-practice]
summary: Report-level choices that speed up loading: fewer visuals, bounded tables, query reduction, drillthrough pages, and careful custom visuals.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S675, S623, S678, S608]
references: []
related: [16.performance_analyzer, 16.directquery_tuning, 16.optimization_checklist]
---

# Report design for performance

## Purpose
Even a perfect model feels slow if a page asks it for too much. These rules reduce query count and result size.

## Key facts
- Fact: The more data a visual must display, the slower it loads (S675).
- Fact: A table left unfiltered over a 100 million row model loads all those rows into memory and is uncompressed at every refresh; a Top N filter (for example 10,000) keeps the view the same for users but cuts memory use (S675).
- Fact: Microsoft recommends limiting the visuals on a page to what is necessary and using drillthrough pages and report page tooltips for extra detail (S675).
- Fact: Poorly optimized custom visuals can slow the whole report, so test each one (S675).

## Rules
| Rule | Why |
|---|---|
| Few visuals per page | Fewer queries; in DirectQuery fewer serial refreshes (S623) |
| Bound every table and matrix | Row count drives memory and render time (S675) |
| Use drillthrough and tooltip pages for detail | Detail loads only on demand (S675) |
| Prefer measures that are simple and folded into the model | Heavy DAX runs per visual |
| Turn off unneeded cross-filter and cross-highlight interactions | Each interaction sends queries (S623) |
| Use the Query reduction preset for DirectQuery | Apply button, no cross-filtering by default (S678) |
| Apply filters before adding fields (DirectQuery authoring) | Keeps intermediate queries small (S623) |
| Replace several cards with one multi-row card | One query instead of many (S623) |
| Keep composite-model visuals within one source group | Faster queries (S608) |
| Check measure filters and Top N filters on DirectQuery | Two queries each (S623) |

## Steps to slim a slow page
1. Record with [Performance Analyzer](16_performance_analyzer.md).
2. Sort visuals by total duration. Fix the top three.
3. Replace a huge table with a summary plus a drillthrough page.
4. Remove visuals that repeat information.
5. Edit interactions so slicers do not drive visuals that do not need them (Format, Edit interactions, None).
6. Replace custom visuals with built-in ones in a test copy and compare.
7. Re-test in the service, not only Desktop.

## Slicers
Many slicers each send queries. Use a hierarchy or list slicer where it fits, group related filters in the filter pane, and keep slicer fields low-cardinality. Inference: a slicer over a high-cardinality column returns a long list and costs memory.

## Common mistakes
- A page of 30 cards and 5 tables.
- Default table showing every row.
- High-cardinality fields on axes.
- Using the same page for overview and detail.

## See also
- [Optimization checklist](16_optimization_checklist.md)
- [DirectQuery tuning](16_directquery_tuning.md)
