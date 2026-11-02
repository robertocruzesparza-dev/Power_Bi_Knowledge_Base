---
id: 08.lineage_impact_analysis
title: Lineage view and impact analysis
domain: service
type: how-to
level: intermediate
tags: [governance, service, semantic-model, how-to]
summary: How to use lineage view and impact analysis to see upstream and downstream dependencies before changing a semantic model or data source.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S940, S941, S942, S943, S944]
references: []
related: [08.workspace_roles, 08.endorsement, 08.scheduled_refresh]
---
## Purpose

Lineage view draws how items in a workspace connect, from data sources to semantic models, reports, and dashboards. Impact analysis tells you what a change would break and who to warn.

## Key facts

- Lineage view shows all items in the workspace and one level of upstream items from other workspaces. Downstream items in other workspaces are not drawn; use impact analysis for them. Fact.
- Data source cards show details such as the server and database name. Fact.
- Lineage view requires a Pro license and workspace access with Admin, Member, or Contributor. Viewers cannot switch to lineage view. Fact.
- Selecting the arrow under an item highlights its lineage and dims the rest. Fact.
- Semantic model to dataflow lineage displays correctly only if the dataflow was connected through Get Data and the Dataflows connector. Fact.

## Steps

1. Open the workspace and switch to lineage view.
2. Find the semantic model or data source card.
3. Select the impact analysis button on the card.
4. Review the summary: affected workspaces, reports, dashboards, and views.
5. Use Notify contacts to message owners of affected workspaces.

Impact analysis for a semantic model shows distinct viewers and total views over the last 30 days, excluding today, including views through related apps. Fact.

For a data source, it shows the connection string and the count of affected workspaces, dataflows, and semantic models, including workspaces you cannot open. You see only direct children; run impact analysis on those children for further levels. Fact.

## Worked example

You plan to rename a measure in a shared model. Impact analysis shows 14 reports in 6 workspaces and one report with 20,000 viewers. You test that report first and notify the other owners. Illustrative example.

## Common mistakes

- Running impact analysis on an external model shown in lineage view. You must go to the source workspace. Fact.
- Renaming a model or workspace used by composite models. Those connect by names, not IDs, and may break. Fact.

## Limits and version notes

- Lineage view is not supported in Internet Explorer. Fact.
- Lineage for Power BI items can also flow into Microsoft Purview after a tenant scan. Fact.

## See also

- [Endorsement](08_endorsement.md)
- [Workspace roles](08_workspace_roles.md)
