---
id: 07.design_principles
title: Report design principles and canvas settings
domain: report_design
type: concept
level: beginner
tags: [report, best-practice, visual, performance]
summary: Practical report design rules from Microsoft guidance: audience, one-screen stories, hierarchy, page size, grouping, and performance limits on visuals.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S990, S989, S988, S991, S992, S970, S996]
references: []
related: [07.visual_catalog, 07.accessibility, 07.mobile_layouts, 07.themes_json]
---
## Purpose

Good design helps users find the answer fast. These rules come from Microsoft's report and dashboard guidance and its accessibility checklist.

## Key facts

- Start from the audience: what decisions they make, which metrics matter, and where they view the report. Fact.
- A report page should tell its story at a glance on one screen, ideally without scrolling. Fact.
- Large monitors take more content; tablets and phones need fewer visuals. Fact.
- Microsoft's own tips cite books by Stephen Few, Edward Tufte, and Cole Nussbaumer Knaflic, and the SQLBI dashboard design video. Fact (cited, not summarized).

## Design rules

1. Put the highest-level numbers at top left; add detail as the eye moves right and down.
2. Make the most important number the biggest, for example a card, and give context with text boxes or tooltips.
3. Pick the visual that fits the data and the question; see [Visual catalog](07_visual_catalog.md).
4. Use consistent fonts, sizes, slicer positions, and colors across pages.
5. Remove redundancy. Two visuals showing the same thing add clutter.
6. Use drillthrough pages and page tooltips for detail rather than adding more visuals.
7. Apply a theme for brand colors; see [Themes](07_themes_json.md).
8. Check accessibility; see [Accessibility](07_accessibility.md).
9. Use the squint test: if labels grab attention before data points, turn labels off.

## Canvas and page settings

| Setting | Options |
|---|---|
| Aspect ratio | 16:9 (default), 4:3, Letter, Tooltip, Custom pixel size |
| 16:9 sizes | 1280x720, 1920x1080, 2560x1440, 3840x2160 |
| Vertical alignment | Top or Middle |
| Page view | Fit to page (default), Fit to width, Actual size |
| Layout helpers | Gridlines, snap to grid, lock objects, Selection pane, grouping |

You can set the default size of new pages in a theme. Fact.

## Performance rules for design

- The more data a visual shows, the slower it loads. Limit table rows with Top N filters; a table left unfiltered over 100M rows loads everything. Fact.
- Limit visuals per page. Use drillthrough and page tooltips for extras. Fact.
- Test each custom visual for speed; a poor one slows the whole report. Fact.
- For DirectQuery, apply filters before adding fields, limit visuals, and consider query reduction options. Fact.

## Worked example

A sales page for regional managers: row of three cards (revenue, margin, orders) at top left; a line chart of monthly revenue beside them; a bar chart by region below; one slicer for fiscal year, fixed in the same place on every page. Each bar chart has a drillthrough to a region detail page, so the main page holds six objects, not twenty. Illustrative.

## Common mistakes

- Cramming everything on one page to avoid navigation.
- Same size for every element, so nothing stands out.
- Choosing a canvas size after building. Changing it later can force re-layout work (Inference).

## See also

- [Visual catalog](07_visual_catalog.md)
- [Mobile layouts](07_mobile_layouts.md)
- [Slicers and filters](07_slicers_filters.md)
