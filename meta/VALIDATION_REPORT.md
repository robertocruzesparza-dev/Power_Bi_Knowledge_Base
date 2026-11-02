---
id: meta.validation_report
title: Validation report
domain: meta
type: reference
level: intermediate
tags: [metadata, reference]
summary: Results of validation, re-verification, cold-read, and adversarial checks for this build, with limits stated.
status: n/a
volatile: false
last_verified: 2026-10-08
confidence: moderate
sources: []
references: []
related: []
---

# Validation report

## Automated validation

`python tools/validate_kb.py` checks line limits, front matter, tags, links, orphans, domain indexes, and table size. The final run is re-run on the extracted zip. One style warning remains: a semicolon-separated list in the tenant settings catalog averages 20.3 words per sentence. The tool tests (`python tools/test_tools.py`) pass 5 of 5.

## Re-verification (fact check)

Three verifiers re-checked claims on 2026-10-08, and three refreshers repeated the pass on 2026-10-09 for every volatile file last verified on 2026-10-07. Details: [verification log](VERIFICATION.md).

| Result | Count |
|---|---|
| Confirmed | 187 |
| Corrected in the KB | 53 |
| Unresolved | 26 |

All 152 files marked `volatile: true` now carry a `last_verified` of 2026-10-08 or later. Two to three files were only partly checked; the log says which. Pricing, limit, and feature-status claims in the pricing, licensing, and service domains were the priority.

## Adversarial pass

Each verifier tried to disprove its claims by searching for newer pages, deprecations, and contradictions. This was folded into the re-verification. It was not a separate pass on a fixed list of 20 claims, so the requirement is only partly met.

## Notable corrections

- Q&A retirement: current Learn pages say February 2027. The January 2026 notes said December 2026.
- Real-time streaming: new streaming models can be created until 2027-10-31. An older tutorial note was wrong.
- Model size: the S017/S018 difference was a small versus large storage format difference, not a conflict.
- Data agents: generally available. DAX user-defined functions: generally available.
- Sensitivity-label licensing wording changed to match the current Learn page.

## Unresolved (see the log for the full list)

- End date of Premium P SKU for Enterprise Agreement customers: Microsoft gives no fixed date.
- Fabric prices: the Azure pricing page shows no amounts. Rates come from the Azure Retail Prices API (West US 2) and are US dollars only.
- Meaning of the new On-Demand Usage meters.
- Deployment pipeline rules for Direct Lake on OneLake: two Microsoft pages disagree.
- Whether PBIR reports work in deployment pipelines: one page says no.
- Tabular Editor 3 price. DAX Studio v3.6.1 and Bravo v1.0.13 are the latest releases, but their GitHub dates show no year.
- No Power BI feature summary for September or October 2026 was published at the last check, so whether August previews reached general availability is unknown.

## Cold-read test

15 of 15 questions reached the answer in 3 reads. See [cold-read test](COLD_READ.md).

## Limits of this validation

- Many claims rest on search snippets, not full page reads. The sources register marks access level.
- Expert and community sources are few. Microsoft Learn dominates.
- Two sites (Power BI blog, Guy in a Cube) returned errors, so their content is not used directly.
- The validator checks structure and style, not truth.
