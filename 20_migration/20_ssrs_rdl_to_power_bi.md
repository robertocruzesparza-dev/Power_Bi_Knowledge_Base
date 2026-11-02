---
id: 20.ssrs_rdl_to_power_bi
title: Migrating SSRS and RDL reports to Power BI
domain: migration
type: how-to
level: intermediate
tags: [migration, paginated-report, report-server]
summary: Official tools and steps to move SSRS paginated reports (RDL) to Power BI, and to migrate a report server to Power BI Report Server.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1536, S1537, S1538, S1539, S1510, S2721, S2722, S2723]
references: []
related: [20.migration_process, 20.migration_checklist, 13.premium_p_sku_retirement]
---
## Purpose

SQL Server Reporting Services (SSRS) stores reports as Report Definition Language (RDL) files. Each RDL report migrates to a Power BI paginated report.

## Key facts

- Fact: A built-in Publish feature in Power BI Report Server and SQL Server 2022 Reporting Services copies .rdl reports, linked reports and folders to a Power BI workspace [S1536].
- Fact: It also migrates Power BI (.pbix) reports from Power BI Report Server [S1536].
- Fact: Older SSRS versions (2012 to 2019) use the RDL Migration Tool, shipped with Power BI Report Builder and also on GitHub [S1537, S1539].
- Fact: The RDL tool converts shared data sources and shared datasets to embedded ones, checks for unsupported data sources and features, and publishes passing reports. It does not change the source [S1537, S1539].
- Fact: Publishing to My Workspace works with a Free license. Other workspaces need Pro or PPU plus write access [S1536].
- Fact: Migration needs no downtime. You can keep the old server until retirement [S1536].
- Fact: There is no in-place upgrade from SSRS to Power BI Report Server. You migrate [S1538].
- Fact: From SQL Server 2025, on-premises reporting consolidates under Power BI Report Server. No new SSRS versions are planned [S1538].

## Choose a path

| Goal | Path |
|---|---|
| Move RDL to cloud, SSRS 2022 or Report Server | Built-in Publish |
| Move RDL to cloud, SSRS 2012 to 2019 | RDL Migration Tool |
| Stay on-premises | Migrate the report server to Power BI Report Server |

Capacity: paginated reports in the service need a capacity (Fabric F, P, EM or A). Plan capacity before cutover [S1539].

## Steps: publish RDL to the service

1. In the web portal choose Publish. Pick Publish all reports or Select reports to publish.
2. Select the target workspace.
3. Review the summary of successes and failures.
4. Fix unsupported items, then rerun.
5. Test data sources, parameters, subscriptions and exports [S1536].

Command line for older servers: `RdlMigration <endpoint> <folder path> <workspace name>`, which writes ConversionLog.txt [S1537].

## Steps: move to Power BI Report Server

1. Back up the encryption key in Report Server Configuration Manager.
2. Back up ReportServer and ReportServerTempDB.
3. Restore the databases under the same names on the target SQL Server.
4. Install Power BI Report Server (instance name PBIRS).
5. Connect it to the restored database in Configuration Manager.
6. Clean up the old instance [S1538].

SharePoint-integrated mode needs scripted copy (for example rs.exe). Migrating from SQL Server 2022 Reporting Services or later needs Power BI Report Server May 2025 or later [S1538].

## Common mistakes

- Expecting every SSRS feature to exist in the service. The tool flags unsupported items [S1539].
- Skipping the encryption key backup, losing stored credentials [S1538].
- Cancelling a Premium subscription before checking Report Server rights. See [P SKU retirement](../13_licensing_pricing/13_premium_p_sku_retirement.md).

## Limits and version notes

Unsupported in Power BI paginated reports (FAQ, checked 2026-10-08) [S2721]:

- SSRS-style shared data sources (.rds) and shared datasets (.rsd). Use embedded sources, named connections or semantic models.
- Linked reports, custom fonts and custom assemblies (use embedded code instead).
- Document maps in the service (they render on export), pinning pages to dashboards, and SSRS data-driven subscriptions (use dynamic per-recipient subscriptions).
- Item types that cannot migrate: resources such as images, KPIs, mobile reports, report models and report parts [S2722].

Version scope differs between Microsoft pages (Inference: the pages were written at different times). The planning article lists SSRS 2012 to 2022 as migratable and says the built-in tool covers Power BI Report Server and SSRS after 2016. The publish article and FAQ describe SSRS 2022 [S2722]. Test the Publish button on your version first. Migration to Power BI Report Server supports SSRS 2008 and later [S2723].

## See also

- [Migration process](20_migration_process.md)
- [Migration checklist](20_migration_checklist.md)
