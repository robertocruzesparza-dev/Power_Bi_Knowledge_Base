---
id: 08.workspace_apps
title: Workspace apps
domain: service
type: how-to
level: intermediate
tags: [app, service, how-to, workspace]
summary: How to create, publish, update, and unpublish a workspace app, including audiences, auto-install, licenses, and the documented limits.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S924, S926, S925, S958, S2606]
references: []
related: [08.org_apps, 08.workspace_roles, 08.distribution_decision_guide, 08.dashboards]
---
## Purpose

A workspace app packages reports, dashboards, and other items from one workspace with built-in navigation. You publish it to a broad audience while keeping the workspace as a private staging area.

## Key facts

- One workspace app per workspace. Fact.
- The workspace is the staging area. Changes reach app users only when you select Update app. Fact.
- App users cannot modify content. They can filter, highlight, and sort. Fact.
- Workspace apps are the experience formerly called Power BI apps. Org apps are a newer, separate Fabric item type. Existing workspace apps are not auto-migrated. Fact.
- Power BI does not email internal users when you publish or update. External users get an email with a direct link. Fact.

## Steps to publish an app

1. In the workspace list, select Create app.
2. Setup tab: name, description, theme color, support link, contacts.
3. Content tab: add items and links; order them.
4. Audience tab: create audiences, hide or show items per audience, and add users or groups.
5. Publish app. Copy the link from the confirmation or the Setup page.

By default a first publish includes all content for every audience. When you update, newly added content is hidden by default and must be unhidden per audience. Fact.

## Audiences

- Each audience sees only the items you leave visible. Users in several audiences see tabs plus a combined All view. Fact.
- Advanced settings per audience: allow sharing of the semantic models, and allow building content on them. Build applies only to models in the same workspace as the app. Fact.
- "Access to hidden content" lets anyone with a direct link open hidden items. Hiding is a navigation choice, not security. Fact.
- Dashboard tiles break if their source report is missing or hidden from the audience. Add the reports, or allow access to hidden content. Fact.
- If an audience reaches models in other workspaces, give those users access to the models yourself. Fact.

## Licenses

- You need Pro or Premium per user (PPU) to create or update an app. Fact.
- In a workspace on Premium capacity or Fabric F64 or larger, users without Pro or PPU can view the app but cannot copy reports. Otherwise every viewer needs Pro or PPU. Fact.
- Free users cannot edit, update, republish, create, or reshare apps. Fact.

## Update, unpublish, install

- Update: change the workspace, then Update app. People who already have permission keep it; removing permission in the app does not remove existing semantic model rights. Remove them manually. Fact.
- Removing a report and updating deletes user bookmarks and comments for it for good. Fact.
- Unpublish uninstalls the app for all and also drops users' customizations, even after republishing. Admin or Member can do it. Fact.
- Auto-install: if the Fabric admin allows it, tick install automatically. It cannot be combined with "Entire organization". Guests who have not accepted an invite do not get it. Fact.
- Users can request access. You can replace the default request flow with a custom message, but mobile apps still show the default flow. Fact.

## Common mistakes

- Adding a dashboard without its reports, giving the audience an empty app.
- Forgetting that the app ID of an item differs from the workspace item ID when reading logs.
- Publishing at peak hours with many items; publish off-hours and verify with a few users first.

## Limits and version notes

| Limit | Value |
|---|---|
| Apps per workspace | 1 |
| Audiences per app | 25 |
| Users and groups with access, whole app | 10,000 |
| Users or groups per audience | 1,000 |
| Dashboards per app | 200 |
| Publish or update timeout | 1 minute |

Workspace users count once per audience against the 10,000 total. You can hit 10,000 before 25 audiences. Fact. Multiple audiences are not fully supported in deployment pipelines; manage visibility manually. Fact.

## See also

- [Org apps](08_org_apps.md)
- [Distribution decision guide](08_distribution_decision_guide.md)
