---
id: 19.credentials_auth_errors
title: Credential and sign-in errors
domain: troubleshooting
type: troubleshooting
level: intermediate
tags: [troubleshooting, refresh, error-message, desktop, security]
summary: Fixes for expired or invalid credentials in refresh, OAuth limits, Desktop sign-in failures behind proxies, and Excel account mismatches.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2122, S2127, S2139, S2123]
references: []
related: [19.refresh_errors, 19.gateway_errors]
---

# Credential and sign-in errors

## Purpose
Separate three problems: data source credentials, Power BI sign-in, and wrong-account use in Excel.

## Data source credentials in the service
- "Access to the resource is forbidden" and refresh failure after a password change: usually cached credentials. Clear the browser cache, sign in, then open `https://app.powerbi.com?alwaysPromptForContentProviderCreds=true` to force a prompt [S2122].
- `GatewayNotReachable` while setting credentials: often an outdated gateway; update [S2122].
- Entra ID OAuth tokens last about one hour and the service waits up to two hours for loads, so long loads can fail with a credentials error [S2122].
- OAuth2 sources must be in the same tenant as the service. Guest accounts and custom AD FS authentication endpoints are unsupported [S2122, S2143].
- "The token service reported by the resource is not trusted" appears with custom AD FS endpoints [S2143].

## Desktop sign-in
| Symptom | Cause | Fix |
|---|---|---|
| Proxy authentication required | Proxy blocks requests | Allow app.powerbi.com, api.powerbi.com and *.analysis.windows.net [S2127] |
| non_https_redirect_failed | A redirect in the sign-in chain is not HTTPS | Ask admin to use HTTPS sites [S2127] |
| "unsupported mode 'query'" with default browser option | Old Desktop | Update, or clear Use my default web browser [S2127] |
| Source sign-in fails after Power BI sign-in works | Old sign-in flow | Options > Security > enable updated sign-in for data sources [S2127] |

## Excel
- "Forbidden": Excel used another Power BI account. Sign in with the account that has access [S2139].

## Common mistakes
- Re-entering the same credentials without clearing the cache.
- Mixing up service credentials and gateway data source credentials.

## See also
- [Gateway errors](19_gateway_errors.md)
- [Refresh errors](19_refresh_errors.md)
