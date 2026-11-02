---
id: 12.audit_operations
title: Selected audit log operation names
domain: admin_governance_security
type: reference
level: advanced
tags: [audit, catalog, reference]
summary: A curated list of common Power BI and Fabric audit operation names with friendly names, taken from the Microsoft operation list.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1524, S3006]
references: []
related: [12.audit_activity_logs]
---
## Scope

The full Microsoft list has hundreds of operations. This is a curated subset for common governance questions. Use the operation name in filters. Source: S1524.

## Viewing and content lifecycle

| Operation name | Friendly name |
|---|---|
| ViewReport | Viewed Power BI report |
| ViewDashboard | Viewed Power BI dashboard |
| CreateReport | Created Power BI report |
| DeleteReport | Deleted Power BI report |
| CreateDataset | Created Power BI semantic model |
| DeleteDataset | Deleted Power BI semantic model |
| CreateApp | Created Power BI app |
| UpdateApp | Updated Power BI app |
| InstallApp | Installed Power BI app |
| PostComment | Posted Power BI comment |
| CreateWorkspace | Create Workspace |

## Sharing and export

| Operation name | Friendly name |
|---|---|
| ShareReport | Shared Power BI report |
| ShareDashboard | Shared Power BI dashboard |
| PublishToWebReport | Published Power BI report to web |
| ExportReport | Exported Power BI report to another file format or exported report visual data |
| ExportArtifact | Exported Power BI item to another file format |
| ExportDataflow | Exported Power BI dataflow |
| PrintReport | Printed Power BI report page |
| AnalyzedByExternalApplication | Analyzed Power BI semantic model |
| GenerateEmbedToken | Generated Power BI Embed Token |

## Security and admin

| Operation name | Friendly name |
|---|---|
| SensitivityLabelApplied | Applied sensitivity label to Power BI item |
| SensitivityLabelChanged | Changed sensitivity label for Power BI item |
| SensitivityLabelRemoved | Deleted sensitivity label from Power BI item |
| SetLakehouseSensitivityLabel | Set Lakehouse Sensitivity Label |
| UpdatedAdminFeatureSwitch | Updated organization's Power BI settings |
| UpdateWorkspaceAccess | Updated Power BI workspace access |
| AddWorkspaceRoleViaAdminApi | Add workspace role |
| ChangeCapacityState | Changed capacity state |
| ExportActivityEvents | Export Power BI activity events |
| GetPublishToWebArtifactsAsAdmin | Get Publish To Web Artifacts As Admin |

## Data operations

| Operation name | Friendly name |
|---|---|
| RefreshDataset | Requested Power BI semantic model refresh |
| SetScheduledRefresh | Set scheduled refresh on Power BI semantic model |
| GetRefreshHistory | Retrieved Power BI refresh history |
| CreateGateway | Created Power BI gateway |
| ApplyChangeToPowerBIModel | Applied a change to model in Power BI |

Notes: ViewReport also fires once per page on export. AddFolderAccess and AddUsersToGatewayCluster are listed as not currently used. All names above were found on the live list on 2026-10-09 [S1524, S3006].
