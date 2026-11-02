---
id: 07.bookmarks_navigation
title: Bookmarks, buttons, and navigators
domain: report_design
type: concept
level: intermediate
tags: [bookmark, report, interaction, limits]
summary: What report and personal bookmarks save, buttons and navigators, the Selection pane, and documented limits including the 20-personal-bookmark cap.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S972, S973, S974, S996, S963, S2904, S2905]
references: []
related: [07.slicers_filters, 07.drill_tooltips, 07.accessibility]
---
## Purpose

A bookmark saves the state of a report page so users can return to it or step through a story. Buttons and navigators trigger bookmarks and page jumps.

## Key facts

- A bookmark captures the current page, filters, slicers and their state, selected data points, sort order, drill location, and visual visibility from the Selection pane. Fact.
- Slicers keep filtering even when hidden, so bookmarks can show different data views on one page. Fact.
- A bookmark stores state, not position. Moving a visual later does not change what the bookmark restores. Fact.
- Adding a slicer to a page that already has bookmarks clears that slicer in the bookmarks. Fact.
- Bookmarks can be shown as a slide show in Desktop and in the service. Fact.

## Report versus personal bookmarks

| Type | Created by | Travels with report | Limit |
|---|---|---|---|
| Report bookmark | Designer with edit rights | Yes, visible to all viewers | Not stated here |
| Personal bookmark | Any viewer, no edit rights needed | No | 20 per report, 2,000 across all reports; expire after six months |

Personal bookmark rules (Fact):

- Create or update them only while viewing a report.
- They do not capture changes on other pages, even with sync slicers.
- Renamed or removed fields can break them and cause an error.
- Hiding visuals in a personal bookmark may still show them in PDF or PowerPoint exports; use a report bookmark.
- iOS and Android apps show bookmarks but cannot create them.

## Buttons and navigators

- Buttons can navigate pages, apply bookmarks, open URLs, run Q&A, or trigger drillthrough. Fact.
- Page navigators and bookmark navigators build controls that update as pages or bookmarks are added. Fact.
- With two or more bookmark navigators controlling overlapping settings, the shown active bookmark can mislead. Keep groups separate. Fact.
- A bookmark navigator's selected state is not reflected in exports. Fact.

## Steps for a toggle view

1. In Selection pane, show Chart A and hide Table B. Add bookmark "Chart".
2. Show Table B and hide Chart A. Add bookmark "Table".
3. For a visibility-only toggle, clear the Data option on each bookmark so filters and slicers stay untouched.
4. Insert a bookmark navigator and select the two bookmarks.
5. After changing visibility later, right-click the bookmark and Update.

## Common mistakes

- Expecting a bookmark to restore layout positions.
- Using bookmarks for security. Hidden content is still reachable.
- Overlapping bookmark groups with shared filters.

## Limits

| Limit | Value |
|---|---|
| Personal bookmarks per report | 20 |
| Personal bookmarks across reports | 2,000 |
| Personal bookmark lifetime | 6 months |

## See also

- [Slicers and filters](07_slicers_filters.md)
- [Accessibility](07_accessibility.md)
