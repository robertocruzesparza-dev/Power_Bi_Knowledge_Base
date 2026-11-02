---
id: 14.rest_api_overview
title: Power BI REST API overview
domain: embedding_apis
type: concept
level: intermediate
tags: [rest-api, automation, sdk]
summary: What the Power BI REST API is, how callers authenticate, how throttling works, and when to use the Fabric REST API instead.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1811, S1812, S1818, S1826, S2927]
references: []
related: [14.rest_api_endpoint_catalog, 14.embed_tokens, 14.powershell_cli_tooling]
---
## Purpose

The Power BI REST API lets code manage workspaces, semantic models, reports, refreshes, pipelines, and embed tokens. A script can, for example, trigger a refresh and read its history without opening the portal.

## Key facts

- Fact: The base address for most calls is `https://api.powerbi.com/v1.0/myorg/`. Admin calls add `/admin/`.
- Fact: The reference groups operations into areas such as Groups (workspaces), Datasets, Reports, Pipelines, and Embed Token. See the [endpoint catalog](14_rest_api_endpoint_catalog.md).
- Fact: Calls authenticate with a Microsoft Entra ID access token, from either a signed-in user or a service principal.
- Fact: Some operations do not work with a service principal. Dataflow management is one documented example for embedding scenarios.
- Fact: Power BI Embedded capacity management (create, pause, scale) uses Azure Resource Manager APIs, not this API.
- Fact: The same API powers the .NET SDK package `Microsoft.PowerBI.Api`, and PowerShell wrappers.

## How a call works

1. Register a Microsoft Entra app, or use a user sign-in.
2. Get an access token for the Power BI resource.
3. Send an HTTPS request with the header `Authorization: Bearer <token>`.
4. Read the JSON response. Long operations return an operation ID that you poll.

Example: `GET https://api.powerbi.com/v1.0/myorg/groups` lists the workspaces the caller can see.

For a service principal, a tenant admin must turn on **Allow service principals to use Power BI APIs** in Developer settings. The principal also needs workspace access. Microsoft advises not adding API permissions to the Entra app for this scenario, because unused permissions can cause hard-to-trace errors [S1812].

## Throttling

Power BI limits calls per user inside a time window. When you exceed the limit, you get HTTP 429 (Too Many Requests) and a `Retry-After` header with the wait time in seconds [S1811]. Honor the header. Back off and retry. Exact request quotas are not published in the page I read: unverified.

## Power BI API or Fabric API

- The Power BI REST API covers Power BI item types only.
- The Fabric REST API covers both Power BI and other Fabric items, and offers item-definition operations used by CI/CD [S1826].
- Fabric APIs only work against Fabric workspaces. XMLA endpoints need Fabric or Premium capacity. Power BI import and pipeline calls can also reach workspaces on other capacities [S1826].
- Rule of thumb (Inference): use the Fabric API for new automation of Git-style item definitions. Use the Power BI API for refresh, embed tokens, and pipeline operations that have no Fabric equivalent you rely on.

## Common mistakes

- Ignoring 429 and retrying in a tight loop. The wait gets longer.
- Using a user token for unattended jobs. Use a service principal with a certificate.
- Adding delegated or application permissions to the Entra app "just in case" [S1812].
- Assuming every admin API works with a service principal. Read-only admin APIs need a separate tenant setting [S1812].

## Limits and version notes

Throttling rules, preview endpoints, and supported principals change. Verify against the live reference before building production automation.

## See also

- [REST API endpoint catalog](14_rest_api_endpoint_catalog.md)
- [Embed tokens](14_embed_tokens.md)
- [PowerShell and CLI tooling](14_powershell_cli_tooling.md)
