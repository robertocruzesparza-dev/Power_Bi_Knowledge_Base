---
id: 07.accessibility
title: Accessible report design checklist
domain: report_design
type: how-to
level: intermediate
tags: [accessibility, report, how-to, best-practice]
summary: Built-in accessibility features and the author checklist for alt text, tab order, contrast, color, tooltips, and bookmarks in Power BI reports.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S970, S971, S974, S977, S964]
references: []
related: [07.themes_json, 07.drill_tooltips, 07.bookmarks_navigation, 07.design_principles]
---
## Purpose

Accessible reports work for keyboard and screen reader users, people with low vision, and people with color vision deficiency. The product supplies tools; the author must use them.

## Key facts

- Built in, no setup: keyboard navigation of all visuals, screen reader support, high contrast color view, focus mode, and the Show data table (Alt+Shift+F11). Fact.
- Needs author setup: alt text, tab order, titles and labels, markers, themes. Fact.
- Desktop detects Windows high contrast and applies it; the setting travels with the published report. In the service, choose View then High contrast colors in edit mode if detection fails. Fact.
- Screen readers read the visual title, type, and any alt text. Fact.
- Press Shift+? in the service to see keyboard shortcuts. Fact.
- Report tooltips are invisible to screen readers. Fact.

## Author checklist

| Area | Rule |
|---|---|
| All visuals | Text contrast at least 4.5:1; do not use color alone; plain titles without jargon; alt text on non-decorative visuals |
| Slicers | Same font, color, and position on every page |
| Text boxes | Put the text in alt text too |
| Interactions | Do not hide key insight behind an interaction; pre-filter instead |
| Bookmarks | Test navigation by keyboard only |
| Sort order | Set it on purpose; the Show data table follows it |
| Tooltips | Ancillary information only |
| Video and audio | No autoplay; captions or transcripts |
| Shapes and images | Hide decorative ones from tab order; add alt text when they point at data |
| Custom visuals | Check the Show data table; a Play Axis visual must not autoplay |
| Page order | Set tab order in the Selection pane and hide decorative items |

## Steps to set alt text and tab order

1. Select a visual and find its Alt text setting in the Format pane; describe the point of the visual.
2. Open View, then Show panes, then Selection.
3. Choose Tab order. Move objects with arrows or drag.
4. Select the number beside a decorative object to remove it from tab order.
5. Test with Tab and Shift+Tab.

Bookmark navigators: use alt text such as "2025 sales data modifier", place the navigator next to the visual it controls, and avoid other focusable items between them. Fact.

## Color and contrast

- WCAG 2.1 success criterion 1.4.3 asks for 4.5:1 contrast for text. Fact.
- Avoid these pairs together: green and red, green and brown, blue and purple, green and blue, light green and yellow, blue and grey, green and grey, green and black. Fact.
- Use fewer colors or a monochrome palette; test with a color blindness simulator and a squint test. Fact.
- A built-in accessible theme and a color-blind-safe community theme exist. See [Themes](07_themes_json.md).

## Common mistakes

- Using tooltips to carry essential numbers.
- Relying on red and green status colors only; add icons or text.
- Too many visuals: clutter hurts everyone and slows the page.

## Limits and version notes

For best results with a screen reader and Desktop, start the reader before opening Desktop files. Fact.

## See also

- [Drill and tooltips](07_drill_tooltips.md)
- [Bookmarks and navigation](07_bookmarks_navigation.md)
