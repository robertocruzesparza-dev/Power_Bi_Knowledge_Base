---
id: 17.fabric_data_agents
title: Fabric data agents
domain: ai_features
type: concept
level: intermediate
tags: [fabric, copilot, semantic-model, governance, limits]
summary: What Fabric data agents are, prerequisites, how they query lakehouses, warehouses and semantic models, governance layers, and hard limits.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2108, S2102, S2112, S2523, S2524, S2525]
references: []
related: [17.copilot_overview, 17.copilot_privacy_data]
---

# Fabric data agents

## Purpose
A data agent is a configurable conversational Q&A item over OneLake data. Unlike Copilot, you add instructions and examples, then publish and share it [S2108].

## Status (re-verified 2026-10-08)
- Fact: the concept page calls data agent generally available (GA) [S2108, S2523].
- Fact: the standard runtime is GA and the default. A separate preview runtime carries preview-only items such as schema object descriptions, topics and Advanced NL2SQL [S2524].
- Fact: data source routing and the Copilot Studio integration reached GA in August 2026 [S2525]. Purview protection features and access restriction policies stay preview [S2523].
- The earlier release-status table (S2112) that listed data agent as preview no longer appears on the Fabric preview page. Resolved: GA, with preview sub-features.

## Key facts
- Prerequisites: F2+ or P1+ capacity with Fabric enabled, cross-geo processing and storing settings as needed, at least one data source with read access [S2108].
- Sources: up to five, from lakehouse, warehouse, semantic model, KQL database, mirrored database, ontology, Microsoft Graph [S2108].
- Query generation: NL2SQL, NL2DAX, NL2KQL; strictly read-only [S2108].
- Semantic models need Read permission only; RLS and column-level security still apply [S2108].
- Instruction precedence: organizational, role-based, developer, user [S2108].
- Lifecycle: Git integration, deployment pipelines, diagnostics [S2108].
- Purview DLP and access restriction policies can truncate or block answers; some are preview [S2108].

## Limits
- Responses capped at 25 rows and 25 columns [S2108].
- 100 example queries per source; example queries are not supported for semantic model sources [S2108].
- English only; no unstructured files (PDF, DOCX, TXT); lakehouse files must be tables [S2108].
- Cannot change the LLM; history may reset after service updates [S2108].
- Source and agent capacities must be in the same region [S2108].
- Fact: chat history is stored for 28 days unless cleared [S2102].

## Common mistakes
- Asking for "all rows" and trusting the output; it is capped at 25 [S2108].
- Pointing at raw files instead of tables.

## See also
- [Copilot privacy](17_copilot_privacy_data.md)
- [Copilot overview](17_copilot_overview.md)
