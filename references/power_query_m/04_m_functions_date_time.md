---
id: ref.m_functions_date_time
title: M functions: Date, Time, Duration
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Date, DateTime, DateTimeZone, Time and Duration M functions for calendars, arithmetic and conversion.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---

## Table of Contents

- [Date functions](#date-functions)
- [DateTime functions](#datetime-functions)
- [DateTimeZone functions](#datetimezone-functions)
- [Time functions](#time-functions)
- [Duration functions](#duration-functions)
- [See also](#see-also)

# M functions: Date, Time, Duration

Purpose: a lookup list of M functions from the official function reference. 118 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Date functions

- `Date.AddDays`: Returns a Date/DateTime/DateTimeZone value with the day portion incremented by the number of days provided. It also
- `Date.AddMonths`: Returns a DateTime value with the month portion incremented by n months.
- `Date.AddQuarters`: Returns a Date/DateTime/DateTimeZone value incremented by the number of quarters provided. Each quarter is defined 
- `Date.AddWeeks`: Returns a Date/DateTime/DateTimeZone value incremented by the number of weeks provided. Each week is defined as a d
- `Date.AddYears`: Returns a DateTime value with the year portion incremented by n years.
- `Date.Day`: Returns the day for a DateTime value.
- `Date.DayOfWeek`: Returns a number (from 0 to 6) indicating the day of the week of the provided value.
- `Date.DayOfWeekName`: Returns the day of the week name.
- `Date.DayOfYear`: Returns a number that represents the day of the year from a DateTime value.
- `Date.DaysInMonth`: Returns the number of days in the month from a DateTime value.
- `Date.EndOfDay`: Returns the end of the day.
- `Date.EndOfMonth`: Returns the end of the month.
- `Date.EndOfQuarter`: Returns the end of the quarter.
- `Date.EndOfWeek`: Returns the end of the week.
- `Date.EndOfYear`: Returns the end of the year.
- `Date.From`: Returns a date value from a value.
- `Date.FromText`: Creates a Date from local, universal, and custom Date formats.
- `Date.IsInCurrentDay`: Indicates whether the given datetime value dateTime occurs during the current day, as determined by the current dat
- `Date.IsInCurrentMonth`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current month, 
- `Date.IsInCurrentQuarter`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current quarter
- `Date.IsInCurrentWeek`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current week, a
- `Date.IsInCurrentYear`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current year, a
- `Date.IsInNextDay`: Indicates whether the given datetime value dateTime occurs during the next day, as determined by the current date a
- `Date.IsInNextMonth`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next month, as 
- `Date.IsInNextNDays`: Indicates whether the given datetime value dateTime occurs during the next number of days, as determined by the cur
- `Date.IsInNextNMonths`: Indicates whether the given datetime value dateTime occurs during the next number of months, as determined by the c
- `Date.IsInNextNQuarters`: Indicates whether the given datetime value dateTime occurs during the next number of quarters, as determined by the
- `Date.IsInNextNWeeks`: Indicates whether the given datetime value dateTime occurs during the next number of weeks, as determined by the cu
- `Date.IsInNextNYears`: Indicates whether the given datetime value dateTime occurs during the next number of years, as determined by the cu
- `Date.IsInNextQuarter`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next quarter, a
- `Date.IsInNextWeek`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next week, as d
- `Date.IsInNextYear`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next year, as d
- `Date.IsInPreviousDay`: Indicates whether the given datetime value dateTime occurs during the previous day, as determined by the current da
- `Date.IsInPreviousMonth`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous month,
- `Date.IsInPreviousNDays`: Indicates whether the given datetime value dateTime occurs during the previous number of days, as determined by the
- `Date.IsInPreviousNMonths`: Indicates whether the given datetime value dateTime occurs during the previous number of months, as determined by t
- `Date.IsInPreviousNQuarters`: Indicates whether the given datetime value dateTime occurs during the previous number of quarters, as determined by
- `Date.IsInPreviousNWeeks`: Indicates whether the given datetime value dateTime occurs during the previous number of weeks, as determined by th
- `Date.IsInPreviousNYears`: Indicates whether the given datetime value dateTime occurs during the previous number of years, as determined by th
- `Date.IsInPreviousQuarter`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous quarte
- `Date.IsInPreviousWeek`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous week, 
- `Date.IsInPreviousYear`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous year, 
- `Date.IsInYearToDate`: Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred in the period starting Jan
- `Date.IsLeapYear`: Returns a logical value indicating whether the year portion of a DateTime value is a leap year.
- `Date.Month`: Returns the month from a DateTime value.
- `Date.MonthName`: Returns the name of the month component.
- `Date.QuarterOfYear`: Returns a number between 1 and 4 for the quarter of the year from a DateTime value.
- `Date.StartOfDay`: Returns the start of the day.
- `Date.StartOfMonth`: Returns the start of the month.
- `Date.StartOfQuarter`: Returns the start of the quarter.
- `Date.StartOfWeek`: Returns the start of the week.
- `Date.StartOfYear`: Returns the start of the year.
- `Date.ToRecord`: Returns a record containing parts of a Date value.
- `Date.ToText`: Returns a text value from a Date value.
- `Date.WeekOfMonth`: Returns a number for the count of week in the current month.
- `Date.WeekOfYear`: Returns a number for the count of week in the current year.
- `Date.Year`: Returns the year from a DateTime value.

## DateTime functions

- `DateTime.AddZone`: Adds timezone information to the datetime value.
- `DateTime.Date`: Returns the date component of the given date, datetime, or datetimezone value.
- `DateTime.FixedLocalNow`: Returns the current date and time in the local timezone. This value is fixed and doesn't change with successive cal
- `DateTime.From`: Creates a datetime from the given value.
- `DateTime.FromFileTime`: Creates a datetime from a 64-bit long number.
- `DateTime.FromText`: Creates a datetime from local and universal datetime formats.
- `DateTime.IsInCurrentHour`: Indicates whether this datetime occurs during the current hour, as determined by the current date and time on the s
- `DateTime.IsInCurrentMinute`: Indicates whether this datetime occurs during the current minute, as determined by the current date and time on the
- `DateTime.IsInCurrentSecond`: Indicates whether this datetime occurs during the current second, as determined by the current date and time on the
- `DateTime.IsInNextHour`: Indicates whether this datetime occurs during the next hour, as determined by the current date and time on the syst
- `DateTime.IsInNextMinute`: Indicates whether this datetime occurs during the next minute, as determined by the current date and time on the sy
- `DateTime.IsInNextNHours`: Indicates whether this datetime occurs during the next number of hours, as determined by the current date and time 
- `DateTime.IsInNextNMinutes`: Indicates whether this datetime occurs during the next number of minutes, as determined by the current date and tim
- `DateTime.IsInNextNSeconds`: Indicates whether this datetime occurs during the next number of seconds, as determined by the current date and tim
- `DateTime.IsInNextSecond`: Indicates whether this datetime occurs during the next second, as determined by the current date and time on the sy
- `DateTime.IsInPreviousHour`: Indicates whether this datetime occurs during the previous hour, as determined by the current date and time on the 
- `DateTime.IsInPreviousMinute`: Indicates whether this datetime occurs during the previous minute, as determined by the current date and time on th
- `DateTime.IsInPreviousNHours`: Indicates whether this datetime occurs during the previous number of hours, as determined by the current date and t
- `DateTime.IsInPreviousNMinutes`: Indicates whether this datetime occurs during the previous number of minutes, as determined by the current date and
- `DateTime.IsInPreviousNSeconds`: Indicates whether this datetime occurs during the previous number of seconds, as determined by the current date and
- `DateTime.IsInPreviousSecond`: Indicates whether this datetime occurs during the previous second, as determined by the current date and time on th
- `DateTime.LocalNow`: Returns the current date and time in the local timezone.
- `DateTime.Time`: Returns the time part of the given datetime value.
- `DateTime.ToRecord`: Returns a record containing the datetime value's parts.
- `DateTime.ToText`: Returns a textual representation of the datetime value.

## DateTimeZone functions

- `DateTimeZone.FixedLocalNow`: Returns a DateTimeZone value set to the current date, time, and timezone offset on the system.
- `DateTimeZone.FixedUtcNow`: Returns the current date and time in UTC (the GMT timezone).
- `DateTimeZone.From`: Returns a datetimezone value from a value.
- `DateTimeZone.FromFileTime`: Returns a DateTimeZone from a number value.
- `DateTimeZone.FromText`: Creates a datetimezone from local, universal, and custom datetimezone formats.
- `DateTimeZone.LocalNow`: Returns a DateTime value set to the current system date and time.
- `DateTimeZone.RemoveZone`: Returns a datetime value with the zone information removed from the input datetimezone value.
- `DateTimeZone.SwitchZone`: Changes the timezone information for the input DateTimeZone.
- `DateTimeZone.ToLocal`: Returns a DateTime value from the local time zone.
- `DateTimeZone.ToRecord`: Returns a record containing parts of a DateTime value.
- `DateTimeZone.ToText`: Returns a text value from a DateTime value.
- `DateTimeZone.ToUtc`: Returns a DateTime value to the Utc time zone.
- `DateTimeZone.UtcNow`: Returns a DateTime value set to the current system date and time in the Utc timezone.
- `DateTimeZone.ZoneHours`: Gets the timezone hour of the value.
- `DateTimeZone.ZoneMinutes`: Gets the timezone minute of the value.

## Time functions

- `Time.EndOfHour`: Returns the end of the hour.
- `Time.From`: Returns a time value from a value.
- `Time.FromText`: Creates a Time from local, universal, and custom Time formats.
- `Time.Hour`: Returns an hour value from a DateTime value.
- `Time.Minute`: Returns a minute value from a DateTime value.
- `Time.Second`: Returns a second value from a DateTime value
- `Time.StartOfHour`: Returns the start of the hour.
- `Time.ToRecord`: Returns a record containing parts of a Date value.
- `Time.ToText`: Returns a text value from a Time value.

## Duration functions

- `Duration.Days`: Returns the days portion of a duration.
- `Duration.From`: Creates a duration from the given value.
- `Duration.FromText`: Returns a duration value from a text value.
- `Duration.Hours`: Returns the hours portion of a duration.
- `Duration.Minutes`: Returns the minutes portion of a duration.
- `Duration.Seconds`: Returns the seconds portion of a duration.
- `Duration.ToRecord`: Returns a record containing the parts of the duration.
- `Duration.TotalDays`: Returns the total days this duration spans.
- `Duration.TotalHours`: Returns the total hours this duration spans.
- `Duration.TotalMinutes`: Returns the total minutes this duration spans.
- `Duration.TotalSeconds`: Returns the total seconds this duration spans.
- `Duration.ToText`: Returns the text of the form "d.h:m:s".

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
