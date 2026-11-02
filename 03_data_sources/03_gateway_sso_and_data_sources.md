---
id: 03.gateway_sso_and_data_sources
title: Gateway data sources and single sign-on
domain: data_sources
type: how-to
level: intermediate
tags: [gateway, data-source, security, refresh]
summary: How to add a gateway data source for refresh or DirectQuery, name-matching rules, and which sources support single sign-on and how.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S311, S312, S319, S2554, S2555]
references: []
related: [03.gateway_types_compared, 03.authentication_and_credentials, 03.privacy_levels]
---

# Gateway data sources and single sign-on

Purpose: connect a published semantic model to an on-premises source through a gateway, with the right identity.

## Steps: add a data source (Fact, S312)

1. In the Power BI service header, open Settings > Manage connections and gateways.
2. Select New, choose On-premises, then name the gateway cluster and connection.
3. Pick the data source type, for example SQL Server, and enter server and database.
4. Choose an authentication method: Basic, Windows or OAuth2, and enter credentials.
5. Optionally set single sign-on (SSO) and a privacy level, then select Create.
6. Open the semantic model settings, find Gateway connections, and map the model to the gateway.

## Rules that cause most failures

- Server and database names must match exactly between Desktop and the gateway source. If Desktop used an IP address, use the same IP address (Fact, S312, S319).
- Your account must be listed on the data source's Users tab (Fact, S319).
- If a model has several sources, add each one to the gateway, or the gateway is not offered for scheduled refresh (Fact, S312).
- After republishing, the model owner must associate the model with the gateway data source again (Fact, S319).
- The privacy level on the gateway does not apply to DirectQuery (Fact, S312).
- Analysis Services, SQL Server and SAP HANA can be used for refresh, DirectQuery or live connection (Fact, S319).
- Do most data source management through the REST APIs for gateways (Fact, S312).

## Single sign-on (Fact, S311)

Options: Active Directory SSO (Kerberos constrained delegation, or Security Assertion Markup Language for SAP HANA) and Microsoft Entra SSO. SSO applies to semantic models, not dataflows. Microsoft Entra SSO works for DirectQuery only. Kerberos SSO can serve DirectQuery or refresh. Power BI does not support SSO for M extensions.

| Method | Sources listed |
|---|---|
| Microsoft Entra ID | Amazon Redshift, Azure Databricks, Azure Data Explorer, Azure SQL, Azure Synapse, Denodo, Dremio Cloud, Snowflake |
| Kerberos | Denodo, Hive LLAP, Impala, Oracle, SAP BW (application and message server), SAP HANA, Spark, SQL Server, Teradata, TIBCO Data Virtualization |
| SAML | SAP HANA |

In the data source dialog, choose "Use SSO via Kerberos for DirectQuery queries", "Use SSO via Kerberos for DirectQuery and Import queries", or "Use SSO via Microsoft Entra ID for DirectQuery queries". With the first option, DirectQuery runs as the signed-in user while refresh uses the stored credentials. SSO for Import queries needs Kerberos constrained delegation (Fact, S312).

SQL Server Analysis Services supports SSO through live connections instead (Fact, S311).

Re-verified 2026-10-08 (S2554, S2555): the source list above matches the SSO overview. Two nuances. First, the Entra SSO tenant setting for the gateway is off by default and a Fabric admin must enable it. Second, the data source dialog page names only SQL Server, Azure Data Explorer, Snowflake and Denodo for the Entra option, so the dialog may offer fewer sources than the overview lists (conflict, unresolved). SAML allows one data source per gateway.

## Refresh limits (Fact, S318)

Shared capacity: up to 8 scheduled refresh slots a day. Premium, PPU and Fabric: up to 48. Power BI pauses scheduled refresh after two months with no visits to any report or dashboard built on the model.

## See also

- [Authentication and credentials](03_authentication_and_credentials.md)
- [Gateway install, network and high availability](03_gateway_install_network_ha.md)
