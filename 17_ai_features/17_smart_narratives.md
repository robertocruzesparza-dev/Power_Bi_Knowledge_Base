---
id: 17.smart_narratives
title: Narrative visual - custom and Copilot modes
domain: ai_features
type: how-to
level: beginner
tags: [ai-visual, copilot, visual, report]
summary: How the Narrative visual produces text summaries in custom (smart narrative) and Copilot modes, with limits for each.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S2110, S2142, S2145, S2821, S2822]
references: []
related: [17.copilot_overview, 17.key_influencers]
---

# Narrative visual - custom and Copilot modes

## Purpose
The Narrative visual writes a text summary of a page or visual. It has two modes [S2110].

## Key facts
- Fact: Copilot mode uses AI, needs Copilot, and accepts prompts up to 10,000 characters [S2110].
- Fact: Custom mode (the classic smart narrative) lets you edit text with dynamic values tied to fields and measures [S2110].
- Fact: custom mode generates up to four summaries per visual and 16 per page [S2110].
- Fact: custom narratives update when users cross-filter. Copilot narratives do not; viewers press refresh to fetch an updated summary [S2110, S2142].

## Steps
1. Select the Narrative icon on the Visualizations pane.
2. If Copilot mode opens, switch the dropdown to Custom for an editable summary [S2110].
3. For one visual: right-click, choose Summarize, optionally pin it [S2110].
4. For Copilot mode, write a prompt such as "shorten this summary and bold key information", then refine.

## Limits
Custom mode does not support (selected list from S2110): pinning to dashboards, Publish to web, Report Server, Analysis Services live connections, tables, matrices, R or Python visuals, custom visuals, calculation groups, and renaming dynamic values.
Copilot mode (S2142):
- Authoring in the service needs a workspace on paid dedicated Fabric capacity.
- You cannot edit the generated visual directly; change it with prompts.
- Key influencers is not yet supported.
- Hidden-bookmark visuals count only for display-only bookmarks reachable by a button or navigator.
- Embedding: secure embed, SharePoint and user-owns-data (embed for your organization) are supported; app-owns-data (embed for your customers) is supported in preview (S2821).
- Fact: smart narrative is not supported with visual calculations [S2145].

## Common mistakes
- Expecting a Copilot narrative to refresh on slicer change. It does not.
- Pinning a narrative to a dashboard (custom mode does not support it).

## See also
- [Copilot requirements](17_copilot_requirements_capacity.md)
- [Key influencers](17_key_influencers.md)
