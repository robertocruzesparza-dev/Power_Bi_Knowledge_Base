---
id: 23.domain_index
title: Index of patterns recipes
domain: patterns_recipes
type: index
level: beginner
tags: [index, navigation]
summary: Lists every file in the patterns recipes domain with tags and summaries.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: high
sources: []
references: []
related: []
---

# Domain index: patterns recipes

Scope: Decision guides and recipes

[Back to INDEX](../INDEX.md)

| ID | Title | Kind | Tags | Summary | Path |
|---|---|---|---|---|---|
| 23.dataflow_vs_semantic_model | Dataflow or semantic model - where to put the transformation | core | dataflow, semantic-model, power-query, decision-guide | Guidance on when to prepare data in a dataflow, a lakehouse, or inside the semantic model, including the Gen1 versus Gen2 status. | [23_dataflow_vs_semantic_model.md](23_dataflow_vs_semantic_model.md) |
| 23.embedding_choice | Choosing an embedding approach | core | embedding, decision-guide, licensing, capacity | A decision guide for picking secure embed, embed for your organization, or embed for your customers, with licensing consequences. | [23_embedding_choice.md](23_embedding_choice.md) |
| 23.import_vs_directquery_vs_direct_lake | Import vs DirectQuery vs Direct Lake | core | storage-mode, direct-lake, comparison, decision-guide | Side-by-side comparison of Import, DirectQuery, and the two Direct Lake options, with licensing, refresh, and limit differences. | [23_import_vs_directquery_vs_direct_lake.md](23_import_vs_directquery_vs_direct_lake.md) |
| 23.license_choice | Choosing between Pro, PPU, and Fabric capacity | core | licensing, capacity, decision-guide | Decision guide for Free, Pro, Premium Per User, and Fabric F SKU licensing based on authors, viewers, and features needed. | [23_license_choice.md](23_license_choice.md) |
| 23.recipe_dev_to_prod_release | Recipe - release a report from development to production | core | deployment-pipeline, devops, example, how-to | A step-by-step recipe to promote a report and semantic model through a three-stage deployment pipeline with per-stage data sources. | [23_recipe_dev_to_prod_release.md](23_recipe_dev_to_prod_release.md) |
| 23.recipe_embed_report_with_rls | Recipe - embed a report for external customers with RLS | core | embedding, rls, rest-api, how-to | Steps to embed a report for external customers with a service principal and a row-level security identity in the embed token. | [23_recipe_embed_report_with_rls.md](23_recipe_embed_report_with_rls.md) |
| 23.recipe_pbix_to_git | Recipe - move a PBIX report into Git | core | pbip, git-integration, devops, how-to | Steps to convert a PBIX into a PBIP project, commit it, and connect a Fabric workspace to the repository. | [23_recipe_pbix_to_git.md](23_recipe_pbix_to_git.md) |
| 23.rls_pattern_choice | Choosing a row-level security pattern | core | rls, security, decision-guide, embedding | When to use static roles, dynamic roles, custom data, or workspace isolation for row-level security, including embedding cases. | [23_rls_pattern_choice.md](23_rls_pattern_choice.md) |
| 23.storage_mode_choice | Choosing a table storage mode | core | storage-mode, composite-model, decision-guide, data-modeling | A decision guide for choosing Import, DirectQuery, Dual, or hybrid storage per table, with the reasoning behind each recommendation. | [23_storage_mode_choice.md](23_storage_mode_choice.md) |
| 23.workspace_design | Workspace design decision guide | core | workspace, governance, decision-guide, best-practice | How to decide workspace scope, whether to split data from reports, and how many stages to use. | [23_workspace_design.md](23_workspace_design.md) |
| 23.ref_direct_lake_guardrails | Direct Lake guardrails (pointer) | reference | direct-lake, limits, capacity, reference | Pointer to the single authoritative Direct Lake guardrail table per Fabric SKU, plus the pattern-level takeaways. | [23_direct_lake_guardrails.md](../references/patterns_recipes/23_direct_lake_guardrails.md) |
