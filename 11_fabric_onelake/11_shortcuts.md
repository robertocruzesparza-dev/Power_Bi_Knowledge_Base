---
id: 11.shortcuts
title: OneLake shortcuts
domain: fabric_onelake
type: reference
level: intermediate
tags: [onelake, fabric, lakehouse, limits, security]
summary: Shortcut types, where they can live, identity behavior, caching, deletion rules, and numeric limits.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1239, S1203, S2916]
references: []
related: [11.onelake, 11.mirroring, 11.direct_lake]
---
## Purpose

A shortcut is a pointer in OneLake to data stored elsewhere. It works like a symbolic link. Data stays in the source, and Fabric engines read it as if local.

## Key facts

- Fact: You can create shortcuts in lakehouses and KQL databases. [S1239]
- Fact: Deleting a shortcut does not touch the target. Deleting a file inside a shortcut path deletes it in the target if you have write rights there. [S1239]
- Fact: Moving, renaming, or deleting a target can break the shortcut. [S1239]
- Fact: Schema changes in the source sync to shortcut tables automatically. [S1239]
- Fact: Direct Lake semantic models can read shortcut tables. [S1239, S1203]

## Where shortcuts live

In a lakehouse there are two top folders. In Tables, shortcuts go only at the top level, not in subfolders. If the target is Delta, the folder is recognized as a table. In Files, shortcuts can be at any depth and hold any format. [S1239]

Table names with spaces are not recognized as Delta tables. [S1239]

Schema shortcuts (a parent folder of many tables) need a schema-enabled lakehouse. [S1239]

## Types

| Class | Targets |
|---|---|
| Internal | Lakehouses, warehouses, KQL databases, SQL databases, mirrored databases, mirrored Azure Databricks catalogs, semantic models |
| External | Amazon S3, S3-compatible, ADLS Gen2, Azure Blob, Dataverse, Google Cloud Storage, Iceberg, OneDrive and SharePoint |
| Network-restricted | On-premises or private locations through an on-premises data gateway |

Source: S1239. Item types need not match; a lakehouse shortcut can point to a warehouse.

## Identity and security

- Internal shortcut: OneLake checks the calling user's identity against the target. [S1239]
- Exception: through Direct Lake over SQL, or T-SQL in delegated identity mode, the item owner's identity is passed, not the caller's. Use Direct Lake over OneLake or T-SQL user identity mode to fix this. [S1239]
- External ADLS and S3 shortcuts use a cloud connection. Only users with rights on the connection can bind it. [S1239]

## Caching and deletion

Caching cuts egress cost for cross-cloud reads. It supports GCS, S3, S3-compatible, and gateway shortcuts. Retention is 1 to 28 days, reset on each access. Files over 1 GB are not cached. Set it in Workspace settings, OneLake tab. [S1239]

## Limits

| Limit | Value |
|---|---|
| Shortcuts per Fabric item | 100,000 |
| Unique data source connections per item | 100 |
| Shortcuts on one OneLake path | 10 |
| Shortcut-to-shortcut chain depth | 5 |
| Forbidden characters in names and paths | `%` and `+`; non-Latin characters unsupported |

Source: S1239. Lineage for shortcuts to warehouses and semantic models is not available. The Table API can take about a minute to see a new shortcut. [S1239]

## Common mistakes

- Making a shortcut in a Tables subfolder.
- Expecting delete of the shortcut to delete data.
- Forgetting the caller needs rights on the target.

## See also

- [OneLake](11_onelake.md)
- [Mirroring](11_mirroring.md)
