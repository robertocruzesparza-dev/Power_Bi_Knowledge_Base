---
id: 05.relationships_cardinality
title: Relationships and cardinality
domain: data_modeling
type: concept
level: intermediate
tags: [data-modeling, relationship, semantic-model]
summary: Covers relationship cardinality types, active and inactive relationships, regular versus limited relationships, blank rows, and how to create them in Desktop.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S602, S603, S605, S606]
references: []
related: [05.star_schema, 05.filter_direction_ambiguity, 05.composite_models]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [Cardinality types](#cardinality-types)
- [Regular and limited relationships](#regular-and-limited-relationships)
- [Blank rows](#blank-rows)
- [Steps to create a relationship](#steps-to-create-a-relationship)
- [Common mistakes](#common-mistakes)
- [See also](#see-also)

# Relationships and cardinality

## Purpose
A relationship passes a filter from a column in one table to a column in another. It does not enforce data integrity (S603).

## Key facts
- Fact: Filters flow along a relationship path, and the path is deterministic (S603).
- Fact: A many-to-one relationship needs at least one side with unique values. Otherwise Desktop shows "One of the columns must have unique values" (S602).
- Fact: Only one active relationship can exist between two tables. Others must be inactive. An inactive one is used only inside a calculation with USERELATIONSHIP (S603).
- Fact: Desktop can autodetect relationships at load time from column names. If it is not confident, it creates nothing (S602).
- Fact: Default option "Import relationships from data sources on first load" is on. "Update or delete relationships when refreshing data" is off by default. Do not turn it on if row-level security depends on a relationship (S602).

## Cardinality types
| Type | Meaning | Notes |
|---|---|---|
| Many-to-one (*:1) | Default. The one side is a lookup | Most common (S602) |
| One-to-many (1:*) | Mirror of many-to-one | Same behavior, reversed direction |
| One-to-one (1:1) | Both columns unique | Cross filter is both; tables act as one (S602, S606) |
| Many-to-many (*:*) | No unique column needed | Always a limited relationship (S603) |

Pick cardinality from the data you expect after future refreshes, not just today. In the Microsoft example, a budget table was one-to-one until it received repeat rows; the author set many-to-one on purpose (S602).

## Regular and limited relationships
Fact: Evaluation type is inferred, not set (S603).
- Regular: the engine can confirm the one side is unique. All one-to-many relationships inside one source group are regular. A source group is the Vertipaq cache or one DirectQuery source.
- Limited: no guaranteed one side. This is any many-to-many relationship, or any relationship across source groups (composite models).

| Behavior | Regular | Limited |
|---|---|---|
| Table expansion | Yes | No |
| Join semantics | Left outer (one-to-one: full outer) | Inner join |
| Blank row for unmatched keys | Yes | No |
| RELATED to the one side | Works | Not usable |
| Row-level security (RLS) | Normal | Topology restrictions |

Fact: Microsoft ranks filter performance fastest to slowest as one-to-many in one source group, then many-to-many via a bridge table with a bi-directional link, then many-to-many cardinality, then cross source group (S603).

## Blank rows
When a many-side key has no match, a regular relationship adds a virtual blank row to the one side. Visuals then show a "(Blank)" group. Fix the source data rather than hide it (S603). With limited relationships, unmatched rows silently drop out of results (S606).

## Steps to create a relationship
1. Open Model view, or Modeling tab, Manage relationships, New (S602).
2. Choose the many-side table and column, then the one-side table and column.
3. Accept cardinality and direction, or set them; keep Make this relationship active checked unless it is a second path.
4. Select OK, then test a visual.
Alternative: drag a column from one table onto another in Model view. A Properties pane editor for relationships is documented as preview and must be enabled under Preview features (S602).

## Common mistakes
- Keys with different data types, or hidden whitespace and case differences.
- Using many-to-many to patch a missing dimension. Add the dimension instead (S605).
- Two paths between the same tables where the wrong one is active (S602).
- Assuming a relationship protects against orphan keys.

## See also
- [Filter direction and ambiguity](05_filter_direction_ambiguity.md)
- [Star schema](05_star_schema.md)
- [Composite models](05_composite_models.md)
