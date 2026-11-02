---
id: 05.domain_index
title: Index of data modeling
domain: data_modeling
type: index
level: beginner
tags: [index, navigation]
summary: Lists every file in the data modeling domain with tags and summaries.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: high
sources: []
references: []
related: []
---

# Domain index: data modeling

Scope: Star schema, relationships, storage modes, composite, Direct Lake, aggregations

[Back to INDEX](../INDEX.md)

| ID | Title | Kind | Tags | Summary | Path |
|---|---|---|---|---|---|
| 05.aggregations | Aggregations (user-defined and automatic) | core | aggregation, storage-mode, composite-model, optimization | Shows how aggregation tables speed up large DirectQuery models, including relationship and GroupBy styles, validation rules, and automatic aggregations. | [05_aggregations.md](05_aggregations.md) |
| 05.calculation_groups | Calculation groups | core | calculation-group, dax, measure, semantic-model | Explains calculation groups and items, SELECTEDMEASURE, precedence, sideways recursion, and typical time intelligence and currency patterns. | [05_calculation_groups.md](05_calculation_groups.md) |
| 05.composite_models | Composite models | core | data-modeling, composite-model, storage-mode, relationship | Explains composite models, source groups, cross source group relationships, and Microsoft's design recommendations and risks. | [05_composite_models.md](05_composite_models.md) |
| 05.date_tables_hierarchies | Date tables and hierarchies | core | data-modeling, time-intelligence, star-schema, best-practice | Date table requirements, auto date/time behavior, ways to build a date table, and how to create user hierarchies in Model view. | [05_date_tables_hierarchies.md](05_date_tables_hierarchies.md) |
| 05.direct_lake | Direct Lake storage mode | core | direct-lake, fabric, onelake, storage-mode, limits | Explains Direct Lake on OneLake versus on SQL analytics endpoints, framing, column loading, fallback, and the main limitations. | [05_direct_lake.md](05_direct_lake.md) |
| 05.filter_direction_ambiguity | Filter direction, bi-directional filtering, and path ambiguity | core | data-modeling, relationship, filter-context, best-practice | Explains single versus both cross-filter direction, when bi-directional filtering is risky, and how Power BI resolves ambiguous filter paths. | [05_filter_direction_ambiguity.md](05_filter_direction_ambiguity.md) |
| 05.incremental_refresh_basics | Incremental refresh basics | core | incremental-refresh, refresh, query-folding, semantic-model | Explains how incremental refresh partitions a table, the RangeStart and RangeEnd parameters, policy settings, real-time hybrid tables, and common pitfalls. | [05_incremental_refresh_basics.md](05_incremental_refresh_basics.md) |
| 05.relationships_cardinality | Relationships and cardinality | core | data-modeling, relationship, semantic-model | Covers relationship cardinality types, active and inactive relationships, regular versus limited relationships, blank rows, and how to create them in Desktop. | [05_relationships_cardinality.md](05_relationships_cardinality.md) |
| 05.star_schema | Star schema design for Power BI models | core | data-modeling, star-schema, semantic-model, best-practice | Explains dimension and fact tables, grain, and the star schema patterns Microsoft recommends for fast, understandable Power BI semantic models. | [05_star_schema.md](05_star_schema.md) |
| 05.storage_modes | Storage modes compared (Import, DirectQuery, Dual, Hybrid, Live connection) | core | data-modeling, storage-mode, semantic-model, limits | Compares table storage modes in Power BI semantic models, how Dual and Hybrid work, and the rules for changing a mode. | [05_storage_modes.md](05_storage_modes.md) |
| 05.ref_direct_lake_guardrails | Direct Lake capacity guardrails (pointer) | reference | direct-lake, limits, capacity, reference | Pointer to the single authoritative per-SKU Direct Lake guardrail table kept in the Fabric domain. | [05_direct_lake_guardrails.md](../references/data_modeling/05_direct_lake_guardrails.md) |
