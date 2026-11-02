---
id: 20.migration_checklist
title: BI migration checklist
domain: migration
type: how-to
level: intermediate
tags: [migration, best-practice, cheatsheet]
summary: A stage-by-stage checklist for moving from any legacy BI tool to Power BI, covering inventory, model, security, licensing, validation and cutover.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S1535, S1542, S1543, S1509, S1510]
references: []
related: [20.migration_process, 12.governance_frameworks, 13.who_needs_which_license]
---
## Purpose

Use this list with the [migration process](20_migration_process.md). Items follow Microsoft's stages [S1535]. Some items are our additions, marked (KB).

## Before you start

- [ ] Executive sponsor named [S1535]
- [ ] Initial governance model agreed: ownership, trusted data sources, security, compliance [S1535]
- [ ] Fabric admin role assigned; tenant settings reviewed. See [Tenant settings](../12_admin_governance_security/12_tenant_settings.md)
- [ ] Home region and capacity region chosen. See [Tenant region and Multi-Geo](../12_admin_governance_security/12_tenant_region_multigeo.md)
- [ ] License plan: authors, readers, capacity size (F64 line). See [Who needs which license](../13_licensing_pricing/13_who_needs_which_license.md)

## Stage checklist

Stage 1, requirements:
- [ ] Inventory of reports, data sources, owners, usage in last 12 months (KB)
- [ ] Prioritize by value and usage; mark reports to retire
- [ ] Record security rules of the old tool

Stage 2, deployment planning:
- [ ] Workspace layout, app plan, refresh schedule, gateway needs
- [ ] Import, DirectQuery or Direct Lake choice per subject
- [ ] Capacity and Pro or PPU needs

Stage 3, proof of concept:
- [ ] One narrow solution proves the data path, a hard calculation and security

Stage 4, create and validate:
- [ ] Star-schema semantic model; measures defined once
- [ ] Row-level security rebuilt and tested with real users
- [ ] Reports redesigned around business questions

Stage 5, deploy and monitor:
- [ ] Pilot group, then staged rollout
- [ ] Training and support route
- [ ] Activity log export running. See [Audit and activity logs](../12_admin_governance_security/12_audit_activity_logs.md)

## Validation checklist

- [ ] Totals and counts match the old tool for agreed dates (side-by-side reconciliation) [S1542]
- [ ] Calculation edge cases tested: blanks, filters, time periods, ties
- [ ] Performance tested with realistic data volume
- [ ] Security tested with users in and out of each role
- [ ] Exports and subscriptions tested (KB)
- [ ] Parallel run period completed [S1543]

## Cutover checklist

- [ ] Old reports marked read-only with a retirement date (KB)
- [ ] Links, bookmarks and scheduled emails redirected
- [ ] Do not cancel the old platform or a Premium subscription until all workspaces are moved and verified [S1509]
- [ ] Lessons learned captured for the next wave [S1535]

## Common mistakes

- Treating migration as only a technology task. Training and communication are part of the plan [S1535].
- Leaving old subscriptions and licenses running without an owner.

## See also

- [Tableau](20_tableau_to_power_bi.md), [Qlik](20_qlik_to_power_bi.md), [Excel](20_excel_to_power_bi.md), [SSRS and RDL](20_ssrs_rdl_to_power_bi.md), [Cognos](20_cognos_and_other_tools.md)
