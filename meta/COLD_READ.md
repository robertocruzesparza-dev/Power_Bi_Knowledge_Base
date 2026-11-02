---
id: meta.cold_read
title: Cold-read test
domain: meta
type: reference
level: intermediate
tags: [metadata, reference]
summary: Fifteen questions routed from INDEX through a domain index to the answering file, with read counts.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: []
---

# Cold-read test

Method: start at INDEX.md (or the quick routes in 00_START_HERE.md), pick a domain, read its index, pick a file. Reads counted: INDEX, domain index, file. Pass means the file exists, is listed in the domain index, and contains the expected answer term.

| Level | Question | Path | Reads | Result |
|---|---|---|---|---|
| Beginner | What is a semantic model? | INDEX -> 09_semantic_models_dataflows/_domain_index.md -> 09_semantic_model_basics.md | 3 | pass |
| Beginner | How many scheduled refreshes per day does Pro allow? | INDEX -> 09_semantic_models_dataflows/_domain_index.md -> 09_semantic_model_refresh.md | 3 | pass |
| Intermediate | What does CALCULATE do to filter context? | INDEX -> 06_dax/_domain_index.md -> 06_calculate_context_transition.md | 3 | pass |
| Beginner | How much does a Power BI Pro license cost? | INDEX -> 13_licensing_pricing/_domain_index.md -> 13_pricing_reference.md | 3 | pass |
| Intermediate | What is query folding and what breaks it? | INDEX -> 04_power_query_m/_domain_index.md -> 04_query_folding.md | 3 | pass |
| Intermediate | How do I set up dynamic row-level security? | INDEX -> 12_admin_governance_security/_domain_index.md -> 12_rls_static_dynamic.md | 3 | pass |
| Advanced | When does Direct Lake fall back to DirectQuery? | INDEX -> 11_fabric_onelake/_domain_index.md -> 11_direct_lake_fallback.md | 3 | pass |
| Intermediate | How do I fix a gateway connection error? | INDEX -> 19_troubleshooting/_domain_index.md -> 19_gateway_errors.md | 3 | pass |
| Intermediate | What does Copilot in Power BI require? | INDEX -> 17_ai_features/_domain_index.md -> 17_copilot_requirements_capacity.md | 3 | pass |
| Advanced | How many stages can a deployment pipeline have? | INDEX -> 15_devops_lifecycle/_domain_index.md -> 15_deployment_pipelines.md | 3 | pass |
| Intermediate | Embed for customers or for the organization? | INDEX -> 14_embedding_apis/_domain_index.md -> 14_embed_for_customers.md | 3 | pass |
| Intermediate | How do Tableau concepts map to Power BI? | INDEX -> 20_migration/_domain_index.md -> 20_tableau_to_power_bi.md | 3 | pass |
| Beginner | What does the PL-300 exam cover? | INDEX -> 21_certification_learning/_domain_index.md -> 21_pl300_exam.md | 3 | pass |
| Advanced | How do I find a slow visual? | INDEX -> 16_performance/_domain_index.md -> 16_performance_analyzer.md | 3 | pass |
| Intermediate | When does Q&A retire? | INDEX -> 17_ai_features/_domain_index.md -> 17_qna_deprecation.md | 3 | pass |

Result: 15 of 15 questions answered within 3 reads. Note: the first run failed one row only because the test term "$14" did not match the file wording "14.00 USD"; the answer is present, so the term was changed to "14.00". Limitation: the author who wrote the questions also chose the paths, and the term check is a keyword test, not a reading-comprehension test.
