---
id: 12.sensitivity_labels_purview
title: Sensitivity labels and Microsoft Purview
domain: admin_governance_security
type: concept
level: intermediate
tags: [sensitivity-label, governance, security]
summary: Explains how Microsoft Purview sensitivity labels work in Power BI and Fabric, the four tenant settings, inheritance, mandatory labels and license needs.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S1521, S1525, S1545, S2714, S2715]
references: []
related: [12.tenant_settings, 12.audit_activity_logs, 12.external_sharing_b2b]
---
## Purpose

A sensitivity label classifies content, for example "Highly Confidential". Labels are created in Microsoft Purview and applied to Power BI and Fabric items. A label with encryption also protects exported files.

## Key facts

- Fact: Labels are created and managed in the Microsoft Purview portal under Classification, Sensitivity labels [S1521].
- Fact: Labels from the old Azure Information Protection must be migrated to the unified labeling platform first [S1521].
- Fact: The enable-labels article (checked 2026-10-08) says applying or viewing labels needs an Azure Information Protection (AIP) Premium P1 or P2 license, bought standalone or in a suite such as Microsoft 365 E5. To apply labels to Power BI items a user also needs Pro or PPU, plus Create and Edit permission on the item [S2714]. Older wording named a Purview Information Protection license; confirm with your account team [S1521].
- Fact: Labels work in public cloud, US Government (GCC, GCC High, DoD) and China. Other national clouds are not supported [S1521].
- Fact: Default and mandatory label policies are set in Purview when you publish the label policy. They apply to Power BI content created or edited after publishing, not retroactively [S1521].
- Fact: Mandatory labeling does not apply to service principals or APIs [S1521].

## How it works

Four related tenant settings sit under Information protection [S1525]:

| Setting | Effect |
|---|---|
| Allow users to apply sensitivity labels for content | Turns on label integration |
| Apply sensitivity labels from data sources to their data in Power BI | Upstream inheritance |
| Automatically apply sensitivity labels to downstream content | Downstream inheritance |
| Allow workspace admins to override automatically applied sensitivity labels | Lets admins relax automatic labels |

A fifth setting restricts protected-label content from "people in your organization" sharing links [S1525].

Inheritance types [S1521]:

- Upon creation: a new report inherits the label of its semantic model. Failure to label does not block creation.
- Upstream: a semantic model inherits from a labeled source. Supported sources are Azure Synapse Analytics and Azure SQL Database. The user connecting needs Pro or PPU.
- Downstream: a label on a model flows to dependent reports and dashboards. It never overwrites a manual label or replaces a label with a less restrictive one. It stops if more than 80 downstream items exist [S2715].
- Downstream has two modes: user consent (a checkbox, selected by default) and fully automated (the downstream tenant setting). Fully automated mode ignores the user's edit rights on downstream items [S2715].
- Export: files exported to Excel, PowerPoint and PDF carry the label.

## Steps to roll out

1. Define and publish labels and policies in Purview. Test with a pilot group.
2. Decide who may apply labels, whether to inherit, and whether to require labels.
3. Enable the tenant settings in stages.
4. Use the information protection APIs to label existing content in bulk if you need a default [S1521].
5. Track label changes in the activity log. See [Audit and activity logs](12_audit_activity_logs.md).

## Common mistakes

- Setting tenant settings before labels and policies are published [S1521].
- Expecting a default label to relabel old content. It does not.
- Using labels as access control. A label with encryption restricts files; it does not replace RLS or workspace roles.
- Enabling information protection for external Entra members. Purview Information Protection is not supported for external members [S1530].

## Limits and version notes

Upstream inheritance in Desktop works even when the tenant setting is off, but after publishing, refresh updates only apply when the setting is on [S1521]. The Microsoft security baseline marks label use as a customer responsibility [S1545].

## See also

- [Tenant settings](12_tenant_settings.md)
- [Compliance and encryption](12_compliance_encryption.md)
