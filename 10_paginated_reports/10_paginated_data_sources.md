---
id: 10.paginated_data_sources
title: Paginated report data sources and authentication
domain: paginated_reports
type: reference
level: intermediate
tags: [paginated-report, data-source, gateway, rls]
summary: Native and gateway data sources for paginated reports, authentication choices, timeouts, and row-level security behavior.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1224, S1225, S1228, S2920, S2919]
references: []
related: [10.paginated_overview, 10.paginated_parameters]
---
## Purpose

Pick the source type first. It decides authentication, gateway need, and whether row-level security (RLS) works.

## Native sources

| Source | Authentication | Notes |
|---|---|---|
| Azure SQL Database, Azure Synapse | Basic, single sign-on (SSO), OAuth2 | Must set credentials after first upload. Enterprise gateway is possible for SQL Database. |
| Azure SQL Managed Instance | Basic, SSO, OAuth2 | VNet-local endpoints route through an enterprise gateway. |
| Azure Analysis Services | SSO, OAuth2 | No gateway. SSO from an external tenant is unsupported. |
| Power BI semantic model | SSO | Import and DirectQuery models. Needs Read permission. |
| Direct Lake models | SSO, OAuth2 | SQL endpoint models allow both; models on OneLake allow SSO. |
| Dataverse | SSO, OAuth2 | No gateway, since multifactor authentication is unsupported. |
| Enter data | none | Data is embedded in the report. |

Source: S1225. Changing Azure Analysis Services to OAuth2 cannot be reverted to SSO and applies to all reports using that source in the tenant. [S1225]

## Gateway sources

Through an enterprise or virtual network (VNet) gateway: SQL Server, SQL Server Analysis Services. Enterprise gateway only: Oracle, Teradata, ODBC. [S1225]

The publisher must be a gateway admin to bind the report to a connection. Gateway admin does not give access to existing connections automatically. SSO through Kerberos needs constrained delegation. [S1225]

Stored procedures through a gateway work for SQL Server, including parameters. [S1224]

You can also reach Snowflake and Databricks through the Get Data experience in Report Builder. [S1225]

## Semantic model sources

- Queries to a DirectQuery semantic model have a fixed 10-minute time-out. For longer queries use the XMLA read/write endpoint as the source. [S1225]
- For the XMLA source, tick Do not use credentials in Report Builder. Contributor or higher can render; others need Build. [S1225]
- Data source rules do not work for models using Direct Lake. [S1225]
- A lakehouse SQL analytics endpoint cannot set Query type in Report Builder. Choose Text and call the stored procedure. [S1225]

## Security and timeouts

- RLS in paginated reports only works with SSO. Report Builder RLS needs Viewer on the model's workspace plus Build. [S1225, S1228]
- To filter by user in the query, create a parameter that uses the built-in `User!UserID` and use it in a filter or query. [S1228]
- Embedded dataset time-out defaults to 600 seconds. The maximum you can set is 2147483646. [S1224]
- A report may have at most 250 data sources. Over that, publish fails or render fails. [S1224]
- DateTime parameters in the service arrive in US format (MM/DD/YYYY). [S1224]

## Common mistakes

- Leaving Azure SQL credentials unset after upload.
- Choosing OAuth2 then expecting RLS to work.
- Using AAS through a gateway.

## See also

- [Paginated overview](10_paginated_overview.md)
- [Parameters](10_paginated_parameters.md)
