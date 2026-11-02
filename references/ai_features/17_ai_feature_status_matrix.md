---
id: 17.ai_feature_status_matrix
title: AI feature status matrix
domain: ai_features
type: reference
level: intermediate
tags: [copilot, ai-visual, release, reference]
summary: One-table view of Power BI and Fabric AI features, their status per Microsoft docs, and key blockers, as of 2026-10-07.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S2101, S2104, S2105, S2106, S2107, S2108, S2109, S2110, S2112, S2818, S2819, S2820]
references: []
related: [17.copilot_overview]
---

# AI feature status matrix

| Feature | Status | Key blockers | Source |
|---|---|---|---|
| Copilot report pane | GA | Needs F2+/P1+ capacity | S2101 |
| Standalone Copilot agent | Preview | Extra tenant setting; region gaps | S2101 |
| App-scoped Copilot | Preview | Per-app setting, on by default | S2101 |
| Copilot in web modeling | Preview | Edit mode, write access | S2101 |
| Prep data for AI | Preview | Q&A enabled on model | S2109 |
| Copilot narrative visual | Per docs (GA in S2112 table) | Dedicated Fabric capacity to author | S2112 |
| Custom smart narrative | Available | No dashboards, no Report Server | S2110 |
| Q&A | Retiring Feb 2027 | Replace with Copilot | S2107 |
| Key influencers | GA | No DirectQuery | S2104 |
| Decomposition tree | GA | No on-prem AS; AI splits limits | S2105 |
| Anomaly detection | GA | Line chart only | S2106 |
| Fabric data agent | Concept page says GA (S2819); release-status page still lists Data Science agents as Preview (S2818) | F2+/P1+ capacity, English only, 25 rows by 25 columns per chat answer | S2819, S2818 |
| Copilot for Data Factory dataflows and pipelines | GA | Fabric capacity | S2112 |
| Copilot in notebooks, Data Warehouse | Preview | Fabric capacity | S2112 |
