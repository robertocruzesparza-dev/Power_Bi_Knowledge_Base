---
id: 17.qna_deprecation
title: Power BI Q&A and its retirement
domain: ai_features
type: concept
level: beginner
tags: [ai-visual, copilot, roadmap]
summary: What Q&A does, how its underline colors work, and the announced end of Q&A experiences in February 2027 in favor of Copilot.
status: deprecated
volatile: true
last_verified: 2026-11-02
confidence: high
sources: [S2107, S2103, S2145, S2520, S2521, S2522, S3022]
references: []
related: [17.copilot_overview, 17.prep_data_for_ai]
---

# Power BI Q&A and its retirement

## Purpose
Q&A lets users type a natural-language question and get a visual. Microsoft announced it is going away.

## Key facts
- Fact: the Q&A introduction page states Q&A experiences go away in February 2027 and recommends Copilot [S2107].
- Fact: Q&A is free and available to all users today [S2107].
- Conflict (re-verified 2026-10-08): the January 2026 monthly notes, the Power BI blog and Message Center item MC1218421 said December 2026. Every current Learn Q&A article now says February 2027. Learn is the later and official wording, so use February 2027 but plan for the earlier date; no official note explaining the change was found [S2520, S2521, S2522].
- Fact (rechecked 2026-11-02): the Learn Q&A articles (limitations, live connections, visual, tooling, best practices) all still say Q&A experiences go away in February 2027 [S3022].
- Inference: plan migrations of Q&A visuals and dashboard Q&A boxes before that date. The detail page is the "Deprecating Power BI Q&A" link on [S2107]; I did not fetch it.
- Fact: Copilot still needs Q&A enabled on a semantic model for data questions [S2103]. Treat that dependency as unresolved after the retirement date: unknown.

## How Q&A works
- Ask questions like "top 10 products by sales", "sales in the USA", "median sales by product", or add "as pie chart" [S2107].
- Supported result types: line, bar, matrix, table, card, area, pie, scatter or bubble, map [S2107].
- Underlines: solid blue means matched to a field or value; orange dots mean low confidence or synonym match; red double underline means not recognized [S2107].
- Teach Q&A defines unrecognized terms [S2107].

## Limits
- Fact: Q&A visuals are not supported by visual calculations, nor in the Explore preview, and smart narratives do not support them [S2145].

## Common mistakes
- Building new reports on the Q&A visual now. Prefer Copilot or standard visuals.

## See also
- [Copilot overview](17_copilot_overview.md)
- [Prep data for AI](17_prep_data_for_ai.md)
