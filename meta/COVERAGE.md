---
id: 00.coverage
title: Coverage plan
domain: meta
type: index
level: intermediate
tags: [metadata, index]
summary: Per-domain research plan with owners, key questions, source targets, and the saturation rule. Plan plus actual coverage status.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: [00.start]
---

# Coverage plan

Saturation rule: stop a domain when the last 10 new sources add no fact that changes any KB file.
Official first: Microsoft Learn, Power BI blog, Fabric roadmap, Trust Center. Then experts (SQLBI, RADACAD, Guy in a Cube, Chris Webb, Data Goblins, Tabular Editor docs), then community (labeled).
Actual coverage is reported in `GAPS.md` and the final report. Each worker logs sources in `meta/sources/`.

| Domain folder | Scope | Worker |
|---|---|---|
| 01_foundations | Product family, architecture, concepts, terminology | W1 |
| 02_desktop | Desktop app: install, UI, options, preview features, file formats | W1 |
| 03_data_sources | Connectors, gateways, authentication, privacy levels | W2 |
| 04_power_query_m | Power Query editor, M language, folding, parameters | W2 |
| 05_data_modeling | Star schema, relationships, storage modes, composite, Direct Lake, aggregations | W3 |
| 06_dax | DAX concepts, functions, patterns, time intelligence, performance | W3 |
| 07_report_design | Visuals, custom visuals, accessibility, themes, mobile | W4 |
| 08_service | Workspaces, apps, dashboards, sharing, subscriptions, refresh | W4 |
| 09_semantic_models_dataflows | Semantic models, dataflows Gen1/Gen2, datamarts | W5 |
| 10_paginated_reports | Report Builder, RDL, subscriptions, limits | W5 |
| 11_fabric_onelake | Fabric items, OneLake, shortcuts, Direct Lake, mirroring | W5 |
| 12_admin_governance_security | RLS/OLS, labels, tenant settings, audit, compliance | W6 |
| 13_licensing_pricing | Licenses, SKUs, capacities, pricing, limits | W6 |
| 14_embedding_apis | REST, embedded, custom visuals SDK, XMLA | W7 |
| 15_devops_lifecycle | Deployment pipelines, Git, PBIP, TMDL, PBIR | W7 |
| 16_performance | Optimization, Performance Analyzer, capacity metrics | W3 |
| 17_ai_features | Copilot, Q&A, smart narratives, AI visuals | W8 |
| 18_ecosystem_tools | DAX Studio, Tabular Editor, ALM Toolkit, Power Automate, Apps, Excel, Teams | W8 |
| 19_troubleshooting | Error messages and fixes, known issues | W8 |
| 20_migration | From Tableau, Qlik, Excel, SSRS | W6 |
| 21_certification_learning | PL-300, DP-600, learning paths, expert sources | W4 |
| 22_release_roadmap | Monthly releases, deprecations, roadmap | W2 |
| 23_patterns_recipes | Decision guides and recipes | W7 |

## Questions every domain must answer

1. What is it, in one paragraph a beginner understands?
2. How do I do the 3 most common tasks, step by step?
3. What are the limits, quotas, and version or license requirements?
4. What goes wrong, and what fixes it?
5. What changed recently, and what is preview or deprecated?
6. Where does official documentation disagree with community experience?

## Actual status (2026-10-08)

No domain met the saturation rule. Workers stopped on budget. Depth labels are the author's judgment from worker reports and `GAPS.md`.

| Domain | Core | Refs | Depth |
|---|---|---|---|
| 01_foundations | 7 | 1 | partial |
| 02_desktop | 10 | 1 | moderate |
| 03_data_sources | 9 | 4 | mostly saturated |
| 04_power_query_m | 9 | 7 | incomplete |
| 05_data_modeling | 10 | 1 | core covered |
| 06_dax | 11 | 7 | core covered, depth incomplete |
| 07_report_design | 10 | 1 | incomplete (no per-visual reference) |
| 08_service | 15 | 1 | saturated at current depth |
| 09_semantic_models_dataflows | 7 | 1 | moderate |
| 10_paginated_reports | 7 | 0 | incomplete |
| 11_fabric_onelake | 9 | 1 | incomplete |
| 12_admin_governance_security | 10 | 2 | partial |
| 13_licensing_pricing | 9 | 0 | largely covered, prices US-only |
| 14_embedding_apis | 10 | 1 | incomplete (JS client, Fabric REST) |
| 15_devops_lifecycle | 9 | 1 | well covered, thin on CI/CD tools |
| 16_performance | 7 | 0 | core covered |
| 17_ai_features | 10 | 1 | reasonable |
| 18_ecosystem_tools | 9 | 0 | incomplete |
| 19_troubleshooting | 8 | 3 | partial |
| 20_migration | 7 | 0 | thin for non-Microsoft tools |
| 21_certification_learning | 7 | 0 | saturated at current depth |
| 22_release_roadmap | 6 | 0 | mostly complete |
| 23_patterns_recipes | 10 | 1 | official sources only |
