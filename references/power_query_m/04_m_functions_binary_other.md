---
id: ref.m_functions_binary_other
title: M functions: Binary, Combiner, Splitter, Uri, Lines, Comparer
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Binary, combiner, splitter, URI, lines and comparer M functions for files, splitting and combining text.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---

## Table of Contents

- [Binary functions](#binary-functions)
- [Combiner functions](#combiner-functions)
- [Splitter functions](#splitter-functions)
- [Uri functions](#uri-functions)
- [Lines functions](#lines-functions)
- [Comparer functions](#comparer-functions)
- [See also](#see-also)

# M functions: Binary, Combiner, Splitter, Uri, Lines, Comparer

Purpose: a lookup list of M functions from the official function reference. 67 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Binary functions

- `BinaryFormat.7BitEncodedSignedInteger`: A binary format that reads a 64-bit signed integer that was encoded using a 7-bit variable-length encoding.
- `BinaryFormat.7BitEncodedUnsignedInteger`: A binary format that reads a 64-bit unsigned integer that was encoded using a 7-bit variable-length encoding.
- `BinaryFormat.Binary`: Returns a binary format that reads a binary value.
- `BinaryFormat.Byte`: A binary format that reads an 8-bit unsigned integer.
- `BinaryFormat.Choice`: Returns a binary format that chooses the next binary format based on a value that has already been read.
- `BinaryFormat.Decimal`: A binary format that reads a .NET 16-byte decimal value.
- `BinaryFormat.Double`: A binary format that reads an 8-byte IEEE double-precision floating point value.
- `BinaryFormat.Group`: Returns a binary format that reads a group of items. Each item value is preceded by a unique key value. The result 
- `BinaryFormat.Length`: Returns a binary format that limits the amount of data that can be read. Both BinaryFormat.List and BinaryFormat.Bi
- `BinaryFormat.List`: Returns a binary format that reads a sequence of items and returns a list.
- `BinaryFormat.Null`: A binary format that reads zero bytes and returns null.
- `BinaryFormat.Record`: Returns a binary format that reads a record. Each field in the record can have a different binary format.
- `BinaryFormat.SignedInteger16`: A binary format that reads a 16-bit signed integer.
- `BinaryFormat.SignedInteger32`: A binary format that reads a 32-bit signed integer.
- `BinaryFormat.SignedInteger64`: A binary format that reads a 64-bit signed integer.
- `BinaryFormat.Single`: A binary format that reads a 4-byte IEEE single-precision floating point value.
- `BinaryFormat.Text`: Returns a binary format that reads a text value. The optional encoding value specifies the encoding of the text.
- `BinaryFormat.Transform`: Returns a binary format that will transform the values read by another binary format.
- `BinaryFormat.UnsignedInteger16`: A binary format that reads a 16-bit unsigned integer.
- `BinaryFormat.UnsignedInteger32`: A binary format that reads a 32-bit unsigned integer.
- `BinaryFormat.UnsignedInteger64`: A binary format that reads a 64-bit unsigned integer.
- `BinaryFormat.ByteOrder`: Returns a binary format with the byte order specified by a function.
- `Table.PartitionValues`: Returns information about how a table is partitioned.
- `Binary.ApproximateLength`: Returns the approximate length of the binary.
- `Binary.Buffer`: Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a de
- `Binary.Combine`: Combines a list of binaries into a single binary.
- `Binary.Compress`: Compresses a binary value using the given compression type.
- `Binary.Decompress`: Decompresses a binary value using the given compression type.
- `Binary.From`: Returns a binary value from the given value.
- `Binary.FromList`: Converts a list of numbers into a binary value
- `Binary.FromText`: Decodes data from a text form into binary.
- `Binary.InferContentType`: Returns a record with field Content.Type that contains the inferred MIME-type.
- `Binary.Length`: Returns the length of binary values.
- `Binary.Range`: Returns a subset of the binary value beginning at an offset.
- `Binary.Split`: Splits the specified binary into a list of binaries using the specified page size.
- `Binary.ToList`: Converts a binary value into a list of numbers
- `Binary.ToText`: Encodes binary data into a text form.
- `Binary.View`: Creates or extends a binary with user-defined handlers for query and action operations.
- `Binary.ViewError`: Creates a modified error record which won't trigger a fallback when raised by a handler defined on a view (via Bina
- `Binary.ViewFunction`: Creates a function that can be intercepted by a handler defined on a view (via Binary.View).

## Combiner functions

- `Combiner.CombineTextByDelimiter`: Returns a function that combines a list of text using the specified delimiter.
- `Combiner.CombineTextByEachDelimiter`: Returns a function that combines a list of text using a sequence of delimiters.
- `Combiner.CombineTextByLengths`: Returns a function that combines a list of text using the specified lengths.
- `Combiner.CombineTextByPositions`: Returns a function that combines a list of text using the specified output positions.
- `Combiner.CombineTextByRanges`: Returns a function that combines a list of text using the specified positions and lengths.

## Splitter functions

- `Splitter.SplitByNothing`: Returns a function that does no splitting, returning its argument as a single element list.
- `Splitter.SplitTextByCharacterTransition`: Returns a function that splits text into a list of text according to a transition from one kind of character to ano
- `Splitter.SplitTextByAnyDelimiter`: Returns a function that splits text by any supported delimiter.
- `Splitter.SplitTextByDelimiter`: Returns a function that will split text according to a delimiter.
- `Splitter.SplitTextByEachDelimiter`: Returns a function that splits text by each delimiter in turn.
- `Splitter.SplitTextByLengths`: Returns a function that splits text according to the specified lengths.
- `Splitter.SplitTextByPositions`: Returns a function that splits text according to the specified positions.
- `Splitter.SplitTextByRanges`: Returns a function that splits text according to the specified ranges.
- `Splitter.SplitTextByRepeatedLengths`: Returns a function that splits text into a list of text after the specified length repeatedly.
- `Splitter.SplitTextByWhitespace`: Returns a function that splits text according to whitespace.

## Uri functions

- `Uri.BuildQueryString`: Assemble a record into a URI query string.
- `Uri.Combine`: Returns a Uri based on the combination of the base and relative parts.
- `Uri.EscapeDataString`: Encodes special characters in accordance with RFC 3986.
- `Uri.Parts`: Returns a record value with the fields set to the parts of a Uri text value.

## Lines functions

- `Lines.FromBinary`: Converts a binary value to a list of text values split at lines breaks.
- `Lines.FromText`: Converts a text value to a list of text values split at lines breaks.
- `Lines.ToBinary`: Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified lineSepara
- `Lines.ToText`: Converts a list of text into a single text. The specified lineSeparator is appended to each line. If not specified 

## Comparer functions

- `Comparer.Equals`: Returns a logical value based on the equality check over the two given values.
- `Comparer.FromCulture`: Returns a comparer function based on the specified culture and case-sensitivity.
- `Comparer.Ordinal`: Returns a comparer function which uses Ordinal rules to compare values.
- `Comparer.OrdinalIgnoreCase`: Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values.

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
