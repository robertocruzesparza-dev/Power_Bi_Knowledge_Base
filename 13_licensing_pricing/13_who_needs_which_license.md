---
id: 13.who_needs_which_license
title: Who needs which license
domain: licensing_pricing
type: decision
level: beginner
tags: [licensing, decision-guide, power-bi]
summary: Decision table showing the license each role needs to create, share, view and embed Power BI content, depending on capacity size.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1501, S1503, S1510, S1512, S1513, S1530, S2704]
references: []
related: [13.license_types_overview, 13.fabric_capacity_f_skus, 12.external_sharing_b2b]
---
## Purpose

Use this page to answer "does this person need a paid license?" The answer depends on the role and on where the content lives.

## Key facts

- Fact: The F64 line decides viewing rules. On F64 or larger, and on P capacities, a user with a Free license and a workspace Viewer role can view Power BI content [S1501].
- Fact: On F SKUs below F64, and on all A and EM SKUs, each viewer needs Pro, PPU or an individual trial in the "embed for your organization" and Microsoft 365 app cases [S1501, S1512].
- Fact: Publishing to a workspace other than My workspace needs Pro or PPU, even on a large capacity [S1501, S1503].

## Decision table

| Person and task | Content location | License needed |
|---|---|---|
| Author publishing a report | Any workspace except My workspace | Pro or PPU |
| Reader viewing an app or report | F64+ or P capacity, Viewer role | Free |
| Reader viewing an app or report | Pro workspace, or F2 to F32 | Pro or PPU |
| Reader viewing | PPU workspace | PPU |
| Contributor, Member or Admin role | Any capacity | Pro or PPU |
| Creator of lakehouse or notebook | F or trial capacity | Free is enough |
| Embedded customer (app owns data) | F, A, EM or P capacity | None for end users |
| External guest viewer | F64+ capacity | Free (guest) |
| External guest viewer | Pro workspace | Pro, own or assigned |
| Person who invites guests | Any | Pro or PPU |

Sources: S1501, S1510, S1512, S1530.

## How to decide

1. Find the workspace type: Pro, PPU, Fabric, or Premium.
2. If it is a capacity, find its size. F64 and above unlock Free viewing.
3. List roles. Anyone with a role above Viewer needs Pro or PPU.
4. Check embedding. App-owns-data needs no end-user license, but a service principal or master account must publish [S1512].

## Worked example

A school district buys F32 to save money. Viewers then need Pro, so 2,000 viewers cost more than one F64 with Free viewers. Compare per-user cost with the F64 step before choosing a size. See [Pricing reference](13_pricing_reference.md) for current rates.

## Common mistakes

- Assuming an F32 capacity lets Free users view. It does not [S1501].
- Assigning a Pro trial to a person who must invite guests. Pro trial users cannot invite guests [S1530].
- Forgetting the sharer in an external share needs Pro or PPU [S1510].

## Limits and version notes

PPU users can only share with other PPU users inside a PPU workspace [S1513]. Guest license rules differ across clouds. Bring-your-own license does not work across Azure clouds [S1530].

## See also

- [License types overview](13_license_types_overview.md)
- [External sharing and B2B](../12_admin_governance_security/12_external_sharing_b2b.md)
