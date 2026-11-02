---
id: 23.ref_direct_lake_guardrails
title: Direct Lake guardrails (pointer)
domain: patterns_recipes
type: reference
level: advanced
tags: [direct-lake, limits, capacity, reference]
summary: Pointer to the single authoritative Direct Lake guardrail table per Fabric SKU, plus the pattern-level takeaways.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2600]
references: [../fabric_onelake/11_direct_lake_guardrails.md]
related: [23.import_vs_directquery_vs_direct_lake, 11.direct_lake_guardrails_ref]
---
## Where the numbers live

The per-SKU table (files, row groups, rows, model size, memory) is kept in one place: [Direct Lake guardrails by SKU](../fabric_onelake/11_direct_lake_guardrails.md). Re-verified against Learn on 2026-10-08 [S2600].

## Pattern-level takeaways

- Fact: F2 to F32 allow 1,000 files per table and 300 million rows per table. F64 and up start at 5,000 files and 1,500 million rows [S2600].
- Fact: Direct Lake on OneLake fails refresh when a guardrail is exceeded. Direct Lake on SQL falls back to DirectQuery if fallback is on [S2600].
- Fact: Model size is checked per model. The other guardrails are checked per query [S2600].
- Fact: Max memory is a paging threshold, not a guardrail [S2600].
- Fact: Deployment pipeline data source rules are not supported for Direct Lake on OneLake, but are for Direct Lake on SQL [S2600].
