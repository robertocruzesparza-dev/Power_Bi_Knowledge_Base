---
id: 04.power_query_editor
title: Power Query editor and the get data flow
domain: power_query_m
type: concept
level: beginner
tags: [power-query, desktop, data-source, m-language]
summary: What Power Query is, the editor's panes, the Applied steps list, and how the get data flow turns clicks into M code.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S322, S325, S330, S331]
references: []
related: [04.m_language_basics, 04.common_transformations, 04.query_folding, 03.data_sources_overview]
---

# Power Query editor and the get data flow

Purpose: orient a new user in Power Query and show how the visual editor and the M script relate.

## Key facts

- Power Query is the data preparation engine behind Power BI, Excel, dataflows and other Microsoft products. It connects to sources and transforms data into the shape you want (Fact, S331).
- Every query has an M script, whether the editor writes it, you type it in the Advanced Editor, or you start with a Blank Query (Fact, S322).
- In Power BI Desktop, open the editor with Home > Transform data (Fact, S331).

## Editor components (Fact, S331)

1. Ribbon: tabs with transforms and options.
2. Queries pane: all queries; supports groups and folders.
3. Current view: data preview by default; a diagram view can be shown beside it.
4. Query settings: query name and the Applied steps list.
5. Status bar: execution time, row and column counts, view buttons.

The schema view and diagram view exist only in Power Query Online (Fact, S331).

## How it works

The get data experience has four stages: choose a connector, enter connection settings and credentials, preview data in the Navigator, then transform or load. Each transform adds a named step in Applied steps. The step names become identifiers in the M script. A name with spaces is wrapped as `#"Kept top rows"` (Fact, S322).

You can view the script with View > Advanced Editor, or show it in the formula bar. Edits in the editor update the script automatically. Renaming a step renames it in the script.

## Example

Connect to SQL Server. Applied steps show Source (the connection), Navigation (pick the table), Removed other columns, Sorted rows, Kept top rows. Each is one line in the M script (Fact, S322).

## Data profiling tools (Fact, S325)

Column quality shows the share of valid, error and empty values. Column distribution shows value frequency. Column profile gives detailed statistics for one column. Turn them on in the View tab. Profiling can run over the whole data set, so it can reveal errors beyond the rows used for type detection (Fact, S329).

## Data types

Set the right type on every column. Type-specific filters and menus appear only when the type is set. Common types: Decimal number (64-bit float), Fixed decimal number (four decimal digits), Whole number (64-bit integer), Date/Time, Date, Time, Date/Time/Timezone and Duration (Fact, S330). Unstructured sources such as CSV get automatic type detection by default, which infers types from only the first 200 rows, so later values can truncate or error (Fact, S329).

## Common mistakes

- Typing the M for every step by hand when a ribbon command would create it.
- Leaving columns untyped, then wondering why date filters are missing.
- Editing a query in Advanced Editor in a way that the visual Applied steps can no longer show.

## See also

- [M language basics](04_m_language_basics.md)
- [Common transformations](04_common_transformations.md)
- [Performance and best practices](04_performance_best_practices.md)
