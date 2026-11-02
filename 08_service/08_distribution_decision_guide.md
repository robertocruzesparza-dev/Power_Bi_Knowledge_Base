---
id: 08.distribution_decision_guide
title: Choosing a way to distribute Power BI content
domain: service
type: decision
level: beginner
tags: [service, decision-guide, app, workspace]
summary: A decision guide for workspace access, sharing links, workspace apps, org apps, subscriptions, and Teams when delivering content to users.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S928, S960, S924, S925, S959, S957]
references: []
related: [08.workspace_apps, 08.org_apps, 08.item_permissions_sharing, 08.subscriptions, 08.license_requirements]
---
## Purpose

Pick the lightest method that meets the audience size, control, and license needs. The PL-300 exam asks you to choose a distribution method, so the logic below is testable.

## Decision table

| Scenario | Best method | Needs |
|---|---|---|
| Co-author content with a team | Workspace roles | Pro or PPU for roles above Viewer |
| Give a few named people one report | Sharing link (Specific people) or direct access | Pro or PPU, or content in capacity |
| Polished content for a large team or the organization | Workspace app or org app | Pro or PPU to publish; free users can consume on capacity |
| Many apps from one workspace, or access follows items | Org app | Fabric item support |
| Email a snapshot on a schedule | Subscription | Paid license to create |
| Alert on a number crossing a threshold | Data alert on a dashboard tile | Gauge, KPI, or card tile |
| Discuss in Microsoft Teams | Teams integration | Power BI app for Teams |
| People outside the organization | Microsoft Entra B2B guest access | Admin enables external sharing |

(The table follows the Microsoft sharing guidance; the org app row is an inference from the app comparison.)

## Rules of thumb

- Keep workspace access for authors, testers, and owners. Send consumers to an app. Fact (Microsoft planning guidance).
- Use security groups, not individual accounts, for roles and audiences. Fact (guidance).
- Free-license consumers need the content on Premium capacity or Fabric F64 or larger. Fact.
- Always define RLS when users should not see all data. Sharing a report shares the model. Fact.
- Avoid sharing from My workspace for business content; leaving staff break access. Fact.

## Worked example

A finance team of 6 authors serves 800 managers. Authors get Member or Contributor roles. The workspace sits on an F64 capacity. They publish a workspace app with two audiences, "Executives" and "Managers", mapped to security groups. Managers use free licenses. RLS limits each manager to their cost center. Inference.

## Common mistakes

- Sharing 800 individual links instead of one group-based audience.
- Making consumers Contributors so they can "see everything".
- Forgetting build permission on the model for self-service report builders.

## See also

- [Workspace apps](08_workspace_apps.md)
- [Org apps](08_org_apps.md)
- [Item permissions and sharing](08_item_permissions_sharing.md)
