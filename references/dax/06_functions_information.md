---
id: 06.ref_functions_information
title: DAX information and security functions catalog
domain: dax
type: reference
level: intermediate
tags: [dax, dax-function, catalog, rls]
summary: Catalog of DAX information functions: type tests, filter-state tests, text search, user identity, and calculation group helpers.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S646, S2829, S2832]
references: []
related: [06.calculate_context_transition, 05.calculation_groups]
---

# DAX information and security functions catalog

Fact: Names come from the Microsoft Learn "Information functions" page read on 2026-10-07 (S646). Several entries are recent additions; confirm availability in your Desktop and service version.

## Filter-state tests
| Function | Returns TRUE when |
|---|---|
| HASONEVALUE | The column in context has exactly one distinct value |
| HASONEFILTER | The column is directly filtered to exactly one value |
| ISFILTERED | The column is directly filtered |
| ISCROSSFILTERED | The column, or another column in that or a related table, is filtered |
| ISINSCOPE | The column is the current level in a hierarchy of levels |
| ISSUBTOTAL | A SUMMARIZE row holds subtotals for a column |
| ISEMPTY | A table has no rows |
| ISBLANK | A value is blank |

Difference worth knowing: ISFILTERED looks only at direct filters. ISCROSSFILTERED also sees filters arriving through relationships. HASONEVALUE tests the result, whatever its source (S646).

## Type tests
ISBOOLEAN (alias ISLOGICAL), ISCURRENCY (alias ISDECIMAL), ISDATETIME, ISDOUBLE, ISINT64 (alias ISINTEGER), ISNONTEXT, ISNUMBER (alias ISNUMERIC), ISSTRING (alias ISTEXT), ISERROR, ISEVEN, ISODD.

## Containment and search
- CONTAINS: TRUE if a row with the given column values exists in a table.
- CONTAINSROW: TRUE if a row of values exists in a table.
- CONTAINSSTRING (case insensitive) and CONTAINSSTRINGEXACT (case sensitive): substring test.
- TEXTCONTAINS: full-text style match against a column. TEXTSIMILARITY: relevance score for a match.
- ISAFTER and ISONORAFTER: emulate Start At behavior in sort-based queries.

## User and session identity
| Function | Returns |
|---|---|
| USERPRINCIPALNAME | User principal name (UPN); the common choice for dynamic row-level security (RLS) |
| USERNAME | Domain and user name from connection credentials |
| USEROBJECTID | Object ID or security identifier |
| USERCULTURE | Locale of the current user |
| CUSTOMDATA | The CustomData value from the connection string |

## Calculation group helpers
SELECTEDMEASURE, SELECTEDMEASURENAME, SELECTEDMEASUREFORMATSTRING, ISSELECTEDMEASURE. See [calculation groups](../../05_data_modeling/05_calculation_groups.md).

## Metadata and model functions
- NAMEOF: name of a table, column, measure, or calendar as text.
- TABLEOF: table associated with a column, measure, or calendar.
- COLUMNSTATISTICS: statistics for every column in every table of the model.
- NONVISUAL: marks a value filter in SUMMARIZECOLUMNS as non-visual.

Fact: The mention of "calendar" in NAMEOF and TABLEOF reflects calendar objects used by calendar-based time intelligence (S646). See [time intelligence](../../06_dax/06_time_intelligence.md).

## Example
Test whether a total or a single product is shown:
```dax
Label = IF ( HASONEVALUE ( Product[Name] ), VALUES ( Product[Name] ), "All products" )
```
Use SELECTEDVALUE ( Product[Name], "All products" ) as the shorter form.
