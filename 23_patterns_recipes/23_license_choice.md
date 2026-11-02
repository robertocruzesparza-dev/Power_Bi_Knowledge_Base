---
id: 23.license_choice
title: Choosing between Pro, PPU, and Fabric capacity
domain: patterns_recipes
type: decision
level: beginner
tags: [licensing, capacity, decision-guide]
summary: Decision guide for Free, Pro, Premium Per User, and Fabric F SKU licensing based on authors, viewers, and features needed.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S1830, S1831, S1832, S2610]
references: []
related: [23.embedding_choice, 23.workspace_design, 23.import_vs_directquery_vs_direct_lake]
---
## Purpose

A user license and a workspace type work together. This guide helps you pick the cheapest combination that gives your authors and viewers what they need. It contains no prices, because prices change; check the official pricing page.

## Key facts

- Fact: There are three per-user licenses: Fabric (Free), Pro, and Premium Per User (PPU). Capacity licenses are F SKUs, and legacy P SKUs [S1831].
- Fact: Pro lets users create and share Power BI content with other Pro users [S1830].
- Fact: PPU adds most Premium features per user, but all users of a PPU workspace need PPU [S1830].
- Fact: PPU does not give a Fabric capacity. Lakehouses, warehouses, and notebooks need an F or trial capacity [S1830].
- Fact: On F64 or larger (and P SKUs), users with a Free license and Viewer role can view Power BI content. On smaller F SKUs each viewer needs Pro or PPU [S1830, S1832].
- Fact: Authors and editors need Pro or PPU for shared workspaces whatever the capacity size [S1832].
- Fact: Microsoft says PPU is more cost effective when Premium features are needed for fewer than 250 users [S1830].
- Fact: P SKUs are being retired for new purchases; consider F SKUs [S1832].

## Comparison

| Consideration | Pro workspace | PPU workspace | Fabric capacity workspace |
|---|---|---|---|
| Other Fabric workloads | No | No | Yes |
| Max semantic model size | 1 GB | 100 GB | Varies by SKU |
| Scheduled refreshes per day | 8 | 48 | 48 |
| XMLA read-write | No | Yes | Yes |
| Deployment pipelines | No | Yes | Yes |
| Dedicated compute | No | No | Yes |
| Free viewers allowed | No | No | Yes, F64 and up |

Source: [S1831]. These numbers come from a guidance page; confirm limits on the live licensing pages.

## Decision flow

1. Only you, personal use: Free license, My workspace [S1831].
2. Small team, standard sharing, small models: Pro for everyone who shares or views.
3. Need Premium features for fewer than about 250 people: PPU for each user in those workspaces [S1830].
4. Many viewers who do not author: Fabric capacity at F64 or higher so viewers can have Free licenses. Compare the cost of the capacity with the cost of Pro licenses for all viewers (Inference: do the arithmetic with current prices).
5. Need lakehouses, Direct Lake, notebooks, or Copilot-style Fabric workloads: Fabric capacity [S1827, S1830].
6. Embedding for customers: any capacity; viewers need no license [S1813].

## Common mistakes

- Buying F32 and expecting free viewers. They need F64 or larger [S1832].
- Giving authors only Free licenses.
- Assuming PPU workspaces can be shared with Pro users. Only PPU users can open them [S1830].
- Forgetting that trial capacities expire.

## Limits and version notes

Licensing is volatile. Microsoft is consolidating Premium into Fabric. Recheck pages [S1830] and [S1831] before decisions. Prices are not listed here by design.

## See also

- [Embedding choice](23_embedding_choice.md)
- [Import vs DirectQuery vs Direct Lake](23_import_vs_directquery_vs_direct_lake.md)
- [Workspace design](23_workspace_design.md)
