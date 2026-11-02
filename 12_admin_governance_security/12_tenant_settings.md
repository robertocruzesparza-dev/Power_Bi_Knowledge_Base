---
id: 12.tenant_settings
title: Tenant settings overview
domain: admin_governance_security
type: concept
level: intermediate
tags: [tenant-setting, admin, governance]
summary: Explains where Fabric and Power BI tenant settings live, who can change them, how scoping works, and which groups of settings matter most.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1525, S1528, S2718]
references: [../references/admin_governance_security/12_tenant_settings_catalog.md]
related: [12.service_principals, 12.sensitivity_labels_purview, 12.external_sharing_b2b]
---
## Purpose

Tenant settings are switches that control features for the whole organization. They are the main governance lever for admins. The full list is in the [tenant settings catalog](../references/admin_governance_security/12_tenant_settings_catalog.md).

## Key facts

- Fact: Open them at OneLake catalog, Govern, Configurations, Tenant settings [S1525]. The older admin portal path leads to the same settings.
- Fact: You need the Fabric administrator role to change them [S1528].
- Fact: Most settings can be enabled for the entire organization or for specific Entra security groups, and some allow excluded groups [S1528].
- Fact: Service principals get access to every setting they are enabled for, through groups or the whole organization [S1529].
- Fact: Some settings can also be set at capacity level, for example Users can create Fabric items [S1525].
- Fact: Settings change over time, and many carry preview labels. Review the index regularly (see [Governance frameworks](12_governance_frameworks.md)).

## How it works

Think of each setting as three decisions: on or off, who is in scope, and whether delegated levels (capacity or domain) can override it. Microsoft's adoption guidance expects settings to align with written governance policy and be reviewed regularly [S1532].

## Groups that matter first

| Group | Why it matters |
|---|---|
| Export and sharing | Publish to web, external sharing, export formats, shareable links |
| Information protection | Sensitivity labels and inheritance |
| Developer and Admin API | Service principal access |
| Advanced networking and Encryption | Private Link, public access block, customer-managed keys |
| Copilot and Azure OpenAI | Cross-region data processing consent |
| Audit and usage | Usage metrics, per-user data visibility |
| Workspace | Who may create workspaces; item recovery retention |

## Steps to review a setting

1. Find the setting by name in the catalog.
2. Decide the audience. Create a dedicated security group rather than using "entire organization".
3. Apply, then record the change in your governance log.
4. Verify with a test user in and out of the group.
5. Export current values with the Fabric REST API on a schedule to detect drift [S1532].

## Common mistakes

- Enabling Publish to web for everyone. Reports published there need no sign-in [S1525].
- Granting service principals the admin API settings through a broad group. Those settings expose user names, emails and model metadata [S1528].
- Assuming a disabled setting removes existing access. Guest users keep existing permissions if Guest users can browse and access Fabric content is turned off later [S1530].

## Limits and version notes

Setting names and locations changed with the Govern tab rollout. Verify names against the live index. Item recovery is on by default and keeps deleted items for 3 days, configurable up to 90 days; an admin can turn it off, and only some item types support it. Deleted collaborative workspaces are kept 7 days by default (7 to 90 configurable); My workspaces are fixed at 30 days [S2718]. One Learn page says 7 to 90 for item recovery; the retention overview and tenant index say 3 to 90 (Fact: conflict inside Microsoft docs).

## See also

- [Tenant settings catalog](../references/admin_governance_security/12_tenant_settings_catalog.md)
- [Service principals](12_service_principals.md)
