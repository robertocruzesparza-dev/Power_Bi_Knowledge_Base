---
id: 18.sharepoint_embedding
title: Power BI in SharePoint Online
domain: ecosystem_tools
type: how-to
level: intermediate
tags: [ecosystem, embedding, service, licensing, limits]
summary: How the Power BI web part embeds reports in SharePoint Online pages, with licensing, access setup, and known issues.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S2119, S2141, S2824, S2801]
references: []
related: [18.teams_integration, 18.power_apps_visual]
---

# Power BI in SharePoint Online

## Purpose
Show interactive reports in an intranet page while keeping permissions and row-level security (RLS). In Power BI choose File > Embed report > SharePoint Online, then paste the link in the web part.

## Prerequisites
- Modern pages [S2119].
- Pro or PPU licence to embed; viewers need Pro or PPU, or content on Premium or F64+ capacity [S2119].
- Users must sign in to Power BI once to activate the licence [S2119].
- Access is separate from embedding. Use a Microsoft 365 group, or share an installed app and copy the embed URL from the installed app [S2119].

## Key facts
- Fact: web part settings include page name, display, navigation pane, filter pane and action bar [S2119].
- Fact: an Enable Copilot checkbox exists in the embed dialog; it needs the Copilot tenant switch and paid capacity [S2119].
- Fact: secure embed for other portals needs an HTTPS top-level page [S2141].
- Fact: Browse workspaces lets you pick a workspace, report and page in SharePoint, and the Embed a single visual toggle embeds one visual (listed in the August 2026 update) [S2824, S2801].
- Fact: SharePoint embed is supported in air-gapped environments [S2824].

## Known issues
| Issue | Fix or note | Source |
|---|---|---|
| "Missing refresh token" (400, code 10001) | Sign out and in, close browsers, use MFA device | S2119 |
| Free user upgrade prompt | Report and model not on Premium or F64+ | S2119 |
| Azure B2B guests | Not supported | S2119 |
| Classic SharePoint Server | Not supported | S2119, S2141 |
| Apps embedded in a page | Cannot be viewed through the web part | S2119 |
| Auto-append URL filters | Not supported; append manually | S2119 |
| Cross-Origin-Opener-Policy same-origin on your site | Breaks sign-in for secure embed; use restrict-properties | S2141 |

## See also
- [Teams integration](18_teams_integration.md)
