---
id: 20.qlik_to_power_bi
title: Migrating from Qlik to Power BI
domain: migration
type: comparison
level: intermediate
tags: [migration, dax, power-query]
summary: Maps QlikView and Qlik Sense concepts such as associative model, load scripts and set analysis to Power BI equivalents, with pitfalls.
status: n/a
volatile: true
last_verified: 2026-10-08
confidence: low
sources: [S1535, S1543, S2725]
references: []
related: [20.migration_process, 20.tableau_to_power_bi]
---
## Purpose

Qlik apps combine script, model and front end. Power BI separates Power Query, the semantic model with DAX, and reports. This page shows how to split an app.

## Key facts

- Fact (vendor): Qlik's associative engine does not map directly to Power BI. Power BI needs defined relationships and works best with star or snowflake schemas, so models are restructured [S1543].
- Fact (vendor): Set Analysis has no direct equivalent. It is usually rewritten as CALCULATE measures with explicit filters [S1543].
- Fact (vendor): Load scripts are rewritten step by step in Power Query (M language), not converted line by line [S1543].
- Fact (vendor): Click-to-filter-everything behavior differs, so users need guidance [S1543].
- Fact (vendor): Section Access needs rebuilding as security [S1543]. Inference: this maps to row-level security.

## Concept map

| Qlik | Power BI | Basis |
|---|---|---|
| Load script (ETL) | Power Query / Dataflow Gen2 | Vendor [S1543] |
| QVD files | Parquet or Delta in OneLake, or Import tables | Inference |
| Associative data model | Star schema with relationships | Vendor [S1543] |
| Synthetic keys | Redesign keys or bridge tables | Inference |
| Set Analysis | CALCULATE with filter arguments | Vendor [S1543] |
| Master items (dimension, measure) | Model columns and measures | Inference |
| Variables | Parameters or measures | Inference |
| Section Access | Row-level security | Inference |
| Sheets and objects | Report pages and visuals | Inference |
| QlikView (12.90 support ends 2026-10-31; 12.100 ends 2027-09-30, per Qlik community lifecycle table) | Power BI | Vendor [S1543, S2725] |

## Steps

1. List apps, QVDs, scripts, expressions and Section Access rules.
2. Group apps by shared data. Build one semantic model per subject.
3. Rebuild transforms in Power Query. Keep query folding in mind.
4. Convert key set expressions to measures and test with known totals.
5. Rebuild security as RLS. See [Row-level security](../12_admin_governance_security/12_rls_static_dynamic.md).
6. Run both systems in parallel for a period and reconcile [S1543].

## Common mistakes

- Keeping a flat, many-to-many shape from Qlik. Power BI then needs bi-directional filters and slows down.
- Expecting identical selection behavior. Teach slicers and cross-filtering.
- Trusting accelerator claims such as 90 to 95 percent automation. These are unverified vendor claims [S1543].

## Limits and version notes

Effort estimates in sources range from 6 to 16 weeks for small projects to 6 to 18 months for large ones. Both are vendor estimates, not measured data [S1543].

## See also

- [Migration process](20_migration_process.md)
- [Migration checklist](20_migration_checklist.md)
