---
id: 19.embedding_error_catalog
title: Embedding error catalog
domain: troubleshooting
type: reference
level: advanced
tags: [troubleshooting, embedding, error-message, reference]
summary: Catalog of documented Power BI embedded IError messages, HTTP codes and possible causes for user-owns-data and app-owns-data scenarios.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2124]
references: []
related: [19.embedding_errors]
---

# Embedding error catalog

## Embedding for Power BI users
| Message | Detail | Code | Possible reasons |
|---|---|---|---|
| TokenExpired | Access token has expired | 403 | Expired token |
| PowerBIEntityNotFound | Get report failed | 404 | Wrong or missing report ID |
| Invalid parameters | powerbiToken not specified | n/a | No token or report ID |
| LoadReportFailed | Fail to initialize - Couldn't resolve cluster | 403 | Bad token; embed type mismatch |
| PowerBINotAuthorizedException | Get report failed | 401 | Wrong or unauthorized group ID |
| TokenExpired | ...Couldn't render a report visual | n/a | Query data with expired token |
| OpenConnectionError | Can't display the visual | n/a | Capacity paused or deleted mid-session |
| ExplorationContainer_FailedToLoadModel_DefaultDetails | Couldn't load model schema | n/a | Capacity paused or deleted |

## Embedding with an embed token (non-Power BI users)
| Message | Code | Possible reasons |
|---|---|---|
| TokenExpired | 403 | Expired token |
| LoadReportFailed (Get report failed) | 404 | Wrong report ID or report missing |
| LoadReportFailed (Get report failed) | 403 | Report ID does not match token |
| LoadReportFailed (Get report failed) | 500 | Report ID is not a GUID |
| Invalid parameters | n/a | No token or report ID |
| LoadReportFailed (Couldn't resolve cluster) | 403 | Wrong token type or bad token |
| PowerBINotAuthorizedException | 401 | Wrong group ID |
| OpenConnectionError, FailedToLoadModel | n/a | Capacity paused or deleted |

## Identity and registration
| Symptom | Cause |
|---|---|
| AADSTS70002 / AADSTS50053 | Direct authentication not enabled |
| AADSTS90094 grant requires admin permission | User consent disabled |
| CS1061 AcquireToken missing | Needs ActiveDirectory library 2.22.302111727 |
| Power BI service missing in app registration | No user signed up for Power BI |
| App registration failure | Not Entra admin and user registration disabled |

All rows from S2124.
