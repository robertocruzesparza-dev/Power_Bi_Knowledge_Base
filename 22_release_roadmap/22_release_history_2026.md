---
id: 22.release_history_2026
title: Monthly release history, 2026
domain: release_roadmap
type: reference
level: beginner
tags: [release, power-bi, desktop, service]
summary: Power BI Desktop and service highlights for January through October 2026, with version numbers.
status: mixed
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S335, S336, S339, S2556, S2801, S2802, S2803, S2832, S2843, S2845, S3016, S3017, S3018]
references: []
related: [22.release_history_2024_2025, 22.deprecations_retirements, 22.release_cadence_and_tracking]
---

# Monthly release history, 2026

Purpose: recent changes in one place. Read on 2026-10-07 from Microsoft's What's new and archive pages. Preview and GA words are as stated by Microsoft in that month.

## Table

| Month | Desktop version | Highlights |
|---|---|---|
| Jan 2026 | not stated | Q&A deprecation announced for December 2026, SSRS SharePoint web part support ends April 13, 2026, modern visual tooltips GA, markers in Azure Maps, Copilot report and model attachments in chat, setting renamed to Approved for Copilot |
| Feb 2026 | 2.151.1052.0 | Input slicer GA, paste selections into slicers, scorecard hierarchies removal announced, legacy Excel and CSV import in the service deprecated, Simba Vertica driver deprecation begins, Copilot prompt limit raised from 500 to 10,000 characters |
| Mar 2026 | 2.152.882.0 | Translytical task flows GA, Direct Lake on OneLake GA, modern visual defaults (preview), custom totals (preview), TMDL view in web modeling (preview), DAX user-defined functions (preview), IBM Netezza ODBC driver GA, QuickBooks Online connector retirement |
| Apr 2026 | 2.153.910.0 | Old file picker removed, built-in Netezza driver deprecated, Copilot chat in mobile reports, Direct Lake calculated columns (preview), fixed-size layout for card and slicer visuals |
| May 2026 | 2.154.1260 | Visual calculations and custom totals GA, Copilot summary shortcuts, new Get Data experience in Desktop (preview), set as landing page GA, subscriptions for org app reports |
| Jun 2026 | 2.155.756.0 | Fabric Apps for semantic models (preview), Copilot in web modeling (preview), shape map GA, date picker for slicers (preview), DAX user-defined functions with optional parameters, PBIR default-on rollout update, Power BI Desktop Bridge (preview) |
| Jul 2026 | 2.156.951.0 | Org apps with audiences GA, bookmarks and storytelling in org apps, CRUD APIs for org apps and paginated reports, TMDL view on the web, downloading .pbix from a model now gives an empty report with the dataset, data privacy firewall partitions setting |
| Aug 2026 | not stated | Modern visual defaults and Theme pane GA, date picker slicer GA, donut center value GA, matrix expand and collapse for column headers GA, OneLake file URLs in visuals GA, Refresh schema/data/sync options, Fabric Apps need only Read permission on the model, Direct Lake calculated columns (preview) |
| Sep 2026 | 2.158.1304.0 | Agentic authoring, Microsoft 365 Copilot integration, new report formatting controls, semantic model search capabilities, new Power Query editor; old file picker deprecation notice repeated. Build per Download Center (published 2026-10-07) |
| Oct 2026 | 2.159.883.0 | Gantt chart (preview), list slicer dropdown option (preview), custom visual authoring with the Power BI Report skill GA, plot area background color GA, auto-expand hierarchy axis with field parameters GA, personal bookmarks keep column widths GA, continuous capacity usage reporting for surge protection, mobile page indicator, artifact info header for Teams tabs. Build published 2026-10-15 |

All rows: Fact from S335 and S336, selective and paraphrased.

## September 2026

As of 2026-11-02 the Learn archive carries an official September 2026 section: agentic authoring, Microsoft 365 Copilot integration, new report formatting controls, semantic model search capabilities and a new Power Query editor, plus the repeated old file picker notice (Fact, S3017). This replaces the 2026-10-09 finding that no official September summary existed (S2801, S2843). One Message Center mirror item (community mirror, not official) says Power BI reports as references in Copilot Notebooks enters public preview in late September 2026 and general availability in late October 2026 (S339). The October 2026 What's new page does not mention it, so treat it as unverified (S3016).

## October 2026

The Learn What's new page now shows the October 2026 update as current (Fact, S3016). Desktop 2.159.883.0 was published to the Download Center on 2026-10-15 (Fact, S3018). The October notes list no new deprecations or retirements (Fact, S3016).

## Fabric and DAX items found for September 2026

- The Fabric What's new page lists September 2026 items and links to a Fabric September 2026 Feature Summary post (Fact, S2803, S2845). Examples marked generally available: Fabric IQ in Microsoft 365 Copilot, SQL change data capture custom capture names, Copy job workspace monitoring, custom Copy job staging, Snowflake read-only change data capture (Fact, S2803).
- Two DAX functions are listed as new in September 2026: TEXTCONTAINS and TEXTSIMILARITY (Fact, S2832).
- The Snowflake connector page (updated 2026-09-25) says username and password sign-in will be deprecated and the connector is moving from ODBC to the ADBC driver (Fact, S2810).

## Recurring items in this period

- The old Desktop file picker was removed in April 2026. From October 2026, Desktop versions from March 2026 or earlier cannot save or share to OneDrive and SharePoint; update Desktop (Fact, S335).
- The "Allow data privacy firewall partitions" setting arrived in the July 2026 build (Fact, S316).

## Caveats

- A change can be listed in one month as preview and in a later month as GA. Search several months before concluding a feature's state.
- The archive and the monthly blog may differ in detail. The blog posts are the full lists.

## See also

- [2024 and 2025 history](22_release_history_2024_2025.md)
- [Deprecations and retirements](22_deprecations_retirements.md)
- [Release cadence and how to track change](22_release_cadence_and_tracking.md)
