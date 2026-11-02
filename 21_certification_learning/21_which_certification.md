---
id: 21.which_certification
title: Which Microsoft certification should I take
domain: certification_learning
type: decision
level: beginner
tags: [certification, decision-guide, power-bi, fabric]
summary: A decision guide that maps roles and goals to PL-300, DP-600, DP-700, or DP-900, plus a simple study plan.
status: n/a
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S901, S904, S907, S910, S912, S2900, S2901]
references: []
related: [21.pl300_exam, 21.dp600_exam, 21.certification_landscape, 21.learning_paths]
---
## Purpose

Pick the exam that matches your daily work. The mapping below is an inference from the role descriptions on each Microsoft certification page.

## Decision table

| If you mostly... | Take | Why |
|---|---|---|
| Build reports and simple models in Desktop, publish to the service | PL-300 | Covers Power Query, DAX, visuals, workspaces, security |
| Own enterprise semantic models, lakehouses, warehouses; use SQL, KQL, DAX | DP-600 | Role is analytics engineer; 45-50% is data preparation |
| Build pipelines, notebooks, streaming, orchestration in Fabric | DP-700 | Role is data engineer; PySpark, SQL, KQL |
| Are new to data and cloud services | DP-900 | Beginner; includes Power BI basics; does not expire |
| Want to prove report skills only | PL-300 | There is no separate visuals-only exam in the lists checked |

## Worked example

Maria builds sales dashboards and manages a workspace for her team. She writes DAX measures but does not load lakehouse data. PL-300 fits her. If her company moves to Direct Lake models and she starts owning them, DP-600 becomes the next step. Inference.

## A 6-week study plan for PL-300

1. Week 1: read the study guide; do the Power Query learning path.
2. Week 2: modeling path; build a star schema and a date table.
3. Week 3: DAX, including CALCULATE and time intelligence.
4. Week 4: report design, bookmarks, drillthrough, accessibility.
5. Week 5: service tasks: workspaces, apps, refresh, subscriptions, row-level security.
6. Week 6: practice assessment, sandbox, gap review.

## Common mistakes

- Choosing DP-600 for report design skills. Only a small part of it covers semantic model design.
- Booking an exam without checking the study-guide date. Both DP-600 and DP-700 change on 2026-10-19.

## See also

- [PL-300 exam](21_pl300_exam.md)
- [DP-600 exam](21_dp600_exam.md)
- [Certification landscape](21_certification_landscape.md)
- [Learning paths](21_learning_paths.md)
