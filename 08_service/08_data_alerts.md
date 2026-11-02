---
id: 08.data_alerts
title: Data alerts on dashboards and Activator alerts on reports
domain: service
type: reference
level: beginner
tags: [dashboard, service, automation, limits]
summary: How data alerts work on dashboard tiles, their limits, and the preview Fabric Activator alerts for reports.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S933, S934, S935, S962, S2607]
references: []
related: [08.dashboards, 08.subscriptions, 08.scheduled_refresh]
---
## Purpose

Alerts notify you when a number crosses a threshold. Dashboard alerts are the long-standing feature. Reports use a newer, preview route through Fabric Activator.

## Key facts

- Dashboard alerts work only on tiles pinned from report visuals or Q&A, and only for gauge, KPI, and card visuals. Fact.
- Alerts work only on numeric data and only on data that refreshes. Static sample data does not trigger them. Fact.
- Cards with date or time measures are not supported. Fact.
- Streaming: alerts work if you pin a KPI, legacy card, or gauge built from a streaming dataset visual. Tiles made directly on the dashboard with custom streaming data are not supported. Fact.
- Only you see alerts you set, even on a shared dashboard. They are not co-owned. To transfer, create a new alert and rebuild any Power Automate flow. Fact.
- You can create up to 250 alerts across all your models. Fact.
- Alerts are available in the service, mobile apps, and Teams, not in Desktop. Fact.

## Dashboard data alerts

Who can set them: any license can set alerts on tiles in My workspace or on dashboards shared with you in Premium reserved capacity. For other workspaces you need Pro or PPU. Fact.

Notification: email (optional) and the notification center. Alerts fire only when the value changes, so an unchanged value gives no duplicates. The setup example uses a once-a-day limit; the mobile article describes hourly or daily reminders. Fact.

Automation: a Power Automate template sends an email to any audience when an alert fires. Fact.

## Steps to add a dashboard alert

1. Open the dashboard and the tile's More options menu.
2. Choose Manage alerts and add an alert rule.
3. Name the rule, set the condition (above or below) and threshold.
4. Choose email delivery and frequency, then save.

## Activator alerts on reports (preview)

- Set alert on a visual in a report, choose a measure, a condition, and a threshold. Notify by email or Teams. Fact.
- Requires write permission on a workspace with Fabric capacity F64 or higher, or Premium capacity. Power BI creates an Activator item that watches the semantic model. Fact.
- The article labels the feature public preview. Preview status can change.

## Common mistakes

- Expecting alerts on column or table visuals.
- Forgetting that a lost phone still receives alert notifications; disable rules in the service.

## Limits and version notes

The 250-alert cap and tile restrictions come from current documentation. Recheck before large rollouts.

## See also

- [Dashboards](08_dashboards.md)
- [Subscriptions](08_subscriptions.md)
