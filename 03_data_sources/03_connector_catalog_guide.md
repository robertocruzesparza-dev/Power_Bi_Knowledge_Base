---
id: 03.connector_catalog_guide
title: Connector categories and how to use the catalog
domain: data_sources
type: reference
level: beginner
tags: [connector, data-source, catalog, reference]
summary: Connector categories in Get data, how to read the official index, and pointers to the full alphabetical catalog in the references folder.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S301, S304, S317, S320, S2809]
references: [../references/data_sources/03_connector_catalog_part1.md, ../references/data_sources/03_connector_catalog_part2.md, ../references/data_sources/03_connector_catalog_part3.md, ../references/data_sources/03_connector_capability_details.md]
related: [03.data_sources_overview, 03.import_directquery_support, 03.connector_lifecycle_changes]
---

# Connector categories and how to use the catalog

Purpose: help you find a connector, read its support flags, and know which parts of this KB hold the full lists.

## Key facts

- The legacy Get Data dialog groups connectors into All, File, Database, Microsoft Fabric, Power Platform, Azure, Online Services and Other (Fact, S317).
- The official index lists 194 connector rows in alphabetical tables (counted 2026-10-09, S2809). Columns show support in Excel, Power BI semantic models, Power BI dataflows, Fabric Dataflow Gen2, Power Apps dataflows, Customer Insights dataflows and Analysis Services (Fact, S301).
- About 170 of the 194 rows link to a reference page, on Microsoft Learn or a partner site. The other rows carry no link (Fact, counted from S2809 on 2026-10-09).
- Publishers include Microsoft and many partners such as Databricks, Autodesk, Planview, Celonis and Supermetrics (Fact, S301).
- A note in the index says government cloud sources with an organizational account stopped working from non-government Power BI environments after March 31, 2024 (Fact, S301).

## Categories by example

| Category | Typical connectors |
|---|---|
| File | Excel, Text/CSV, JSON, XML, PDF, Parquet, Folder, SharePoint folder |
| Database | SQL Server, Oracle, PostgreSQL, MySQL, Teradata, IBM Db2, SAP HANA |
| Microsoft Fabric | Lakehouse, Warehouse, KQL Database, Dataflows |
| Azure | Azure SQL Database, Synapse, Data Lake Storage Gen2, Blob Storage, Cosmos DB, Databricks |
| Online services | Salesforce, Google Analytics, Dynamics 365, SharePoint Online list, Smartsheet |
| Other | Web, OData, ODBC, Python and R scripts, Blank query |

## How to use the catalog

1. Open the alphabetical catalog parts: [part 1](../references/data_sources/03_connector_catalog_part1.md), [part 2](../references/data_sources/03_connector_catalog_part2.md), [part 3](../references/data_sources/03_connector_catalog_part3.md).
2. Check the SM flag for semantic models and DF2 for Dataflow Gen2.
3. For authentication and Import or DirectQuery support, open the [capability details](../references/data_sources/03_connector_capability_details.md).
4. For anything not covered, read the connector page on Microsoft Learn before building on it.

## Power BI Report Server

Report Server supports a shorter list. For DirectQuery or live connection it lists SQL Server, Analysis Services, Azure SQL Database, Azure Analysis Services and Azure Synapse. Many others are cached-data only (Fact, S320). Report Server does not support OAuth-based authentication for DirectQuery (Fact, S320).

## Common mistakes

- Treating the count of connectors as fixed. The list grows monthly; some entries retire (see [connector lifecycle changes](03_connector_lifecycle_changes.md)).
- Assuming a custom connector works in the service without a gateway or a supported host.

## Limits and version notes

- Excel column support differs by Excel version (Fact, S301).
- The index states a known issue where gateway-based connectors in dataflows on Premium workspaces can raise "matches no exports"; a fix was pending when read (Fact, S301).

## See also

- [Data sources overview](03_data_sources_overview.md)
- [Import versus DirectQuery support](03_import_directquery_support.md)
