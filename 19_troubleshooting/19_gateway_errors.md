---
id: 19.gateway_errors
title: Gateway errors - causes and fixes
domain: troubleshooting
type: troubleshooting
level: intermediate
tags: [troubleshooting, gateway, error-message, refresh]
summary: The most common on-premises data gateway errors for Power BI, grouped by configuration, data source, model and Kerberos, with first fixes.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2123, S2116, S2122]
references: [../references/troubleshooting/19_gateway_error_catalog.md]
related: [19.refresh_errors, 19.credentials_auth_errors, 19.diagnostics_workflow]
---

# Gateway errors - causes and fixes

## Purpose
Resolve gateway problems quickly. Gateway types: standard, personal, and virtual network (VNet) gateway [S2116]. Full list: [gateway error catalog](../references/troubleshooting/19_gateway_error_catalog.md).

## Rules that explain many failures
- Fact: Desktop server and database names must equal the gateway data source names, case insensitive; an IP in Desktop needs an IP in the gateway [S2123].
- Fact: your account must be on the data source Users list [S2123].
- Fact: every on-premises source in a file needs a matching gateway data source [S2123].
- Fact: only the last six gateway versions are supported; update first [S2122, S2123].

## Frequent errors
| Message or code | Cause | First fix |
|---|---|---|
| Invalid connection credentials | Source rejected login | Test the same login on the gateway machine [S2123] |
| Cannot connect to the database | Server reached; database or permission wrong | Check database name and rights [S2123] |
| DM_GWPipeline_UnknownError | Source unreachable or other | Test from gateway host; check gateway service event log [S2123] |
| DM_GWPipeline_Gateway_DataSourceAccessError | Gateway reached; source access failed | Validate data source; Analysis Services needs server admin rights [S2123] |
| No gateway installed or configured for data sources | Missing or mismatched data source | Add data source; clear cache or re-sign-in [S2123] |
| There is not enough space for this row | Row over about 4 MB | Split or filter large text columns [S2123] |
| Uncompressed data exceeded the limit | 10 GB uncompressed per table segment | Surrogate keys, remove columns, split tables, consider DirectQuery [S2123] |
| DM_GWPipeline_Gateway_SpooledOperationMissing | Gateway service restarted, or cloned VM | Avoid cloning; reinstall on new host [S2123] |
| Credentials invalid on test but refresh works | Test connection omits optional parameters (for example Snowflake role) | Ignore if refresh succeeds [S2123] |
| SSL certificate server name mismatch | NetBIOS name vs FQDN | Use the FQDN in gateway and PBIX [S2123] |

## Kerberos and single sign-on
- ImpersonationLevel Identification: set up a service principal name (SPN) and constrained delegation [S2123].
- FailedToImpersonateUserException: user not valid in AD or no cross-domain trust [S2123].
- SAP HANA 1033 error: needs the sAMAccountName replacement setting; -10709: fix delegation tab [S2123].

## Common mistakes
- Using a personal-mode gateway for shared sources.
- Forgetting Private Link is unsupported on a bring-your-own Azure Relay [S2123].

## See also
- [Refresh errors](19_refresh_errors.md)
- [Diagnostics workflow](19_diagnostics_workflow.md)
