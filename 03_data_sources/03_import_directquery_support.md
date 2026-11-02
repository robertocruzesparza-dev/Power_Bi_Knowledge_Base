---
id: 03.import_directquery_support
title: Import versus DirectQuery support by connector
domain: data_sources
type: comparison
level: intermediate
tags: [storage-mode, connector, data-source, comparison]
summary: Which common connectors list DirectQuery, how to check for any connector, and when DirectQuery needs a gateway or stored credentials.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S303, S304, S320, S321, S2507, S2508]
references: [../references/data_sources/03_connector_capability_details.md]
related: [03.data_sources_overview, 03.gateway_types_compared, 03.gateway_sso_and_data_sources]
---

# Import versus DirectQuery support by connector

Purpose: tell you quickly whether a connector can run in DirectQuery, and what that implies for refresh and gateways.

## Key facts

- Microsoft advises Import by default. It uses the in-memory engine and has the richest feature set. Move to DirectQuery only for latency, size, governance or architecture reasons (Fact, S321).
- The authoritative check is the "Supported capabilities" section of the connector page. A missing DirectQuery entry means unsupported (Fact, S303).
- Import models on shared capacity schedule up to 8 refreshes a day. Premium, Premium Per User (PPU) and Fabric capacities allow up to 48 (Fact, S318, S321).
- DirectQuery tiles on dashboards can refresh as often as every 15 minutes (Fact, S321).

## Connectors that list DirectQuery (read 2026-10-07)

Listed with Import plus DirectQuery on their pages: SQL Server, Azure SQL Database, Azure Synapse Analytics (SQL), Oracle, PostgreSQL, Teradata, Amazon Redshift, Amazon Athena, Snowflake, Google BigQuery, Databricks and Azure Databricks, Azure Data Explorer, KQL Database, Azure Cosmos DB v2, IBM Db2, Impala, ClickHouse, SingleStore, MongoDB Atlas SQL interface, Palantir Foundry datasets, Denodo, TIBCO Data Virtualization, Dataflows, Dataverse, CData Connect Cloud and OpenSearch connectors (Fact, S304).

Listed as Import only on their pages: Excel, Text/CSV, JSON, XML, PDF, Parquet, SharePoint list and folder, Azure Blob Storage, Azure Data Lake Storage Gen1, Hive LLAP, Azure Table Storage, Azure Cost Management and MySQL (Fact, S304). Analysis Services connectors use live connection, which this table does not cover.

Conflict to note: a Microsoft DirectQuery article discusses MySQL and PostgreSQL tuning, but the MySQL connector page lists only Import in its capabilities. Treat the connector page as the official capability statement and verify in your Desktop build (Unknown on current behavior, S304, S321).

## DirectQuery needs

- Cloud sources named above need no gateway, but you must set credentials on the semantic model in the service, or the report fails to open (Fact, S303).
- Other DirectQuery sources need an on-premises gateway with the source registered (Fact, S303).
- An Azure SQL Database with a private IP address needs a gateway (Fact, S303).
- Personal-mode gateways do not support DirectQuery (Fact, S306).

## Report Server note

Report Server lists live or DirectQuery support only for SQL Server, Analysis Services, Azure SQL Database, Azure Analysis Services and Azure Synapse (Fact, S320).

## Common mistakes

- Choosing DirectQuery because the data is large, without checking source speed. Visual latency depends on the source (Fact, S321).
- Expecting DirectQuery to bypass the 16 MB uncompressed response limit of the gateway (Fact, S305).

## See also

- [Gateway types compared](03_gateway_types_compared.md)
- [Gateway SSO and data sources](03_gateway_sso_and_data_sources.md)
- [Capability details](../references/data_sources/03_connector_capability_details.md)
