---
id: 15.deployment_rules
title: Deployment rules
domain: devops_lifecycle
type: how-to
level: intermediate
tags: [deployment-pipeline, data-source, devops]
summary: How data source, parameter, and default lakehouse rules change item settings per pipeline stage, with their limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1807, S1824, S1827, S2935]
references: []
related: [15.deployment_pipelines, 15.environments_workspace_strategy]
---
## Purpose

Test and production usually read different databases. A deployment rule tells the pipeline to swap a data source or parameter value when content lands in a stage. You define it once; it applies on every later deployment.

## Key facts

- Fact: Rules are created on the target stage under the item. They cannot be created in the development stage [S1807].
- Fact: You must own the item to create a rule [S1807].
- Fact: Rules take effect only on the next deployment to that stage [S1807].
- Fact: A data source rule can only swap to a source of the same type [S1807].
- Fact: One data source cannot appear in more than one rule [S1807].

## Rule types by item

| Item | Data source | Parameter | Default lakehouse |
|---|---|---|---|
| Dataflow Gen1 | Yes | Yes | No |
| Semantic model | Yes | Yes | No |
| Paginated report | Yes | No | No |
| Mirrored database | Yes | No | No |
| Notebook | No | No | Yes |

Source: [S1807].

## Steps

1. Open the target stage (Test or Production) and select **Deployment rules**.
2. Pick the item. Only items with a rule type are listed.
3. Choose a rule type and **Add rule**.
4. For a data source rule, pick the source and the new value from a list, or choose Other and type it.
5. For a parameter rule, pick the parameter and set its value.
6. Deploy again so the rule applies.

Example: a semantic model has parameter `ServerName`. Set a parameter rule on Production to `prod-sql.contoso.com`. Every deploy from Test then sets that value.

## Supported data sources

Data source rules work for these sources on semantic models and Dataflow Gen1 [S1807]: Azure Analysis Services, Azure Synapse, SQL Server Analysis Services, Azure SQL Server, SQL Server, OData feed, Oracle, SAP HANA (Import mode only), SharePoint, and Teradata. For other sources, use parameters.

## Common mistakes

- Setting a rule, then not redeploying.
- Changing or removing the source parameter in the earlier stage. The rule becomes invalid and the deployment fails [S1807].
- Unassigning and reassigning a workspace. Rules for it are lost [S1807].
- Expecting Direct Lake models to follow rules the same way. Per the Direct Lake page, deployment pipeline rules to rebind data sources are not supported for Direct Lake on OneLake, but supported for Direct Lake on SQL [S1827]. The assign-workspace page says to use data source rules to bind Direct Lake models [S1824]. Official pages differ; test your case.

## Limits

Not supported [S1807]:
- Data source rules for dataflows with other dataflows as sources, or CDM folders.
- Data source rules for models that use Dataflow Gen1 as their source.
- Data source rules on models that mix native query and DirectQuery.
- Data source rules on parameterized sources.
- Parameter rules for paginated reports.
- Power Query Online data sources in paginated reports.
- After deploying a paginated report with a rule, Power BI Report Builder cannot open it [S1807].

## See also

- [Deployment pipelines](15_deployment_pipelines.md)
- [Environments and workspace strategy](15_environments_workspace_strategy.md)
