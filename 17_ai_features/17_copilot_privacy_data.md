---
id: 17.copilot_privacy_data
title: Copilot data use, privacy and cross-region processing
domain: ai_features
type: concept
level: intermediate
tags: [copilot, security, compliance, tenant-setting]
summary: What data Copilot in Power BI sends to the model, where it is processed, and which tenant settings control cross-region use.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S2102, S2103, S2108, S2816, S2817]
references: []
related: [17.copilot_requirements_capacity, 17.fabric_data_agents]
---

# Copilot data use, privacy and cross-region processing

## Purpose
Help admins answer "what leaves my tenant when users press Copilot?" Always confirm against the linked Microsoft pages for compliance reviews.

## Key facts
- Fact: Copilot uses the semantic model data you provide plus the prompt to build visuals [S2103].
- Fact: interactions can include prompts, meta prompts, data structure (schema) and conversation history. Table contents are not sent unless you direct it [S2102].
- Fact: for measure descriptions Copilot uses the DAX formula and table name, not DAX comments or text in double quotes [S2103].
- Fact: for DAX queries it uses model metadata (table and column names, properties) plus the request [S2103].
- Fact: Microsoft states prompts and responses are not stored after the session ends, data stays within the tenant boundary, and data is not used to train foundation models [S2103]. Notebook and data agent chat history is an exception: kept up to 28 days unless cleared [S2102].
- Fact: Copilot answers data questions only if Q&A is enabled on the semantic model [S2103].
- Fact: by default Copilot uses Azure OpenAI hosted by Microsoft. An admin can opt in to the OpenAI as a Microsoft Subprocessor tenant setting so designated capacities use that service instead, with its own cross-region setting [S2816].
- Fact: Copilot is not supported on trial SKUs, and capacities outside the US and EU data boundary have it off unless the cross-geo setting is on [S2816, S2817].

## Where processing happens
| Capacity geography | Azure OpenAI hosting | Cross-geo setting needed |
|---|---|---|
| US | US | No |
| EU Data Boundary | EU Data Boundary | No |
| UK | EU Data Boundary | Yes |
| Australia, Brazil, Canada, India, Asia, Japan, Korea, South Africa, UAE | US | Yes |

Source: S2102. The tenant setting is "Data sent to Azure OpenAI can be processed outside your capacity's geographic region, compliance boundary, or national cloud instance".

## Responsible use
- Review generated DAX before applying it [S2103].
- Be specific in prompts and name real tables and columns [S2103].
- Mitigations named by Microsoft: content filtering, grounded responses, human oversight [S2103].

## Common mistakes
- Treating "not stored" as "not processed outside region". They are separate questions.
- Forgetting that Purview policies apply to data agents but behave differently for classic Copilot. Unknown; verify per scenario.

## See also
- [Requirements](17_copilot_requirements_capacity.md)
- [Data agents governance](17_fabric_data_agents.md)
