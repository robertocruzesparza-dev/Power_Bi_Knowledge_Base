---
id: 01.key_concepts_terminology
title: Key concepts and terminology
domain: foundations
type: reference
level: beginner
tags: [power-bi, glossary, semantic-model, report, dashboard, workspace]
summary: Plain definitions of the core Power BI terms, including renamed terms such as dataset to semantic model.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S001, S003, S009]
references: []
related: [01.architecture, 01.product_family_and_components]
---
## Purpose

Read this first when a Power BI article uses a word you do not know. The terms below appear in nearly every other file.

## Core terms

| Term | Meaning (paraphrased from S003 unless noted) |
|---|---|
| Visualization or visual | A chart, table, or map in a report; interactive |
| Semantic model | Container of data and logic that reports are built on; can combine several sources |
| Report | One or more pages of visuals based on a single semantic model |
| Dashboard | One screen of tiles pinned from reports; built in the service |
| App | Bundle of dashboards and reports published to a wider audience |
| Workspace | Shared area where creators store and manage items |
| Capacity | Dedicated compute resources for performance and scale |
| Workbook | An Excel file uploaded to the service |
| Dataflow | Reusable data-preparation steps stored in the service |
| Copilot | AI assistant in Power BI; needs paid Fabric (F2 or higher) or Premium (P1 or higher) capacity per S003 |
| Tenant | The organisation's Microsoft Entra directory where Power BI runs (S009) |
| SKU | Stock-keeping unit; a capacity size such as F64 (S009) |

## Renamed terms

| Old | New | Note |
|---|---|---|
| Dataset | Semantic model | Same object (S003) |
| License mode | Workspace type | Terminology change only (S009) |
| Power BI Premium capacity (P) | Fabric capacity (F) | P SKUs are retiring (S026) |
| Power BI Embedded A SKUs | Still exist | Not part of the P retirement (S026) |

## Report versus dashboard

- A report has pages and filters and is based on one model.
- A dashboard collects tiles from many reports and models on one canvas.
- Inference: use a report to explore; use a dashboard to monitor.

## Roles

- Creators (designers) build and publish. Consumers (business users) view and interact (S003).
- Workspace roles are Admin, Member, Contributor, and Viewer (S003).

## Common mistakes

- Searching old articles for "dataset" and missing results. Search for "semantic model" too.
- Saying "premium workspace" when you mean a PPU workspace. They are different (S007).
- Calling a Fabric workspace a "Power BI workspace". Same container; the type decides which items it can hold.

## See also

- [Architecture](01_architecture_how_pieces_fit.md)
- [Licenses and capacity](01_licenses_and_capacity.md)
- [Getting started](01_getting_started_first_report.md)
