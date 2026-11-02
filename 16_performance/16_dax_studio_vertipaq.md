---
id: 16.dax_studio_vertipaq
title: DAX Studio and VertiPaq Analyzer
domain: performance
type: how-to
level: advanced
tags: [performance, dax-studio, optimization, ecosystem]
summary: How to use DAX Studio Server Timings to split query time between formula engine and storage engine, and View Metrics to find memory-heavy columns.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S676, S677, S681, S670]
references: []
related: [16.performance_analyzer, 16.model_size_reduction, 06.best_practices]
---

# DAX Studio and VertiPaq Analyzer

## Purpose
DAX Studio is a free, community tool that runs DAX queries and traces them. Its Server Timings feature explains why a query is slow. Its View Metrics feature (the VertiPaq Analyzer view) explains why a model is big.

## Key facts
- Fact: Microsoft lists DAX Studio among tools that can create and run DAX queries (S681).
- Fact: You need sufficient rights. View Metrics needs full rights in Desktop, Contributor on Premium XMLA endpoints, or Database Admin on Analysis Services (S676). Server Timings needs server admin rights, or its buttons are disabled (S677).
- Inference: For models in a Fabric or Premium workspace, XMLA endpoint access must be enabled for read.

## Server Timings (S677)
| Metric | Meaning |
|---|---|
| Total | Full server-side duration of the query |
| Formula Engine (FE) | Total minus storage engine time; single-threaded; builds requests and serializes results |
| Storage Engine (SE) | Sum of SE query durations; multi-threaded; scans compressed column data |
| SE CPU | Total CPU from SE events; rough; the ratio hints at parallelism |
| SE Queries | Number of storage engine requests |
| SE Cache | Cache hits |
xmSQL is a readable form of SE requests, not executable. For DirectQuery it shows generic T-SQL. XMLA endpoints can add ExecutionMetrics such as rows processed, throttling delay, memory, and CPU (S677).

## Reading timings
1. Copy a slow visual query from [Performance Analyzer](16_performance_analyzer.md) into DAX Studio.
2. Enable Server Timings, clear the cache, run.
3. High FE share: the formula is doing heavy work in one thread. Look at iterators, nested measure calls, and large intermediate tables.
4. High SE share: scans are the cost. The docs say a larger SE share is generally the tuning goal because SE runs in parallel (S677). Then reduce columns scanned, cardinality, or table size.
5. Many small SE queries: review the DAX pattern or model (S677). SQLBI shows that separate filter contexts on one column can cause sequential requests (S661).
6. Re-run to compare warm cache results.

## View Metrics (S676)
Tabs: Table Metrics (default; expand a table to see columns, biggest first), Column Metrics (flat list), Relationships, Partitions, Summary (total model memory, compatibility mode, last processed).
Options (defaults): read statistics from data on; DirectQuery scan off; Direct Lake scan mode ResidentOnly; column batch size 50.
The sizes are in-memory sizes, larger than the compressed on-disk size (S676).

How to use the output (inference, consistent with S671): sort columns by size, look for high-cardinality text or datetime columns, unused columns, and large dictionaries; then remove, split, or round them. See [model size reduction](16_model_size_reduction.md).

## Common mistakes
- Timing with a warm cache and drawing wrong conclusions.
- Running View Metrics on a Direct Lake model without noticing that scan mode controls what is read.
- Treating SE CPU as exact.

## See also
- [Model size reduction](16_model_size_reduction.md)
- [DAX best practices](../06_dax/06_best_practices.md)
