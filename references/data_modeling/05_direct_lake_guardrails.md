---
id: 05.ref_direct_lake_guardrails
title: Direct Lake capacity guardrails (pointer)
domain: data_modeling
type: reference
level: advanced
tags: [direct-lake, limits, capacity, reference]
summary: Pointer to the single authoritative per-SKU Direct Lake guardrail table kept in the Fabric domain.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2600]
references: [../fabric_onelake/11_direct_lake_guardrails.md]
related: [05.direct_lake]
---

# Direct Lake capacity guardrails

The per-SKU table (files, row groups, rows, model size, memory) lives in one place: [Direct Lake guardrails by SKU](../fabric_onelake/11_direct_lake_guardrails.md). It was re-verified against Microsoft Learn on 2026-10-08 [S2600].

Modeling takeaway (Fact, S2600): model size is checked per model, the other guardrails per query. Direct Lake on SQL can fall back to DirectQuery when fallback is on. Direct Lake on OneLake fails the refresh instead.
