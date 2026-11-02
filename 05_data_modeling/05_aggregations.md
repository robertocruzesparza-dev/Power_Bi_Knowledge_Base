---
id: 05.aggregations
title: Aggregations (user-defined and automatic)
domain: data_modeling
type: how-to
level: advanced
tags: [aggregation, storage-mode, composite-model, optimization]
summary: Shows how aggregation tables speed up large DirectQuery models, including relationship and GroupBy styles, validation rules, and automatic aggregations.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S615, S624, S622, S2544]
references: []
related: [05.storage_modes, 05.composite_models, 16.directquery_tuning]
---

# Aggregations (user-defined and automatic)

## Purpose
An aggregation table stores a summarized copy of a big DirectQuery table, usually in Import mode. Queries at a coarse level hit the small cached table; others fall through to the detail table.

## Key facts
- Fact: Users query the detail table; the engine redirects invisibly. Aggregation tables are hidden and read-only users cannot query them (S615).
- Fact: The aggregation table is best built as an Import table. Once set to Import, the mode cannot change again (S615).
- Fact: Open Manage aggregations from the table's context menu in the Data pane (S615).
- Fact: The detail table must be DirectQuery, not Import (S615).

## Two styles
| Style | Fits | GroupBy entries |
|---|---|---|
| Relationship-based | Star or snowflake from a warehouse | Optional (except for DISTINCTCOUNT) |
| GroupBy-based | Denormalized big-data tables with attributes in the fact | Required, else no hit |

Both can combine in one model (S615).

## Steps (relationship-based)
1. Build Sales Agg at a coarser grain (for example customer, date, subcategory) in the source or in Power Query.
2. Relate Sales Agg to the same dimensions as Sales.
3. Set Sales Agg to Import. Accept the offer to set related dimensions to Dual (S615).
4. In Manage aggregations, map each column: Sum, Min, Max, Count, Count table rows, or GroupBy, with detail table and column.
5. Apply all. Test with a visual and check the query path in Performance Analyzer.

Why Dual: regular relationships are needed for hits. Regular means many-side Dual, Import with Import or Dual, or DirectQuery with DirectQuery or Dual, from one source. Cross-source regular only if both are Import. Many-to-many is always limited (S615).

## Which queries hit
- Hit: Sum, Min, Max, Count, COUNTROWS with a Count table rows mapping, and AVERAGE if both Sum and Count are mapped. DISTINCTCOUNT can hit with a GroupBy on that column (S615).
- Hit: Time intelligence functions such as DATESYTD are aggregation aware when the table covers the date grain they produce (S615).
- Miss: grouping by an attribute below the aggregation grain, such as a Product column when the aggregation holds only subcategory (S615).
- Not supported: grouping by an inactive relationship's key with USERELATIONSHIP; use TREATAS with no active relationship instead (S615).

## Validation rules (S615)
1. Detail and aggregation column data types must match, except Count and Count table rows.
2. No chained aggregations across three or more tables.
3. No duplicate aggregation entries for the same function, table, and column.
4. Detail table in DirectQuery.
5. Relationships between aggregation tables cannot be authored in Desktop; use XMLA tools.

Precedence (S615): when several aggregation tables cover a detail table, the higher Precedence value is tried first. List the detail table, not another aggregation table, as the detail.

A DirectQuery aggregation table from a different source than the detail table is supported only when it is SQL Server, Azure SQL, or Azure Synapse (S615).

## Automatic aggregations (S624)
- Fact: A machine-learning process reads seven days of query log and builds in-memory aggregations marked System.
- Fact: Supported for Premium per capacity, Premium per user, and Embedded models; DirectQuery sources include Azure SQL, Synapse dedicated pool, SQL Server 2019 or later, BigQuery, Snowflake, Databricks, Amazon Redshift.
- Fact: Training runs in the first scheduled refresh of the chosen frequency, with a 60-minute limit. Up to 48 refreshes per day can be scheduled.
- Fact: Only the model owner can configure it. It is available only in the service, not Desktop.
- Do not enable it when the source uses single sign-on with per-user security, when the model has only hybrid tables, and note calculated columns are ignored.
- User-defined and automatic aggregations can coexist.

## Common mistakes
- Forgetting GroupBy entries in a GroupBy-style setup.
- Leaving dimensions in DirectQuery, so relationships stay limited.
- Aggregating at a grain that no report ever uses.

## See also
- [Storage modes](05_storage_modes.md)
- [DirectQuery tuning](../16_performance/16_directquery_tuning.md)
