---
id: ref.m_functions_text_number
title: M functions: Text and Number
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Text and number M functions for parsing, cleaning, formatting, converting and math.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---

## Table of Contents

- [Text functions](#text-functions)
- [Number functions](#number-functions)
- [See also](#see-also)

# M functions: Text and Number

Purpose: a lookup list of M functions from the official function reference. 97 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Text functions

- `Text.InferNumberType`: Infers the granular number type (Int64.Type, Double.Type, and so on) of a number encoded in text.
- `Text.Length`: Returns the number of characters in a text value.
- `Character.FromNumber`: Converts a number to a text character.
- `Character.ToNumber`: Converts a character to a number value.
- `Guid.From`: Returns a GUID value from the given value.
- `Json.FromValue`: Produces a JSON representation of a given value.
- `Text.From`: Creates a text value from the given value.
- `Text.FromBinary`: Decodes data from a binary value in to a text value using an encoding.
- `Text.NewGuid`: Returns a GUID value as a text value.
- `Text.ToBinary`: Encodes a text value into binary value using an encoding.
- `Text.ToList`: Returns a list of characters from a text value.
- `Value.FromText`: Creates a strongly-typed value from a textual representation.
- `Text.At`: Returns a character starting at a zero-based offset.
- `Text.Middle`: Returns the substring up to a specific length.
- `Text.Range`: Returns a number of characters from a text value starting at a zero-based offset and for count number of characters
- `Text.Start`: Returns the count of characters from the start of a text value.
- `Text.End`: Returns the number of characters from the end of a text value.
- `Text.Insert`: Inserts one text value into another at a given position.
- `Text.Remove`: Removes all occurrences of the given character or list of characters from the input text value.
- `Text.RemoveRange`: Removes count characters at a zero-based offset from a text value.
- `Text.Replace`: Replaces all occurrences of a substring with a new text value.
- `Text.ReplaceRange`: Replaces length characters in a text value starting at a zero-based offset with the new text value.
- `Text.Select`: Selects all occurrences of the given character or list of characters from the input text value.
- `Text.Contains`: Returns true if a text value substring was found within a text value string; otherwise, false.
- `Text.EndsWith`: Returns a logical value indicating whether a text value substring was found at the end of a string.
- `Text.PositionOf`: Returns the first position of the value (-1 if not found).
- `Text.PositionOfAny`: Returns the first position in the text value of any listed character (-1 if not found).
- `Text.StartsWith`: Returns a logical value indicating whether a text value substring was found at the beginning of a string.
- `Text.AfterDelimiter`: Returns the portion of text after the specified delimiter.
- `Text.BeforeDelimiter`: Returns the portion of text before the specified delimiter.
- `Text.BetweenDelimiters`: Returns the portion of text between the specified startDelimiter and endDelimiter.
- `Text.Clean`: Returns the original text value with non-printable characters removed.
- `Text.Combine`: Returns a text value that is the result of joining all text values with each value separated by a separator.
- `Text.Lower`: Returns the lowercase of a text value.
- `Text.PadEnd`: Returns text of a specified length by padding the end of the given text.
- `Text.PadStart`: Returns text of a specified length by padding the start of the given text.
- `Text.Proper`: Returns a text value with first letters of all words converted to uppercase.
- `Text.Repeat`: Returns a text value composed of the input text value repeated a number of times.
- `Text.Reverse`: Reverses the provided text.
- `Text.Split`: Returns a list containing parts of a text value that are delimited by a separator text value.
- `Text.SplitAny`: Returns a list containing parts of a text value that are delimited by any separator text values.
- `Text.Trim`: Removes all the specified leading and trailing characters.
- `Text.TrimEnd`: Removes all specified trailing characters.
- `Text.TrimStart`: Removes all specified leading characters.
- `Text.Upper`: Returns the uppercase of a text value.

## Number functions

- `Number.IsEven`: Returns true if a value is an even number.
- `Number.IsNaN`: Returns true if a value is Number.NaN.
- `Number.IsOdd`: Returns true if a value is an odd number.
- `Byte.From`: Returns an 8-bit integer number value from the given value.
- `Currency.From`: Returns a currency value from the given value.
- `Decimal.From`: Returns a decimal number value from the given value.
- `Double.From`: Returns a Double number value from the given value.
- `Int8.From`: Returns a signed 8-bit integer number value from the given value.
- `Int16.From`: Returns a 16-bit integer number value from the given value.
- `Int32.From`: Returns a 32-bit integer number value from the given value.
- `Int64.From`: Returns a 64-bit integer number value from the given value.
- `Number.From`: Returns a number value from a value.
- `Number.FromText`: Returns a number value from a text value.
- `Number.ToText`: Converts the given number to text.
- `Percentage.From`: Returns a percentage value from the given value.
- `Single.From`: Returns a Single number value from the given value.
- `Number.Round`: Returns a nullable number (n) if value is an integer.
- `Number.RoundAwayFromZero`: Returns Number.RoundUp(value) when value >= 0 and Number.RoundDown(value) when value < 0.
- `Number.RoundDown`: Returns the largest integer less than or equal to a number value.
- `Number.RoundTowardZero`: Returns Number.RoundDown(x) when x >= 0 and Number.RoundUp(x) when x < 0.
- `Number.RoundUp`: Returns the larger integer greater than or equal to a number value.
- `Number.Abs`: Returns the absolute value of a number.
- `Number.Combinations`: Returns the number of combinations of a given number of items for the optional combination size.
- `Number.Exp`: Returns a number representing e raised to a power.
- `Number.Factorial`: Returns the factorial of a number.
- `Number.IntegerDivide`: Divides two numbers and returns the whole part of the resulting number.
- `Number.Ln`: Returns the natural logarithm of a number.
- `Number.Log`: Returns the logarithm of a number to the base.
- `Number.Log10`: Returns the base-10 logarithm of a number.
- `Number.Mod`: Divides two numbers and returns the remainder of the resulting number.
- `Number.Permutations`: Returns the number of total permutations of a given number of items for the optional permutation size.
- `Number.Power`: Returns a number raised by a power.
- `Number.Sign`: Returns 1 for positive numbers, -1 for negative numbers, or 0 for zero.
- `Number.Sqrt`: Returns the square root of a number.
- `Number.Random`: Returns a random fractional number between 0 and 1.
- `Number.RandomBetween`: Returns a random number between the two given number values.
- `Number.Acos`: Returns the arccosine of a number.
- `Number.Asin`: Returns the arcsine of a number.
- `Number.Atan`: Returns the arctangent of a number.
- `Number.Atan2`: Returns the arctangent of the division of two numbers.
- `Number.Cos`: Returns the cosine of a number.
- `Number.Cosh`: Returns the hyperbolic cosine of a number.
- `Number.Sin`: Returns the sine of a number.
- `Number.Sinh`: Returns the hyperbolic sine of a number.
- `Number.Tan`: Returns the tangent of a number.
- `Number.Tanh`: Returns the hyperbolic tangent of a number.
- `Number.BitwiseAnd`: Returns the result of a bitwise AND operation on the provided operands.
- `Number.BitwiseNot`: Returns the result of a bitwise NOT operation on the provided operands.
- `Number.BitwiseOr`: Returns the result of a bitwise OR operation on the provided operands.
- `Number.BitwiseShiftLeft`: Returns the result of a bitwise shift left operation on the operands.
- `Number.BitwiseShiftRight`: Returns the result of a bitwise shift right operation on the operands.
- `Number.BitwiseXor`: Returns the result of a bitwise XOR operation on the provided operands.

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
