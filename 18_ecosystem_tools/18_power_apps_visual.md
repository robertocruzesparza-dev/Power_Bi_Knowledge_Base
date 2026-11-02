---
id: 18.power_apps_visual
title: Power Apps visual
domain: ecosystem_tools
type: how-to
level: intermediate
tags: [ecosystem, visual, automation, limits]
summary: How the Power Apps visual embeds a canvas app in a report that receives report data, with its browser, embedding and record limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2121]
references: []
related: [18.power_automate_visual, 18.sharepoint_embedding]
---

# Power Apps visual

## Purpose
Embed a canvas app that reads the report's filtered data so users can act on insights. Example: update a record while looking at its chart.

## Key facts
- Fact: the app shares the report data source and reacts to slicers [S2121].
- Fact: the app is shared separately from the report [S2121].
- Fact: the visual cannot filter the report or send data back to it [S2121].
- Fact: if you change the bound fields, edit the app from the service (... > Edit), or changes will not propagate [S2121].

## Limits
- Maximum 1,000 records passed through the `PowerBIIntegration` object [S2121].
- Supported for Embed for your organization, not Embed for your customers [S2121].
- Launch function supports https only [S2121].
- Guest users need a tenant ID in the app link, Power BI authentication and app sharing [S2121].
- No Report Server support; no multi-level embedding in sovereign clouds [S2121].
- `PowerBIIntegration.Refresh()` needs an app created from the visual, a DirectQuery source and a DirectQuery connection [S2121].
- Desktop cannot be refreshed by the app; changes show on the next refresh [S2121].
- Edge and Chrome support view, create and modify. Safari views only, with cross-site tracking allowed. Firefox is not supported [S2121].
- Power BI mobile does not support the microphone control [S2121].

## Common mistakes
- Publishing the report before creating the app is the documented recommendation; do it in that order [S2121].

## See also
- [Power Automate visual](18_power_automate_visual.md)
