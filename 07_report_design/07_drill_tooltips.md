---
id: 07.drill_tooltips
title: Drill down, drillthrough, and tooltips
domain: report_design
type: concept
level: intermediate
tags: [drill, report, interaction, how-to]
summary: How drill mode, drillthrough pages, cross-report drillthrough, visual tooltips, and report page tooltips work, with design guidance and limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S975, S976, S980, S977, S978, S979, S981]
references: []
related: [07.bookmarks_navigation, 07.slicers_filters, 07.accessibility]
---
## Purpose

These features move users from a summary to detail without crowding the page. Drill mode moves within a hierarchy. Drillthrough moves to another page. Tooltips add detail on hover.

## Key facts

- Drill mode steps through hierarchy levels in one visual. It is available only when the designer enables drill on a visual with a hierarchy. By default drilling one visual does not filter others; the designer can change that. Fact.
- Drillthrough opens a target page filtered to the selected item, by right-click or by a button. Fact.
- Page tooltips display a whole report page on hover. They suit extra perspective, detail, or help text. Fact.

## Drillthrough

- Add a drillthrough field to the target page's drillthrough filters. A Back button is added for you; keep it. Fact.
- The field must exist in the source visual and must not be aggregated there, or the menu entry is missing. Fact.
- Cross-report drillthrough: both reports in the same workspace, matching field names and data types, setting enabled in the target report. The article says it works only in the service. Fact.
- Design advice from Microsoft: match the report style, set sample drillthrough filters while designing and remove them before publishing, avoid visuals that show BLANK for the filter, and consider hiding the page. Add a button with a clear-filters bookmark if the page stays visible. Fact.
- Order of drillthrough pages in the context menu can differ between Desktop and the service. Fact.

## Tooltips

| Type | Notes |
|---|---|
| Default visual tooltip | Shows the data point; can include extra fields; "Tooltip fields only" option; sentence format option |
| Report page tooltip | A page sized with the Tooltip canvas type; chosen per visual |
| Help tooltip | Text attached to a visual header icon |
| Actions footer | Adds drill down, drill up, and drillthrough actions to the tooltip |

Page tooltip rules (Fact):

- They are not interactive: no slicer use, tabbing, or scrolling. Design for no scroll. Use drillthrough if users must interact.
- Screen readers cannot read them. See [Accessibility](07_accessibility.md).
- A visual shows a page tooltip only if the page filter fields match the visual's fields and summarization.
- Dashboards do not support report page tooltips. Python and R visuals do not appear inside them. Clusters are not supported as tooltip fields.
- Button visuals also support tooltips.

## Steps to build a drillthrough page

1. Add a page and add a field to its Drillthrough filters.
2. Build visuals that answer "tell me about this item".
3. Test with a filter set, then clear it.
4. Optionally hide the page from the tab bar.
5. Optionally add a drillthrough button on the source page.

## Steps to build a page tooltip

1. Add a page; set Canvas settings type to Tooltip.
2. Set Page View to Actual size to preview.
3. Name the page, add small visuals, and configure the page as a tooltip in its page information (exact option names are in Microsoft's tooltip article).
4. On the source visual, set the tooltip type to Report page and pick the page.

## Common mistakes

- Putting essential numbers only in tooltips.
- Forgetting that drillthrough menu entries vanish if the source field is summarized.
- Publishing with test drillthrough filters still set.

## Limits and version notes

Complex slicers with measures that lack hierarchy can raise an error; remodel or avoid. Fact.

## See also

- [Bookmarks and navigation](07_bookmarks_navigation.md)
- [Slicers and filters](07_slicers_filters.md)
