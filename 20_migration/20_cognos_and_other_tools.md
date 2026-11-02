---
id: 20.cognos_and_other_tools
title: Migrating from Cognos and other BI tools
domain: migration
type: comparison
level: intermediate
tags: [migration, semantic-model, paginated-report]
summary: Concept map from IBM Cognos to Power BI and a general pattern for other legacy BI tools, with coexistence and vendor-claim cautions.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: low
sources: [S1535, S1544]
references: []
related: [20.migration_process, 20.ssrs_rdl_to_power_bi]
---
## Purpose

Cognos and similar enterprise tools separate a metadata model from reports. Power BI follows the same idea with a semantic model and reports.

## Key facts

- Fact (vendor): Treat the Framework Manager model as the center. Map each package to a semantic model and rebuild query subjects, relationships and calculations as tables, relationships and DAX [S1544].
- Fact (community): Reports generally cannot be converted directly because tools have different design philosophies. Plan to rebuild [S1544].
- Fact (community): Scope first. Find which parts of the Cognos model the in-scope reports use and rebuild a minimal model [S1544].
- Fact (vendor): Paginated reports are the closest match to Report Studio output. One analyst view says they have less historical depth, so some features need workarounds [S1544].
- Fact (vendor): Automation vendors claim 30 to 70 percent effort reduction. These are unverified claims [S1544].

## Concept map

| Cognos | Power BI | Basis |
|---|---|---|
| Framework Manager package | Semantic model | Vendor [S1544] |
| Query subject / namespace | Table / folder | Inference |
| Report Studio list and crosstab | Paginated report table / matrix | Vendor [S1544] |
| Analysis Studio / dashboards | Interactive report | Inference |
| Prompts | Report parameters (paginated) or slicers | Inference |
| Burst / scheduled distribution | Subscriptions, Power Automate | Inference; check limits |
| Data module | Semantic model or dataflow | Inference |
| Namespace security | RLS and workspace roles | Inference |

## Steps

1. Rank reports by use in the last 12 months. Retire the rest.
2. Classify each as operational (paginated) or analytical (interactive).
3. Rebuild the model in one place, with measures defined once.
4. Rebuild paginated reports with Report Builder. See [SSRS and RDL migration](20_ssrs_rdl_to_power_bi.md) for the publishing side.
5. Reconcile totals and run in parallel before cutover.
6. Consider coexistence: Cognos keeps legacy operational reporting while Power BI serves interactive analysis [S1544].

## Pattern for other tools

For MicroStrategy, Business Objects, SAP tools and similar, no source was gathered (see gaps). Use the generic path: inventory, model once, rebuild measures, reconcile, train. The Microsoft series applies to any third-party tool [S1535].

## Common mistakes

- Trusting a conversion tool to produce finished reports.
- Missing prompts, bursting and subscriptions in scoping. These need explicit design.
- Planning a big-bang switch for a deeply embedded estate. A multi-year effort is common (consultancy view) [S1544].

## Limits and version notes

All Cognos-specific claims are tier 3. Validate with a proof of concept on representative reports.

## See also

- [Migration process](20_migration_process.md)
- [Migration checklist](20_migration_checklist.md)
