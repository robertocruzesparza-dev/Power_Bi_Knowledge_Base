---
id: 23.workspace_design
title: Workspace design decision guide
domain: patterns_recipes
type: decision
level: intermediate
tags: [workspace, governance, decision-guide, best-practice]
summary: How to decide workspace scope, whether to split data from reports, and how many stages to use.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S1835, S1842, S1826, S1819, S1836]
references: []
related: [15.environments_workspace_strategy, 23.rls_pattern_choice, 23.license_choice]
---
## Purpose

A workspace is the unit of access, capacity assignment, and release. A poor layout causes over-sharing, outages, and group sprawl. These questions help you settle the layout once.

## Key facts

- Fact: Roles are set per workspace. You cannot let someone edit some items but not others in the same workspace [S1835].
- Fact: One workspace maps to one Power BI app. A broad workspace yields a crowded app [S1835].
- Fact: A workspace can hold at most 1,000 items (Fabric and Power BI) per the Git integration limits [S1819]. Treat as a design guardrail.
- Fact: Row-level security (RLS) does not apply to Admin, Member, or Contributor roles. Only Viewers are filtered [S1836].
- Fact: Microsoft advises separating data workspaces from reporting workspaces for subject areas, to simplify roles and semantic model security [S1842].

## Decision questions

1. Who owns the content: business unit, shared model team, or central BI [S1835]?
2. Do many report authors reuse one certified model? If yes, separate the model into a data workspace [S1835].
3. Do consumers need only to read? Give them an app or Viewer role on production.
4. Will content be released in stages? If yes, plan Dev, Test, Prod; see [environments](../15_devops_lifecycle/15_environments_workspace_strategy.md).
5. Will several developers use Git? Add private workspaces per branch [S1835].
6. Does sensitive data need a different audience or capacity? Use its own workspace.

## Recommended defaults

| Scenario | Layout |
|---|---|
| Small team, one report | One workspace, one app; add a test stage later |
| Managed self-service | Data workspace per subject area, reporting workspaces per team |
| Enterprise BI | Staged pipelines for models and reports, with autobinding |
| Experiments | Sandbox workspace, cleaned on a schedule |

Source: [S1835]; table shaped by Inference.

Avoid one workspace per department as the first move. Departments are broad and the resulting workspace gets crowded [S1835].

## Common mistakes

- Giving report authors Contributor on the model workspace, which bypasses RLS for them [S1836].
- Skipping naming rules once data and report workspaces are split [S1835].
- Granting access to individuals rather than Entra groups.
- Letting production receive direct edits [S1826].

## See also

- [Environments and workspace strategy](../15_devops_lifecycle/15_environments_workspace_strategy.md)
- [RLS pattern choice](23_rls_pattern_choice.md)
- [License choice](23_license_choice.md)
