---
id: 23.import_vs_directquery_vs_direct_lake
title: Import vs DirectQuery vs Direct Lake
domain: patterns_recipes
type: comparison
level: intermediate
tags: [storage-mode, direct-lake, comparison, decision-guide]
summary: Side-by-side comparison of Import, DirectQuery, and the two Direct Lake options, with licensing, refresh, and limit differences.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1827, S2918]
references: [../references/fabric_onelake/11_direct_lake_guardrails.md]
related: [23.storage_mode_choice, 23.license_choice]
---
## Purpose

Direct Lake adds a third big option beside Import and DirectQuery. This file shows how the three differ so you can choose without reading the full overview.

## Key facts

- Fact: Direct Lake loads Delta tables from OneLake into memory on demand. Queries run in the VertiPaq engine, the same engine Import uses [S1827].
- Fact: A Direct Lake refresh copies only metadata (framing), so it takes seconds. An Import refresh copies all data [S1827].
- Fact: Direct Lake needs a Fabric capacity. Import and DirectQuery work with any Power BI or Fabric license [S1827].
- Fact: Two flavors exist. Direct Lake on OneLake does not fall back to DirectQuery. Direct Lake on SQL (analytics endpoint) can fall back [S1827].
- Fact: Microsoft says Import still fits self-service analysts who need freedom without IT dependency [S1827].
- Fact: Prototype first to confirm Direct Lake is right for you [S1827].

## Comparison

| Capability | Direct Lake on OneLake | Direct Lake on SQL | Import | DirectQuery |
|---|---|---|---|---|
| License | Fabric capacity | Fabric capacity | Any | Any |
| Sources | Fabric Delta tables | One Fabric source with SQL endpoint | Any connector | DirectQuery-capable connectors |
| Composite with other modes | Yes | No | Yes | Yes |
| Calculated tables | Yes (preview) | Limited | Yes | No |
| Calculated columns | Yes, preview, user context | No | Yes | Yes |
| Hybrid tables, partitions | No | No | Yes | Partitions no |
| User-defined aggregations | No | No | Yes | Yes |
| Large data, no refresh load | Yes | Yes | No | Yes |
| Lower data latency | Yes | Yes | No | Yes |
| Embedding | Yes, V2 token | Yes, V2 token | Yes | Yes |

Source: [S1827], table "Compare storage mode capabilities", shortened.

## When to pick which

- Direct Lake: IT-driven, lake-centric projects with large Delta data and frequent change, and a Fabric F capacity [S1827].
- Import: small to medium data, any source, Power Query transformations inside the model, self-service work [S1827].
- DirectQuery: near real-time needs or data that cannot be copied, accepting slower visuals [S1827].
- Import with OneLake integration: writes Import tables to Delta in OneLake, to gain Fabric benefits without redesign [S1827].
- If the author cannot change the lakehouse, add Import tables to a Direct Lake model for local preparation [S1827].

## Common mistakes

- Forgetting that Direct Lake moves transformation upstream. Delta tables must be well tuned (V-Order, row groups) [S1827].
- Basing a Direct Lake on OneLake table on a non-materialized SQL view. Not supported; use a materialized lakehouse view [S1827].
- Expecting SQL-endpoint row-level security to apply to Direct Lake on OneLake. It does not [S1827].
- Using a gateway. Direct Lake supports only cloud connections [S1827].

## Limits and version notes

Guardrails (files, row groups, rows, model size, memory) depend on SKU. See the [guardrail table](../references/fabric_onelake/11_direct_lake_guardrails.md). Exceeding them makes OneLake-mode refresh fail, but SQL-mode falls back to DirectQuery [S1827]. The feature set changes rapidly; recheck the Learn page.

## See also

- [Choosing a storage mode](23_storage_mode_choice.md)
- [License choice](23_license_choice.md)
