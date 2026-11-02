---
id: 18.tabular_editor
title: Tabular Editor 2 and 3
domain: ecosystem_tools
type: comparison
level: intermediate
tags: [tabular-editor, semantic-model, tmdl, licensing, ecosystem]
summary: Compare free open-source Tabular Editor 2 with commercial Tabular Editor 3, their editions, and typical uses.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S2131, S2132, S2114, S2122, S2551]
references: []
related: [18.external_tools_overview, 18.dax_studio, 18.alm_toolkit_bravo]
---

# Tabular Editor 2 and 3

## Purpose
Both tools edit the Tabular Object Model (TOM) of a semantic model. Example: bulk-rename measures, apply a Best Practice Analyzer rule set, or run a C# script across many columns.

## Comparison
| Aspect | Tabular Editor 2 | Tabular Editor 3 |
|---|---|---|
| License | Free, MIT open source [S2131] | Commercial [S2131] |
| Focus | Lightweight TOM editing | Full IDE with DAX editor, debugger, table browser [S2131] |
| Best Practice Analyzer | Yes [S2131] | Built-in rules [S2131] |
| Scripting | C#-style [S2131] | C# and DAX scripting [S2131] |
| Desktop external tool | Yes [S2131] | Yes [S2131] |
| Command line | Yes [S2131] | Not stated in fetched text |

## Editions of version 3 (volatile)
- Desktop, Business, Enterprise and Companywide editions exist, billed per user monthly or yearly with a stated 17 percent yearly saving [S2132].
- Business limits Power BI XMLA to Premium Per User, SSAS to Standard edition and Azure AS to Basic tier. Enterprise has no such limits and includes dedicated support [S2132].
- Enterprise is needed for Analysis Services models with perspectives or multi-partition tables; not for Desktop or PPU models [S2132].
- A 30-day trial matching Enterprise exists [S2132]. Prices were not visible in the fetched text: unknown, check the pricing page.

## Why it matters for refresh issues
Microsoft cites Tabular Editor as the way to submit several calculated-table changes in one transaction when fixing the SummarizeColumns circular-dependency error [S2122].

## Cautions
Modifying metadata outside Desktop can cause inconsistencies in rare cases [S2114].

## See also
- [External tools overview](18_external_tools_overview.md)
- [ALM Toolkit and Bravo](18_alm_toolkit_bravo.md)
