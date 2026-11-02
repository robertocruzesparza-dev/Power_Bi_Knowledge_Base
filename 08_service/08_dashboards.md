---
id: 08.dashboards
title: Dashboards in the Power BI service
domain: service
type: concept
level: beginner
tags: [dashboard, service, concept]
summary: What a dashboard is, how it differs from a report, how tiles are pinned, and the licensing and design notes for service dashboards.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S927, S989, S933, S931, S925]
references: []
related: [08.data_alerts, 08.subscriptions, 08.workspace_apps, 08.scorecards_goals]
---
## Purpose

A dashboard is a single-page canvas of tiles that gives an at-a-glance view. Each tile links back to the report or model behind it.

## Key facts

- Dashboards exist only in the Power BI service. You cannot create them in Desktop or on mobile, but you can view and share them on mobile. Fact.
- Creating one is a creator task and needs edit rights on the source report. Fact.
- You need Pro or Premium per user (PPU) to create dashboards in workspaces. In My workspace no paid license is needed. Fact.
- Tiles come from reports, other dashboards, Excel, Q&A, and widgets such as images, text, video, and web content. A pinned live report page keeps its interactivity. Fact.
- A dashboard can combine multiple reports and multiple semantic models, including on-premises and cloud sources. Fact.
- Promotion and certification are not available for dashboards. Fact (see [Endorsement](08_endorsement.md)).

## Dashboards versus reports

| Capability | Dashboard | Report |
|---|---|---|
| Pages | One | One or more |
| Data sources | Many models and reports | One semantic model |
| Drill down | Only for a pinned live report page | Yes |
| Filter or slice | No (focus mode filter cannot be saved) | Yes |
| Built in Desktop | No | Yes |
| Alerts | Yes, on some tiles | No (preview Activator alerts exist) |
| Subscribe | Yes | Yes, per page |
| See model tables and fields | No | Yes |

## Ways to add tiles

1. Pin a visual from a report.
2. Pin an entire report page as a live tile.
3. Pin from another dashboard or from Excel.
4. Ask a question in Q&A and pin the answer. (Q&A is scheduled for retirement; see [Q&A deprecation](../07_report_design/07_visual_catalog.md).)
5. Add an image, text box, video, or web content tile.

## Design tips

- Put the most important number at top left in a card, and add context.
- Fit the story on one screen with no scrolling.
- Fewer tiles read better on phones and tablets.
- Dashboard tiles tied to RLS do not render in email subscriptions. Fact.

## Common mistakes

- Treating a dashboard as a detailed report.
- Adding a dashboard to an app without its source reports; tiles then fail.
- Expecting dashboards inside an org app. They cannot be included there.

## Limits and version notes

- An app can hold up to 200 dashboards. Fact.
- Dashboard tile alerts only work on gauge, KPI, and card tiles. See [Data alerts](08_data_alerts.md).

## See also

- [Data alerts](08_data_alerts.md)
- [Subscriptions](08_subscriptions.md)
- [Workspace apps](08_workspace_apps.md)
