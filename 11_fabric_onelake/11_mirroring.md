---
id: 11.mirroring
title: Mirroring in Fabric
domain: fabric_onelake
type: concept
level: intermediate
tags: [fabric, onelake, warehouse, pricing]
summary: Database, metadata, and open mirroring: supported sources, how replication works, storage cost rules, and retention.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1240, S1203, S2619]
references: []
related: [11.shortcuts, 11.onelake, 11.direct_lake]
---
## Purpose

Mirroring brings an outside database or catalog into OneLake with no pipeline to build. Operational data becomes Delta tables that every Fabric engine can read.

## Key facts

- Fact: Mirroring creates a replication process plus a SQL analytics endpoint in your workspace. [S1240]
- Fact: Changes can be published as often as every 15 seconds. Real latency depends on region, change volume, and bandwidth. [S1240]
- Fact: A running Fabric capacity is required. Paused or deleted capacity stops replication. [S1240]
- Fact: Direct Lake works over mirrored data. [S1240, S1203]

## Three kinds

| Kind | What moves | Example |
|---|---|---|
| Database mirroring | Data and metadata are replicated as Delta | Azure SQL Database |
| Metadata mirroring | Only catalog metadata; data read in place through shortcuts | Azure Databricks Unity Catalog |
| Open mirroring | Your app writes change data to a landing zone URL; Fabric merges it | Custom or partner apps |

Source: S1240. Metadata mirroring also supports cross-tenant sharing, since it uses shortcuts.

## Sources

Listed by Learn on retrieval date: Azure Cosmos DB, Azure Databricks (metadata), Azure Database for PostgreSQL, Azure Database for MySQL (preview), Azure SQL Database, Azure SQL Managed Instance, Dremio catalog (preview), Google BigQuery (generally available), Oracle, SAP, SharePoint List (preview), Snowflake, SQL Server, open mirroring, and Fabric SQL database (automatic). [S1240]

Status changes often. Check the live page before committing.

## Cost

Fact: [S1240]

- Mirroring storage is free up to 1 TB per capacity unit purchased. An F64 gives 64 TB.
- Over the limit, or while capacity is paused, you pay normal OneLake storage rates.
- Background replication compute is free and uses no capacity units.
- Queries by SQL, Power BI, or Spark, and direct OneLake requests, use capacity as normal.

See Fabric pricing for rates. Unverified: current per-TB price.

## Retention and use

Mirroring runs vacuum automatically. For mirrored databases created after mid-June 2025 the default retention is 1 day; older ones default to 7 days. Change it in Settings, Delta table management, or with `retentionInDays` in the API. [S1240] The REST API page still says the default is 7 days, with allowed values 1 to 30. The overview page is newer on portal-created databases. [S2619]

You can share a mirrored database without workspace access. This also shares its SQL analytics endpoint. Cross-database T-SQL queries can join mirrored data, warehouses, and lakehouse endpoints with three-part names. [S1240]

## Common mistakes

- Expecting mirrored data to be free after pausing capacity.
- Using mirroring where a one-off copy or a [shortcut](11_shortcuts.md) is enough.
- Assuming all sources are generally available. Some are preview.

## See also

- [Shortcuts](11_shortcuts.md)
- [OneLake](11_onelake.md)
