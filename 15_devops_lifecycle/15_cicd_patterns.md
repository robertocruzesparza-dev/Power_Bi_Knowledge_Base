---
id: 15.cicd_patterns
title: CI/CD patterns for Power BI and Fabric
domain: devops_lifecycle
type: comparison
level: advanced
tags: [devops, git-integration, deployment-pipeline, automation]
summary: Compares ways to release Power BI content - Git with pipelines, fabric-cicd, bulk API, XMLA, plain REST import - and when to pick each.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1822, S1820, S1821, S1826, S1841, S1844, S1845, S1825, S2928, S2936]
references: []
related: [15.git_integration, 15.deployment_pipelines, 15.pbip_format, 14.powershell_cli_tooling]
---
## Purpose

Continuous integration and continuous delivery (CI/CD) means every change is validated and released by a repeatable process. This file helps you choose that process for Power BI content.

## Key facts

- Fact: Fabric Git integration connects a workspace to GitHub or Azure DevOps. CI jobs run in any runner, such as GitHub Actions or Azure Pipelines [S1820].
- Fact: Microsoft lists several release options: fabric-cicd, the Bulk Import Item Definitions API, and Fabric deployment pipelines [S1822].
- Fact: Microsoft also documents older Premium-based options: Power BI REST APIs with pipelines, plain REST import of PBIX files, and XMLA deployment of model metadata [S1841].
- Fact: XMLA and deployment pipelines are Premium or Fabric features. Plain REST import works without Premium but needs more scripting [S1841].

## Options compared

| Option | Git is source of truth | Dependency order | Per-environment values | Needs Fabric capacity |
|---|---|---|---|---|
| Git integration + deployment pipelines | Dev stage only | Handled by service | Deployment rules | Yes |
| fabric-cicd (Python) | Yes | Handled by library | Parameter file | Yes |
| Bulk Import Item Definitions API | Yes | Handled by service | Custom script | Yes |
| Power BI REST import of PBIX | No | You script it | You script it | No |
| XMLA metadata deploy (Tabular Editor CLI, ALM Toolkit) | Model files | Model only | You script it | Premium or Fabric |

Sources: [S1822, S1821, S1841, S1826]. Cells for the last two rows are Inference from those pages.

Microsoft says to consider the bulk API when Git is the single source of truth, the team uses trunk-based branching, and you need a build step to change workspace-specific values before deploy [S1822]. For the deployment pipelines option, Git connects only to the dev stage; later stages deploy workspace to workspace, and pipeline APIs can run from Azure DevOps or GitHub workflows [S1822].

## Worked example

Branch-per-environment with fabric-cicd on Azure DevOps [S1844, S1845]:

1. Developers branch out to private workspaces, edit, and open a pull request into `main`. `main` syncs to the dev workspace.
2. A pipeline job installs `fabric-cicd`, signs in as a service principal, and runs the deploy for the target environment.
3. A `parameter.yml` file swaps workspace and item IDs, for example via `find_replace` rules.
4. `publish_all_items` deploys. Orphan cleanup can remove items deleted from the branch; use it only for full releases [S1844].
5. A variable library, if present, is always deployed first, and a matching value set is activated by environment name [S1845].

## Common mistakes

- Cleaning up orphans in a selective deploy. It deletes unlisted items of the scoped types [S1844].
- Mixing manual edits in production with automated releases. The next release overwrites them.
- Embedding secrets in YAML. Use a vault; Microsoft suggests Azure Key Vault [S1841].
- Assuming a service principal supports every item and every action. Some do not, such as dataflows [S1841].

## Limits and version notes

- Many Power BI item types in Git and pipelines are still preview [S1804, S1802]. See the [reference](../references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md).
- fabric-cicd needs Python 3.9 through 3.13 [S1839].
- Microsoft describes fabric-cicd as officially supported and open source [S1821].
- Community practice (Fact label: community, unverified here): teams often add automated tests via DAX queries or Best Practice Analyzer rules in the build step.

## See also

- [Fabric Git integration](15_git_integration.md)
- [Deployment pipelines](15_deployment_pipelines.md)
- [PowerShell and CLI tooling](../14_embedding_apis/14_powershell_cli_tooling.md)
