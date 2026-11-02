---
id: 19.gateway_error_catalog
title: Gateway error catalog
domain: troubleshooting
type: reference
level: intermediate
tags: [troubleshooting, gateway, error-message, reference]
summary: Catalog of documented on-premises data gateway errors for Power BI with the underlying message, cause and remedy.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2123]
references: []
related: [19.gateway_errors]
---

# Gateway error catalog

| Error | Underlying detail | Cause | Fix |
|---|---|---|---|
| Power BI service reported local gateway as unreachable | Validation call fails at end of setup | Service communication | Restart Windows service; collect logs |
| Unable to Connect: Invalid connection credentials | `Login failed for user 'username'` | Wrong login or method | Verify credentials on source |
| Unable to Connect: Cannot connect to the database | `Cannot open database ... requested by the login` | Database name or rights | Check name and permissions |
| Unknown error in data gateway | Code DM_GWPipeline_UnknownError | Server unreachable | Test from gateway host; event log |
| Gateway can't access the on-premises data source | Code DM_GWPipeline_Gateway_DataSourceAccessError | Data source access | Validate source details |
| EffectiveUserName value not valid | Account not server admin of Analysis Services | Permissions | Grant server admin rights |
| The username or password is incorrect (Analysis Services) | Missing TGGAU attribute, or no two-way domain trust | AD config | Enable attribute; verify trust |
| No gateway installed or configured for these data sources | Source not on gateway | Missing data source | Add data source; relogin |
| Credentials invalid on test | Test omits optional parameters | Connector needs them | Ignore if refresh works |
| There is not enough space for this row | Row about 4 MB | Large row | Reduce or split |
| Server name doesn't match SSL certificate | NetBIOS vs FQDN | Name mismatch | Use FQDN |
| Gateway not shown for scheduled refresh | Names differ, not on Users list, or a source undefined | Config | Align names, add user and sources |
| Received uncompressed data exceeded the limit | 10 GB per table segment | Large table | Reduce or DirectQuery |
| DM_GWPipeline_Gateway_SpooledOperationMissing | Service restart or cloned VM | Host event | No cloning; fresh install |
| Report could not access the data source (gateway) | Name mismatch or no data source | Config | Match names; add source |
| Data source access error (contact gateway admin) | EffectiveUserName not matching UPN | UPN mismatch | Check `whoami /upn`; map user names |
| ImpersonationLevel: Identification | SPN or policy | Kerberos | Set SPN and constrained delegation |
| FailedToImpersonateUserException | Cannot impersonate | Domain trust or invalid user | Verify config |
| General error 1033 (SAP HANA) | External ID mismatch | sAMAccountName | Use ADUserNameReplacementProperty |
| -10709 Connection failed (SAP HANA Kerberos) | Delegation | AD delegation | Add SAP HANA server in delegation tab |

All rows from S2123. Also: bring-your-own Azure Relay does not support Private Link [S2123].
