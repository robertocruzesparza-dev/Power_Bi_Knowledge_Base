---
id: 19.embedding_errors
title: Embedding errors and fixes
domain: troubleshooting
type: troubleshooting
level: advanced
tags: [troubleshooting, embedding, error-message, rest-api]
summary: How to debug Power BI embedded apps using the IError object, token and effective identity checks, and Entra consent errors.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2124, S2141]
references: [../references/troubleshooting/19_embedding_error_catalog.md]
related: [19.diagnostics_workflow, 19.credentials_auth_errors]
---

# Embedding errors and fixes

## Purpose
Resolve failures in embedded apps. Full error table: [embedding error catalog](../references/troubleshooting/19_embedding_error_catalog.md).

## Debug steps
1. Confirm the item loads in the Power BI service, then in the embedded analytics playground [S2124].
2. Check the access token has not expired [S2124].
3. Read the IError object from the JavaScript SDK error event and match the message and code in the catalog [S2124].
4. Log the `RequestId` header and give it to support [S2124].
5. Use Fiddler or browser F12 for network traces [S2124].

## Frequent causes
- Fact: GenerateToken with effective identity fails if the model does not support it, username, role or dataset ID is missing, or permissions are wrong. Check `IsEffectiveIdentityRequired` and `IsEffectiveIdentityRolesRequired` via Get Dataset [S2124].
- Fact: AADSTS70002 or AADSTS50053 means direct authentication is not enabled; use a scoped Microsoft Entra policy, per app, with Global Administrator rights [S2124].
- Fact: AADSTS90094 means user consent is disabled; an admin grants consent or enables user consent [S2124].
- Fact: guest users need the tenant ID in `authorityUri` [S2124].
- Fact: 401 on Get report that self-resolves in user-owns-data: add the Refresh User Permissions call [S2124].
- Fact: capacity paused or deleted yields OpenConnectionError or model schema load failures [S2124].
- Fact: every reader of a model sees the whole schema and data; restrict with RLS, OLS or separate models [S2124].

## Secure embed pitfalls
Top-level page must be HTTPS; Cross-Origin-Opener-Policy `same-origin` blocks sign-in; auto-authentication is blocked in the JavaScript SDK from version 2.10.4 [S2141].

## See also
- [Diagnostics workflow](19_diagnostics_workflow.md)
