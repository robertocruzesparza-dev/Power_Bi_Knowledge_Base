---
id: 06.ref_functions_time_intelligence
title: DAX time intelligence functions catalog
domain: dax
type: reference
level: intermediate
tags: [dax, dax-function, time-intelligence, catalog]
summary: Catalog of classic DAX time intelligence functions grouped by type, verified against the Microsoft Learn category page.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S642, S628, S2828, S2832]
references: []
related: [06.time_intelligence, 05.date_tables_hierarchies]
---

# DAX time intelligence functions catalog

Fact: The Learn page for these functions says to mark a table as the date table before using them (S642). Names below were read on 2026-10-07.

## Period-to-date and shortcut totals
| Function | Purpose |
|---|---|
| DATESWTD, DATESMTD, DATESQTD, DATESYTD | Table of dates from period start to the last date in context |
| TOTALWTD, TOTALMTD, TOTALQTD, TOTALYTD | Evaluate an expression over the matching period-to-date |

TOTALxTD is a shortcut for CALCULATE with the matching DATESxTD filter.

## Shift and compare periods
| Function | Purpose |
|---|---|
| SAMEPERIODLASTYEAR | Dates shifted back one year |
| DATEADD | Dates shifted by N intervals (day, month, quarter, year) |
| PARALLELPERIOD | Whole parallel period shifted by N intervals |
| PREVIOUSDAY, PREVIOUSWEEK, PREVIOUSMONTH, PREVIOUSQUARTER, PREVIOUSYEAR | The period before the first date in context |
| NEXTDAY, NEXTWEEK, NEXTMONTH, NEXTQUARTER, NEXTYEAR | The period after the last date in context |

## Ranges
| Function | Purpose |
|---|---|
| DATESBETWEEN | Dates from a start date to an end date |
| DATESINPERIOD | Dates starting at a date and running N intervals (use for rolling windows) |

## Boundary dates and balances
| Function | Purpose |
|---|---|
| FIRSTDATE, LASTDATE | First or last date in the current context |
| STARTOFWEEK, STARTOFMONTH, STARTOFQUARTER, STARTOFYEAR | First date of the period |
| ENDOFWEEK, ENDOFMONTH, ENDOFQUARTER, ENDOFYEAR | Last date of the period |
| OPENINGBALANCEWEEK, OPENINGBALANCEMONTH, OPENINGBALANCEQUARTER, OPENINGBALANCEYEAR | Expression at the first date of the period |
| CLOSINGBALANCEWEEK, CLOSINGBALANCEMONTH, CLOSINGBALANCEQUARTER, CLOSINGBALANCEYEAR | Expression at the last date of the period |

## Notes
- Fact: Week-based variants (WTD, WEEK) appear in the current list. Older sources omit them (S642).
- Fact: Auto date/time hidden tables cannot be used directly in these functions; use your own date table (S627 via [date tables](../../05_data_modeling/05_date_tables_hierarchies.md)).
- Inference: For stock or balance measures that must not add across time, use CLOSINGBALANCE* or LASTDATE patterns, not plain sums.
- See [time intelligence](../../06_dax/06_time_intelligence.md) for worked examples and for calendar-based time intelligence.
