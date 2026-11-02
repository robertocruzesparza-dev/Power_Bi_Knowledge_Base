---
id: 22.deprecations_retirements
title: Deprecations and retirements, 2024 to 2026
domain: release_roadmap
type: reference
level: intermediate
tags: [release, roadmap, limits, power-bi]
summary: Dated list of announced Power BI deprecations and retirements found in monthly notes from October 2024 to October 2026, with the action each needs.
status: mixed
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S304, S335, S336, S340, S2518, S2520, S2521, S2547, S2548, S2545, S2810, S2820, S3016, S3017, S3022, S3024]
references: []
related: [03.connector_lifecycle_changes, 22.release_history_2026, 22.release_cadence_and_tracking]
---

# Deprecations and retirements, 2024 to 2026

Purpose: list what is going away, with dates, so you can plan. Dates are as written in the monthly notes on 2026-10-07 and rechecked on 2026-11-02; confirm in the linked month before acting. The October 2026 monthly notes list no new deprecations (S3016).

## Upcoming or recent (as of 2026-11-02)

| Item | What changes | Date | Announced |
|---|---|---|---|
| Power BI Q&A | Legacy natural language tool retired; use Copilot. Jan 2026 notes said December 2026; the Learn Q&A page (updated 2026-09-10) says February 2027 (S2820; the change from December is not officially explained) | Feb 2027 per Learn (every Learn Q&A article still says this on 2026-11-02, S3022) | Jan 2026 |
| Snowflake username and password sign-in | Connector page says it will be deprecated; use Microsoft Entra ID or key pair. The connector is also moving from the ODBC to the ADBC driver | No date stated | Connector page, 2026-09-25 (S2810) |
| SCOM management packs for SSRS, Power BI Report Server and SSAS | No longer supported | After January 2027 | Feb 2026 |
| Office Online Server (OOS) Excel hosting in Power BI Report Server | Report Server removed OOS configuration support in the January 2026 release; OOS Excel hosting ends Nov 2026; OOS itself retires Dec 31, 2026 (S3024) | Nov to Dec 2026 | Learn Report Server page |

## Already effective

| Item | What changed | Date | Announced |
|---|---|---|---|
| Old Desktop file picker (Desktop March 2026 and older) | Cannot save or share to OneDrive and SharePoint; update Desktop. Took effect per Microsoft's notice; the October 2026 notes no longer list it as upcoming | October 2026 | Mar 2026, repeated Jul to Sep 2026 |
| Simba Vertica ODBC driver | Deprecation began; install the Vertica driver | Feb 2026 | Feb 2026 |
| Scorecard hierarchies and Heatmap view | Removed | April 15, 2026 | Feb 2026 |
| Legacy Import Excel and CSV in service | Entry points removed May 31, 2026; old models stop refreshing July 31, 2026 and stop loading August 31, 2026 | 2026 | Feb 2026 |
| SSRS SharePoint Report Viewer web part | Technical support ends | April 13, 2026 | Jan 2026 |
| Old Desktop file picker toggle | Removed in the SU04 release | April 2026 | Mar 2026 |
| Built-in Netezza ODBC driver | Deprecated; install IBM Netezza driver | April 2026 | Mar and Apr 2026 |
| QuickBooks Online connector | Retired; no new connections | After March 2026 | Mar 2026 |
| R and Python visuals in Embed for your customers | Deprecation announced | See Nov 2025 notes | Nov 2025 |
| Bing Maps | Bing Maps visual icon removed from default visuals from October 2025; paginated report maps move to Azure Maps in two phases | Oct 2025 onward | Sep and Oct 2025 |
| 32-bit Power BI Desktop | Scheduled for deprecation | August 2025 | May 2025 |
| QuickBooks Online (beta) connector | Deprecation planned | 2025 | Jun 2025 |
| Windows 7 for Desktop | Not supported; Windows 8 or newer, latest release only | Listed from 2024 | Notes through Apr 2025 |
| Teams activity analytics | Retirement announced | Oct 2024 | Oct 2024 |
| Government cloud sources with org account in non-government environments | Stopped | After March 31, 2024 | 2024 |

All rows: Fact from S301, S335 or S336 unless the date says otherwise.

## Other Microsoft lifecycle context

Microsoft's "Ending Support in 2026" page lists product retirements such as Office 2021 apps on October 13, 2026. It did not list Power BI Desktop items when read (Fact, S340). It is a separate source from the monthly notes.

## How to act

1. For each item, name the affected reports or datasets in your tenant.
2. Set a work date at least one release before the effective date.
3. Test replacements in a copy.
4. Re-check the dated source before you finish, because Microsoft sometimes moves dates.

## Common mistakes

- Reading "deprecated" as "gone". Many items keep working for months.
- Missing items buried in the General or Data connectivity sections of a monthly note.

## See also

- [Connector changes](../03_data_sources/03_connector_lifecycle_changes.md)
- [Release cadence and how to track change](22_release_cadence_and_tracking.md)
