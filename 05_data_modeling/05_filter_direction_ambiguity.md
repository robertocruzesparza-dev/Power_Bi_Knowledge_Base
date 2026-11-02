---
id: 05.filter_direction_ambiguity
title: Filter direction, bi-directional filtering, and path ambiguity
domain: data_modeling
type: concept
level: intermediate
tags: [data-modeling, relationship, filter-context, best-practice]
summary: Explains single versus both cross-filter direction, when bi-directional filtering is risky, and how Power BI resolves ambiguous filter paths.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S602, S603, S604]
references: []
related: [05.relationships_cardinality, 06.filter_context]
---

# Filter direction, bi-directional filtering, and path ambiguity

## Purpose
Cross-filter direction controls which way filters travel along a relationship. Single is the safe default. Both is a tool to use sparingly.

## Key facts
- Fact: Single direction sends filters from the one side to the many side. This is the default and the most common (S602).
- Fact: Both treats the two tables as one for filtering. It works in a plain star around one fact table (S602).
- Fact: Bi-directional relationships can hurt performance and can create ambiguous paths (S603, S604).
- Fact: Desktop refuses a Both setting that would create ambiguity in most cases, but it does not fully validate composite and cross source group cases (S602, S608).
- Fact: A relationship set to Both gets an extra option to apply bi-directional filtering when RLS is enforced (S603).

## Worked example
Model: Sales fact with Customer and Product dimensions, all single direction. A measure that counts distinct Customer countries for each Product returns the same number on every row, because the Product filter reaches Sales but does not travel on to Customer.

Preferred fix (S604): switch the direction only inside the measure.

```dax
Different Countries Sold =
CALCULATE (
    DISTINCTCOUNT ( Customer[Country-Region] ),
    CROSSFILTER ( Customer[CustomerCode], Sales[CustomerCode], BOTH )
)
```

CROSSFILTER can also set direction to one-way or disable a relationship during one calculation (S603).

## When to avoid Both
- Two fact tables share a dimension (sales actuals and budget share Department). Both on each link creates loops and ambiguity (S602).
- Large models: each added direction adds filter work.
- Slicer lists: Both makes slicers show only values that have data, which changes user expectations (S604).

## Resolving ambiguity
Power BI picks a path by priority, then by weight (S603).
1. Priority order, first match wins: all one-to-many; one-to-many or many-to-many; all many-to-one; one-to-many then many-to-one; mixed with many-to-many; any other.
2. A relationship present in every path is removed from consideration.
3. Within a tier, higher weight wins. Weight is equal by default. USERELATIONSHIP raises it; the innermost call gets the highest weight.
4. Same priority and same weight gives an ambiguous path error. Remove or change a relationship, or use USERELATIONSHIP.

Practical fixes (S602): mark one relationship inactive, or load a table twice under a different name to break a loop and restore a star.

## Error: "Can't determine relationships between the fields"
Cause: a visual combines columns that are only indirectly many-to-many (two facts via one dimension) and no measure constrains it (S602). Steps:
1. Check whether the model can become a true star.
2. Add a model measure to the visual; a measure counts as a constraint that relates everything.
3. A summarized column can relate to only some tables, so a measure is safer.
4. Consider a direct many-to-many relationship or a bridge table (S602).

## Common mistakes
- Turning Both on everywhere "to make slicers work".
- Using Both to patch a missing dimension.
- Forgetting that DAX CROSSFILTER and USERELATIONSHIP change only the one calculation.

## See also
- [Relationships and cardinality](05_relationships_cardinality.md)
- [Filter context in DAX](../06_dax/06_filter_context.md)
