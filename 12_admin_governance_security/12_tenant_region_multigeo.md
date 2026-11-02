---
id: 12.tenant_region_multigeo
title: Tenant home region and Multi-Geo
domain: admin_governance_security
type: concept
level: intermediate
tags: [admin, capacity, compliance]
summary: Explains home region, Multi-Geo capacities, what data stays where, and the three kinds of tenant migration (cross-tenant, split, remap).
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S1526, S1527, S1533, S1534, S1547, S1509, S2719]
references: []
related: [12.compliance_encryption, 13.fabric_capacity_f_skus]
---
## Purpose

Data residency rules often say where data must be stored. Power BI separates the tenant home region from the capacity region. Multi-Geo uses that split.

## Key facts

- Fact: A tenant gets a home region when it first signs up, based on the Entra tenant country. The first user's location sets it [S1534, S1547].
- Fact: Find it in the Fabric portal: Help, About Microsoft Fabric, label "Your data is stored in" [S1547].
- Fact: Multi-Geo lets you create capacities in other regions and assign workspaces to them. Compute and storage for the items stay in that region. Tenant metadata stays in the home region [S1533].
- Fact: Some artifact metadata, such as report structure, can stay at rest in the home region. Some transit and processing can still occur there [S1534].
- Fact: Multi-Geo works with any capacity license except shared capacity. It is not available with PPU, because PPU data lives in the home region [S1547, S1526].
- Fact: Power BI Embedded supports Multi-Geo. China North does not [S1526].
- Fact: Sovereign clouds support Multi-Geo across regions within that cloud [S1526].

## Steps to place a workspace in another region

1. Create a capacity in the target region. See [Fabric capacity F SKUs](../13_licensing_pricing/13_fabric_capacity_f_skus.md).
2. Open workspace settings and change the capacity, or call Assign To Capacity. You need workspace admin and capacity assign rights.
3. Verify with the capacity region in Get Capacities (field `region`) [S1526].

Embedded capacity location cannot be edited later. Create a new one, reassign workspaces, then delete or pause the old one [S1526].

## Moving data across regions

- Standard Power BI items survive reassignment. Large-format semantic models and all Fabric items do not. Back them up or use Git integration first [S1509, S1527].
- Dataflow Gen1 storage can use your own ADLS Gen2 account in the desired region [S1527].

## Tenant migration types

| Scenario | Meaning | Trigger |
|---|---|---|
| Side-by-side (cross-tenant) | Two tenants run in parallel; items move one by one | Merger or acquisition |
| Tenant split | One tenant divides into two | Divestment |
| Tenant remap | Tenant deleted and recreated in a new home region, same Microsoft 365 tenant | Strict residency |

Source: S1527. Remap needs a Microsoft support request. Support only deletes and remaps; it does not migrate your content. Downtime is three to 24 hours or more, and loss is possible if backups are incomplete [S1527]. Try Multi-Geo first.

## Common mistakes

- Picking a trial or capacity region without checking residency rules. Moving later deletes Fabric items [S1511].
- Believing Multi-Geo moves tenant metadata. It does not [S1533].
- Cross-region Copilot or Azure OpenAI processing. Separate tenant settings ask consent. See [Tenant settings catalog](../references/admin_governance_security/12_tenant_settings_catalog.md).

## Limits and version notes

After a cross-region move, source data can remain in the old region up to 30 days, hidden from users. Multi-Geo does not support Metrics in Power BI or Q&A settings; permissions, credentials and push datasets metadata stay in the home region [S2719].

Region availability for each Fabric workload varies and changes. Verify in the Fabric region availability page (not fetched here).

## See also

- [Compliance and encryption](12_compliance_encryption.md)
