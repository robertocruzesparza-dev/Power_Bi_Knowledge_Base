---
id: 06.function_catalog
title: DAX function catalog index
domain: dax
type: index
level: beginner
tags: [dax, dax-function, catalog, index]
summary: Index that routes from a task to the right DAX function category and reference file, with a quick lookup of the most-used functions.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S640, S641, S642, S643, S644, S645, S646, S648, S649, S650, S657, S658, S2831, S2832]
references: [../references/dax/06_functions_filter.md, ../references/dax/06_functions_table.md, ../references/dax/06_functions_time_intelligence.md, ../references/dax/06_functions_aggregation_logical.md, ../references/dax/06_functions_information.md, ../references/dax/06_functions_date_text_math.md, ../references/dax/06_functions_statistical_relationship.md]
related: [06.dax_basics, 06.patterns]
---

# DAX function catalog index

## Purpose
Microsoft describes over 250 DAX functions (S640). This index points to a catalog file per category. Names were checked against the Learn category pages on 2026-10-07.

## I want to...
| Task | Category | Start with |
|---|---|---|
| Change what is filtered | Filter | CALCULATE, REMOVEFILTERS, KEEPFILTERS |
| Add up, count, average | Aggregation | SUM, COUNTROWS, DISTINCTCOUNT, SUMX |
| Compare periods | Time intelligence | TOTALYTD, SAMEPERIODLASTYEAR, DATEADD |
| Build or reshape a table | Table manipulation | ADDCOLUMNS, SUMMARIZECOLUMNS, TOPN |
| Use a relationship in a calculation | Relationship | USERELATIONSHIP, CROSSFILTER, RELATED |
| Branch on a condition | Logical | IF, SWITCH, COALESCE |
| Test context | Information | HASONEVALUE, ISFILTERED, ISINSCOPE |
| Get the user identity for RLS | Information | USERPRINCIPALNAME |
| Work with dates | Date and time | CALENDAR, DATEDIFF, EOMONTH |
| Manipulate text | Text | CONCATENATEX, FORMAT, SEARCH |
| Round or divide safely | Math | ROUND, DIVIDE |
| Rank, percentile, deviation | Statistical | RANKX, PERCENTILE.INC, STDEV.S |
| Running total, previous row | Filter (window) | WINDOW, OFFSET, RUNNINGSUM |

## Catalog files
1. [Filter and window functions](../references/dax/06_functions_filter.md)
2. [Table manipulation](../references/dax/06_functions_table.md)
3. [Time intelligence](../references/dax/06_functions_time_intelligence.md)
4. [Aggregation, logical, and other](../references/dax/06_functions_aggregation_logical.md)
5. [Information and security](../references/dax/06_functions_information.md)
6. [Date, text, math](../references/dax/06_functions_date_text_math.md)
7. [Statistical and relationship](../references/dax/06_functions_statistical_relationship.md)

## Not catalogued
Financial, parent and child, and any category added after 2026-10-07. Use the Learn function reference.

## Ten functions to learn first
CALCULATE, FILTER, ALL (or REMOVEFILTERS), SUMX, DIVIDE, VALUES, SELECTEDVALUE, RELATED, IF or SWITCH, and one time function such as TOTALYTD.

## Version notes
Fact: Functions are added over time; some are marked visual-calculation-only (S641), and some Information entries are recent (S646). Check your Desktop version when a function is not recognized.

## See also
- [DAX basics](06_dax_basics.md)
- [Patterns](06_patterns.md)
- [User-defined functions](06_user_defined_functions.md)
