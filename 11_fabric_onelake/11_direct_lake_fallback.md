---
id: 11.direct_lake_fallback
title: Direct Lake fallback and diagnosis
domain: fabric_onelake
type: troubleshooting
level: advanced
tags: [direct-lake, troubleshooting, performance, semantic-model]
summary: When Direct Lake on SQL falls back to DirectQuery, how to control it, diagnose it, and fix common causes.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1238, S1203, S2918]
references: []
related: [11.direct_lake, 11.lakehouse_vs_warehouse]
---
## Purpose

Fallback silently swaps a query to DirectQuery against the SQL analytics endpoint. Results stay correct but get slower. This page shows how to spot and avoid it.

## Key facts

- Fact: Only Direct Lake on SQL analytics endpoints can fall back. Direct Lake on OneLake runs as DirectLakeOnly and never falls back. [S1238]
- Fact: Fallback queries return the latest data, not the last-framed snapshot. [S1238]
- Fact: One table over a guardrail blocks Direct Lake mode for the whole model. [S1238]
- Fact: With Direct Lake on OneLake, a guardrail breach makes refresh fail instead. [S1203]

## When Direct Lake stays on

All of these must hold: [S1238]

1. No SQL row-level security (RLS) on referenced tables at the endpoint.
2. No SQL dynamic data masking.
3. No SQL object-level security (OLS).
4. No tables built on unmaterialized SQL views.
5. No table over the Parquet file, row group, or row guardrails.
6. The model was framed after the Delta tables were created or changed.

## Control the behavior

The DirectLakeBehavior property applies only to Direct Lake on SQL. [S1238]

| Value | Effect | Use |
|---|---|---|
| Automatic (default) | Silently falls back | Production |
| DirectLakeOnly | Query fails with an error | Development, to find causes |
| DirectQueryOnly | Always DirectQuery | Measuring fallback cost |

Set it in Model view, Properties pane. Or in code: `database.Model.DirectLakeBehavior = DirectLakeBehavior.DirectLakeOnly;` then SaveChanges. [S1238]

## Diagnose

Run this DAX query:

```dax
EVALUATE TABLETRAITS()
```

The column DirectLakeFallbackInfo gives the reason per table. None means the table uses Direct Lake. [S1238]

For deeper analysis use Performance Analyzer or SQL Server Profiler. [S1238]

## Fix table

| Cause | Fix |
|---|---|
| Table not framed | Refresh the model. Always refresh after adding tables with TOM or TMSL. |
| Table is a SQL view | Materialize it as a Delta table, or accept DirectQuery. |
| Table missing | Check the Delta table and schema drift. |
| Transient error | Retry; check capacity health. |
| OLS at the endpoint | Move OLS into the semantic model. |
| RLS or masking at the endpoint | Move RLS into the semantic model. |
| Over guardrails | Run OPTIMIZE and VACUUM. If still over, move to a larger F SKU. |
| Memory pressure | Reduce concurrent load, tune other models, or scale up. |

Source for the table: S1238.

Inference: Prefer Direct Lake on OneLake for new models so these fallbacks do not occur. Check the migration notes for your source item first.

## See also

- [Direct Lake](11_direct_lake.md)
- [Lakehouse versus warehouse](11_lakehouse_vs_warehouse.md)
