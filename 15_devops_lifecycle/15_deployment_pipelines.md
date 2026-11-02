---
id: 15.deployment_pipelines
title: Deployment pipelines
domain: devops_lifecycle
type: concept
level: intermediate
tags: [deployment-pipeline, devops, workspace]
summary: How Fabric deployment pipelines promote content through stages, how pairing works, who can deploy, and which API calls automate it.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1802, S1823, S1824, S1825, S1840, S1826, S2600, S2601]
references: [../references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md]
related: [15.deployment_rules, 15.git_integration, 15.cicd_patterns, 15.environments_workspace_strategy]
---
## Purpose

A deployment pipeline gives a team a release path. Content moves from a development workspace to a test workspace to a production workspace. Users of production never see half-finished work.

## Key facts

- Fact: A pipeline has 2 to 10 stages. The default is three: Development, Test, Production [S1802].
- Fact: Each stage is backed by one workspace. Workspaces must be on a Fabric capacity, and a workspace can sit in only one pipeline [S1824].
- Fact: Data is not copied between stages. After a deployment, refresh the semantic models [S1823].
- Fact: Deployment copies item metadata. Item properties that are not copied are listed on the Learn page "Understand the deployment process" [S1802].
- Fact: Many Power BI item types are still marked preview in the supported list: dashboards, dataflows, paginated reports, reports, and semantic models from PBIX [S1802]. Check the live list.
- Fact: The new pipeline user interface is in preview; the original design still exists [S1802].
- Fact: Since 2026-02-12, semantic models not upgraded to enhanced metadata are no longer supported in pipelines [S1802].
- Fact: A deployment plan (preview) can attach explicit order and actions to a deployment [S1802].

## How it works

**Pairing.** An item in one stage is linked to the same item in the next stage. Paired items overwrite on deploy. Unpaired items with the same name are not overwritten; a duplicate is created [S1802]. Paired items keep the link when renamed.

**Autobinding.** After a deploy, a report in the target stage points to the paired semantic model in the target stage, so you do not rebind by hand. Direct Lake models are an exception: they stay bound to the source-stage item. Learn says to use data source rules [S1824, S2601]. The Direct Lake overview says rules are supported for Direct Lake on SQL but not for Direct Lake on OneLake [S2600]. Treat OneLake-mode rebinding as unresolved; rebind with the semantic model API or Git instead (inference).

**Selective deployment.** You can deploy chosen items. Use **Select related** so a report is deployed together with its semantic model [S1826].

**Backward deployment.** New items can be pushed to an earlier stage, only if they do not already exist there [S1825].

## Steps

1. Create a pipeline (needs a Pro, PPU, or Premium license) [S1823].
2. Assign a workspace to the Development stage. Deploying to an empty stage creates a new workspace on a capacity for that stage [S1823].
3. Deploy Development to Test. Refresh the semantic models.
4. Add [deployment rules](15_deployment_rules.md) on the Test or Production stage so each stage uses its own data source.
5. Compare stages. Deploy Test to Production.

## Automation

The Power BI Pipelines API group supports create, assign, unassign, deploy all, selective deploy, get operations, and user management. A deploy call can update the related app [S1825]. These APIs apply to Power BI items and cannot attach a deployment plan; use the Fabric Deploy Stage Content API for that [S1825]. Microsoft recommends a service principal for pipeline calls [S1840].

## Common mistakes

- Editing production content directly. Microsoft advises one direction: development to test to production [S1826].
- Forgetting to refresh after the first deploy.
- Believing a pipeline admin can deploy. Deploying also requires workspace roles [S1823].
- Removing and re-adding a workspace. Pairing and rules are lost.

## Limits and version notes

- Not all workspaces qualify: no template-app workspaces, no workspaces containing Power BI samples [S1824].
- Learn lists a single deployment at most 300 items. It also says PBIR reports are not supported in deployment pipelines (verified 2026-10-08; recheck, as PBIR is the default format) [S2601].
- From 2026-12-01, users without read-write permission on all items cannot deploy into workspaces holding items protected by label protection policies [S1823].
- Paginated report deployments with rules in bulk can fail on capacity overload. Use a larger SKU or selective deployment [S1840].
- The supported-item list and permission table live in the [reference](../references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md).

## See also

- [Deployment rules](15_deployment_rules.md)
- [CI/CD patterns](15_cicd_patterns.md)
- [Environments and workspace strategy](15_environments_workspace_strategy.md)
