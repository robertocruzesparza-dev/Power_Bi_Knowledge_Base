---
id: ref.connector_capability_details
title: Connector capability details (verified subset)
domain: data_sources
type: reference
level: intermediate
tags: [connector, data-source, reference, catalog]
summary: Release state, authentication types and Import or DirectQuery support for the connectors that have their own Microsoft Learn reference page.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S301, S304, S2810, S2811, S2812, S2813]
references: []
related: [03.connector_catalog_guide, 03.connector_lifecycle_changes]
---

## Table of Contents

- [See also](#see-also)

# Connector capability details (verified subset)

Purpose: show, for connectors with a Learn reference page, the release state, the authentication types and whether DirectQuery is listed. Each line reads: connector page name; release state; authentication; modes. Data was read from each page on 2026-10-07 by script, so cut-off text is marked as not extracted. A mode that the page does not list is not supported in that connector. Partner connectors without a Learn page are not covered here. Read the page itself before relying on a line.

- Access Database; GA; Anonymous; Windows; Basic; Organizational Account; Import
- Active Directory; GA; Windows; Import
- Adobe Analytics; GA; Organizational account; Import
- Adp Analytics; GA; Organizational account; Import
- Amazon Athena; GA; Microsoft Entra ID; Import + DirectQuery
- Amazon Opensearch Service; Preview; NONE; BASIC; AWS_SIGV4; Import + DirectQuery
- Amazon Redshift; GA; Amazon Redshift; Microsoft Entra ID; Import + DirectQuery
- Anaplan; GA; OAuth; UsernamePassword; not stated
- Assemble Views; GA; OAuth; Import
- Autodesk Construction Cloud; GA; OAuth; Import
- Automy Data Analytics; GA; Key; Import
- Azure Analysis Services; GA; Organizational account (OAuth 2.0); Import
- Azure Blob Storage; GA; Anonymous; Account key; Organizational account; Shared access signature (SAS); Service pri; Import
- Azure Cosmos DB For Mongodb Vcore; not stated; not extracted; Import+DQ
- Azure Cosmos DB V2; GA; Key; Microsoft Entra ID; Import + DirectQuery
- Azure Cost Management; GA; Microsoft Entra ID; Import
- Azure Data Explorer; Preview; Microsoft Entra ID; Import + DirectQuery
- Azure Data Lake Storage Gen1; GA; Microsoft Entra ID; Import
- Azure Device Registry; Preview; Microsoft Entra ID; Import
- Azure HDInsight; GA; Anonymous; Account Key; Import
- Azure Resource Graph; GA; Microsoft Entra ID; Import
- Azure SQL Data Warehouse; GA; Database (Power BI Desktop, Excel); Microsoft Account (all); Basic (online service); Servi; Import + DirectQuery
- Azure SQL Database; not stated; not extracted; Import + DirectQuery
- Azure Table Storage; GA; Account Key; Import
- Bitsight Security Ratings; GA; API Authentication; Import
- Bloomberg Data And Analytics; GA; Bloomberg Account; Import
- Bqecore; GA; CORE Login; Import
- Buildingconnected; Preview; OAuth; Import
- Cdata Connect Cloud; GA; CData Connect account; Import + DirectQuery
- Celonis Ems; GA; API key; Import
- Clickhouse; GA; UsernamePassword; Import + DirectQuery
- Cloudbluepsa; Preview; Key; Import
- Data Lake Storage; GA; Organizational Account; Account Key; Shared Access Signature (SAS) Key; Service principal; Import
- Databricks; GA; OAuth (OIDC); Personal Access Token; Databricks Client Credentials; Import + DirectQuery
- Databricks Azure; GA; Microsoft Entra ID; Personal Access Token; Databricks Client Credentials; Service principa; Import + DirectQuery
- Dataflows; GA; not extracted; Import + DirectQuery
- Dataverse; GA; not extracted; Import + DirectQuery
- Delta Sharing; GA; OAuth; Authentication; Import
- Denodo; not stated; not extracted; Import + DirectQuery
- Digital Construction Works Insights; not stated; not extracted; Import
- Dremio Cloud; not stated; Microsoft Entra ID (SSO via gateway); DirectQuery listed
- Dremio Software; not stated; not extracted; Import+DQ
- Dynamics 365 Online; GA; Anonymous; Windows; Basic; Web API; Organizational account; Import
- Dynatrace Grail Dql; GA; OAuth; Import
- Eduframe; Preview; Eduframe Login; Access Token; Import
- Equis; GA; API Token; Basic; Microsoft Entra ID; Import
- Essbase; GA; Basic (Username/Password); Import
- Exact Online Premium; GA; OAuth; Import
- Excel; GA; Anonymous (online); Basic (online); Organizational account (online); Import
- Factset; not stated; not extracted; Import
- Funnel; GA; Funnel Sign in; Import
- Google Analytics; GA; Google Account; Import
- Google Bigquery; GA; Organizational account; Service account; Import + DirectQuery
- Google Bigquery Aad; GA; Organizational account; Import + DirectQuery
- Google Sheets; GA; Google Account; Import
- Hadoop File System; GA; Anonymous; Windows; Microsoft account; Import
- Hive Llap; GA; Basic (Username/Password); Windows; Import
- Ibm DB2 Database; GA; Basic; Database; Windows; Import + DirectQuery
- Ibm Netezza Database; Deprecating Simba driver, IBM driver preview/GA; Database; Import+DQ
- Impala Database; GA; Anonymous; Database; Windows; Import + DirectQuery
- Intersystems Healthinsight; GA; not extracted; Import + DirectQuery
- Inwink; Beta; Organizational account; Import
- Json; GA; Anonymous; Basic (Web only); Organizational Account; Web API (Web only); Windows; Import
- Kql Database; Preview; Microsoft Entra ID; Import+DQ
- Microsoft Exchange; GA; Exchange account; Microsoft account; Import
- Microsoft Exchange Online; GA; Exchange account; Microsoft account; Import
- Microstrategy For Power Bi; GA; Basic; OAuth 2.0; Import
- Mongodb Atlas SQL Interface; GA; Database; X.509; OAuth (OIDC); AWS IAM; Import+DQ
- Mysql Database; not stated; not extracted; Import
- Odbc; GA; Database (Username/Password); Windows; Default or Custom; Import
- Opensearch Project; Beta; Basic; Import + DirectQuery
- Oracle Database; GA; Windows (desktop/online); Database (desktop); Basic (online) ; Microsoft account (desktop); Import + DirectQuery; built-in managed Oracle driver is the default for Import from June 2026, for DirectQuery it is preview, and personal gateways are unsupported with it (S2813)
- Palantir Foundry Datasets; GA; Foundry OAuth; Foundry Token; Foundry Client Credentials; Import + DirectQuery
- Parquet; not stated; not extracted; Import
- Pdf; GA; not extracted; Import
- Planview Okr; Preview; Planview Admin account; Import
- Postgresql; GA; Database (Username/Password); Microsoft account (Microsoft Entra ID); Import + DirectQuery
- Profisee; GA; Organizational account; Import
- Salesforce Objects; GA; Salesforce account; Import (production, custom, custom domains)
- Salesforce Reports; GA; Salesforce account; Import
- Samsara; GA; Web API; Import
- Sharepoint Folder; GA; Anonymous; Microsoft Account; Windows; Organizational; Workspace identity; Import (folder, combine)
- Sharepoint List; GA; Anonymous; Windows; Microsoft Account; Import (site URL)
- Sharepoint Online List; GA; Anonymous; Windows; Microsoft Account; Workspace identity; Import (site URL)
- Singlestore; GA; Basic; Windows; Import+DQ
- Smartsheet; GA; OAuth; Import
- Snowflake; GA; Snowflake user/password (deprecation announced, no date); Microsoft Entra ID; key pair (ADBC); service principal; Import+DQ; implementation 2.0 (ADBC driver) is the default for new connections (S2810)
- SQL Server; GA; Database/Basic; Windows; Organizational account; Service principal; Import+DQ
- SQL Server Analysis Services; GA; Basic; Microsoft account; Organizational; Windows; Import
- Starburst; not stated; Microsoft Entra ID SSO listed; Import+DQ
- Sybase Database; GA; Database; Windows; Import
- Synapse; Beta; Organizational account; Import
- Teradata; GA; Database; Windows; Import + DirectQuery
- Text Csv; not stated; not extracted; Import
- Tibco; GA; Database (Username/Password); Windows Authentication (NTLM/Kerberos); Import + DirectQuery
- Usercube; Beta; Client Credentials; Import
- Vertica Database; Deprecating Simba driver; GA with Vertica ODBC driver; Database; Import+DQ
- Vessel Insight; GA; Organizational account; Import
- Warehouse; Beta; not extracted; Import
- Xml; GA; not extracted; Import
- Zendesk Data; Beta; Zendesk account; Import

## See also

- [Connector catalog guide](../../03_data_sources/03_connector_catalog_guide.md)
- [Import versus DirectQuery by connector](../../03_data_sources/03_import_directquery_support.md)
