---
id: 06.ref_functions_date_text_math
title: DAX date, text, and math functions catalog
domain: dax
type: reference
level: beginner
tags: [dax, dax-function, catalog]
summary: Catalog of DAX date and time, text, and math and trig functions, verified against the Microsoft Learn category pages.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S648, S649, S650]
references: []
related: [06.measures_columns_variables, 06.ref_functions_aggregation_logical]
---

# DAX date, text, and math functions catalog

Fact: Names come from Microsoft Learn category pages read on 2026-10-07 (S648, S649, S650).

## Date and time
| Function | Purpose |
|---|---|
| CALENDAR | One-column table "Date" with a contiguous range |
| CALENDARAUTO | Same, range inferred from model dates |
| DATE, TIME | Build a date or time from parts |
| DATEVALUE, TIMEVALUE | Convert text to date or time |
| YEAR, QUARTER, MONTH, DAY | Parts of a date (YEAR returns 1900 to 9999) |
| HOUR, MINUTE, SECOND | Parts of a time |
| WEEKDAY, WEEKNUM | Day of week (1 to 7); week number by return type |
| DATEDIFF | Count of interval boundaries between two dates |
| EDATE, EOMONTH | Shift by months; last day of a shifted month |
| NETWORKDAYS | Whole workdays between two dates |
| YEARFRAC | Fraction of a year between two dates |
| NOW, TODAY | Current local date and time, or date |
| UTCNOW, UTCTODAY | Current UTC date and time, or date |

Inference: In the Power BI service, NOW and TODAY return UTC unless the model handles time zones, so many teams use UTCNOW with an explicit offset. Verify in your tenant.

## Text
- Combine: CONCATENATE (two strings), CONCATENATEX (per row of a table), COMBINEVALUES (joins values; built for multi-column relationships in DirectQuery).
- Extract: LEFT, RIGHT, MID.
- Find: FIND (case sensitive), SEARCH (case insensitive, wildcards).
- Edit: REPLACE, SUBSTITUTE, TRIM, UPPER, LOWER, REPT.
- Convert: FORMAT (value to text by format string), FIXED (rounded number as text), VALUE (text to number), UNICHAR, UNICODE.
- Compare: EXACT.
- LEN: character count.

Fact: FIND vs SEARCH case sensitivity is long-standing Excel-derived behavior; confirm on the function page if it matters.

## Math and trig
| Group | Functions |
|---|---|
| Rounding | ROUND, ROUNDUP, ROUNDDOWN, MROUND, CEILING, ISO.CEILING, FLOOR, INT, TRUNC, EVEN, ODD |
| Arithmetic | ABS, SIGN, MOD, QUOTIENT, DIVIDE, POWER, SQRT, SQRTPI, EXP, LN, LOG, LOG10, FACT, GCD, LCM |
| Constants and random | PI, RAND, RANDBETWEEN |
| Conversion | CONVERT (change data type), CURRENCY, DEGREES, RADIANS |
| Trig | SIN, COS, TAN, COT and the arc and hyperbolic forms (ASIN, ACOS, ATAN, ACOT, SINH, COSH, TANH, COTH, ASINH, ACOSH, ATANH, ACOTH) |

Key points:
- DIVIDE performs division and returns BLANK or an alternate result when dividing by zero (S648).
- MOD returns a result with the sign of the divisor (S648).
- QUOTIENT returns only the integer part of a division (S648).
- RAND and RANDBETWEEN are volatile: results change on each evaluation, so avoid them in measures people compare.

## Example
Last day of the next month from each order date, as a calculated column:
```dax
Next Month End = EOMONTH ( Sales[OrderDate], 1 )
```
