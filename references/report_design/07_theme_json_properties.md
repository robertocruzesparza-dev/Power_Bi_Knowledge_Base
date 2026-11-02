---
id: 07.theme_json_properties
title: Theme JSON properties reference
domain: report_design
type: reference
level: advanced
tags: [theme, reference, catalog]
summary: Reference tables of theme color classes, text classes, named theme colors for DAX, and the visualStyles pattern.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S965]
references: []
related: [07.themes_json]
---

## Table of Contents

- [Purpose](#purpose)
- [Structural color classes](#structural-color-classes)
- [Text classes](#text-classes)
- [Named theme colors for DAX](#named-theme-colors-for-dax)
- [visualStyles pattern](#visualstyles-pattern)
- [Value formats](#value-formats)
- [See also](#see-also)

## Purpose

Lookup tables for authors editing theme JSON by hand. The schema repository is the authority for full property lists.

## Structural color classes

| Preferred name | Also called | Typical use |
|---|---|---|
| firstLevelElements | foreground | Table values, card labels, KPI text, filter pane text, trend lines |
| secondLevelElements | foregroundNeutralSecondary | Legend, axis, table headers, button text |
| thirdLevelElements | backgroundLight | Gridlines, shape fill, gauge arc background |
| fourthLevelElements | foregroundNeutralTertiary | Dimmed legend, disabled button text, card category labels |
| background | | Button fill, data label background inside points, tooltip background |
| secondaryBackground | backgroundNeutral | Table outline, shape map default, disabled button fill |
| tableAccent | | Table and matrix grid outline |

For dark themes, set first and second level elements and the background with enough contrast. Fact.

## Text classes

| Class | JSON name | Default | Used for |
|---|---|---|---|
| Callout | callout | DIN, 45 pt | Card values, KPI indicators |
| Header | header | Segoe UI Semibold, 12 pt | Key influencers headers |
| Title | title | DIN, 12 pt | Axis titles, multi-row card titles, slicer header |
| Large title | largeTitle | 14 pt | Visual title |
| Label | label | Segoe UI, 10 pt | Table and matrix text |
| Light label | lightLabel | grey, same size | Legend, axis labels, button text |
| Small label | smallLabel | 9 pt | Reference line labels, slicer search |
| Bold label | boldLabel | bold | Totals and subtotals |
| Large and light | largeLightLabel | 12 pt grey | Card category labels |
| Small and light | smallLightLabel | 9 pt grey | Data labels, value axis labels |

Primary classes are callout, title, header, and label. Secondary classes inherit from them unless you set them. Fact.

## Named theme colors for DAX

Return these names from a measure under Field value formatting. Most use the JSON name. Divergent colors differ.

| JSON name | DAX name |
|---|---|
| center | midColor |
| maximum | maxColor |
| minimum | minColor |
| null | nullColor |
| background, backgroundDark, backgroundLight, backgroundNeutral | same |
| foreground, foregroundNeutralLight, foregroundNeutralSecondary, foregroundNeutralTertiary, disabledText | same |
| good, neutral, bad | same |
| hyperlink, visitedHyperlink, mapPushpin, shapeStroke, tableAccent | same |

## visualStyles pattern

```json
"visualStyles": {
  "<visualName>": {
    "<stylePresetName or *>": {
      "<cardName or *>": [ { "<propertyName>": <value> } ]
    }
  }
}
```

The `*` wildcard on visual name applies to all visuals. Card names may differ from the Format pane labels; use the schema or a saved PBIP report (PBIR files) to find them. Filter cards use `$id` values such as Applied and Available. Fact.

## Value formats

- Booleans true or false; strings in double quotes; numbers without quotes.
- Colors: `{ "solid": { "color": "#FFFFFF" } }`, three or six hex digits.
- Dates: ISO format prefixed with `datetime`.
- Enumerations are strings, such as `RightCenter` for legend position.

## See also

- [Themes and JSON theme files](../../07_report_design/07_themes_json.md)
