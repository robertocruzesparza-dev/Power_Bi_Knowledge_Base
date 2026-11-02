---
id: 11.onelake
title: OneLake concepts
domain: fabric_onelake
type: concept
level: beginner
tags: [onelake, fabric, security, governance]
summary: OneLake is the single tenant-wide data lake in Fabric. Learn its hierarchy, open formats, access paths, security, and protection.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1243, S1244, S1240]
references: []
related: [11.shortcuts, 11.mirroring, 11.direct_lake]
---
## Purpose

OneLake is the built-in data lake for Fabric. Think of it as OneDrive for analytics data. Every engine reads the same files, so you keep one copy.

## Key facts

- Fact: One OneLake per tenant. You cannot delete it or create a second one. [S1243]
- Fact: It is built on Azure Data Lake Storage and stores tables as Delta Parquet or Iceberg, both open formats. [S1243]
- Fact: Hierarchy is tenant, then workspace, then data item (lakehouse, warehouse, eventhouse, and so on). [S1243]
- Fact: Each workspace belongs to a capacity tied to one region and billed separately. [S1243]
- Fact: Engines such as T-SQL, Apache Spark, and Analysis Services (Direct Lake) all read the same Delta files. [S1243]

## How it works

Access paths: [S1243]

1. Fabric portal and the OneLake catalog.
2. OneLake file explorer for Windows.
3. ADLS Gen2 APIs and SDKs. A workspace looks like a container and items look like folders.
4. Azure services such as Synapse, Storage Explorer, and Databricks.

Example path pattern (from Learn): `https://onelake.dfs.fabric.microsoft.com/<Workspace>/<Item>/Tables/<Table>`.

Iceberg: OneLake uses metadata virtualization, so Iceberg tables read as Delta in Fabric, and Delta tables read as Iceberg for outside tools such as Snowflake. [S1243]

## Security and protection

- OneLake security roles set permissions down to folders, tables, rows, and columns. Roles apply across SQL, Spark, and Power BI. [S1243]
- Sensitivity labels and data loss prevention policies apply to OneLake items. [S1243]
- Redundancy: zone-redundant storage where availability zones exist, otherwise locally redundant. Optional business continuity and disaster recovery (BCDR) geo-replicates data to a paired region. [S1243]
- Soft delete keeps deleted files for 7 days. [S1243]
- OneLake diagnostics streams access logs to a lakehouse when enabled at workspace level. [S1243]

## OneLake catalog

The catalog lets users find items by domain, workspace, type, or endorsement. It shows owners, schema, lineage, and usage, plus governance tips. [S1243]

## Cross-tenant sharing

External data sharing creates a read-only shortcut in the consumer tenant. No copy is made. [S1243, S1240]

## Common mistakes

- Copying data between lakehouses when a [shortcut](11_shortcuts.md) would do.
- Forgetting that capacity region fixes where data sits.
- Assuming SQL permissions cover Spark. Use OneLake security for cross-engine rules.

## See also

- [Shortcuts](11_shortcuts.md)
- [Mirroring](11_mirroring.md)
- [Direct Lake](11_direct_lake.md)
