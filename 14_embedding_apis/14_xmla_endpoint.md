---
id: 14.xmla_endpoint
title: XMLA endpoint (read and write)
domain: embedding_apis
type: concept
level: advanced
tags: [xmla, semantic-model, capacity]
summary: How the XMLA endpoint exposes Power BI semantic models to Analysis Services tools, how to enable read-write, and its limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1808, S1826, S2925]
references: [../references/embedding_apis/14_xmla_tools_security_audit.md]
related: [14.powershell_cli_tooling, 14.rest_api_overview]
---
## Purpose

The XMLA endpoint lets Analysis Services client tools talk to a Power BI workspace as if it were an Analysis Services server. Tools such as SQL Server Management Studio (SSMS), Tabular Editor, and DAX Studio use it to query, script, refresh, and edit semantic models.

## Key facts

- Fact: It works for Premium, Premium Per User (PPU), Fabric, and Embedded workspaces [S1808].
- Fact: Read-only is the default for the semantic model workload. Read-write must be enabled by an admin [S1808].
- Fact: Workspace Contributor and above get Write permission, comparable to Analysis Services database admin. Build permission is comparable to database reader, and RLS applies [S1808].
- Fact: Service principals can use the endpoint for deployment and refresh, but they do not work with RLS or OLS and cannot be role members [S1808].
- Fact: Refresh over XMLA is not capped at 48 per day and is not bound by the scheduled-refresh timeout [S1808].
- Fact: Tools and permissions overview is in the [reference file](../references/embedding_apis/14_xmla_tools_security_audit.md).

## Enable read-write

1. Capacity: Admin portal, then the capacity, then Workloads, and set **XMLA Endpoint** to Read Write. The setting applies to all workspaces on the capacity [S1808].
2. PPU: Admin portal, Premium Per User, Semantic model workload settings, XMLA Endpoint, Read Write [S1808].
3. Tenant: **Allow XMLA endpoints and Analyze in Excel with on-premises semantic models** must be on. It is on by default [S1808].

## Connect

The workspace URL is `powerbi://api.powerbi.com/v1.0/<tenant>/<workspace name>`, with the name URI-encoded. Copy it from Workspace settings, Premium, Workspace Connection. Use `myorg` instead of the tenant name in the home tenant [S1808].

In SSMS choose server type Analysis Services, paste the URL, and sign in with Active Directory Universal with MFA. Workspaces appear as servers and models as databases [S1808].

If two workspaces share a name, append the workspace GUID. If two models share a name, append the model GUID [S1808].

## What read-write allows

- Deploy a model from Visual Studio, or script changes with Tabular Model Scripting Language (TMSL).
- Refresh single tables or partitions, for example one historical incremental-refresh partition.
- Edit metadata with Tabular Editor or ALM Toolkit.
- Credentials cannot be set over XMLA. Set them in the model settings page [S1808].
- Azure Pipelines can call third-party tools such as the Tabular Editor command line to deploy metadata over XMLA [S1826].

## Common mistakes

- Writing to a model authored in Desktop without enhanced metadata. This is required [S1808].
- Assuming you can still download the PBIX after an XMLA write. A write prevents download as PBIX; keep the original [S1808].
- Expecting every model to appear. Live-connected, push, and Excel-workbook models are not available [S1808].

## Limits and version notes

- Default models created for Fabric warehouses cannot be changed via XMLA [S1808].
- SSMS needs version 18.9 or higher; use the February 2026 release or later for personal workspaces [S1808].
- Operations needing server-admin rights are not supported.

## See also

- [XMLA tools, security, and audit reference](../references/embedding_apis/14_xmla_tools_security_audit.md)
- [PowerShell and CLI tooling](14_powershell_cli_tooling.md)
- [ALM Toolkit](../15_devops_lifecycle/15_alm_toolkit.md)
