---
id: ref.m_functions_list
title: M functions: List
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: List-category M functions for building, transforming, aggregating and comparing lists.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---

## Table of Contents

- [List functions](#list-functions)
- [See also](#see-also)

# M functions: List

Purpose: a lookup list of M functions from the official function reference. 70 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## List functions

- `List.Count`: Returns the number of items in a list.
- `List.IsEmpty`: Returns true if the list is empty.
- `List.NonNullCount`: Returns the number of non-null items in the list.
- `List.Alternate`: Returns a list comprised of all the odd numbered offset elements in a list.
- `List.Buffer`: Buffers a list.
- `List.Distinct`: Returns a list of values with duplicates removed.
- `List.FindText`: Returns a list of values (including record fields) that contain the specified text.
- `List.First`: Returns the first value of the list or the specified default if empty.
- `List.FirstN`: Returns the first set of items in the list by specifying how many items to return or a qualifying condition.
- `List.InsertRange`: Inserts values into a list at the given index.
- `List.IsDistinct`: Indicates whether there are duplicates in the list.
- `List.Last`: Returns the last value of the list or the specified default if empty.
- `List.LastN`: Returns a list of the last item or items in the specified list. Can optionally specify how many values to return or
- `List.MatchesAll`: Returns true if the condition function is satisfied by all values in the list.
- `List.MatchesAny`: Returns true if the condition function is satisfied by any value.
- `List.Positions`: Returns a list of offsets for the input.
- `List.Range`: Returns a subset of the list beginning at an offset.
- `List.Select`: Returns a list of values that match the condition.
- `List.Single`: Returns the one list item for a list of length one, otherwise raises an error.
- `List.SingleOrDefault`: Returns the one list item for a list of length one and the default value for an empty list.
- `List.Skip`: Returns a list that skips the specified number of elements at the beginning of the list.
- `List.Accumulate`: AAccumulates a summary value from the items in the list.
- `List.Combine`: Returns a single list by combining multiple lists.
- `List.RemoveFirstN`: Returns a list that skips the specified number of elements at the beginning of the list.
- `List.RemoveItems`: Removes items from the first list that are present in the second list.
- `List.RemoveLastN`: Returns a list that removes the specified number of elements from the end of the list.
- `List.RemoveMatchingItems`: Removes all occurrences of the input values.
- `List.RemoveNulls`: Removes all null values from the specified list.
- `List.RemoveRange`: Removes count number of values starting at the specified position.
- `List.Repeat`: Returns a list that is count repetitions of the original list.
- `List.ReplaceMatchingItems`: Replaces occurrences of existing values in the list with new values that match the condition.
- `List.ReplaceRange`: Replaces count number of values starting at position with the replacement values.
- `List.ReplaceValue`: Searches a list for the specified value and replaces it.
- `List.Reverse`: Reverses the order of values in the list.
- `List.Split`: Splits the specified list into a list of lists using the specified page size.
- `List.Transform`: Returns a new list of values computed from this list.
- `List.TransformMany`: Returns a list whose elements are transformed from the input list using specified functions.
- `List.Zip`: Returns a list of lists by combining items at the same position in multiple lists.
- `List.AllTrue`: Returns true if all expressions are true.
- `List.AnyTrue`: Returns true if any expression is true.
- `List.Contains`: Indicates whether the list contains the value.
- `List.ContainsAll`: Indicates where a list includes all the values in another list.
- `List.ContainsAny`: Indicates where a list includes any of the values in another list.
- `List.PositionOf`: Returns the offset(s) of a value in a list.
- `List.PositionOfAny`: Returns the first offset of a value in a list.
- `List.Difference`: Returns the difference of the two given lists.
- `List.Intersect`: Returns the intersection of the list values found in the input.
- `List.Union`: Returns the union of the list values found in the input.
- `List.Max`: Returns the maximum value or the default value for an empty list.
- `List.MaxN`: Returns the maximum value(s) in the list. The number of values to return or a filter condition must be specified.
- `List.Median`: Returns the median value in the list.
- `List.Min`: Returns the minimum value or the default value for an empty list.
- `List.MinN`: Returns the minimum value(s) in the list. The number of values to return or a filter condition may be specified.
- `List.Sort`: Sorts a list of data according to the criteria specified.
- `List.Percentile`: Returns one or more sample percentiles corresponding to the given probabilities.
- `List.Average`: Returns the average of the values. Works with number, date, datetime, datetimezone and duration values.
- `List.Mode`: Returns the most frequent value in the list.
- `List.Modes`: Returns a list of the most frequent values in the list.
- `List.StandardDeviation`: Returns a sample based estimate of the standard deviation. This function performs a sample based estimate. The resu
- `List.Sum`: Returns the sum of the items in the list.
- `List.Covariance`: Returns the covariance between the two lists of numbers.
- `List.Product`: Returns the product of the numbers in the list.
- `List.Dates`: Generates a list of date values given an initial value, count, and incremental duration value.
- `List.DateTimes`: Generates a list of datetime values given an initial value, count, and incremental duration value.
- `List.DateTimeZones`: Generates a list of datetimezone values given an initial value, count, and incremental duration value.
- `List.Durations`: Generates a list of duration values given an initial value, count, and incremental duration value.
- `List.Generate`: Generates a list of values.
- `List.Numbers`: Returns a list of numbers given an initial value, count, and optional increment value.
- `List.Random`: Returns a list of random numbers.
- `List.Times`: Generates a list of time values given an initial value, count, and incremental duration value.

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
