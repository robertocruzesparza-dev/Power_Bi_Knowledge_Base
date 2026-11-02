---
id: meta.automation_audit
title: Automation audit
domain: meta
type: reference
level: intermediate
tags: [metadata, tooling]
summary: Every place the build chose code or hand-written text, with the reason, using the four-part test.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: [meta.coverage]
---

# Automation audit

Test: code wins when (a) 5 or more items share one schema, (b) content must stay consistent across files, (c) content changes often, or (d) someone would otherwise scan by hand. The audit read the whole KB (290 Markdown files) after drafting.

## Decisions

| Candidate | Items | Decision | Reason |
|---|---|---|---|
| Domain indexes, INDEX, JSONL index | 240 files | Generate: `build_index.py` | Tests a, b, c, d all pass. Front matter is the single source. |
| Glossary ordering and sharding | 319 terms | Generate: `build_glossary.py` | Tests a, b, d. Workers supplied terms in separate files. |
| Gaps, claims, sources index | 96 / 83 / 435 rows | Generate: `build_meta.py` | Tests a, c. Many workers wrote the inputs. |
| Table of contents | files over 100 lines | Generate: `add_toc.py` | Tests b, d. Must match headings exactly. |
| Front matter, tags, links, limits, orphans | all files | Validate: `validate_kb.py` | Tests b, d. Cannot be trusted by eye. |
| Style lint (sentence length, acronyms) | all prose | Validate: `lint3c.py` | Tests b, d. Reports warnings, not errors. |
| Split proposals | oversize files | Assist: `split_file.py` | Test d. Proposes only; a person edits. |
| Freshness of volatile files | volatile files | Report: `check_freshness.py` | Test c. Prices and previews age fast. |
| DAX function catalogs | 7 reference files | Hand-written from Learn, validated structurally | No `data/` source of truth was built. Test a passes, so a future scraper to `data/` plus a renderer is justified. |
| M function catalogs | 7 reference files | Same as DAX | Same reason. |
| Connector catalog | 3 reference files | Same as DAX | Parsed from Learn pages by a worker script that is not kept in the KB. |
| Tenant settings, audit operations, error catalogs | 6 reference files | Hand-written | Under 80 rows each and the source layout is irregular. |
| License and SKU comparison | few tables | Hand-written | Under 15 rows. Wrong precision is the risk, so a person checks each value. |
| Release timeline | 6 files | Hand-written | Items are narrative, not one schema. |
| REST endpoint list | 1 reference | Hand-written | Grouped by area; below the size where code pays off. |
| Visual types | 1 table | Hand-written | Fewer than 40 rows with prose descriptions. |

## Not built

`render_tables.py` was not built. The tool needs `data/` tables as the source of truth, and the build did not create any. Building it now would make a second copy of the catalogs. Recommended next step: export the catalogs to `data/*.csv`, then add the renderer.

## Tools in `tools/`

`kbcommon.py`, `lint3c.py`, `validate_kb.py`, `build_index.py`, `build_glossary.py`, `build_meta.py`, `add_toc.py`, `split_file.py`, `check_freshness.py`.
