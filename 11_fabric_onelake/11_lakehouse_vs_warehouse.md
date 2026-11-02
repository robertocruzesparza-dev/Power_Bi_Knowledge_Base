---
id: 11.lakehouse_vs_warehouse
title: Lakehouse versus warehouse in Fabric
domain: fabric_onelake
type: comparison
level: intermediate
tags: [lakehouse, warehouse, comparison, decision-guide]
summary: Compare the Fabric lakehouse and warehouse by language, transactions, data types, and SQL capability, with a choice guide.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1245, S1246]
references: []
related: [11.onelake, 11.direct_lake, 09.datamarts_status]
---
## Purpose

Both items store Delta tables in OneLake and share one SQL engine. They differ in how you build and load them.

## Key facts

- Fact: A lakehouse stores structured and unstructured data. You work in Apache Spark (Python, Scala, Spark SQL, R). It gets a read-only SQL analytics endpoint. [S1245]
- Fact: A warehouse is a relational store built mainly with T-SQL. It has multi-table ACID transactions, views, functions, and stored procedures. [S1245, S1246]
- Fact: Warehouse compute and storage scale separately. [S1246]
- Fact: Warehouse data is replicated to OneLake Files for external access. [S1246]

## Choose quickly

| Question | Lakehouse | Warehouse |
|---|---|---|
| Main language | Spark | T-SQL |
| Multi-table transactions | No | Yes |
| Data shape | Unstructured plus structured | Structured only |
| Typical user | Data engineer, data scientist | SQL developer, citizen developer |

Source: S1245.

## Compare capabilities

| Capability | Warehouse | Lakehouse SQL endpoint |
|---|---|---|
| Write with T-SQL (INSERT, CTAS, COPY INTO) | Yes | No (read-only) |
| T-SQL DDL | Full | Limited: views and table-valued functions |
| Load by | T-SQL, pipelines, dataflows | Spark, pipelines, dataflows, shortcuts |
| Delta | Reads and writes | Reads |
| Tool support (first and third party) | Read/write | Limited |

Source: S1245.

## Pairing pattern

Use a lakehouse for bronze and silver zones in a medallion design. Use a warehouse for curated gold tables when teams want T-SQL. Cross-database queries join both with zero copies. [S1245, S1246]

## Power BI angle

Both support Direct Lake semantic models. A lakehouse endpoint adds SQL-level security, which can force fallback in Direct Lake on SQL. See [Direct Lake fallback](11_direct_lake_fallback.md). Semantic models are not created automatically for new items anymore. See [Semantic model basics](../09_semantic_models_dataflows/09_semantic_model_basics.md).

## Common mistakes

- Trying to INSERT through a lakehouse SQL endpoint.
- Choosing a warehouse for raw files.
- Running Spark writes into warehouse tables. Use T-SQL or load pipelines.

## See also

- [Direct Lake](11_direct_lake.md)
- [Datamarts status](../09_semantic_models_dataflows/09_datamarts_status.md)
