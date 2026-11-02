---
id: 00.readme
title: Master Power BI Knowledge Base
domain: meta
type: index
level: beginner
tags: [index, navigation]
summary: Entry point for the Power BI knowledge base, its topic coverage, AI usage guidance, and maintenance tools.
status: n/a
volatile: false
last_verified: 2026-11-02
confidence: high
sources: []
references: []
related: [00.start, 00.ai_guide, 00.index]
---

# Master Power BI Knowledge Base

This repository is a structured reference library for Microsoft Power BI and closely related Microsoft Fabric capabilities. It brings together conceptual guides, procedures, decision guides, troubleshooting, reference catalogs, source registers, and maintenance tools.

## Start here

- [Quick start and navigation](00_START_HERE.md)
- [AI model usage guide](AI_GUIDE.md)
- [Topic index](INDEX.md)
- [Glossary](GLOSSARY.md)
- [Known coverage gaps](meta/GAPS.md)
- [Sources register](meta/SOURCES.md)

The content is organized into 23 numbered topic domains. Individual articles include structured metadata, status and freshness notes, and source IDs where applicable. This is a broad, actively aging reference—not an exhaustive or permanently current statement of every Power BI feature. Verify volatile facts against current Microsoft documentation before relying on them.

## Maintenance

The knowledge base uses Python's standard library. Run these commands from the repository root:

```powershell
python tools\build_glossary.py
python tools\build_index.py
python tools\validate_kb.py
python tools\test_tools.py
python tools\check_freshness.py
```

Update source material and its metadata before rebuilding generated indexes. See [the changelog](meta/CHANGELOG.md), [validation report](meta/VALIDATION_REPORT.md), and [metadata index](meta/INDEX.md).
