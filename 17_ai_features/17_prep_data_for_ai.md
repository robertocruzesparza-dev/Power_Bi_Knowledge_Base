---
id: 17.prep_data_for_ai
title: Prep data for AI and Approved for Copilot
domain: ai_features
type: how-to
level: intermediate
tags: [copilot, semantic-model, best-practice]
summary: How to improve Copilot answers with AI data schemas, AI instructions, verified answers, the skill picker, and the Approved for Copilot flag.
status: preview
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2109, S2532, S2535]
references: []
related: [17.copilot_overview, 17.qna_deprecation]
---

# Prep data for AI and Approved for Copilot

## Purpose
Reduce ambiguity so Copilot returns consistent, grounded answers. The feature is labelled preview [S2109]. Example: set a verified answer for "monthly revenue" so Copilot returns your trusted visual.

## Key facts
- Fact: three tools exist: AI data schema, AI instructions, verified answers [S2109].
- Fact: you can author them in Desktop (button next to Copilot on the Home ribbon) and in the service. Everyone can consume them wherever Copilot runs [S2109].
- Fact: settings save on the semantic model, not the report [S2109].
- Fact: AI instructions and schemas are stored in the linguistic schema definition (LSDL) [S2109].
- Fact: Q&A must be enabled on the semantic model [S2109].
- Fact: results are not guaranteed identical; AI is nondeterministic [S2109].

## Steps
1. Open the model in Desktop, or the model page in the service.
2. Select Prep data for AI. Edit the schema and instructions, then apply.
3. For a verified answer, select a visual, open the ... menu, choose set verified answer, add trigger phrases. In the service you need edit mode, a Copilot-enabled workspace and authoring permission on the model.
4. Test in the Desktop Copilot pane. Close and reopen the pane after each save.
5. Use the skill picker to simulate surfaces: answer questions, analyze report visuals, create report pages.
6. Troubleshoot with the "How Copilot arrived at this" (HCAAT) detail and Download diagnostics in the pane menu.
7. In the service, open model settings > Approved for Copilot, tick it, apply.

## Approved for Copilot
- Fact: formerly called "prepped for AI" [S2109].
- Fact: standalone Copilot removes its friction treatment for answers from approved models and their reports [S2109].
- Fact: there is no way to mark a report, dashboard or app as approved; only models [S2109].
- Fact: an admin setting can restrict standalone Copilot to approved items only [S2109].
- Fact: changes usually apply within an hour, up to 24 hours for models with many reports [S2109].

## Limits and version notes
- Desktop supports Import, DirectQuery and local composite models. The service supports all model types [S2109].
- After Git or deployment pipeline changes, refresh the model to sync LSDL. DirectQuery and Direct Lake: once a day at most [S2109].
- Region conflict (re-verified 2026-10-08): this page lists Spain Central, Qatar, India West and Mexico as lacking standalone Copilot [S2109]. The overview page lists 12 regions without standalone Copilot and Copilot in apps: India West, Indonesia Central, Korea South, Malaysia West, New Zealand North, Qatar Central, Taiwan North, Taiwan North West, UAE Central, France South, Germany North, Norway West [S2532]. The overview is the fuller list; the prep-data list looks stale. Confirm against the Fabric region availability page [S2535].

## See also
- [Copilot overview](17_copilot_overview.md)
- [Q&A deprecation](17_qna_deprecation.md)
