---
id: 07.mobile_layouts
title: Mobile-optimized report layouts
domain: report_design
type: how-to
level: intermediate
tags: [mobile, report, how-to, best-practice]
summary: How to build phone layouts for report pages in Power BI Desktop or the service, including auto-create, best practices, and limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S985, S986, S987, S972, S925]
references: []
related: [07.design_principles, 07.bookmarks_navigation, 07.accessibility]
---
## Purpose

A mobile layout is a second, phone-shaped arrangement of the visuals on a report page. It changes only layout, never the desktop view.

## Key facts

- The mobile view appears automatically when a phone is in portrait orientation in the Power BI mobile apps (iOS and Android). Turning the phone sideways shows the standard layout. Fact.
- In a web browser, reports always show the standard layout. Fact.
- Reports with mobile pages show a special icon in the mobile app. Fact.
- You can open mobile layout view in Desktop (View ribbon or the layout switcher at the page bottom) and in the service (Edit, then Mobile layout). Fact.
- Publishing from Desktop sends the mobile layout with the report. In the service, saving is enough. Fact.
- Removing a visual from the mobile canvas does not remove it from the desktop page. Fact.
- Audience tabs of org apps are not supported in the Power BI mobile apps. Fact.

## Steps to create a mobile layout

1. Open the page and switch to mobile layout view.
2. Choose Auto-create, or drag visuals from the Page visuals pane onto the phone canvas.
3. Resize with handles; hold Shift to keep aspect ratio.
4. Format visuals with the mobile Visualizations pane.
5. Use the Selection pane to layer objects.
6. Test slicers and buttons on the interactive canvas, then publish or save.

Hidden visuals can be placed too, so bookmark toggles still work. Fact.

## Auto-create tips

The engine reads left to right, top first, and weighs position, size, type, and order. Quality drops with a vertical left nav bar, background images, heavy overlays, or many images (some may not fit). Use Undo (Ctrl+Z) to revert. Fact.

## Best practices

1. Design desktop and mobile layouts of a page together. Duplicating a page copies both layouts, so build a template page first.
2. Keep only the key visuals.
3. Use titles no smaller than nine points.
4. Drop axis titles, gridlines, and legends where possible.
5. Place navigators and slicers horizontally.
6. Remove extra white space inside visuals.

## Common mistakes

- Shrinking a desktop page instead of selecting the important visuals.
- Leaving a left-hand navigation bar and relying on auto-create.
- Assuming mobile edits change the desktop layout. They do not.

## Limits and version notes

Auto-create was announced as a preview in March 2024; the current doc describes it without a preview label. The docs also note some canvas limitations that were not read in full. Unknown for details.

## See also

- [Report design principles](07_design_principles.md)
- [Bookmarks and navigation](07_bookmarks_navigation.md)
