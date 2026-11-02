---
id: 14.embed_tokens
title: Embed tokens and the Generate Token API
domain: embedding_apis
type: reference
level: advanced
tags: [embedding, rest-api, rls]
summary: What an embed token is, the V2 Generate Token request, its limits, RLS identity rules, and token lifetime behavior.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1809, S1810, S1827, S2617]
references: []
related: [14.embed_for_customers, 14.js_client_api, 14.embed_service_principal_capacity]
---
## Purpose

An embed token is a short-lived credential that lets a browser open specific Power BI items. Your back end creates it. It applies only to the app-owns-data model.

## Key facts

- Fact: Endpoint: `POST https://api.powerbi.com/v1.0/myorg/GenerateToken` (V2). It handles reports and semantic models, single or several [S1809].
- Fact: Dashboards and tiles use the older V1 APIs, one item per call [S1810].
- Fact: Limits: up to 50 reports, 50 datasets, and 50 target workspaces per token. All items must be in V2 workspaces [S1809].
- Fact: You cannot create a token for My workspace [S1810].
- Fact: If the report and semantic model are in different workspaces, the caller must be at least a Member of both [S1810].

## Request body fields

| Field | Meaning |
|---|---|
| reports | Reports to open. `allowEdit: true` permits editing |
| datasets | Semantic models. `xmlaPermissions` can be `Off` or `ReadOnly` |
| targetWorkspaces | Workspaces where the user may create or save reports |
| identities | RLS identities: username, roles, datasets, customData |
| datasourceIdentities | Single sign-on identities, with an identity blob |
| lifetimeInMinutes | Shortens the token life. It cannot extend it. 0 means default |

Source: [S1809].

## Worked example

Open one report read-only with an RLS role, valid for at most 10 minutes:

```json
{
  "reports": [{ "id": "<report-id>" }],
  "datasets": [{ "id": "<dataset-id>" }],
  "identities": [{
    "username": "john@contoso.com",
    "roles": ["sales"],
    "datasets": ["<dataset-id>"]
  }],
  "lifetimeInMinutes": 10
}
```

The response holds `token`, `tokenId`, and `expiration`. The `tokenId` helps tie audit-log entries to the generate call [S1809].

## RLS and identity rules

- A service principal must always supply an identity for any item with an RLS model [S1810].
- A master user may omit the identity for cloud RLS; then the token sees all data [S1810].
- Paginated reports (RDL) cannot use a master user to get a token; use a service principal [S1810].
- Roles: up to 50 per identity. A role name cannot contain a comma and has a 50-character limit. A username has a 256-character limit and no spaces [S1809].
- With single sign-on (SSO) on App-owns-data, only Azure SQL Database is supported for DirectQuery, and every SSO source needs an identity blob [S1810].
- A report whose model uses DirectQuery over another Power BI model needs all related dataset IDs listed with `xmlaPermissions: ReadOnly`. Trial tokens do not work for this case [S1810].
- Direct Lake embedding needs the V2 token [S1827].

## Token lifetime

The token life equals the remaining life of the Entra token that made the call. Reusing one Entra token shortens each new embed token [S1810]. Renew the embed token before expiry with the JavaScript client; see [JS client API](14_js_client_api.md).

## Common mistakes

- Asking for a longer life with `lifetimeInMinutes`. It can only shorten.
- Sharing one token across users with different RLS needs. Make one per identity.
- Caching the Entra token and wondering why embed tokens expire sooner.

## See also

- [Embed for your customers](14_embed_for_customers.md)
- [JS client API](14_js_client_api.md)
- [REST API overview](14_rest_api_overview.md)
