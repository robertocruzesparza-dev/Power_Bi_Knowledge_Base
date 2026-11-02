---
id: 21.dp600_exam
title: DP-600 Fabric Analytics Engineer exam
domain: certification_learning
type: reference
level: intermediate
tags: [certification, fabric, semantic-model, reference]
summary: Exam code, skill areas, weights, and the 19 October 2026 update for the Fabric Analytics Engineer Associate certification.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S904, S905, S908, S2612, S2900, S2902]
references: []
related: [21.pl300_exam, 21.certification_landscape, 21.learning_paths, 21.which_certification]
---
## Purpose

DP-600 leads to Microsoft Certified: Fabric Analytics Engineer Associate. It targets people who build and manage semantic models, lakehouses, and warehouses in Microsoft Fabric.

## Key facts

- Exam code: DP-600. Credential page showed Last Updated 2026-07-21 on 2026-10-08 (earlier note said 2026-09-18). Fact.
- Duration 100 minutes, proctored, passing score 700. Fact.
- Languages: English, Japanese, Chinese (Simplified), German, French, Spanish, Portuguese (Brazil). Fact.
- Renewal every 12 months through the free online assessment. Fact.
- The English exam updates on 2026-10-19, 12 days after the verification date. Fact.
- The study guide lists the skills "as of October 19, 2026". The earlier objective list was not retrieved here. Unknown; check the Microsoft page before an exam taken before that date.
- Candidates need SQL, Kusto Query Language (KQL), and Data Analysis Expressions (DAX). Fact.

## Skill areas from 19 October 2026

| Area | Weight |
|---|---|
| Maintain a data analytics solution | 25-30% |
| Prepare data | 45-50% |
| Implement and manage semantic models | 25-30% |

The change log marks only "Query and analyze data" as a minor change in this update. Fact.

## Detail by area

Maintain a data analytics solution:

- Workspace-level and item-level access controls; row-level, column-level, object-level, and file-level security.
- Sensitivity labels and endorsement.
- Version control, Power BI Desktop projects (.pbip), deployment pipelines, impact analysis, XMLA endpoint deployment.
- Reusable assets: .pbit templates, .pbids data source files, shared semantic models.

Prepare data:

- Connections, OneLake catalog, Real-Time hub, choosing a data store, OneLake integration for Eventhouse and semantic models.
- Views, functions, stored procedures, star schemas, denormalizing, merging, cleaning.
- Querying with the visual query editor, SQL, KQL, and DAX.

Implement and manage semantic models:

- Storage mode choice, star schema, bridge tables, many-to-many relationships.
- DAX with variables, iterators, windowing, and information functions; calculation groups, dynamic format strings, field parameters.
- Large semantic model storage format; composite models.
- Direct Lake configuration, including fallback and refresh; choosing Direct Lake on OneLake versus on the SQL analytics endpoint; incremental refresh.

## Choosing PL-300 or DP-600

PL-300 suits report authors and analysts. DP-600 suits model owners who work across lakehouses, warehouses, and enterprise semantic models. See [Which certification](21_which_certification.md).

## Limits and version notes

- Most questions cover generally available features; popular preview features can appear. Fact.
- Localized exams follow the English update by about eight weeks. Fact.
- Confidence is moderate because only the post-update objective list was read.

## See also

- [PL-300 exam](21_pl300_exam.md)
- [Certification landscape](21_certification_landscape.md)
- [Learning paths](21_learning_paths.md)
