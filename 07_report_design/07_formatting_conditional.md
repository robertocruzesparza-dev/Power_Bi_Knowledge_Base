---
id: 07.formatting_conditional
title: Formatting visuals and conditional formatting
domain: report_design
type: how-to
level: intermediate
tags: [visual, report, theme, how-to]
summary: How visual formatting interacts with themes, how conditional formatting works, and where visual calculations, the Analytics pane, and small multiples fit.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S963, S964, S965, S988]
references: []
related: [07.themes_json, 07.visual_catalog, 07.accessibility]
---
## Purpose

Formatting makes visuals readable and consistent. Conditional formatting makes color follow the data.

## Key facts

- Format a visual in the Format pane. Settings on a visual win over the report theme. Fact.
- Reset to default returns a visual to the theme style. It also removes conditional formatting rules, button and image actions, images from URLs or data fields, and reference labels. Fact.
- Picking a theme color keeps the visual in sync when the theme changes. Picking a custom color from More colors does not. Fact.
- Page size and canvas settings live in the Format pane under Canvas settings. Fact.

## Formatting precedence

1. Base theme: Microsoft-managed defaults stored with the report.
2. Custom theme: layers on the base theme.
3. Direct visual formatting: overrides both until reset.

New releases may update the base theme, but an existing report keeps its original base until you update it. Fact.

## Conditional formatting

Conditional formatting changes a property from data. Three ways to set it:

| Style | How it works |
|---|---|
| Color scale | Maps values to a gradient |
| Rules | If value meets a condition, apply a color |
| Field value | A column or DAX measure returns the color |

Where it applies: table and matrix backgrounds, font colors, data bars, icons, and web URLs; bar colors in charts and many other elements. Fact.

A custom theme cannot hold conditional formatting rules. Apply them to each visual after the theme. Fact.

## Related analysis features

- Visual calculations: DAX written on the visual, for running totals, moving averages, percent of total, and ranking, without model changes. Fact.
- Analytics pane: reference lines (constant, average, min, max, median, percentile), forecasting, anomaly detection, and error bars on supported visuals. Fact.
- Small multiples: split one visual into a grid by a field, such as region. Fact.

## Steps for theme-aware status colors

1. Define good, neutral, and bad in the theme JSON.
2. Write a measure that returns the text "good", "neutral", or "bad".
3. In conditional formatting, choose Field value and select the measure.
4. Change the theme later; the colors update automatically.

Example measure from Microsoft's docs pattern: SWITCH(TRUE(), score >= 80, "good", score >= 50, "neutral", "bad"). Fact.

## Common mistakes

- Hard-coding hex colors on every visual, which blocks theme changes.
- Using red and green as the only status signal. See [Accessibility](07_accessibility.md).
- Expecting a theme to carry conditional formatting.

## See also

- [Themes in JSON](07_themes_json.md)
- [Built-in visual catalog](07_visual_catalog.md)
