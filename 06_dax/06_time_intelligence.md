---
id: 06.time_intelligence
title: Time intelligence in DAX
domain: dax
type: how-to
level: intermediate
tags: [dax, time-intelligence, dax-pattern, measure]
summary: How to build year-to-date, prior-period, and rolling measures with classic functions, and how calendar-based time intelligence (preview) differs.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S642, S625, S626, S628, S2531]
references: [../references/dax/06_functions_time_intelligence.md]
related: [05.date_tables_hierarchies, 05.calculation_groups]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [Classic patterns](#classic-patterns)
- [Calendar-based time intelligence](#calendar-based-time-intelligence)
- [Common mistakes](#common-mistakes)
- [See also](#see-also)

# Time intelligence in DAX

## Purpose
Time intelligence functions shift or widen the date filter so a measure can compare periods.

## Key facts
- Fact: Each function works by modifying the filter context on dates (S653).
- Fact: You need a date table with unique, gap-free dates covering full years (S626). Classic functions need it marked as a date table (S625, S626).
- Fact: Pass the date column of your date table, not a fact table date.
- Fact: Docs read on 2026-10-07 call calendar-based time intelligence a preview and the recommended option for best performance and flexibility (S628). Treat that status as volatile.

## Classic patterns
Assume `[Total Sales]` and a marked table 'Date'.
```dax
Sales YTD   = TOTALYTD ( [Total Sales], 'Date'[Date] )
Sales PY    = CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
Sales YoY % = DIVIDE ( [Total Sales] - [Sales PY], [Sales PY] )
Sales R12M  = CALCULATE ( [Total Sales], DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -12, MONTH ) )
Sales PM    = CALCULATE ( [Total Sales], DATEADD ( 'Date'[Date], -1, MONTH ) )
```
- Fiscal year end: TOTALYTD accepts a year-end date argument (check the function page for the exact form).
- Period balance: use CLOSINGBALANCEMONTH or LASTDATE with CALCULATE for measures that must not sum across time.
- Mixed granularity: a prior-year measure on a month visual shifts the whole month. Check partial periods at the current month.
Full function list: [time intelligence catalog](../references/dax/06_functions_time_intelligence.md).

## Choosing an approach (S628)
| Approach | Setup | Flexibility | Note |
|---|---|---|---|
| Auto date/time | None | Low | Hidden tables increase model size |
| Classic functions | Medium | Low | Gregorian or shifted calendars; some slow cases |
| Calendar-based (preview) | High | High | Non-Gregorian calendars, weeks, best performance |
Microsoft also advises against adding offset columns to date tables to avoid time functions, because they inflate models (S628).

## Calendar-based time intelligence
- Enable: File, Options, Preview features, "Enhanced DAX Time Intelligence", then restart Desktop (S628).
- Define a calendar from Calendar options on the date table, or in TMDL. You assign columns to categories (year, quarter, month, and others). Each category needs a primary column (S628).
- Time functions then take the calendar name instead of a date column: `TOTALMTD ( [Total Quantity], 'ISO-454' )` (S628).
- Required categories depend on the function. Missing ones return an error. TOTALQTD needs the Quarter category, or Quarter of Year plus Year (S628).
- Context clearing: a filter on a tagged column clears filters on related categories above and below it. Most functions also clear all time-related columns. DATEADD and SAMEPERIODLASTYEAR only shift laterally and keep other columns (S628).
- Nested time functions are unsupported; wrap with CALCULATETABLE instead (S628).
- Calendar columns not given a category in TMDL are tagged time-related (S628).

## Common mistakes
- A date table with gaps or partial years.
- Using the fact table date column in a time function.
- Relationship to the wrong date role (Order vs Ship date). Use USERELATIONSHIP.
- Treating the preview feature as stable in production without checking release notes.

## See also
- [Date tables and hierarchies](../05_data_modeling/05_date_tables_hierarchies.md)
- [Calculation groups](../05_data_modeling/05_calculation_groups.md)
