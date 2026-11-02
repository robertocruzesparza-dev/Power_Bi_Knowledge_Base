---
id: 07.slicers_filters
title: Slicers, filters, and visual interactions
domain: report_design
type: concept
level: intermediate
tags: [interaction, visual, report, how-to]
summary: Slicer types, sync slicers, the Filters pane, edit interactions, field parameters, persistent filters, and related limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S982, S983, S984, S981, S992, S996]
references: []
related: [07.bookmarks_navigation, 07.drill_tooltips, 07.design_principles]
---
## Purpose

Slicers put filters on the canvas. The Filters pane holds filters at visual, page, and report level. Together they let users focus on a subset of data.

## Key facts

- Slicer formats: list, dropdown, button, date range, and an input slicer that takes typed text or numbers. Hierarchy slicers take several fields. Fact.
- By default a slicer filters every other visual on the page, including other slicers. Fact.
- Slicer search: select the ellipsis and Search, or press Ctrl+F. Fact.
- Date picker slicers do not filter other date picker slicers. Fact.
- Hidden slicers still filter the page, which is why bookmarks can use them. Fact.

## Slicers versus the Filters pane

| Feature | Slicers | Filters pane |
|---|---|---|
| Visibility | Always on canvas | Hidden until opened |
| Best for | Frequent filters, consumers | Complex filtering, authors |
| Cross-page | Yes, with Sync slicers | Report-level filters apply to all pages |

Authors choose which filters consumers see or lock in the Filters pane. Fact.

## Steps to sync a slicer

1. Open View and turn on Sync slicers. The pane sits between Filters and Visualizations.
2. Select the slicer.
3. In the Sync column, tick the pages where selections apply.
4. In the Visible column, tick the pages where the slicer should appear.
5. Format each copy separately if needed.

A page synced but not visible still gets filtered by selections made elsewhere. Sync supports one field per slicer; slicers with several fields or measures cannot sync. Fact.

## Edit interactions and field parameters

- Edit interactions: select the slicer, Format menu, Edit interactions, then pick None on any visual it should not filter. Fact.
- Field parameters let readers switch the measure or dimension a visual shows. Power BI creates a slicer for the parameter. Two-slicer setups let readers pick a dimension and then values from it. Fact.
- Query reduction (Desktop options): turn off cross-highlighting by default and show an Apply button on slicers and filters, which helps DirectQuery models. Fact.

## Persistent filters

By default Power BI saves user slicer and filter choices and reapplies them on return. This can surprise users and confuse bookmarks. Turn off Persistent filters in Desktop report options if everyone should start from the authored state. Users can use Reset to default. Fact.

## Common mistakes

- Leaving the slicer header hidden. In the original slicer visuals, the Clear (eraser) button lives in the slicer header; in the new slicer it lives in the visual container header. Fact.
- Saving range slicers with a selection. Date range slicers work best starting cleared. Fact.
- Too many slicers on a DirectQuery page, each issuing queries.

## Limits and version notes

- Complex slicers using measures with no hierarchy can fail with a "measures not allowed with complex slicers" message. Fact.
- Visual-level filters on a source visual carry into cross-filtered targets. Fact.

## See also

- [Bookmarks and navigation](07_bookmarks_navigation.md)
- [Design principles](07_design_principles.md)
