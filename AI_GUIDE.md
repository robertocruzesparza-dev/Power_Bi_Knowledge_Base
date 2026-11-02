---
id: 00.ai_guide
title: AI model usage guide
domain: meta
type: reference
level: intermediate
tags: [index, navigation]
summary: A portable retrieval and answer protocol for AI models using this Power BI knowledge base.
status: n/a
volatile: false
last_verified: 2026-11-02
confidence: high
sources: []
references: []
related: [00.start, 00.index, meta.gaps, meta.sources]
---

# AI model usage guide

This guide is model-agnostic. It describes how an AI assistant should retrieve, interpret, and cite the material in this repository; it does not depend on a particular model, framework, vector database, or agent format.

## Retrieval workflow

1. Read [00_START_HERE.md](00_START_HERE.md), then use [INDEX.md](INDEX.md) to identify the relevant domain.
2. Open that domain's `_domain_index.md`; use its summaries and tags to select the most relevant article. Search `data/index/*.jsonl` for machine-readable metadata when keyword or programmatic retrieval is available.
3. Read the article itself, including its metadata, caveats, links, and related articles. For multi-part indexes or references, follow the part links.
4. For current or disputed facts, inspect the cited primary source IDs in [the source register](meta/SOURCES.md) and verify current Microsoft documentation. Check [known gaps](meta/GAPS.md) before treating coverage as complete.

## Answer and citation rules

- Ground claims in the article text; do not infer a product capability merely from an article title or search snippet.
- Cite repository-relative article paths, and include source IDs such as `[S1234]` when the article provides them. Resolve source IDs through `meta/SOURCES.md` and its linked shards when a URL is needed.
- Separate sourced facts from recommendations or inferences. Preserve the article's qualifications, scope, and disagreements instead of silently choosing one side.
- For volatile material, report its `last_verified` date and verify current official documentation before answering as current—especially for pricing, licensing, limits, previews, deprecations, release notes, and service behavior.
- Do not present this library as complete. State relevant gaps or uncertainty and direct the reader to official Microsoft documentation when the answer is not established here.
- Use the [glossary](GLOSSARY.md) to disambiguate terminology and the [tag registry](TAGS.md) to broaden related-topic retrieval.

## Evidence and freshness

Each article's front matter records its domain, type, level, tags, status, volatility, verification date, confidence, sources, references, and related topics. Status values include `ga`, `preview`, `deprecated`, `retired`, `mixed`, and `n/a`. These fields support filtering, but do not replace reading the article or checking its sources.

The content includes Microsoft product information that changes over time. `last_verified` describes the recorded verification date, not a guarantee that a fact remains current. Treat unsupported or unresolved claims, source conflicts, and coverage gaps explicitly.

## Contents and formats

- Markdown articles are the canonical human-readable content.
- `data\index\*.jsonl` provides per-domain, one-record-per-article metadata for scripts and retrieval systems.
- `data\domains.csv` maps domain numbers, slugs, and coverage scopes.
- `meta\sources\` contains source-register shards; `meta\claims_in\`, `meta\gaps_in\`, and `meta\verification_in\` are maintenance inputs.
- `tools\` contains standard-library Python utilities for rebuilding indexes, checking freshness, and validating structure.

See the [repository overview](README.md), [topic index](INDEX.md), and [metadata index](meta/INDEX.md).
