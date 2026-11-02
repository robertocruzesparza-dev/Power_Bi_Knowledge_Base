---
id: 18.dax_studio
title: DAX Studio
domain: ecosystem_tools
type: concept
level: intermediate
tags: [dax-studio, dax, performance, ecosystem]
summary: What DAX Studio does for writing and tuning DAX queries, its main features, and where details remain unverified.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: low
sources: [S2114, S2135, S2136, S2826]
references: []
related: [18.external_tools_overview, 18.tabular_editor]
---

# DAX Studio

## Purpose
DAX Studio is a free community tool to write, run and analyze DAX queries against Power BI Desktop, Analysis Services Tabular and Power Pivot [S2114, S2135]. Example: run a slow measure, then read Server Timings to see whether the formula engine or storage engine dominates.

## Key facts
- Fact: Microsoft lists it as an open-source semantic modeling tool with object browsing, integrated tracing, query execution breakdown, DAX formatting and highlighting [S2114].
- Fact (community and project blog, S2136): Server Timings split time into formula engine (single threaded) and storage engine; a Query Plan pane shows logical and physical plans.
- Fact (S2136): All Queries trace captures queries from a connected model without SQL Server Profiler. Version 3.1.0 added filters (for example only queries slower than 100 ms) and Capture Diagnostics, which grabs timings, plan and model metrics in one click.
- Fact (S2136): View Metrics exposes VertiPaq Analyzer data: structure sizes and column cardinality.
- Fact: it registers itself in the External Tools ribbon on install [S2114].

## Steps (typical tuning loop)
1. Connect to the open Desktop model from the ribbon.
2. Paste the query copied from Performance Analyzer.
3. Enable Server Timings and Query Plan, run with a cleared cache.
4. Compare formula and storage engine time. Rewrite, rerun, compare.

## Unverified
- Latest release: the GitHub releases page marks v3.6.1 as Latest, dated 04 Sep (the page shows no year, so 2026 is an assumption). Pre-releases v3.7.0.1252 and v3.7.0.1253 were listed above it [S2826].
- License text and minimum requirements: the project documentation pages were only partly readable. Check daxstudio.org (License and Requirements pages) [S2135].
- Ribbon placement of controls differs between guides; check your version [S2136].

## See also
- [External tools overview](18_external_tools_overview.md)
- [Tabular Editor](18_tabular_editor.md)
