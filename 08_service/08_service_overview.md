---
id: 08.service_overview
title: Power BI service overview and map of this domain
domain: service
type: index
level: beginner
tags: [service, power-bi, index]
summary: Orientation to the Power BI service in Fabric: what lives in a workspace, how content reaches users, and which file covers each task.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S948, S927, S924, S925, S913, S926]
references: []
related: [08.workspaces, 08.workspace_roles, 08.distribution_decision_guide, 08.license_requirements]
---
## Purpose

The Power BI service (app.powerbi.com, also reached through Fabric) is where authors publish and where consumers read. This file shows the parts and points to detail files.

## Key facts

- A workspace is the container for collaboration. It holds reports, semantic models, dashboards, paginated reports, and Fabric items. Fact.
- Dashboards exist only in the service. Reports can be built in Desktop or the service. Fact.
- Content reaches consumers through workspace roles, sharing links, direct access, or an app. Fact.
- "Semantic model" is the current name for what older articles call a dataset. API names still say dataset. Fact.

## How content flows

1. An author builds a model and report in Power BI Desktop.
2. The author publishes the file to a workspace.
3. The semantic model refreshes on a schedule, through a gateway if the source is on-premises.
4. The team reviews content in the workspace.
5. The author distributes: an app (workspace app or org app), sharing links, or workspace access.
6. Consumers read, subscribe, set alerts, and drill from dashboards to reports.
7. Governance adds endorsement, lineage checks, and sensitivity labels.

## Map of files

| Task | File |
|---|---|
| Create and manage workspaces | [Workspaces](08_workspaces.md) |
| Decide what each role can do | [Workspace roles](08_workspace_roles.md) |
| Share one item, set Build or Reshare | [Item permissions and sharing](08_item_permissions_sharing.md) |
| Package content for many users | [Workspace apps](08_workspace_apps.md), [Org apps](08_org_apps.md) |
| Pick a distribution method | [Distribution decision guide](08_distribution_decision_guide.md) |
| Build a one-page overview | [Dashboards](08_dashboards.md) |
| Email snapshots on a schedule | [Subscriptions](08_subscriptions.md) |
| Notify on threshold | [Data alerts](08_data_alerts.md) |
| Keep data current | [Scheduled refresh](08_scheduled_refresh.md) |
| See dependencies before a change | [Lineage and impact analysis](08_lineage_impact_analysis.md) |
| Mark trusted content | [Endorsement](08_endorsement.md) |
| Track goals | [Scorecards and goals](08_scorecards_goals.md) |
| Know which license is needed | [License requirements](08_license_requirements.md) |

## Terminology notes

- "Workspace app" is the long-standing app type formerly just called a Power BI app. "Org app" is a newer Fabric item type. They coexist. Fact.
- A new Apps page is rolling out progressively; you may see either page. Fact.
- Admin-side settings (tenant settings, capacity) belong to the admin and licensing domains, not this one.

## See also

- [Workspaces](08_workspaces.md)
- [Distribution decision guide](08_distribution_decision_guide.md)
