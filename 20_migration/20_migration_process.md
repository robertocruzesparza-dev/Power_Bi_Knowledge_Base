---
id: 20.migration_process
title: Migrating to Power BI: process and stages
domain: migration
type: concept
level: intermediate
tags: [migration, best-practice, governance]
summary: Summarizes Microsoft's five-stage approach to migrating from a third-party BI tool to Power BI, with success practices and a rebuild-not-convert principle.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1535, S1542, S1543, S1544]
references: []
related: [20.migration_checklist, 20.tableau_to_power_bi, 12.governance_frameworks]
---
## Purpose

This page gives the common method for any BI migration. Tool-specific pages (Tableau, Qlik, Excel, SSRS, Cognos) follow it.

## Key facts

- Fact: Microsoft's migration series assumes you already decided to move to Power BI and focuses on the Power BI service [S1535].
- Fact: Formal migration usually runs in parallel with building new Power BI solutions. New work wins buy-in and gives authors practice [S1535].
- Fact: Four phases: set up and evaluate; create new solutions quickly; migrate assets; adopt, govern and monitor [S1535].
- Fact: Migration has pre-migration steps plus five stages [S1535].

## The five stages

| Stage | Name | Output |
|---|---|---|
| 1 | Gather requirements and prioritize | Prioritized inventory of reports and data |
| 2 | Plan for deployment | Solution-level deployment decisions |
| 3 | Conduct proof of concept | Narrow working solution that reduces risk |
| 4 | Create and validate content | Validated production-ready solution |
| 5 | Deploy, support and monitor | Production solution in use |

Source: S1535. Stages 2 and 3 can overlap. Treat the proof of concept as the start of the real solution, not a throwaway.

## Success practices

- Executive sponsor with authority over Power BI outcomes.
- Training, support and a communication plan with a feedback loop.
- Quick wins first. Rebuild around the business question, not the old layout.
- Modernize: remove manual data prep, retire unused reports, consolidate duplicates.
- Short iterations and small proofs of concept.
- Expect resistance, especially from experts of the old tool.
- Realistic budget and timeline [S1535].

## Rebuild, do not convert

Consultancy and vendor sources agree that reports and calculations rarely convert one-to-one [S1542, S1543, S1544] (community and vendor, tier 3). Evaluation context in DAX differs from per-worksheet calculation in Tableau or Qlik set analysis. Automation tools help with inventory and first drafts but need manual review. Treat vendor figures on automation rates as unverified claims.

## Worked example

A district has 300 Cognos reports. Stage 1 inventories usage and finds 90 used in the last year. Stage 2 groups them into six subject areas. Stage 3 builds one semantic model and three reports for the finance area. Stage 4 reconciles totals against Cognos. Stage 5 turns off Cognos finance after a parallel month.

## Common mistakes

- Copying layouts instead of redesigning for the question.
- Duplicating logic in every report. Put measures in a shared semantic model.
- Skipping side-by-side reconciliation before cutover [S1542].
- Ignoring licensing and capacity planning. See [Who needs which license](../13_licensing_pricing/13_who_needs_which_license.md).

## Limits and version notes

Microsoft's series is tool-neutral and does not give per-tool concept maps. Per-tool maps in this KB come from community and consultancy sources (tier 3) plus labeled inference.

## See also

- [Migration checklist](20_migration_checklist.md)
- [Governance frameworks](../12_admin_governance_security/12_governance_frameworks.md)
