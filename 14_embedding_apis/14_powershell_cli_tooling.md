---
id: 14.powershell_cli_tooling
title: PowerShell and CLI tooling for Power BI
domain: embedding_apis
type: reference
level: intermediate
tags: [automation, rest-api, devops]
summary: Which scripting tools drive Power BI and Fabric - MicrosoftPowerBIMgmt, SqlServer cmdlets, Fabric CLI, and fabric-cicd - and when to pick each.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1818, S1808, S1820, S1821, S1839, S1812, S1844, S1826, S2928, S2929, S2933]
references: []
related: [14.rest_api_overview, 14.xmla_endpoint, 15.cicd_patterns]
---
## Purpose

Most Power BI administration can be scripted. This file maps each scripting tool to its job, so you pick the lightest one that works.

## Tool overview

| Tool | Type | Best for |
|---|---|---|
| MicrosoftPowerBIMgmt module | PowerShell | Workspaces, activity events, calling any Power BI REST endpoint |
| `Invoke-PowerBIRestMethod` | PowerShell cmdlet in that module | Any REST call after login |
| SqlServer module (`Invoke-ASCmd`) | PowerShell | XMLA scripting and refresh; needs read-write for writes |
| Fabric CLI (`fab`) | Command line, open source | Filesystem-style work on Fabric items; Git sync; deployment |
| fabric-cicd | Python library | Deploying item definitions from Git to workspaces |
| Terraform provider for Fabric | Infrastructure as code | Provisioning workspaces and capacities |

Sources: [S1818, S1808, S1820, S1821].

## Examples

Sign in and call a REST endpoint [S1818]:

```powershell
Connect-PowerBIServiceAccount
Invoke-PowerBIRestMethod -Url 'groups' -Method Get
```

Add a service principal to a workspace as Member [S1812]:

```powershell
Login-PowerBI
$ws = Get-PowerBIWorkspace -Filter "name eq 'Sales'"
Add-PowerBIWorkspaceUser -Id $ws.Id -AccessRight Member -PrincipalType App -Identifier $spObjectId
```

Install the deployment tools [S1839]: `pip install fabric-cicd` (Python 3.9 through 3.13) and `pip install ms-fabric-cli` (Fabric CLI needs Python 3.10 or higher) [S2933].

## Choosing a tool

- Microsoft recommends `Invoke-PowerBIRestMethod` as the balanced option: simple sign-in, any endpoint [S1818].
- Use cmdlets with names like `Get-PowerBIActivityEvent` when one exists and you do not need other endpoints [S1818].
- For CI/CD of Git-stored items, fabric-cicd is described by Microsoft as the most widely adopted deployment tool for Fabric [S1820]. It resolves dependency order, supports parameter files, and can remove orphan items [S1821].
- `fab deploy` uses fabric-cicd under the hood [S1820].
- Fabric REST APIs can also run inside a Fabric notebook through semantic link, with no app registration [S1826].

## Common mistakes

- Using `Az.AnalysisServices` for Power BI. It is not supported [S1808].
- Running orphan cleanup in a selective deploy. It deletes items of the scoped types that are absent from the branch [S1844].
- Mixing `Login-PowerBI` and `Connect-PowerBIServiceAccount` in one script. Both appear in Microsoft pages; pick one. Whether one is an alias of the other: unverified.

## Limits and version notes

Module and library versions move quickly. Check the PowerShell Gallery and PyPI for current releases.

## See also

- [REST API overview](14_rest_api_overview.md)
- [XMLA endpoint](14_xmla_endpoint.md)
- [CI/CD patterns](../15_devops_lifecycle/15_cicd_patterns.md)
