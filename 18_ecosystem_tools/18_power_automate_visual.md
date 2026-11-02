---
id: 18.power_automate_visual
title: Power Automate visual
domain: ecosystem_tools
type: how-to
level: intermediate
tags: [automation, visual, ecosystem, limits]
summary: How the Power Automate visual runs a data-contextual flow from a report button, plus its permissions and limits.
status: ga
volatile: false
last_verified: 2026-10-08
confidence: high
sources: [S2120, S2552, S2553]
references: []
related: [18.power_apps_visual, 18.teams_integration]
---

# Power Automate visual

## Purpose
Let report readers click a button that runs a flow using the report's current filters. Example: send an email with the filtered rows.

## Steps
1. Add the Power Automate visual (Visualizations pane, or Insert > Power Automate in Desktop).
2. Pick the data fields, create the flow from inside the report, and choose an environment.
3. Test in edit mode: Back to report, then Ctrl+click the button.
4. Share run-only or edit access with users or a Microsoft Entra group [S2120].

## Key facts
- Fact: flows for this trigger can run only from a Power BI report, not from the Power Automate portal [S2120].
- Fact: create the flow from inside the report; the trigger has no field access otherwise [S2120].
- Fact: selected fields reach the Body only if a flow action uses them [S2120].
- Fact: data is processed in the geography where the flow is deployed [S2120].

## Limits
- Maximum 1,000 records [S2120]. Re-verified 2026-10-08: also unsupported in embedded analytics, Publish to web, export and GCC or GCC High tenants [S2552]. The Power Apps visual has the same 1,000-record cap and works only with Embed for your organization [S2553].
- Not supported for embedded analytics, Publish to web, export, or Azure Government (GCC and GCC High) [S2120].
- Running users need permission on the flow [S2120].
- Organizational visual repository: deploy it using Add from AppSource in the admin portal, or it may not render [S2120 related result].

## Common mistakes
- Building the flow in Power Automate first.
- Forgetting to share the flow with report readers.

## See also
- [Power Apps visual](18_power_apps_visual.md)
