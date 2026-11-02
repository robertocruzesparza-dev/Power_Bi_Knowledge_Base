---
id: 05.date_tables_hierarchies
title: Date tables and hierarchies
domain: data_modeling
type: how-to
level: beginner
tags: [data-modeling, time-intelligence, star-schema, best-practice]
summary: Date table requirements, auto date/time behavior, ways to build a date table, and how to create user hierarchies in Model view.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S625, S626, S627, S628, S629, S2547, S2545]
references: []
related: [06.time_intelligence, 05.star_schema]
---

# Date tables and hierarchies

## Purpose
Time intelligence needs a proper date table. Hierarchies make drilling easier for report authors.

## Date table requirements (S626)
A date table is a model table whose date column meets these rules:
1. Data type date or date/time.
2. Unique values.
3. No blanks.
4. No missing dates.
5. Spans full years (fiscal years are allowed).
6. Marked as a date table when you use classic time intelligence. Not needed for calendar-based time intelligence, except in specific cases (S625, S626).

## Three time intelligence approaches (S628)
| Approach | Setup | Flexibility | Notes |
|---|---|---|---|
| Auto date/time | Almost none | Low | Hidden table per date column; can bloat model |
| Classic functions | Medium | Low | Gregorian or shifted calendars; needs marked table |
| Calendar-based (preview in docs) | High | High | Documented as recommended; check current status |

Unverified: the preview label for calendar-based time intelligence comes from docs read on 2026-10-07 and may have changed. See [time intelligence](../06_dax/06_time_intelligence.md).

## Auto date/time (S627)
- Creates a hidden calculated table for each date column when the table is Import, the column is date or date/time, and the column is not the many side of a relationship.
- Each hidden table has Date, Day, MonthNo, Month, QuarterNo, Quarter, and Year, built with CALENDAR over full years.
- It is permanently hidden. DAX uses special syntax such as Sales[OrderDate].[Date].
- Default is on in new installs, globally and per file. Turning off the file option removes the tables and can break visuals.
- Microsoft advises keeping it only for simple, calendar-only models (S626).

## Ways to add your own date table (S626)
1. Connect to an existing date dimension from the warehouse (best; one source of truth).
2. Generate in Power Query.
3. Generate in DAX with CALENDAR or CALENDARAUTO.
4. Clone with DAX.
Share a Desktop template with a configured date table. In DirectQuery models without a source date table, add one at the source.

## Marking a date table (S625)
Marking removes the built-in auto tables, and visuals or DAX that used them break. Set the date column data type first. Marking also stops Desktop from auto-creating date hierarchies.

## Hierarchies (S629)
A hierarchy orders columns from least to most granular, such as Category, Subcategory, Product.
1. In Fields, right-click the top-level column, choose Create hierarchy.
2. In Properties, name it, then add and order levels. Apply Level Changes.
3. Use it in a visual to enable drill down.
Example hierarchies from Microsoft's tutorial: Geography (country, state, city, postal code, customer), Fiscal (year, quarter, month, date), Products (category, subcategory, model, product).

Notes:
- Fact: Auto date/time hierarchies can be switched to the plain date column in a visual; user-created ones cannot (S627).
- Fact: User-defined hierarchies on Direct Lake tables are not supported in Excel and MDX clients (S611 via [Direct Lake](05_direct_lake.md)).
- Fact: Scorecard hierarchies are a different feature and were announced to be retired by April 15, 2026 (docs warning). Verify before relying.

## Common mistakes
- Using the fact table's date as the only date column and calling it a date table.
- Gaps in dates, which break YTD and prior-year logic.
- Many hidden auto tables in a wide model.
- Skipping the date dimension relationship to every fact table that needs it.

## See also
- [Time intelligence](../06_dax/06_time_intelligence.md)
- [Star schema](05_star_schema.md)
