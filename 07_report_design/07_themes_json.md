---
id: 07.themes_json
title: Report themes and JSON theme files
domain: report_design
type: how-to
level: intermediate
tags: [theme, report, how-to, tutorial]
summary: How built-in, organizational, and custom JSON report themes work, the file structure, style presets, and limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S964, S965, S988]
references: [../references/report_design/07_theme_json_properties.md]
related: [07.formatting_conditional, 07.accessibility, 07.design_principles]
---
## Purpose

A report theme sets default colors, fonts, and visual styles for a whole report. Teams export one theme as JSON and reuse it, which keeps reports consistent.

## Key facts

- Built-in themes: Bloom, Dark, Divergent, Frontier, Innovate, Soft dark, Tidal, and Copilot default, plus Reset to default. Fact.
- Dark and Soft dark follow the Fluent 2 base style. Reset to default before publishing if you want a light report. Fact.
- Organizational themes appear in the gallery when the tenant admin adds them. Fact.
- Applying a built-in theme or importing a JSON file removes customizations already added to the report. Visuals formatted by hand keep their formatting until reset. Fact.
- The only required line in a theme file is `name`. Fact.
- Power BI validates imports against a published JSON schema and shows errors for unknown fields. Fact.

## Apply and share a theme

- In Desktop, use the Design ribbon: Themes gallery, Customize theme, Import theme, Download theme. Fact.
- In the service, use View, then Theme. The Design ribbon commands exist only in Desktop. Fact.
- Community themes are listed in a themes gallery on the Fabric Community site. Community resource.

## Theme file structure

A theme has four main parts:

| Part | Keys | Controls |
|---|---|---|
| Theme colors | `dataColors`, `good`, `neutral`, `bad`, `maximum`, `center`, `minimum`, `null` | Data colors, status colors, conditional formatting gradient |
| Structural colors | `firstLevelElements`, `secondLevelElements`, `thirdLevelElements`, `fourthLevelElements`, `background`, `secondaryBackground`, `tableAccent` | Text, gridlines, fills, backgrounds |
| Text classes | `callout`, `title`, `header`, `label` (primary), plus secondary classes derived from them | Fonts, sizes, colors |
| Visual styles | `visualStyles` > visual name > style preset or `*` > card name > properties | Per-visual defaults |

Details are in [Theme JSON properties](../references/report_design/07_theme_json_properties.md). When all data colors are used, Power BI generates more by adjusting saturation and hue. Fact.

## Worked example

Minimal brand theme:

```json
{
  "name": "Contoso",
  "dataColors": ["#0B5394", "#38761D", "#E69138", "#990000"],
  "good": "#38761D",
  "neutral": "#E69138",
  "bad": "#990000",
  "background": "#FFFFFF",
  "foreground": "#252423",
  "tableAccent": "#0B5394"
}
```

Import it, then reference "good", "neutral", or "bad" from a measure for status colors. Illustrative example based on the documented keys.

## Style presets

Define named presets under a visual type so authors pick them from a Style dropdown in the Format pane. Presets inherit from the default style `*`, so put shared settings there. An author-only error appears if a report loses its preset definitions. Fact.

## Common mistakes

- Setting colors per visual instead of using theme colors.
- Expecting conditional formatting rules inside a theme. They are not supported.
- Copying PBIR property values directly into a theme; the theme structure differs.

## Limits and version notes

- You can set the default page size for new pages in a theme; existing pages are unchanged. Fact.
- Themes can be extracted and applied in bulk with Semantic Link Labs in Fabric notebooks. Fact.
- Use the schema at the Microsoft powerbi-desktop-samples repository for current property names. Fact.

## See also

- [Formatting and conditional formatting](07_formatting_conditional.md)
- [Accessibility](07_accessibility.md)
