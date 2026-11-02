---
id: 17.copilot_requirements_capacity
title: Copilot requirements, capacity and cost
domain: ai_features
type: reference
level: intermediate
tags: [copilot, capacity, licensing, tenant-setting, limits]
summary: Capacity, tenant setting, region and workspace requirements for Copilot in Power BI, plus how usage is metered and billed in capacity units.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2101, S2102, S2111, S2113, S2532, S2533, S2534]
references: []
related: [17.copilot_overview, 17.copilot_privacy_data]
---

## Table of Contents

- [Purpose](#purpose)
- [Requirements](#requirements)
- [Standalone and app Copilot](#standalone-and-app-copilot)
- [Fabric Copilot capacity](#fabric-copilot-capacity)
- [Metering](#metering)
- [Common mistakes](#common-mistakes)

# Copilot requirements, capacity and cost

## Purpose
Explain what must be true before Copilot works, and how it consumes capacity. Check the linked pages again before budgeting: rates and regions change.

## Requirements
| Requirement | Detail | Source |
|---|---|---|
| Capacity | Paid Fabric F2 or higher, or Power BI Premium P1 or higher. Trial and free SKUs are not supported | S2101 |
| Licence | Pro or PPU alone is not enough; organizational capacity is needed | S2101 |
| Tenant setting | "Users can use Copilot and other features powered by Azure OpenAI" must be on | S2101 |
| Region | Capacity must be in a supported region. Standalone and app Copilot are not yet in 12 listed regions (see prep-data file) | S2101, S2532 |
| Sovereign clouds | Not supported | S2101 |
| Outside US or EU data boundary | Disabled until admin enables the cross-geo processing tenant setting | S2101, S2102 |
| Desktop | Write access to a workspace on paid Fabric or Premium capacity | S2101 |
| Service pane | Report in a workspace on P1+ or paid Fabric; read access to get summaries | S2101 |
| Narrative visual or generated pages | Edit access to the report or workspace, or build access to the model | S2101 |

## Standalone and app Copilot
- Fact: the tenant-level setting must be on. A capacity-level delegation alone is not enough [S2101].
- Fact: the setting "Users can access a standalone, cross-item Power BI Copilot experience (preview)" must also be on [S2101].
- Fact: usage bills to a Fabric Copilot capacity if one exists; otherwise the service auto-selects an eligible workspace on an F2+ capacity. Users change it under More > Manage workspace [S2101].
- Fact: app Copilot is on by default per app, under Advanced settings > Show Copilot in app navigation [S2101].

## Fabric Copilot capacity
- Fact: an F2+ or P1+ capacity can be designated to collect Copilot billing for a user group, including Desktop and Pro or PPU workspaces [S2111].
- Fact: it must be in the tenant home region; one Copilot capacity per user; Embedded licence mode is not supported [S2111].
- Fact: the Fabric admin enables Copilot and authorizes capacity admins; the capacity admin assigns users [S2111].

## Metering
- Fact: billing is by tokens: input 100 CU seconds per 1,000 tokens, cached input 10, output 400 [S2113].
- Worked example (from S2113): 2,000 input and 500 output tokens equal 400 CU seconds, about 6.67 CU minutes.
- Fact: Copilot runs as a background job, smoothed over 24 hours. Downstream DAX queries and refreshes bill separately [S2101, S2113].
- Fact: rates may change at any time with notice [S2113].
- Fact: watch usage in the Fabric Capacity Metrics app, operation "Copilot in Fabric" [S2113].

## Common mistakes
- Piloting on a trial capacity. Power BI Copilot pages say trials are unsupported (S2101, S2533). The Fabric notebooks Copilot page says trials work for that workload; treat Power BI as unsupported.
- Enabling Copilot only at capacity level for standalone Copilot.
- Rolling out email-subscription summaries widely before measuring cost. Pilot first [S2113].

## See also
- [Copilot overview](17_copilot_overview.md)
- [Privacy and data](17_copilot_privacy_data.md)
