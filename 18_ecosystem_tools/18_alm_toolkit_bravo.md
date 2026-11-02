---
id: 18.alm_toolkit_bravo
title: ALM Toolkit and Bravo
domain: ecosystem_tools
type: concept
level: intermediate
tags: [ecosystem, devops, semantic-model]
summary: What ALM Toolkit (schema compare and deploy) and Bravo (model analysis, DAX formatting, date tables, export) do and who maintains them.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S2114, S2133, S2134, S2827]
references: []
related: [18.external_tools_overview, 18.tabular_editor]
---

# ALM Toolkit and Bravo

## ALM Toolkit
- Fact: a schema comparison tool for Power BI semantic models, hosted in the Microsoft analysis-services repository [S2134].
- Fact: features are schema compare, merge with guardrails, deploying metadata without overwriting data (including incremental refresh partitions), reusing common objects, command-line automation and TMDL display [S2134].
- Fact: Microsoft lists it as a featured open-source tool; it self-registers in the External Tools ribbon [S2114].
- Example: push measure changes from a dev model to production while keeping historic incremental-refresh partitions.
- Unknown: current version, license text and system requirements (not shown on the fetched page).

## Bravo for Power BI
- Fact: a Windows 64-bit desktop app from SQLBI, released under the MIT license, downloaded from GitHub [S2133].
- Fact: four features. Analyze Model finds memory-heavy columns and exports VPAX metadata. Format DAX previews and applies DAX Formatter. Manage Dates builds a Date table from templates with holidays and time intelligence measures. Export Data writes the model to Excel or CSV [S2133].
- Fact: a VS Code extension edits custom date templates [S2133].
- Fact: the latest GitHub release is v1.0.13, dated 21 January (no year shown; likely 2026). Its only change is a VPAX library update, and the page shows no deprecation or archive notice [S2827].

## Common mistakes
- Using schema compare without checking that partition and refresh policy settings are preserved.
- Applying Format DAX to all measures without source control.

## See also
- [External tools overview](18_external_tools_overview.md)
- [Tabular Editor](18_tabular_editor.md)
