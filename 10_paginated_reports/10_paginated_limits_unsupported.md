---
id: 10.paginated_limits_unsupported
title: Paginated reports limits and unsupported features
domain: paginated_reports
type: troubleshooting
level: intermediate
tags: [paginated-report, limits, troubleshooting, migration]
summary: Features SSRS reports use that Power BI paginated reports do not support, plus numeric limits and known authoring gaps.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1224, S1225, S1226, S1227, S1232, S1237, S2919, S2923, S2924, S2920]
references: []
related: [10.paginated_expressions, 10.paginated_data_sources]
---
## Purpose

Use this page before migrating SSRS reports, or when an upload is rejected.

## Unsupported features

Fact: Uploading a file that uses an unsupported feature gives an error. [S1224]

| Not supported | Alternative |
|---|---|
| SSRS shared data sources (.rds) | Named cloud connections in the service |
| SSRS shared datasets (.rsd) | Use a Power BI semantic model as source |
| Linked reports | None stated |
| Custom fonts | Use installed service fonts (inference) |
| Custom assemblies (DLL) | Embedded code or Azure Functions |
| Report viewer control in the service | None. Vote on ideas site |
| Pinning report tiles to dashboards | Listed as not yet available; vote on ideas site |

Source: S1224. Pinning wording is indirect: the FAQ points to the ideas site rather than saying "unsupported".

## Numeric limits

| Limit | Value | Source |
|---|---|---|
| Data sources per report | 250 | S1224 |
| Default dataset time-out | 600 seconds | S1224 |
| Semantic model DirectQuery source time-out | 10 minutes | S1225 |
| Subscription run time | 60 minutes | S1226 |
| Subscription attachment | 25 MB | S1226 |
| Concurrent renders per workload | 500 | S1227 |

## Authoring gaps

- Web authoring is preview and not equal to Report Builder. No hierarchies. No live-connection models. [S1237]
- External tenant accounts can see Access denied in Report Builder. [S1224]
- DateTime parameters arrive in US format. [S1224]
- Embedding: no client events, no setAccessToken, no push-dataset sources, no AAS with SSO enabled. [S1232]

## Migration help

For SQL Server 2022 Reporting Services, Microsoft documents publishing .rdl files to Power BI. For earlier versions it points to the open-source RDL Migration Tool on GitHub. [S1224]

## Common mistakes

- Assuming every .rdl uploads as is. Test with a copy.
- Hard-coding gateway-only sources without a gateway admin.

## See also

- [Expressions](10_paginated_expressions.md)
- [Data sources](10_paginated_data_sources.md)
