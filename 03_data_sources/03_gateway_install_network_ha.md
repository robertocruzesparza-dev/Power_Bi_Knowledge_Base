---
id: 03.gateway_install_network_ha
title: Gateway installation, network ports and clusters
domain: data_sources
type: how-to
level: intermediate
tags: [gateway, admin, monitoring, limits]
summary: Requirements to install the on-premises data gateway, required outbound ports, cluster rules, load balancing and update cadence.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: high
sources: [S305, S308, S309, S310, S313, S2511, S2515, S2517, S2516, S3019]
references: []
related: [03.gateway_types_compared, 03.gateway_sso_and_data_sources, 22.gateway_release_history]
---

# Gateway installation, network ports and clusters

Purpose: prepare a machine and network for a standard on-premises data gateway and keep it healthy.

## Requirements (Fact, S308)

- .NET Framework 4.8.
- Windows 10 or 11, or Windows Server 2019, 2022 or 2025. About 4 GB of disk for performance logs.
- Recommended: 8-core CPU, 8 GB memory, 64-bit Windows Server, SSD storage for spooling, and a wired network.
- Not supported: Server Core, Windows containers and domain controllers. The installer must be a local admin.
- Do not use a laptop or any machine that may sleep or go offline.
- One standard gateway per computer. Install extra cluster members on different machines.
- For Windows authentication, install on a machine in the same Microsoft Entra environment as the sources.

## Network (Fact, S310)

- Outbound only. The gateway uses Azure Relay. Allowed outbound TCP ports: 80, 443, 433, 5671, 5672, and 9350 through 9354. No inbound ports are needed.
- Run the network ports test inside the gateway app to see the exact list for your region.
- Sovereign clouds support installing gateways only in the tenant's default Power BI region (Fact, S308).

## Steps

1. Download the installer and choose On-premises data gateway (standard mode).
2. Sign in with a work account and register the gateway with a name that is unique in the tenant and a recovery key. Store the key safely; Microsoft cannot retrieve it.
3. In the Power BI service, open Settings > Manage connections and gateways to add data sources (see [gateway SSO and data sources](03_gateway_sso_and_data_sources.md)).
4. Add gateway admins and, for resilience, add more gateways to form a cluster.

## Clusters and load balancing (Fact, S309)

- A cluster holds up to 10 members. Existing clusters above 10 keep running but cannot add members until one is deleted.
- The service uses the primary member unless it is unavailable.
- Keep all members on the same gateway version.
- Optionally enable "Distribute requests across all active gateways in this cluster". The default pick is random. With it disabled, requests go round-robin.
- Throttling settings live in the GatewayCore config file: CPUUtilizationPercentageThreshold, MemoryUtilizationPercentageThreshold and ResourceUtilizationAggregationTimeInMinutes. A value of 0 disables the CPU or memory threshold.
- Disable or remove offline members; an offline member can slow queries.
- For Dataflow Gen2, the primary member must be up to create or edit connections.

## Updates

Microsoft supports only the last six releases. The newest listed on 2026-11-02 is October 2026, build 3000.338 (Fact, S3019). See [gateway release history](../22_release_roadmap/22_gateway_release_history.md).

## Common mistakes

- Blocking port 443 or the Service Bus ranges at the firewall.
- Running mixed versions in one cluster.
- Leaving a gateway more than six releases behind.

## See also

- [Gateway types compared](03_gateway_types_compared.md)
