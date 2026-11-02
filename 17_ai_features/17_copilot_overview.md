---
id: 17.copilot_overview
title: Copilot in Power BI overview
domain: ai_features
type: concept
level: beginner
tags: [copilot, power-bi, report, semantic-model]
summary: What Copilot in Power BI does for business users, report authors and model authors, and which surfaces are generally available or preview.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2101, S2102, S2112, S2532, S2533]
references: [../references/ai_features/17_ai_feature_status_matrix.md]
related: [17.copilot_requirements_capacity, 17.copilot_privacy_data, 17.prep_data_for_ai]
---

# Copilot in Power BI overview

## Purpose
Copilot is a chat-based generative AI assistant inside Power BI. It answers questions, summarizes reports, builds report pages and writes DAX. Example: a viewer opens a sales report, asks "why did Q3 drop?", and Copilot answers from the semantic model.

## Key facts
- Fact: the report Copilot pane (right side of a report) is generally available (GA) [S2101].
- Fact: the standalone full-screen Power BI agent, and the app-scoped agent, are preview [S2101].
- Fact: Copilot in web modeling for semantic model authors is preview [S2101].
- Fact: if a question relates to semantic model data, Copilot uses the model. Otherwise it answers from the large language model (LLM) general knowledge [S2101].
- Fact: prompts can be up to 10,000 characters on all Copilot surfaces [S2101].
- Fact: the same exact prompt on an unchanged model is served from a cache for a rolling 24 hours, so the answer repeats [S2101].

## Who uses what
| Audience | Typical tasks | Where |
|---|---|---|
| Business user | Ask data questions, summarize a report, find content | Copilot pane, standalone Copilot, app Copilot |
| Report author | Create report pages, add a narrative visual, write DAX queries, describe measures | Desktop and service |
| Model author | Find naming problems, get best-practice advice, edit DAX and relationships | Copilot in web modeling (preview) |

## Status conflict to know
- Fact: the Power BI overview page labels the report pane GA and standalone preview [S2101].
- Fact: the Fabric status table lists Power BI semantic model and report experiences as GA, with Power BI home "announced" [S2112].
- Inference: both agree on the pane being GA; the table is less granular. Check both pages before promising a feature.

## Common mistakes
- Assuming a Pro or Premium Per User (PPU) licence is enough. It is not; Copilot needs capacity. See [requirements](17_copilot_requirements_capacity.md).
- Skipping model preparation. Unprepared models give generic answers. See [prep data for AI](17_prep_data_for_ai.md).
- Expecting identical answers each time. AI output is nondeterministic [S2109].

## Limits and version notes
- Fact: sovereign clouds are not supported [S2101].
- Fact: multilingual prompts are not officially supported [S2101].
- Fact: new or scaled capacity can take up to 24 hours before Copilot recognises it [S2101].

## See also
- [Privacy and data](17_copilot_privacy_data.md)
- [Smart and Copilot narratives](17_smart_narratives.md)
- [Fabric data agents](17_fabric_data_agents.md)
