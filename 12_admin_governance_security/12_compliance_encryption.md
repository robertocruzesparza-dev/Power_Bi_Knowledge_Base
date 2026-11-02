---
id: 12.compliance_encryption
title: Compliance, Trust Center and encryption
domain: admin_governance_security
type: concept
level: intermediate
tags: [compliance, security, admin]
summary: Where to find Power BI compliance evidence, and how encryption at rest, in transit and customer-managed keys work in Power BI and Fabric.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1502, S1525, S1533, S1534, S1545, S2716, S2717, S3014, S3015]
references: []
related: [12.tenant_region_multigeo, 12.sensitivity_labels_purview, 12.tenant_settings]
---
## Purpose

Auditors ask three questions: what standards does the service meet, where is data kept, and how is it encrypted. This page points to the evidence and describes the controls.

## Key facts

- Fact: The Microsoft Trust Center is the primary source for compliance information. The service follows the Microsoft Online Services Terms, the Data Protection Addendum and the Security Development Lifecycle [S1534].
- Fact: Learn states that Fabric complies with ISO 27001, 27017, 27018 and 27701 and is compliant with the US Health Insurance Portability and Accountability Act (HIPAA). Scope is per service and per cloud: check Appendix A and B of the Azure compliance offerings and the Service Trust Portal (STP) for audit reports [S2716].
- Fact: Power BI is listed as an in-scope service on the Learn pages for ISO 27001 (Office 365 commercial, GCC, GCC High and DoD scope lists), FedRAMP (as part of Office 365 branded plans) and HIPAA/HITECH (with a Business Associate Agreement (BAA) in the Online Services Terms) [S2717].
- Fact: Fabric also has Health Information Trust Alliance Common Security Framework (HITRUST CSF) certification, named in Microsoft healthcare compliance pages [S2716]. Certifications follow product launch on audit cycles, so a new Fabric workload may lack one [S2716].
- Fact: The Microsoft healthcare compliance page lists Power BI as in scope for HITRUST, System and Organization Controls (SOC) 1, SOC 2, ISO 27017, ISO 27001 and EU privacy laws [S3014]. The Fabric standards page defers to the Service Trust Portal and does not list SOC for Fabric itself [S3015].
- Unknown: a complete current per-workload matrix for Fabric items (SOC reports, FedRAMP level for Fabric items, regional schemes). Pull it from the STP, not from this KB.
- Fact: All data persisted by Power BI is encrypted at rest with Microsoft-managed keys by default. Azure SQL data uses transparent data encryption. Blob data uses Azure Storage encryption [S1534].
- Fact: Inbound traffic requires TLS 1.2 or higher. Requests using TLS 1.1 or lower are rejected [S1534]. Fabric also negotiates TLS 1.3 where possible [S1533].
- Fact: Data being processed in memory is not encrypted [S1534].

## How it works

| Connection mode | Data stored in Power BI |
|---|---|
| Import | Yes |
| DirectQuery | No (may cache) |
| Live connection | No |
| Direct Lake | No (stays in OneLake) |
| Composite | Yes if any Import source |
| Streaming | Only if configured to persist |

Source: S1534. Power BI may still cache retrieved data temporarily.

## Customer-managed keys

- Bring your own key (BYOK) at capacity level encrypts imported Power BI semantic models [S1533].
- Workspace-level customer-managed keys (CMK) in Azure Key Vault or Managed HSM encrypt other Fabric items such as lakehouses and notebooks [S1533].
- BYOK and CMK can use the same key or separate keys [S1533].
- Alternative: keep data in ADLS Gen2, S3 or Google Cloud Storage with CMK and read it through OneLake shortcuts. S3 and GCS shortcuts are read-only [S1533].
- Tenant setting: Apply customer-managed keys [S1525].
- PPU supports BYOK only when it is enabled across the whole tenant [S1502].

## Shared responsibility

The Azure security baseline for Fabric assigns encryption at rest by default to Microsoft. Classification, labels, data loss prevention, key management and TLS client configuration are customer duties [S1545].

## Common mistakes

- Treating Microsoft-managed keys as non-compliant by default. Many standards accept them. Decide from your own requirement.
- Forgetting keys must be rotated and access granted to the Power BI and Fabric services [S1533].
- Using CMK for one item type and assuming it covers all.

## Limits and version notes

CMK feature coverage by item type changes quickly. Verify in Learn before committing. Sovereign cloud behavior differs.

## See also

- [Tenant region and Multi-Geo](12_tenant_region_multigeo.md)
- [Sensitivity labels](12_sensitivity_labels_purview.md)
