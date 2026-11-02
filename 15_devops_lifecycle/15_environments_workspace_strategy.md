---
id: 15.environments_workspace_strategy
title: Environments and workspace strategy for the content lifecycle
domain: devops_lifecycle
type: decision
level: intermediate
tags: [workspace, devops, deployment-pipeline, best-practice]
summary: How to lay out development, test, production, and private workspaces, and how many roles and groups that creates.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1835, S1826, S1841, S1847]
references: []
related: [15.deployment_pipelines, 15.git_integration, 15.deployment_rules]
---
## Purpose

An environment is a workspace that plays one stage of a release path. This file shows the workspace layouts Microsoft's planning guidance describes and the cost of each.

## Key facts

- Fact: Microsoft recommends at least two stages, so creators work apart from consumers. A single workspace makes it hard to avoid disrupting live content [S1835].
- Fact: Separate environments are called essential for lifecycle management [S1826].
- Fact: Separate environments can also use separate gateways and capacities, so development refreshes do not slow production [S1826].
- Fact: The deployment pipeline roles are separate from workspace roles. Workspace roles are set per stage; pipeline access is set once [S1841].

## Layouts

| Layout | Use when | Cost |
|---|---|---|
| Dev, Test, Prod in a pipeline | Standard governed release | 3 workspaces per solution |
| Separate data and report workspaces, each with stages | Shared semantic models, many report authors | Up to 6 workspaces and more groups |
| Private workspace per developer (Git branch) | Several developers on one solution | More workspaces; short-lived |
| Preproduction | Performance or gateway tests | Extra capacity use |
| Sandbox | Experiments, emptied regularly | Needs a cleanup routine |

Layouts from [S1835]. Cost column is Inference.

Reasons to separate data from report workspaces [S1835]: easier reuse of trusted models, separate access for data owners, fewer accidental edits to certified models, clearer ownership, and RLS stays enforced for report creators who have only Build access.

Disadvantages [S1835]: naming rules are needed, users must learn where to publish, and more workspaces need governance.

Tip from Microsoft: organize workspaces around a business activity or project, not around the department chart, which tends to be too broad [S1847].

## Access groups

Groups can multiply fast. Splitting data and report workspaces raises the example from 5 groups to 9, and adding stages can triple admin groups [S1835]. Reduce them: skip a viewers group in development, and reuse one admin group across stages [S1835]. Map roles to Microsoft Entra security groups, not individuals.

## Steps

1. Decide ownership: business-led, managed self-service, or enterprise BI [S1835].
2. Choose the layout from the table above.
3. Name workspaces with solution, type, and stage, for example `Sales - Model - Test`.
4. Create the pipeline and assign workspaces. Add [deployment rules](15_deployment_rules.md).
5. Connect the dev workspace to Git if you version-control; see [Git integration](15_git_integration.md).
6. Give consumers an app or Viewer role on production only.

## Common mistakes

- One workspace for everything, with edits made live.
- Granting consumers Contributor on production. RLS does not apply to Contributor and above (Fact from RLS docs, see the [RLS pattern choice](../23_patterns_recipes/23_rls_pattern_choice.md)).
- Making changes in later stages first [S1826].
- Too many roles and groups to maintain.

## See also

- [Deployment pipelines](15_deployment_pipelines.md)
- [Workspace design decision guide](../23_patterns_recipes/23_workspace_design.md)
- [CI/CD patterns](15_cicd_patterns.md)
