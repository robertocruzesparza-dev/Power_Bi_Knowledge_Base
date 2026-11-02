---
id: 15.tmdl_format
title: Tabular Model Definition Language (TMDL)
domain: devops_lifecycle
type: reference
level: advanced
tags: [tmdl, semantic-model, devops]
summary: TMDL syntax rules, folder structure, and serialization API for storing semantic models as readable, Git-friendly text files.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1805, S1803]
references: []
related: [15.pbip_format, 15.pbir_format, 15.git_integration]
---
## Purpose

TMDL describes a tabular semantic model in indented text, close to YAML. Each table, role, and culture lives in its own file, so Git diffs and merges stay small and readable.

## Key facts

- Fact: TMDL works at compatibility level 1200 and higher and exposes every Tabular Object Model (TOM) property [S1805].
- Fact: It applies to SQL Server Analysis Services 2016 and later, Azure Analysis Services, and Fabric or Power BI Premium [S1805].
- Fact: A semantic model in a PBIP uses the `definition` folder in TMDL form [S1803].

## Folder structure

One level of subfolders, each with `.tmdl` files [S1805]:

| Item | File location |
|---|---|
| Database, model | `database.tmdl`, `model.tmdl` |
| Relationships, expressions, data sources | One file each at the root |
| DAX user-defined functions | `functions.tmdl` |
| Each table (columns, measures, hierarchies, partitions inside) | `tables/<name>.tmdl` |
| Each role | `roles/<name>.tmdl` |
| Each perspective, each culture | `perspectives/`, `cultures/` |

## Syntax rules

- Objects are declared by type then name: `table Sales`, `column Quantity`, `measure 'Sales Amount'` [S1805].
- Wrap names in single quotes if they contain a dot, equals, colon, single quote, or space. Double a single quote to escape it [S1805].
- A colon sets a property value (`dataType: int64`). An equals sign starts an expression (`measure Total = SUM(...)`) [S1805].
- Boolean properties can be written as just the name, for example `isHidden` [S1805].
- Indentation is strict: one tab per level. Multi-line expressions sit one level deeper than the object's properties [S1805].
- Three backticks around an expression preserve its exact whitespace [S1805].
- Descriptions use `///` lines directly above the object [S1805].
- `ref table Sales` lines in `model.tmdl` keep collection order stable across round trips [S1805].
- Partial declarations are allowed: measures for many tables can live in one file. A duplicate declaration causes an error [S1805].
- Output uses camelCase. Reading is case insensitive [S1805].

## Example

```tmdl
table Sales
    measure 'Sales Amount' = SUMX('Sales', [Quantity] * [Net Price])
        formatString: $ #,##0

    column Quantity
        dataType: int64
        sourceColumn: Quantity
```

## Serialization API

The `TmdlSerializer` class in `Microsoft.AnalysisServices.Tabular` serializes a TOM database to a folder or string and back. A stream API also exists through `MetadataSerializationContext` [S1805].

## Common mistakes

- Mixing tabs and spaces. Parsing fails.
- Unquoted names with spaces.
- Editing automatic date tables in external tools. Microsoft advises against it [S1803].
- Removing synced objects from composite or Direct Lake models without the `changedProperties` and `PBI_RemovedChildren` markers. The next sync restores them [S1803].
- Applying expression edits when `unappliedChanges.json` exists. Those edits are lost [S1803].

## See also

- [PBIP format](15_pbip_format.md)
- [PBIR format](15_pbir_format.md)
- [Fabric Git integration](15_git_integration.md)
