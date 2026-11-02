---
id: 14.ref_xmla_tools_security_audit
title: XMLA reference - tools, security, and audit operations
domain: embedding_apis
type: reference
level: advanced
tags: [xmla, reference, security, audit]
summary: Reference tables for XMLA client tools and minimum versions, tenant setting combinations, impersonation, and audit log operations.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1808, S2925]
references: []
related: [14.xmla_endpoint]
---
## Client tools

All rows from the official page [S1808]. Read-only means query. Read-write means metadata changes.

| Tool | Needs | Minimum version noted |
|---|---|---|
| Excel PivotTables | Read-only | Click-to-Run Office 16.0.13612.10000 |
| Visual Studio (SSDT) | Read-write to deploy | Extension 2.9.14, compatibility level 1500 or higher |
| SSMS | Read-only to query, read-write to script | 18.9 |
| SQL Server Profiler | Read-only, set Initial Catalog | 18.9 |
| Analysis Services Deployment Wizard | Read-write | Installed with SSMS |
| PowerShell (SqlServer module) | Read-write | 21.1.18256 |
| Power BI Report Builder | Read-only | n/a |
| Tabular Editor 2.x | Read-only query, read-write metadata | n/a |
| DAX Studio | Read-only | n/a |
| ALM Toolkit | Read-only query, read-write metadata | n/a |

The Az.AnalysisServices module is not supported for Power BI models [S1808].

## Tenant settings

Both are on by default [S1808].

| Allow XMLA endpoints and Analyze in Excel with on-premises models | Users can work with semantic models in Excel using a live connection | XMLA | Analyze in Excel |
|---|---|---|---|
| Off | Off | No | No |
| On | Off | Yes | No |
| Off | On | No | Yes |
| On | On | Yes | Yes |

## Impersonation

- `EffectiveUserName` impersonates a user. The account must exist in Entra ID and have Read and Build on the model [S1808].
- The `Roles` property tests role membership. A workspace admin need not belong to the role. Others must [S1808].
- Only Read permission can be set on a role for Power BI models. Other rights come from Power BI security [S1808].

## Audit operations

Access through XMLA is logged with these operation names [S1808]:

| Operation name | Meaning |
|---|---|
| ConnectFromExternalApplication | Connected from an external application |
| RefreshDatasetFromExternalApplication | Refresh requested |
| CreateDatasetFromExternalApplication | Model created |
| EditDatasetFromExternalApplication | Model edited |
| DeleteDatasetFromExternalApplication | Model deleted |

## Unsupported models

Not reachable over XMLA: live connections to Azure or SQL Server Analysis Services, live connections to a model in another workspace, push-data models, and Excel workbook models [S1808].
