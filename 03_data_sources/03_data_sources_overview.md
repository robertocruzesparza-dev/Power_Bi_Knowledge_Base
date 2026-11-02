---
id: 03.data_sources_overview
title: Data sources in Power BI: overview
domain: data_sources
type: concept
level: beginner
tags: [data-source, connector, power-query, storage-mode, gateway]
summary: How Power BI reaches data through Power Query connectors, what connectivity modes exist, and where gateways, credentials and privacy levels fit.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S301, S302, S303, S317, S321, S2809, S2844]
references: [../references/data_sources/03_connector_capability_details.md]
related: [03.connector_catalog_guide, 03.import_directquery_support, 03.gateway_types_compared, 03.authentication_and_credentials]
---

# Data sources in Power BI: overview

Purpose: explain the path from a source system to a Power BI report, so you know which later topic answers your question.

## Key facts

- Power BI connects to data through Power Query connectors. The connector list is documented once, in the Power Query connector reference, and applies to Power BI too (Fact, S302).
- Each connector page has a "Supported capabilities" section. If DirectQuery is not listed there, the connector does not support it (Fact, S302, S303).
- Connection modes: Import copies data into the model; DirectQuery sends a query to the source for each visual; Live connection attaches to an existing Analysis Services or Power BI semantic model (Fact, S321).
- Connectors marked Beta or Preview have limited support and Microsoft says not to use them in production (Fact, S317).
- Cloud sources such as Azure SQL Database, Azure Synapse, Amazon Redshift and Snowflake need no gateway for DirectQuery, but the service still needs credentials. Other DirectQuery sources need a gateway (Fact, S303).

## How it works

1. In Power BI Desktop, you pick a connector in Get data, enter connection details, and choose Import or DirectQuery where offered.
2. You sign in with an authentication type the connector supports (see [authentication and credentials](03_authentication_and_credentials.md)).
3. Power Query shapes the data. When you combine sources, privacy levels decide what may pass between them (see [privacy levels](03_privacy_levels.md)).
4. After you publish, the service refreshes Import models or queries DirectQuery sources. On-premises or network-secured sources go through a gateway (see [gateway types](03_gateway_types_compared.md)).

## Example

An analyst imports a SQL Server table and an Excel file. Desktop reaches both directly. After publishing, scheduled refresh can reach the on-premises SQL Server only through a gateway. The gateway data source must use the same server and database names as the report (Fact, S312).

## Common mistakes

- Assuming a connector in the Get data window works in every product. The index shows separate support flags for semantic models, dataflows and Dataflow Gen2 (Fact, S301).
- Using a Beta connector in production.
- Forgetting to add every data source of a multi-source model to the gateway; the gateway then does not appear for scheduled refresh (Fact, S312).

## Limits and version notes

- Desktop offers a legacy Get Data dialog (categories: All, File, Database, Microsoft Fabric, Power Platform, Azure, Online Services, Other) and a new Power Query Get Data experience in preview. Enable the preview under File > Options and settings > Options > Preview features (Fact, S317).
- Power BI Report Server supports only a subset of sources; see [connector catalog guide](03_connector_catalog_guide.md).

## See also

- [Connector catalog guide](03_connector_catalog_guide.md)
- [Import versus DirectQuery support](03_import_directquery_support.md)
- [Gateway types compared](03_gateway_types_compared.md)
- [Capability details by connector](../references/data_sources/03_connector_capability_details.md)
