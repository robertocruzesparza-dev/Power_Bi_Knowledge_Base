---
id: 05.incremental_refresh_basics
title: Incremental refresh basics
domain: data_modeling
type: how-to
level: intermediate
tags: [incremental-refresh, refresh, query-folding, semantic-model]
summary: Explains how incremental refresh partitions a table, the RangeStart and RangeEnd parameters, policy settings, real-time hybrid tables, and common pitfalls.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S618, S619, S620, S621, S2542, S2543]
references: []
related: [05.storage_modes, 05.aggregations]
---

## Table of Contents

- [Purpose](#purpose)
- [Key facts](#key-facts)
- [How it works](#how-it-works)
- [Steps](#steps)
- [Policy settings](#policy-settings)
- [Real-time data](#real-time-data)
- [Common mistakes](#common-mistakes)
- [Limits and version notes](#limits-and-version-notes)

# Incremental refresh basics

## Purpose
Incremental refresh refreshes only recent partitions of a large table and keeps older data untouched. It cuts refresh time and source load.

## Key facts
- Fact: You configure it in Desktop, but partitions are created and managed only after you publish and refresh once in the service (S618, S619).
- Fact: Two Power Query parameters with the reserved, case-sensitive names RangeStart and RangeEnd, type date/time, drive it (S618).
- Fact: The table must filter a date/time column by those parameters. The toggle stays off until that filter exists (S619).
- Fact: The service overrides the parameter values per partition (S618).
- Fact: Partitions are not visible or editable in Desktop or the service UI. With a Premium or Fabric capacity they can be managed through the XMLA endpoint (S620).

## How it works
On first refresh the service builds refresh partitions and historical partitions. Each later refresh reloads only rows in the refresh period. Periods roll forward: a refresh partition becomes historical, older historical partitions merge into coarser ones, and partitions beyond the archive period are dropped. This is the rolling window pattern (S618).

## Steps
1. In Power Query, create RangeStart and RangeEnd (Date/Time) with a small window, for example two days (S618).
2. Filter the date column manually in the formula bar (not the Custom Filter dialog). Use greater-than-or-equal on RangeStart and less-than on RangeEnd, so no row lands in two partitions (S619).
3. Right-click the table in Table view, choose Incremental refresh, turn it on (S619).
4. Set Archive data starting and Incrementally refresh data starting.
5. Publish and refresh in the service.
Example filter for an integer date key (S619):

```
Table.SelectRows(Source, each [OrderDateKey] >= Int32.From(DateTime.ToText(RangeStart,[Format="yyyyMMdd"])))
```

## Policy settings (S619)
| Setting | Effect |
|---|---|
| Archive data starting | How far back history is kept |
| Incrementally refresh data starting | Recent window reloaded each refresh |
| Only refresh complete days | Skips partial days; forced on when real-time is on |
| Detect data changes | Refresh a period only if a max date/time column changed; use a different column than the partition column; it is held in memory |

The service runs refresh in UTC unless a time zone is set under Refresh, which shifts which days count as complete (S619).

## Real-time data
- Fact: The option "Get the latest data in real time with DirectQuery" adds a DirectQuery partition for rows after the refresh period. This is a hybrid table, and it needs Premium (S618, S619).
- Fact: Tables related to a hybrid table should be Dual to avoid slow queries (S620).
- Fact: Non-folding steps cannot be used with the real-time option (S619).
- Fact: Compatibility levels: Import policy 1550, Hybrid policy 1565 for XMLA-created policies (S620).

## Common mistakes
- Query folding breaks, so the filter runs after loading all rows. A native query can still work if it embeds the parameters in the SQL (S619). Verify with query diagnostics or a source trace (S621).
- Republishing from Desktop wipes partitions and data. Use ALM Toolkit or TMSL for metadata-only changes on Premium (S618).
- Expecting to download the service model back to a .pbix (S618).
- Using a date column whose value changes after load, so rows move between partitions.

## Limits and version notes
Fact: Real-time DirectQuery partitions are Premium-only (S618). Confirm current licensing in the licensing domain.
