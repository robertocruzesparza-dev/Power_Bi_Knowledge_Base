---
id: 03.authentication_and_credentials
title: Authentication types and credentials
domain: data_sources
type: concept
level: intermediate
tags: [data-source, connector, gateway, security, refresh]
summary: The authentication types connectors offer, where credentials are stored and set, and known caching and token limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S304, S305, S307, S312, S319, S334, S2810, S2814, S2815]
references: [../references/data_sources/03_connector_capability_details.md]
related: [03.gateway_sso_and_data_sources, 03.privacy_levels, 03.import_directquery_support]
---

# Authentication types and credentials

Purpose: explain which sign-in methods connectors accept and where credentials live, so refresh and DirectQuery keep working.

## Key facts

- Each connector page lists its authentication types. Common ones: Anonymous, Basic or Database (username and password), Windows, Organizational account (Microsoft Entra ID), OAuth, API key, Web API, Service principal and Workspace identity (Fact, S304).
- SQL Server supports Database, Windows, Organizational account (if the server supports it) and Service principal (Fact, S304).
- Snowflake lists user and password, Microsoft Entra ID, key pair (ADBC) and service principal authentication (Fact, S2810). The page says username and password sign-in will be deprecated, with no date given, and recommends Microsoft Entra ID (Fact, S2810).
- PostgreSQL added Microsoft Entra ID for Flexible Server connections in the August 2025 update (Fact, S336).
- Gateway data sources offer Basic, Windows or OAuth2 as the authentication method (Fact, S312).

## Where credentials are set

| Place | Used for |
|---|---|
| Desktop sign-in dialog | Authoring and local refresh; also sets the privacy level |
| Semantic model settings, Data source credentials | Cloud sources, refresh and DirectQuery in the service |
| Manage connections and gateways | Gateway data sources shared by many models |

## Steps: provide credentials for a published DirectQuery or Import model

1. In the workspace, open the semantic model's More options menu and choose Settings.
2. Under Data source credentials, edit the source and sign in.
3. For gateway sources, select the gateway connection instead and confirm server and database names match the report (Fact, S303, S312).

## Limits and gotchas

- The gateway caches credentials. After you change credentials, the new ones may not apply for about five hours, and a DirectQuery report can fail meanwhile (Fact, S305).
- With OAuth2 gateway sources, queries that run longer than the token lifetime can fail, and cross-tenant Microsoft Entra accounts are not supported (Fact, S312).
- On a VNet data gateway, Dataflow Gen1 cannot refresh OAuth2 tokens mid-stream, so errors such as InvalidConnectionCredentials can appear about an hour after refresh starts. Dataflow Gen2, semantic models and data pipelines refresh tokens mid-stream and are not affected (Fact, S307, S2815).
- Windows authentication on a gateway needs the account to have access on the gateway machine; Microsoft suggests adding NT-AUTHORITY\Authenticated Users to the local Users group if unsure (Fact, S312).
- Some encrypted-column cases return errors on import, for example two or more encrypted Azure SQL Database columns (Fact, S317).
- Currently you cannot connect to custom data sources secured through Microsoft Entra ID (Fact, S317).

## Security practice

Enable encrypted connections where offered, keep certificate revocation checks on, and do not build queries by string concatenation with untrusted parameter values (Fact, S334).

## See also

- [Gateway SSO and data sources](03_gateway_sso_and_data_sources.md)
- [Privacy levels](03_privacy_levels.md)
