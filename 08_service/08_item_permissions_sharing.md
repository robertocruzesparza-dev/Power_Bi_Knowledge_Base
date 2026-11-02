---
id: 08.item_permissions_sharing
title: Item permissions and sharing links
domain: service
type: concept
level: intermediate
tags: [service, security, interaction, report]
summary: How Read, Reshare, Build, and Write permissions work, the three sharing link types, shared views, and limits when sharing reports and semantic models.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S928, S929, S952, S953, S954, S955, S956, S960, S2909, S2910]
references: []
related: [08.workspace_roles, 08.workspace_apps, 08.distribution_decision_guide, 08.license_requirements]
---
## Purpose

Item permissions give access to one item without a workspace role. Use them for a few people. For many people, use an app or group-based roles.

## Key facts

- Sharing an item grants Read by default. Read shows metadata and lets the user view reports built on it. It does not grant access to underlying SQL or OneLake data. Fact.
- Sharing a report also shares access to its semantic model. Unless row-level security (RLS) or object-level security (OLS) restricts it, readers can reach all model data. Fact.
- Hiding a table, column, page, or visual is not security. Fact.
- Sharing needs a Pro license for sender and recipient, or content in capacity. Fact.
- Build permission lets recipients create content on the model, use Analyze in Excel, export underlying data, and connect through the XMLA endpoint. Fact.

## Sharing link types

| Link | Who gets access | Notes |
|---|---|---|
| People in your organization | Anyone in the tenant with the link | Does not work for guests or external users; can be disabled by a tenant setting |
| Specific people | Named users or groups | Can include Microsoft Entra B2B guests; recommended for most cases |
| People with existing access | Nobody new | Just gives a URL |

Link settings: Reshare is included by default. Build is excluded by default. Fact.

Link limits and rules (Fact):

- Each report can have at most 1,000 sharing links. Remove "Specific people" links and use direct access if you hit it.
- Without Reshare permission, or without a Pro license, you can only copy "People with existing access" links.
- Direct access sharing emails individual users, not groups.
- Microsoft 365 Unified groups cannot be used for direct sharing or subscriptions. Use security groups or email-enabled distribution groups.
- Dashboard sharing accepts up to 100 users or groups in the input box. Guests cannot reshare dashboards.
- You cannot share a report you received through an app; ask the app owner.

## Semantic model permissions

| Permission | REST API name | Meaning |
|---|---|---|
| Read | Read | View model content |
| Build | Explore | Create reports and use the model outside Power BI |
| Reshare | Reshare | Share further |
| Write | (workspace based) | Modify the model |

How users get Build: Contributor or higher in the workspace; owner grants on Manage permissions; app audience settings; or a share link that includes Build. Fact.

When RLS exists, users with only Read or Build cannot read data unless they belong to a role. Users with Write can read regardless. Fact.

## Steps to share a report

1. Open the report in Reading view.
2. Select Share and choose the link type.
3. Clear Reshare or add Build as needed.
4. Copy the link or send it by email or Teams.

## Shared views

A filtered link creates a shared view when "Include my changes" is selected. It captures filters, slicers, personalized visuals, cross-filtering, drill state, bookmark, and spotlight. A shared view expires 180 days after last use; each access resets the timer. Fact.

## Common mistakes

- Leaving Reshare on by default and oversharing.
- Using sharing for large audiences. Changes are visible at once to everyone, and per-item permissions are hard to audit.
- Sharing from My workspace. If the owner's account is disabled, recipients lose access.

## Limits and version notes

Link and view limits come from current docs and may change. Recheck before building automation.

## See also

- [Workspace roles](08_workspace_roles.md)
- [Distribution decision guide](08_distribution_decision_guide.md)
