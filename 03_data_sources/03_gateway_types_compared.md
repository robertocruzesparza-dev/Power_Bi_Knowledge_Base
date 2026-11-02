---
id: 03.gateway_types_compared
title: Gateway types compared: standard, personal, VNet
domain: data_sources
type: comparison
level: beginner
tags: [gateway, data-source, comparison, refresh]
summary: Side-by-side comparison of the standard on-premises, personal mode and virtual network data gateways, with limits and when to choose each.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S305, S306, S307, S2511, S2512, S2513, S2514]
references: []
related: [03.gateway_install_network_ha, 03.gateway_sso_and_data_sources, 03.import_directquery_support]
---

# Gateway types compared: standard, personal, VNet

Purpose: choose the right gateway for a data source that Power BI cannot reach directly.

## Key facts

- A gateway is a bridge between a network-protected source and Microsoft cloud services. It makes outbound connections only and needs no inbound ports (Fact, S305).
- Three kinds exist: standard on-premises, on-premises personal mode, and VNet (virtual network) data gateway (Fact, S305).

## Comparison

| Feature | Standard on-premises | Personal mode | VNet data gateway |
|---|---|---|---|
| Install | You install on a Windows machine | You install on your PC | None; Microsoft managed |
| Users | Many users, many sources | One user, not shareable | Many users, many sources |
| Services | Power BI, Power Apps, Power Automate, Logic Apps, Azure Analysis Services, Fabric | Power BI only | Fabric Dataflow Gen2, pipelines, Copy Job, Mirroring, Power BI semantic models, paginated reports |
| DirectQuery and live connection | Yes | No | Semantic models on listed Azure services; DirectQuery not separately verified |
| Clustering, high availability | Yes, up to 10 members | No | Not stated |
| Needs local admin to install | Yes | No | Not applicable |
| Central management | Yes | No | Yes |

## Use each when

- Personal mode: one author refreshing a few Import models, no shared sources. Each user can run one personal gateway; a new install replaces the old one (Fact, S306).
- Standard: shared sources, DirectQuery, composite models, clustering, central auditing (Fact, S306).
- VNet: Azure sources behind private endpoints or Private Link, with no hardware to run (Fact, S307).

## Limits

- Standard and personal: 1,000 data sources maximum per gateway cluster (Fact, S305). VNet: 1,000 per gateway (Fact, S307).
- Power BI DirectQuery through a gateway has a 16 MB uncompressed response limit (Fact, S305).
- Gateways for Power Apps, Power Automate and Logic Apps have a 2 MB request limit and 8 MB compressed read response limit (Fact, S305).
- Microsoft supports only the last six gateway releases, and a new one ships monthly (Fact, S305).
- VNet gateway needs a Premium (P), Fabric (F) or A4-or-higher capacity SKU. F8 and above is recommended, though all F SKUs work. Power BI dataflows and datamarts are not supported (Fact, S307).
- VNet gateway region, subscription and resource group of the VNet cannot be changed after creation (Fact, S307).
- Re-verified 2026-10-08 (S2513, S2514): Fabric trial capacities can also host a VNet gateway for evaluation, and the gateway bills 4 CU per member while it is up, each member running six concurrent queries. It is not supported in GCC L2.
- Personal mode does not support composite models, VNet gateway, clustering or high availability (Fact, S306).
- An on-premises gateway cannot be used when Azure Private Link is enabled for the tenant; use a VNet gateway (Fact, S308).

## See also

- [Gateway install, network and high availability](03_gateway_install_network_ha.md)
- [Gateway SSO and data sources](03_gateway_sso_and_data_sources.md)
