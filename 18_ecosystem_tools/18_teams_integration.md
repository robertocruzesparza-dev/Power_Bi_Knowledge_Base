---
id: 18.teams_integration
title: Power BI in Microsoft Teams
domain: ecosystem_tools
type: how-to
level: beginner
tags: [teams, ecosystem, service, limits]
summary: How to embed Power BI reports in Teams tabs and chats, what content types work, licensing needs, and known limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S2117, S2118, S2823]
references: []
related: [18.sharepoint_embedding, 18.analyze_in_excel]
---

# Power BI in Microsoft Teams

## Purpose
Put reports where teams already talk. Example: add the sales report as a tab in the Sales channel.

## Steps
1. In a channel or chat, select + and choose the Power BI tab, then Save.
2. Paste a link, or Browse workspaces, or Create new [S2118].
3. Grant access in Power BI. Embedding does not give permission [S2117].

## Key facts
- Fact: embeddable items are interactive reports, paginated reports, scorecards, organizational apps and reports inside them. Dashboards cannot be embedded [S2117, S2118].
- Fact: you need at least Viewer on the workspace [S2118].
- Fact: Power BI app must be enabled in the Teams admin center [S2117].
- Fact: Free users can view content in P SKU or F64+ capacity; Pro or PPU users can share and build [S2117].
- Fact: the Power BI tab works in standard, private and shared channels and in chats [S2823].
- Fact: external users need a guest invite, report permission and a licence (Free if content is on Premium) [S2117].
- Fact: Chat in Teams needs the Share to Teams tenant setting on [S2118 related result].

## Limits
- URL filters and query-string links are unsupported; personal bookmarks and cross-tenant links too [S2118].
- Tab not available in national clouds; GCC lacks the messaging extension and activity feed notifications [S2117].
- Fabric items cannot be embedded in the Power BI tab [S2117].
- Organizational apps are not supported in the personal Teams app; they open in a browser [S2117].
- Link previews do not work in meeting chat or private channels [S2117].
- Tab name changes only through Rename [S2117].

## Common mistakes
- Assuming channel membership grants report access. Use a Microsoft 365 group on the workspace.

## See also
- [SharePoint embedding](18_sharepoint_embedding.md)
