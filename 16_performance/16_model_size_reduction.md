---
id: 16.model_size_reduction
title: Reducing semantic model size
domain: performance
type: how-to
level: intermediate
tags: [performance, optimization, semantic-model, limits]
summary: Techniques to shrink Import models: remove columns and rows, summarize, pick data types, use DirectQuery or incremental refresh, and why it matters.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S671, S601, S618, S2505]
references: []
related: [16.dax_studio_vertipaq, 05.incremental_refresh_basics, 05.aggregations]
---

# Reducing semantic model size

## Purpose
Smaller Import models refresh faster, use less capacity memory, and often query faster. The VertiPaq engine compresses well, but loading less data is the biggest lever.

## Key facts
- Fact: Microsoft says 10x compression in memory is a reasonable expectation, with about 20% further reduction on disk (S671).
- Fact: Shared capacity could host models up to 1 GB in the guidance text; Premium sizes depend on SKU (S671). Limits are volatile; check the licensing domain.
- Reasons (S671): capacity limits, memory contention and eviction, refresh speed, and faster calculations on fewer rows.

## Techniques, in order of impact
| Technique | What to do | Trade-off |
|---|---|---|
| Group by and summarize | Load pre-aggregated facts, such as month grain | Loses detail; up to about 99% reduction in the Microsoft example |
| Remove unnecessary rows | Filter history by time or by entity | Less history or many smaller models |
| Remove unnecessary columns | Keep only columns for reporting or model structure | Easier to add later than to remove |
| Optimize data types | Prefer numbers to text; split or strip text prefixes | Needs source or Power Query work |
| Use DirectQuery for big facts | Composite model with summarized Import | Source load, complexity |
| Incremental refresh | Refresh only recent partitions | Does not shrink the model by itself |
Source for all rows: S671 unless noted; incremental refresh is S618.

## How the engine stores data (S671)
- Numeric columns use value encoding. Text and non-numeric data use hash encoding, which assigns a number to each unique value and needs a hash lookup.
- Example: an order number "SO123456" can drop the prefix and become a whole number; set Do Not Summarize on it. Large unique columns benefit most.
- Inference: Cardinality (distinct values) drives dictionary size, so high-cardinality columns such as timestamps, GUIDs, and free text cost most.

## Steps
1. Open View Metrics in [DAX Studio](16_dax_studio_vertipaq.md); list the biggest columns.
2. For each: is it used by a visual, relationship, measure, or security role? If not, remove it in Power Query.
3. Split datetime into date and time columns if you only need date-level slicing (inference: lowers cardinality).
4. Replace GUID or long text keys with integer surrogate keys (see [star schema](../05_data_modeling/05_star_schema.md)).
5. Filter history with parameters, ideally relative to the refresh date.
6. Rebuild the star schema if one wide table mixes facts and attributes.
7. Remove auto date/time tables if you have your own date table ([date tables](../05_data_modeling/05_date_tables_hierarchies.md)).
8. Re-measure total memory and refresh time.

## Common mistakes
- Removing a column that a report, relationship, or security role uses; this can break reports (S671).
- Keeping every column "just in case".
- Loading all available history by default when it is not a known requirement (S671).
- Summarizing without agreeing the grain with report users.

## See also
- [Aggregations](../05_data_modeling/05_aggregations.md)
- [Incremental refresh basics](../05_data_modeling/05_incremental_refresh_basics.md)
- [Optimization checklist](16_optimization_checklist.md)
