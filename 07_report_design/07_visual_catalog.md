---
id: 07.visual_catalog
title: Built-in visual catalog
domain: report_design
type: reference
level: beginner
tags: [visual, report, catalog, reference]
summary: Catalog of Power BI's built-in visuals grouped by purpose, with when to use each, preview status, and the Q&A retirement date.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S963, S996, S993, S994, S995, S990, S2602, S2603]
references: []
related: [07.formatting_conditional, 07.custom_visuals, 07.design_principles, 07.slicers_filters]
---
## Purpose

Visuals turn model data into charts, tables, and indicators. This catalog lists the built-in types by job, so you can pick one quickly.

## Key facts

- Visuals cross-filter and cross-highlight each other and support drillthrough. Fact.
- Preview visuals show "(Preview)" in the Visualizations pane and may need enabling under Preview features in Desktop options. Fact.
- Custom visuals extend the list; see [Custom visuals](07_custom_visuals.md).
- Visual calculations, the Analytics pane, small multiples, and conditional formatting apply to many visuals. See [Formatting](07_formatting_conditional.md).

## Catalog

| Group | Visuals | Use when |
|---|---|---|
| Comparison and trend | Bar, column, line, area, combo, ribbon, waterfall | Comparing categories, time trends, rank change, running contribution |
| Part to whole | Pie, donut, treemap, funnel | Few categories (pie), hierarchies (treemap), stages (funnel) |
| Distribution and relationship | Scatter, bubble, dot plot | Correlation, clusters, a third measure as size |
| Tables | Table, matrix | Exact values; matrix adds stepped layout and drill into hierarchies |
| Maps | Several map types | Geographic data |
| Single values | Card, KPI, gauge, goals visual | One key number, progress to target |
| AI | Decomposition tree, key influencers, smart narrative, anomaly detection | Explore drivers, add narrative text, flag outliers in line charts |
| Filtering | Slicer (list, dropdown, button, date range, input) | On-canvas filters |
| Other | Image, text box, shapes, buttons, page and bookmark navigators, paginated report visual, R and Python visuals, Power Apps visual | Layout, navigation, embedded content |

The card visual supports single and multi-card layouts, images, and reference values. The input slicer accepts free text or numbers with filter operators. Fact.

Use a pie chart only with fewer than eight categories. Gauge charts suit the status of one measure against a goal. Fact (Microsoft tip).

## How to choose

1. Name the question: compare, trend, share, relate, or track.
2. Check the data type: category, number, time, place.
3. Consider the audience and space. Large screens take more detail; phones need fewer visuals.
4. Prefer tables for lookup tasks, charts for pattern tasks.

## Q&A visual deprecation

Official dates differ between pages (re-checked 2026-10-08) [S2602, S2603]:

| Source | Statement |
|---|---|
| January 2026 monthly update and Message Center item MC1218421 (published 2026-01-16) | Q&A deprecated, fully retired by end of December 2026 |
| Current Learn Q&A pages (visual, dashboard, limitations, intro) | Q&A experiences go away in February 2027; use Copilot |
| Microsoft short link in those pages | Redirects to a community blog titled as a February 2027 timeline update (page blocked, title only) |

Fact: the newest official statement is February 2027, and the title of the redirect target describes it as a timeline update. Inference: December 2026 was the original date, and February 2027 replaced it. Plan migration before December 2026 anyway. Q&A also covers the Q&A button and dashboard Q&A. Status: resolved as February 2027, moderate confidence.

## Common mistakes

- Using many visuals on one page. It slows the page and hides the message.
- Using pie charts for comparing similar slices.
- Building new reports around the Q&A visual.

## Limits and version notes

- Preview visuals change before release; do not rely on them in production without a fallback.
- The catalog reflects the overview article in the docs; individual visual pages hold property detail.

## See also

- [Formatting and conditional formatting](07_formatting_conditional.md)
- [Report design principles](07_design_principles.md)
- [Custom visuals](07_custom_visuals.md)
