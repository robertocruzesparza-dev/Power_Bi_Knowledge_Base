---
id: 05.star_schema
title: Star schema design for Power BI models
domain: data_modeling
type: concept
level: beginner
tags: [data-modeling, star-schema, semantic-model, best-practice]
summary: Explains dimension and fact tables, grain, and the star schema patterns Microsoft recommends for fast, understandable Power BI semantic models.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S601, S605, S606]
references: []
related: [05.relationships_cardinality, 05.filter_direction_ambiguity, 05.date_tables_hierarchies]
---

# Star schema design for Power BI models

## Purpose
A star schema splits a model into dimension tables (things you filter and group by) and fact tables (events you summarize). Power BI is built to query this shape quickly.

## Key facts
- Fact: Dimension tables enable filtering and grouping. Fact tables enable summarization (S601).
- Fact: There is no table property for "dimension" or "fact". The relationship cardinality decides it: the one side is a dimension, the many side is a fact (S601).
- Fact: A dimension has a unique key column plus descriptive columns. It usually has relatively few rows (S601).
- Fact: A fact table holds dimension keys and numeric measure columns. It can grow large over time (S601).
- Fact: Dimension key columns set the dimensionality of a fact table. The key values set its granularity (grain) (S601).
- Fact: Keep each fact table at one consistent grain, and do not mix dimension and fact roles in one table (S601).

## Example
A Sales fact table has OrderDateKey, ProductKey, CustomerKey, Quantity, and Amount. It relates many-to-one to Date, Product, and Customer dimensions. A visual that shows Amount by Product Category filters Product, and that filter flows down to Sales.

If a Targets table stores one row per product per month, its grain is month by product. It cannot be sliced by day. Relate it to a month-level key or to a date dimension at month level, not to the daily date.

## Star schema concepts that apply in Power BI (S601)
| Concept | Meaning in a Power BI model |
|---|---|
| Measures | DAX calculations that summarize fact columns |
| Surrogate keys | Integer keys that replace messy or composite natural keys |
| Snowflake dimensions | A dimension split across linked tables; flatten into one table when practical |
| Role-playing dimensions | One dimension used for several roles, such as Order Date and Ship Date |
| Slowly changing dimensions | Dimensions that keep history of changed attributes |
| Junk dimensions | One table that groups low-cardinality flags |
| Degenerate dimensions | A key kept on the fact table, such as an order number |
| Factless fact tables | Fact tables with only keys; used for events or as bridge tables |

## Role-playing dimensions
Two options exist. Duplicate the dimension (Order Date, Ship Date), each with an active relationship. Or keep one dimension with one active and other inactive relationships, and switch with USERELATIONSHIP in a measure. Microsoft recommends active relationships where possible because they give report authors more freedom (S603). See [relationships and cardinality](05_relationships_cardinality.md).

## Many-to-many shapes
- Two dimensions that relate many-to-many: use a bridge table (a factless fact) with one-to-many relationships to each side (S601, S605).
- Two fact tables: do not relate them directly. Add shared dimensions at the grain both facts can reach, then relate each fact to those dimensions (S605).
- A one-to-one relationship is valid for a degenerate dimension or when one entity's data is split across tables from different sources (S606).

## Common mistakes
- One wide, flat table that mixes events and descriptions. It inflates size and blocks reuse.
- Relating fact tables to each other, which limits filtering to the shared ID column.
- Leaving key columns visible. Hide them so report authors use dimension columns.
- Facts at mixed grains in one table, which makes sums wrong.

## Limits and version notes
Fact: Microsoft says model design is part science and part art, and breaking the guidance can be right when you have a reason (S601).

## See also
- [Relationships and cardinality](05_relationships_cardinality.md)
- [Filter direction and ambiguity](05_filter_direction_ambiguity.md)
- [Date tables and hierarchies](05_date_tables_hierarchies.md)
