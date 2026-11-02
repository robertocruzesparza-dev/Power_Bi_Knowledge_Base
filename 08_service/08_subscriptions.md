---
id: 08.subscriptions
title: Email subscriptions for reports and dashboards
domain: service
type: reference
level: intermediate
tags: [service, report, dashboard, limits]
summary: How email subscriptions work in the Power BI service, who can create them, their numeric limits, unsupported visuals, and delivery troubleshooting.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S930, S931, S932, S921, S945, S2605]
references: []
related: [08.data_alerts, 08.dashboards, 08.workspace_roles, 08.license_requirements]
---
## Purpose

A subscription emails a snapshot and link (or, for paginated reports, a file attachment) on a schedule you set.

## Key facts

- You can subscribe to a report page, a dashboard, a paginated report, or a scorecard. Fact.
- The email holds a snapshot and link, or an attachment of the content. Paginated report subscriptions attach the full output as PDF, PPTX, XLSX, DOCX, CSV, or XML. Fact.
- Run now sends a test email at once and does not refresh the semantic model. Fact.
- "Include my changes" saves your filter state into the subscription. It is not available for dashboards or paginated reports. Fact.
- An email can show the subscription owner as sender or come from the no-reply Power BI address during a phased migration. Allow both in mail filters. Fact.

## Limits

| Item | Value |
|---|---|
| Subscriptions per Power BI report or dashboard | 24, each with its own recipients, time, frequency. Paginated reports have no limit |
| Dynamic per-recipient subscriptions | 1,000 recipient rows; paginated version times out at 10 minutes |
| Subscriptions per paginated report | Unlimited |
| Subscribers per item before delivery problems may appear | 200; use group aliases, each counts as one |
| Scorecard subscriptions | 24 per scorecard |
| Paginated report attachment size | 25 MB |
| Paginated report execution time | 60 minutes |
| Dynamic recipient rows | 1,000; extra recipients get nothing |
| Instant (Run now) emails per user per hour | Trial 10, default 15, PPU 20, Premium or Fabric capacity 25 |

Delivery normally should not take more than 24 hours, even in peak demand. Fact.

## Who can subscribe whom

- Create your own: a Pro or PPU license, or content on Premium or Fabric capacity. Fact.
- Subscribe others: Pro or PPU plus the Contributor, Member, or Admin role. Recipients also need a paid license unless the workspace is on capacity. Fact.
- Group aliases and external recipients: on capacity workspaces you can subscribe aliases from other domains.
- External recipients need a paid non-PPU capacity workspace. Trial capacity and PPU workspaces cannot send to external addresses, regardless of tenant settings. Fact.
- B2B guests can subscribe only themselves, and only if the tenant setting allows. Internal guests cannot use subscriptions. Fact.

## Dynamic per recipient subscriptions

A recipient list in a semantic model drives a filter so each person gets their own view. Supports single-value filters only. Not supported: multi-value filters, resolutions under 400 px, SSAS live connection. Rendering counts as interactive capacity use. Paginated version times out at 10 minutes. Receiving the email does not grant report access. Fact.

## Unsupported content

Dashboard tiles with RLS, streaming, video, and custom web content tiles; most custom visuals except certified ones; ESRI ArcGIS, R, Python, Power Apps, Power Automate, paginated report and Visio visuals; semantic model refreshes through the XMLA endpoint. Fact.

## Troubleshooting

1. Subscription stopped: the owner's license expired, the item or owner was deleted, or authentication failed (password reset, token invalidation, MFA). Fact.
2. No data change: only the model owner can refresh the model manually.
3. Large images can exceed email size limits.
4. Check the sender's spam rules, and that the user has a mailbox address in Entra ID.
5. Schedule refresh and subscription at different times to avoid stale snapshots.

## Common mistakes

- Subscribing 500 individuals to one report instead of a group alias.
- Using M365 Unified group addresses; they are not supported.

## See also

- [Data alerts](08_data_alerts.md)
- [Workspace roles](08_workspace_roles.md)
