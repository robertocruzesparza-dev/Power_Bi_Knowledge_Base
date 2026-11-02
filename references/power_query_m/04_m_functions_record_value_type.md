---
id: ref.m_functions_record_value_type
title: M functions: Record, Value, Type
domain: power_query_m
type: reference
level: intermediate
tags: [power-query, m-language, reference, catalog]
summary: Record, value and type M functions, plus geography helpers, for structured values and metadata.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S332, S333]
references: []
related: [04.m_function_categories]
---

## Table of Contents

- [Record and geography functions](#record-and-geography-functions)
- [Value functions](#value-functions)
- [Type functions](#type-functions)
- [See also](#see-also)

# M functions: Record, Value, Type

Purpose: a lookup list of M functions from the official function reference. 71 functions are listed. Descriptions are shortened paraphrases. Functions the source marks as internal-only are omitted. Availability can differ by host (Power BI Desktop, Power Query Online, Excel).

## Record and geography functions

- `Record.FieldCount`: Returns the number of fields in a record.
- `Record.HasFields`: Returns true if the field name or field names are present in a record.
- `Geography.FromWellKnownText`: Translates text representing a geographic value in Well-Known Text (WKT) format into a structured record.
- `Geography.ToWellKnownText`: Translates a structured geographic point value into its Well-Known Text (WKT) representation.
- `GeographyPoint.From`: Creates a record representing a geographic point from parts.
- `Geometry.FromWellKnownText`: Translates text representing a geometric value in Well-Known Text (WKT) format into a structured record.
- `Geometry.ToWellKnownText`: Translates a structured geometric point value into its Well-Known Text (WKT) representation.
- `GeometryPoint.From`: Creates a record representing a geometric point from parts.
- `Record.AddField`: Adds a field from a field name and value.
- `Record.Combine`: Combines the records in a list.
- `Record.RemoveFields`: Removes the specified field(s) from the input record.
- `Record.RenameFields`: Returns a new record that renames the fields specified. The resultant fields will retain their original order. This
- `Record.ReorderFields`: Reorders record fields to match the order of a list of field names.
- `Record.TransformFields`: Transforms fields by applying transformOperations. For more more information about values supported by transformOpe
- `Record.Field`: Returns the value of the given field. This function can be used to dynamically create field lookup syntax for a giv
- `Record.FieldNames`: Returns a list of field names in order of the record's fields.
- `Record.FieldOrDefault`: Returns the value of a field from a record, or the default value if the field does not exist.
- `Record.FieldValues`: Returns a list of field values in order of the record's fields.
- `Record.SelectFields`: Returns a new record that contains the fields selected from the input record. The original order of the fields is m
- `Record.FromList`: Returns a record given a list of field values and a set of fields.
- `Record.FromTable`: Returns a record from a table of records containing field names and values.
- `Record.ToList`: Returns a list of values containing the field values of the input record.
- `Record.ToTable`: Returns a table of records containing field names and values from an input record.

## Value functions

- `Value.Alternates`: Expresses alternate query plans.
- `Value.Compare`: Returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.
- `Value.Equals`: Returns whether two values are equal.
- `Value.Expression`: Returns an abstract syntax tree (AST) that represents the value's expression.
- `Value.VersionIdentity`: Returns the version identity of a value.
- `Value.Versions`: Returns a navigation table containing the available versions of a value.
- `Value.NativeQuery`: Evaluates a query against a target.
- `Value.NullableEquals`: Returns a logical value or null based on two values.
- `Value.Optimize`: If value represents a query that can be optimized, returns the optimized query. Otherwise returns value.
- `Value.Type`: Returns the type of the given value.
- `Value.Add`: Returns the sum of the two values.
- `Value.Divide`: Returns the result of dividing the first value by the second.
- `Value.Multiply`: Returns the product of the two values.
- `Value.Subtract`: Returns the difference of the two values.
- `Value.As`: Returns the value if it is compatible with the specified type.
- `Value.Is`: Determines whether a value is compatible with the specified type.
- `Value.ReplaceType`: Replaces the value's type.
- `Embedded.Value`: Accesses a value by name in an embedded mashup.
- `Module.Versions`: Returns a record of module versions for the current module and its dependencies.
- `Variable.Value`: Returns the value of the specified variable.
- `Variable.ValueOrDefault`: Returns the value of the specified variable or the default value if the variable is not defined.
- `Value.Metadata`: Returns a record containing the input's metadata.
- `Value.RemoveMetadata`: Removes the metadata on the value and returns the original value.
- `Value.ReplaceMetadata`: Replaces the metadata on a value with the new metadata record provided and returns the original value with the new 

## Type functions

- `Type.AddTableKey`: Add a key to a table type.
- `Type.ClosedRecord`: The given type must be a record type returns a closed version of the given record type (or the same type, if it is 
- `Type.Facets`: Returns the facets of a type.
- `Type.ForFunction`: Returns a type that represents functions with specific parameter and return type constraints.
- `Type.ForRecord`: Returns a Record type from a fields record.
- `Type.FunctionParameters`: Returns a record with field values set to the name of the parameters of a function type, and their values set to th
- `Type.FunctionRequiredParameters`: Returns a number indicating the minimum number of parameters required to invoke the a type of function.
- `Type.FunctionReturn`: Returns a type returned by a function type.
- `Type.Is`: Determines if a value of the first type is always compatible with the second type.
- `Type.IsNullable`: Returns true if a type is a nullable type; otherwise, false.
- `Type.IsOpenRecord`: Returns whether a record type is open.
- `Type.ListItem`: Returns an item type from a list type.
- `Type.NonNullable`: Returns the non nullable type from a type.
- `Type.OpenRecord`: Returns an opened version of a record type, or the same type, if it is already open.
- `Type.RecordFields`: Returns a record describing the fields of a record type with each field of the returned record type having a corres
- `Type.ReplaceFacets`: Replaces the facets of a type.
- `Type.ReplaceTableKeys`: Replaces the keys in a table type.
- `Type.ReplaceTablePartitionKey`: Returns a new table type with the partition key replaced by the specified partition key.
- `Type.TableColumn`: Returns the type of a column in a table.
- `Type.TableKeys`: Returns keys from a table type.
- `Type.TablePartitionKey`: Returns the partition key for the given table type if it has one.
- `Type.TableRow`: Returns a row type from a table type.
- `Type.TableSchema`: Returns a table containing a description of the columns (i.e. the schema) of the specified table type.
- `Type.Union`: Returns the union of a list of types.

## See also

- [M function categories overview](../../04_power_query_m/04_m_function_categories.md)
- [Official M function reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
