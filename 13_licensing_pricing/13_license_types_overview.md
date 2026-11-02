---
id: 13.license_types_overview
title: Power BI and Fabric license types
domain: licensing_pricing
type: concept
level: beginner
tags: [licensing, power-bi, fabric]
summary: Explains the three per-user licenses (Free, Pro, PPU) and the capacity subscription that together decide what a person can do.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1501, S1502, S1510, S1513, S2727]
references: []
related: [13.who_needs_which_license, 13.fabric_capacity_f_skus, 13.pricing_reference]
---
## Purpose

Power BI licensing has two layers. A per-user license says what one person may do. A capacity says how much compute the content gets. Most confusion comes from mixing the two layers.

## Key facts

- Fact: There are three per-user licenses: Fabric (Free), Power BI Pro, and Premium Per User (PPU) [S1513].
- Fact: A capacity is a pool of compute bought for the whole organization. Fabric F SKUs are the recommended type [S1501].
- Fact: The Free license is assigned on first sign-in to the Fabric portal when Fabric is enabled [S1501].
- Fact: Power BI Pro is included with each Microsoft 365 E5 license [S1510].
- Fact: PPU includes every Pro capability, so a PPU user does not need a separate Pro license [S1502].
- Fact: Microsoft renamed "license mode" to "workspace type". Only the term changed [S1501].

## How it works

| License | Can do | Cannot do |
|---|---|---|
| Free | View own content; view shared content on F64+ or P capacity with the Viewer role | Publish to other workspaces; share in shared capacity |
| Pro | Publish, share, subscribe; collaborate with other Pro users | Use Premium-only features such as XMLA write or 100 GB models |
| PPU | Everything Pro does, plus most Premium features per user | Create non-Power BI Fabric items; use Multi-Geo; share with non-PPU users in a PPU workspace |

Sources: S1501, S1502, S1513.

## Workspace types

A workspace type ties a workspace to a license and capacity pairing. The main types are Power BI Pro, PPU, Power BI Embedded (A SKU), Fabric (F SKU), Fabric Trial, and Power BI Premium (P SKU) [S1501].

- A PPU workspace is not a capacity. It uses a shared Premium feature pool [S1501].
- PPU does not provision Fabric. To create lakehouses, warehouses or notebooks you still need an F or trial capacity [S1501].

## Worked example

A team of 40 wants to publish reports and have 400 readers view them. With Pro only, all 440 people need Pro. With an F64 capacity, only the 40 authors need Pro. The 400 readers need the Free license and a Viewer role [S1501].

## Common mistakes

- Buying PPU and expecting Fabric lakehouses to work. PPU is a per-user feature set, not a capacity [S1501].
- Assuming Free users can publish. They cannot publish outside My workspace [S1501].
- Forgetting that creators still need Pro or PPU on an F64 or P capacity [S1503].

## Limits and version notes

Prices and limits change. See [Pricing reference](13_pricing_reference.md) and [Limits and quotas](13_limits_and_quotas.md). Grace periods after a license ends are 90 days for volume licenses, 30 days for direct purchases, and none for trials [S1510]. The Microsoft 365 lifecycle page is more detailed: for Enterprise and volume licenses a monthly or annual term has 30 days expired, multi-year has 90 days; confirm in your agreement (Inference: the Power BI page simplifies) [S2727].

## See also

- [Who needs which license](13_who_needs_which_license.md)
- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
