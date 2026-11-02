---
id: 11.direct_lake_guardrails_ref
title: Direct Lake guardrails by SKU
domain: fabric_onelake
type: reference
level: advanced
tags: [direct-lake, limits, capacity, reference]
summary: Per-SKU Direct Lake limits for Parquet files, row groups, rows, model size, and memory, as published by Microsoft.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1203, S2600]
references: []
related: [11.direct_lake, 11.direct_lake_fallback]
---

# Direct Lake guardrails by SKU

This is the single authoritative guardrail table in the KB. Values re-verified against the Learn Direct Lake overview on 2026-10-08. They can change. Rows per table are in millions. Max memory is per model, a paging threshold rather than a hard guardrail. [S1203]

| SKU | Parquet files per table | Row groups per table | Rows per table (M) | Max model size on disk (GB) | Max memory (GB) |
|---|---|---|---|---|---|
| F2, F4, F8 | 1,000 | 1,000 | 300 | 10 | 3 |
| F16 | 1,000 | 1,000 | 300 | 20 | 5 |
| F32 | 1,000 | 1,000 | 300 | 40 | 10 |
| F64, FT1, P1 | 5,000 | 5,000 | 1,500 | Unlimited | 25 |
| F128, P2 | 5,000 | 5,000 | 3,000 | Unlimited | 50 |
| F256, P3 | 5,000 | 5,000 | 6,000 | Unlimited | 100 |
| F512, P4 | 10,000 | 10,000 | 12,000 | Unlimited | 200 |
| F1024, P5 | 10,000 | 10,000 | 24,000 | Unlimited | 400 |
| F2048 to F8192 | 10,000 | 10,000 | 24,000 | Unlimited | 400 |

Rules: [S1203]

- Max model size on disk is checked at model level and affects all queries. The other columns are checked per query.
- Exceeding a guardrail: Direct Lake on OneLake fails refresh and cannot be queried. Direct Lake on SQL falls back to DirectQuery if fallback is on.
- Capacity unit and max-memory-per-query limits also apply. See Capacities and SKUs on Learn.
- Fix by running OPTIMIZE and VACUUM, using fewer and larger files, and V-Order. Scale up only if needed.
