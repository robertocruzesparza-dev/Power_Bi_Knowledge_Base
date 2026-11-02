---
id: 12.tenant_settings_catalog
title: Tenant settings catalog by section
domain: admin_governance_security
type: reference
level: advanced
tags: [tenant-setting, catalog, reference]
summary: Catalog of Fabric tenant setting names grouped by admin portal section, from the Microsoft tenant settings index, rechecked 2026-10-09.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1525, S3001, S3000]
references: []
related: [12.tenant_settings]
---
## Scope

This is a name-level catalog, not a description of every effect. Names can change and many are preview. Check the live index. Source: S1525, S3001.

## Microsoft Fabric and workspace

- Users can create Fabric items (also settable per capacity)
- Preview item creation switches: Ontology, Digital Twin Builder, dbt job, Azure Databricks Storage, mirrored catalog, Fabric Apps (plus anonymous data access for Fabric Apps), Event Schema Sets in Real-Time Hub; operations agents observability to Agent 365; Product Feedback
- ML models can serve real-time predictions (preview); Detect anomalies in Real-Time Intelligence (preview)
- All Power BI users can see "Set alert" button
- Help and support: Publish "Get Help" information; outage notifications by email, Teams and in-product; Users can try Microsoft Fabric paid features; Show a custom message before publishing reports
- Domain management: Allow tenant and domain admins to override workspace assignments (preview)
- Workspace: Create workspaces; Use semantic models across workspaces; Block users from reassigning personal workspaces; Define workspace retention period; automatic PBIR conversion (preview); Fabric item recovery (3 to 90 days)

## Information protection and sharing

- Information protection: Allow users to apply sensitivity labels; labels from data sources; downstream labels; workspace admin override; restrict protected-label link sharing; domain default labels (preview); Allow Microsoft Purview to secure AI interactions
- External sharing: External data sharing; Users can accept external data shares; Guest users can access Microsoft Fabric; Users can invite guest users; Guest users can browse and access Fabric content; See guest users in suggested people
- Publish to web; Copy and paste visuals
- Export: to Excel, .csv, PowerPoint or PDF, MHTML, Word, XML, image; Download reports; Analyze in Excel live connection; Print dashboards and reports
- Certification; Endorse master data; email subscriptions (including B2B guests and external users); Featured content
- Allow shareable links to grant access to everyone in your organization; Teams integration (including automatic app install for Teams); Power BI add-in for PowerPoint
- Allow DirectQuery connections to Power BI semantic models; Guest users can work with shared semantic models in their own tenants; Allow specific users to turn on external data sharing

## Discovery, apps and integration

- Discovery: Make promoted content discoverable; Make certified content discoverable; Discover content; Users can find objects in search
- Apps: Create template organizational apps; Push apps to end users; Publish apps to the entire organization
- Integration: XMLA endpoints and Analyze in Excel with on-premises models; Semantic Model Execute Queries REST API; Power BI Model Context Protocol server endpoint (preview); ArcGIS Maps; global search; Azure Maps visual and related data-processing consents (Azure Maps services and Weather Services in their own section); map and filled map visuals; SharePoint and Lists integration
- Single sign-on switches: Dremio, Snowflake, Redshift, Google BigQuery, Denodo, Starburst; Microsoft Entra SSO for data gateway and VNet gateway
- View Power BI files from OneDrive and SharePoint (preview); Enable granular access control for all data connections; Semantic models can export data to OneLake; ADBC connectivity; Allow non-Entra ID auth in Eventstream

## Visuals, usage and developer

- Power BI visuals: Allow visuals created using the Power BI SDK; Add and use certified visuals only; downloads from custom visuals; AppSource custom visuals SSO; browser local storage
- R and Python visuals: Interact with and share R and Python visuals
- Audit and usage: Usage metrics for content creators; Per-user data in usage metrics; user data in Capacity Metrics app; Azure Log Analytics connections; workspace monitoring (preview); Microsoft can store query text for support
- Dashboard: Web content on dashboard tiles
- Developer: Embed content in apps; Service principals can create workspaces, connections and deployment pipelines; Service principals can call Fabric public APIs; Allow service principals to create and use profiles; Block ResourceKey Authentication; Define maximum number of Fabric identities (default 10,000)
- Admin API: Service principals can access read-only admin APIs; admin APIs used for updates; detailed metadata; DAX and mashup expressions
- Gen1 dataflows; template apps (publish, install, install unlisted); Q&A review questions and synonym sharing; Explore (preview); Semantic Model Security: Block republish and disable package refresh; Users can edit semantic models in the Power BI service; Kusto: Real-Time Dashboards with embedded app visuals; Scorecards; Datamarts (preview)

## Networking, encryption and AI

- Advanced networking: Tenant-level Private Link; Block Public Internet Access; workspace-level inbound and outbound rules; workspace IP firewall rules and trusted resource instances
- Encryption: Apply customer-managed keys
- OneLake: external app access; short-lived user-delegated SAS tokens; OneLake File Explorer; end-user identifiers in diagnostic logs
- Git integration: synchronize with Git; export to other geographies; export with sensitivity labels; GitHub sync
- Copilot and Azure OpenAI: use of Copilot; standalone Copilot (preview); processing and storage outside region consents; designated Copilot capacities; approved items only (preview)
- Scale-out queries for large semantic models; Share Fabric data with Microsoft 365 services; Insights notifications (preview)
- Additional workloads: add and remove workloads by workspace or capacity admins (preview); partner workloads; unvalidated workloads
- Azure AI Service: Allow data processing outside geographic region
