---
id: 16.performance_analyzer
title: Performance Analyzer
domain: performance
type: how-to
level: beginner
tags: [performance, monitoring, desktop, optimization]
summary: How to record visual load times in Performance Analyzer, read its four duration categories, copy visual queries, and avoid misreading the results.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S670, S679, S678, S682]
references: []
related: [16.dax_studio_vertipaq, 16.optimization_checklist, 06.best_practices]
---

# Performance Analyzer

## Purpose
Performance Analyzer shows how long each visual takes to load, split by what the time was spent on. Use it first to find the slow visual.

## Key facts
- Fact: It is a pane in Report view in Desktop (Optimize ribbon, Performance Analyzer) and when editing a report in the web (View menu) (S670).
- Fact: It records visual loads and reloads caused by interactions such as a slicer change (S670).
- Fact: Durations are end minus start timestamps. Most canvas work runs on one UI thread, so durations include queue time (S670).
- Fact: Results can be exported to a JSON file for deeper analysis (S670, S679).

## Duration categories (S670)
| Category | Meaning |
|---|---|
| DAX query | Time from the visual sending its query until the model returns results |
| Direct query | For DirectQuery tables, the time for the external source query |
| Visual display | Time to draw the visual, including images and geocoding |
| Other | Query preparation, waiting for other visuals, background work |
| Evaluated parameters (preview) | Time evaluating field parameters |

## Steps
1. Open the report page to test. Use a realistic filter state.
2. Open Performance Analyzer, select Start recording.
3. Select Refresh visuals, or interact (change a slicer). Use Analyze this visual for one visual.
4. Expand a slow visual. Compare DAX query, Direct query, Visual display, and Other.
5. Select Copy query, or Run in DAX query view (Desktop). In the service, copy the query, open the data model, and run it in DAX query view (S670, S682).
6. Select Stop, then export if you want to compare runs.

## Reading the results
- High DAX query: tune the measure or model. Take it to [DAX Studio](16_dax_studio_vertipaq.md).
- High Direct query: the source is slow; see [DirectQuery tuning](16_directquery_tuning.md).
- High Visual display: the visual draws too much; reduce rows, try another visual, test custom visuals.
- High Other: many visuals waiting on each other; reduce visuals per page.
Microsoft notes that DAX query time depends on calculation complexity, the number of tables, and relationships between them (S670).

## Caveats (S679)
Desktop differs from the service. Data volume, concurrent users, storage modes, gateways, capacity, query caching, query parallelization, connection limits, and row-level security (RLS) all change real timings. Treat Desktop timings as a guide, then confirm in the service.

## Also useful
- The Optimize ribbon has presets: Query reduction (turns off cross-highlighting and cross-filtering, adds an Apply button; best for DirectQuery) and Interactivity (default; best for Import) (S678).
- Visual DAX queries are more verbose than needed. Copilot in DAX query view can simplify them (S670).
- Run the same test several times; cache state changes results.

## Common mistakes
- Testing once on a warm cache.
- Blaming the measure when Other or Visual display is the big number.
- Comparing Desktop on a laptop to a shared capacity.

## See also
- [DAX Studio and VertiPaq Analyzer](16_dax_studio_vertipaq.md)
- [Report design for performance](16_report_design_performance.md)
- [Optimization checklist](16_optimization_checklist.md)
