---
id: 12.governance_frameworks
title: Governance frameworks and operating model
domain: admin_governance_security
type: concept
level: intermediate
tags: [governance, best-practice, admin]
summary: Summarizes Microsoft's Fabric adoption roadmap governance guidance: ownership strategies, decision criteria, maturity levels, COE and system oversight.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S1531, S1532]
references: []
related: [12.tenant_settings, 12.audit_activity_logs, 20.migration_process]
---
## Purpose

Governance sets rules for how data and reports are used. The goal in Microsoft's guidance is to empower users while meeting legal, industry and contract duties [S1531].

## Key facts

- Fact: Microsoft describes three content ownership strategies: business-led self-service, managed self-service, and enterprise BI [S1531].
- Fact: Four delivery scopes exist: personal, team, departmental, enterprise [S1531].
- Fact: Four criteria drive policy: who owns the content, delivery scope, data subject area and sensitivity, and whether the solution is critical [S1531].
- Fact: A Center of Excellence (COE) is an internal team of technical and business experts who help others work with data [S1531].
- Fact: Business-led self-service is not shadow IT. The business unit has authority and still follows governance and gets COE support [S1531].

## Maturity levels

Microsoft uses five levels for governance, COE and system oversight [S1531, S1532].

| Level | Name | Governance state |
|---|---|---|
| 100 | Initial | Informal, depends on individuals |
| 200 | Repeatable | Some documented practices |
| 300 | Defined | Strategy, policies and roles documented |
| 400 | Capable | Exceptions handled; activity data analyzed |
| 500 | Efficient | KPIs reviewed; continuous improvement |

Aim for at least level 300 or 400 [S1531].

## System oversight checklist

By level, Microsoft expects [S1532]:

1. Tenant settings match written policy and are reviewed regularly (200).
2. Settings are documented in a central portal for users (300).
3. An automated process exports activity log and API data to a secure store (300).
4. Data loss prevention policies run in Microsoft Defender for Cloud Apps (400).
5. The Fabric REST API retrieves tenant settings on a schedule (500).

## Worked example

A district starts at level 100: any admin flips settings. Step one is to name two to three admins and write down each setting's owner. Step two is a daily activity-log export. See [Audit and activity logs](12_audit_activity_logs.md).

## Common mistakes

- Locking down everything. Users then create shadow solutions.
- Choosing one policy for all content. Critical or sensitive content needs stricter rules than personal BI [S1531].
- Treating governance as a one-time project. There is no formal end [S1531].

## Limits and version notes

This KB paraphrases the adoption roadmap. The roadmap changes; check the source. Governance tooling in Fabric (domains, endorsement, metadata scanning, Govern tab) lives in the OneLake catalog [S1525].

## See also

- [Tenant settings](12_tenant_settings.md)
- [Migration process](../20_migration/20_migration_process.md)
