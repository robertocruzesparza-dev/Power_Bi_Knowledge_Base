---
id: 08.scorecards_goals
title: Scorecards and goals (metrics)
domain: service
type: reference
level: intermediate
tags: [service, dashboard, limits, monitoring]
summary: What scorecards and goals are, license rules, creation steps, status rules, subscriptions, and the documented limitations.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S945, S946, S947, S930, S924, S2906, S2907]
references: []
related: [08.dashboards, 08.subscriptions, 08.workspace_roles]
---
## Purpose

Scorecards collect goals so teams can track progress against business objectives in one view. A goal has a current value, a final target, owners, a status, and dates.

## Key facts

- Docs use "goals" and "scorecards". Older URLs and text still say "metrics". Fact.
- Goals can be manual (check-ins) or connected to a report visual. Fact.
- Subgoals nest up to four levels. Fact.
- Scorecard permissions are separate at goal level, so some people see only certain goals. Fact.
- A scorecard saves with an associated semantic model that houses the goal data, in its workspace. Fact.

## Licenses

| Task | Minimum |
|---|---|
| Author and share scorecards and goals, do check-ins | Pro |
| View scorecards and goals | Premium or Fabric F64 or larger with a free user, or Pro |
| View samples and author in My workspace | Free |

Creating a scorecard in a workspace requires the Contributor role or higher, plus Build permission on any connected semantic model. Fact.

## Steps to create a scorecard

1. Open Scorecards from the navigation pane, then create a new scorecard.
2. Name it. It saves in My workspace; move it to another workspace through the File menu if needed.
3. Add a goal: name (the only required field), owners, current value, final target, status, start and due dates.
4. Optionally add subgoals, status rules, and sharing.

## Status rules

Rules set a goal's status from value, percent of target met, or date, or a combination. Connected goals update on scorecard data refresh. Manual goals update on check-in. Rules can be reordered by priority. Fact. Automatic refresh of status rules is not supported in the mobile experience. Fact.

## Limitations

| Limitation | Detail |
|---|---|
| Goals per scorecard | 1,000 maximum |
| Row-level security | Not supported |
| Bring your own key | Not supported |
| Publish to web | Not supported |
| Cross-tenant (B2B) sharing | Not supported |
| Multi-Geo capacity | Not supported |
| Embedded analytics | Not supported |
| SharePoint embed of scorecard visual | Not working |
| Subscriptions | Up to 24 per scorecard; none from inside an app or org app |

## Common mistakes

- Sharing a scorecard with view-only rights and expecting users to add check-ins. They need edit permission.
- Assuming RLS on the source model protects goal data. Goals do not support RLS.

## See also

- [Dashboards](08_dashboards.md)
- [Subscriptions](08_subscriptions.md)
