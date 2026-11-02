---
id: 23.recipe_dev_to_prod_release
title: Recipe - release a report from development to production
domain: patterns_recipes
type: how-to
level: intermediate
tags: [deployment-pipeline, devops, example, how-to]
summary: A step-by-step recipe to promote a report and semantic model through a three-stage deployment pipeline with per-stage data sources.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1802, S1807, S1823, S1824, S1825, S1826, S2930, S2931, S2935]
references: []
related: [15.deployment_pipelines, 15.deployment_rules, 23.workspace_design]
---
## Goal

Release a Sales report and its semantic model from Dev to Test to Production. Test and Production must read their own SQL databases.

## Before you start

- You are admin of the Dev workspace, and it is on a Fabric capacity [S1824].
- Test and Production workspaces can be created by the deployment, or already exist and be on a capacity [S1823].
- The model exposes the database server as a Power Query parameter. Parameter rules are the safest way to switch it (Inference from the supported-source list in [S1807]).
- You have a Pro, PPU, or Premium license to create a pipeline [S1823].

## Steps

1. Create a pipeline. Keep the default three stages [S1802].
2. Assign the Dev workspace to Development.
3. Deploy to Test. The service creates a workspace for the stage [S1823].
4. On the Test stage, open **Deployment rules**, pick the semantic model, and add a parameter rule for the server name. Deploy again so the rule applies [S1807].
5. Refresh the semantic model in Test. Data is not copied between stages [S1823].
6. Check the report with testers. Compare stages to see differences.
7. Deploy Test to Production. Add the same kind of rule for Production first, or deploy then redeploy.
8. Refresh Production. Update the app if one is used.

## Automate it

Use the Pipelines API group: Deploy All or Selective Deploy, with the option to update the app after deployment [S1825]. Poll the operation until it ends. Use a service principal and keep secrets in a vault. For Fabric items beyond Power BI, use the Fabric Deploy Stage Content API [S1825].

## Checks

- Report in Test shows the paired model of Test (autobinding) [S1824].
- Production data comes from the production server, not Test.
- Roles for consumers are set only on Production.

## Common mistakes

- Creating rules but not redeploying [S1807].
- Selecting only the report in a selective deploy. Use **Select related** to include the model [S1826].
- Editing production directly, which pairing may later overwrite.

## See also

- [Deployment pipelines](../15_devops_lifecycle/15_deployment_pipelines.md)
- [Deployment rules](../15_devops_lifecycle/15_deployment_rules.md)
- [Workspace design](23_workspace_design.md)
