---
id: meta.VERIFICATION4
title: Re-verification log part 4
domain: meta
type: reference
level: intermediate
tags: [metadata, reference]
summary: Claims re-checked against live sources on 2026-10-08, with results.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: []
---

# Re-verification log

Result is confirmed, corrected, or unresolved. Rows come from the three verification passes.

Parts: [part 1](VERIFICATION.md) | [part 2](VERIFICATION_part2.md) | [part 3](VERIFICATION_part3.md) | [part 4](VERIFICATION_part4.md)

| Verifier | File | Claim | Result | Note | Source |
|---|---|---|---|---|---|
| V2 | 10_paginated_reports/10_paginated_export_subscriptions.md | Paginated subscription limit conflict (24 vs unlimited) | confirmed | 24 applies to reports/dashboards only; paginated unlimited | S2605 |
| V2 | 08_service/08_workspace_apps.md | One app/workspace; 25 audiences; 10,000 users+groups; 1,000 per audience; 200 dashboards | confirmed | also 1 min publish timeout; workspace users counted per audience | S2606 |
| V2 | 08_service/08_data_alerts.md | Up to 250 alerts across all models; only gauge KPI card tiles | confirmed | also numeric only, not on date/time card, no co-ownership; Activator report alerts still public preview (F64+/Premium) | S2607 |
| V2 | 08_service/08_workspaces.md | Workspace limit 1,000 items | confirmed | Fabric admin portal page; item-type limits may be lower | S2608 |
| V2 | 08_service/08_workspaces.md | Pro user max 1,000 workspaces | confirmed | also 1,000 users/groups in roles per workspace | S2609 |
| V2 | 08_service/08_license_requirements.md | Free users view only on Premium or F64+ | confirmed | viewer role required; F<64 needs Pro/PPU; trial acts as F64 (60 days) | S2610 |
| V2 | 14_embedding_apis/14_embed_service_principal_capacity.md | Free viewers only on P SKUs or F64+; smaller F/A need Pro or PPU | confirmed | per Learn licenses scenario table | S2610 |
| V2 | 23_patterns_recipes/23_license_choice.md | Pro 1 GB model 8/day; PPU 100 GB 48/day | confirmed | Pro storage 10 GB/user; PPU 100 TB | S2610 |
| V2 | 21_certification_learning/21_pl300_exam.md | PL-300 skills as of 2026-04-20; weights; passing 700; 12-month renewal | confirmed | study guide + cert page last updated 04/20/2026 | S2611 |
| V2 | 21_certification_learning/21_pl300_exam.md | PL-300 100 minutes | unresolved | duration not on study guide or cert page fetched; marked unverified | S2611 |
| V2 | 21_certification_learning/21_pl300_exam.md | PL-300 price US 165 | corrected | official Exam FAQ: associate/expert typically US$165 by country; replaced third-party attribution | S2611 |
| V2 | 21_certification_learning/21_dp600_exam.md | English update 2026-10-19; weights 25-30/45-50/25-30 | confirmed | study guide and cert page; credential last-updated corrected to 2026-07-21 | S2612 |
| V2 | 21_certification_learning/21_certification_landscape.md | DP-700 weights 30-35 x3 and update 2026-10-19 | confirmed | full study guide read now (was snippet); no prior list available | S2612 |
| V2 | 21_certification_learning/21_dp600_exam.md | DP-600/DP-700 pre-2026-10-19 skills lists | unresolved | Learn now serves only post-update list; revisit after update | S2612 |
| V2 | 09_semantic_models_dataflows/09_datamarts_status.md | Datamarts unsupported since 2025-11-01; new creation redirects since 2025-06-01 | confirmed | page still calls datamarts a preview feature in one sentence (inconsistency persists); added default semantic model decoupling dates | S2613 |
| V2 | 14_embedding_apis/14_rest_api_endpoint_catalog.md | Real-time streaming datasets retire 2027-10-31 (creation stopped 2024-10-31) | corrected | primary page: creation enabled until 2027-10-31, existing models unaffected; ASA Power BI output jobs stopped from 2027-10-31; old tutorial note outdated | S2614 |
| V2 | 15_devops_lifecycle/15_git_integration.md | Workspace 1,000 items; file size 25 MB; commit limits 25 MB ADO SP, 125 MB ADO user, 50 MB GitHub | confirmed | also branch name 244 chars, path 250 chars, folders 10 levels | S2615 |
| V2 | 15_devops_lifecycle/15_git_integration.md | From 2026-12-01 users without read-write permission cannot use Git integration | confirmed | Learn note ties to label-protected items | S2615 |
| V2 | 15_devops_lifecycle/15_pbir_format.md | PBIR limits 1,000 pages, 1,000 visuals/page, 300 MB report files; GA and default | confirmed | also 1,000 resource package files, 300 MB resource files; service silently converts PBIR-Legacy on edit; restore 28 days | S2616 |
| V2 | 14_embedding_apis/14_embed_tokens.md | GenerateToken V2: 50 reports, 50 datasets, 50 target workspaces | confirmed | reports/datasets/target workspaces must be V2 workspaces; roles per identity max 50 | S2617 |
| V2 | 09_semantic_models_dataflows/09_large_semantic_models.md | Default model limit 1 GB; large format = capacity size or admin max | confirmed | added small-format SKU hard ceiling table (F2 1 GB ... F64+ 10 GB) | S2618 |
| V2 | 09_semantic_models_dataflows/09_dataflow_gen2_refresh_limits.md | 300 refreshes/24h (150 non-CI/CD), 8 h per query, 24 h per refresh, 50 queries | confirmed | schedule pause rules 72h/6 refreshes and 168h/5 refreshes also confirmed | S2618 |
| V2 | 09_semantic_models_dataflows/09_dataflows_gen1_vs_gen2.md | Gen1 legacy, no new investment; new Gen2 items CI/CD only since April 2026 | confirmed | Learn what-is-Dataflow-Gen2 states April 2026; Upgrade Wizard Gen1 to Gen2 CI/CD is preview | S2618 |
| V2 | 11_fabric_onelake/11_mirroring.md | Free mirroring storage 1 TB per CU purchased; default retention 1 day for new databases | confirmed | REST API page still says default 7 days (1-30 allowed); overview says 1 day after mid-June 2025 portal-created, 7 for old; noted both | S2619 |
| V2 | 11_fabric_onelake/11_fabric_capacity_and_licensing.md | P SKUs retire at end of agreement term; 30-day grace, throttle day 31, rejected day 91 | confirmed | EA active customers can renew annually; PPU, EM/A, sovereign unaffected | S2619 |
| V2 | 11_fabric_onelake/11_capacity_throttling.md | Stages: 10 min overage protection, 20 s delay up to 60 min, interactive rejection to 24 h, background rejection beyond | confirmed | capacity overage 3x PAYG rate, opt-in vs default-enabled wording inconsistent; RTI skips the 20 s delay stage | S2619 |
| V2 | 10_paginated_reports/10_paginated_licensing_capacity.md | Free users view paginated only on F64+/P1+ with Viewer; Pro or PPU to publish to other workspaces | confirmed | free can publish to My workspace only; Build permission on dataset and Contributor role needed | S2610 |
| V3 | 13_licensing_pricing/13_pricing_reference.md | Pro 14.00 and PPU 24.00 USD per user/month billed yearly | confirmed | microsoft.com pricing page fetched 2026-10-08 shows same; add-on 14.00; reservation 40.5% saving; effective 2025-04-01 corroborated | S2701 |
| V3 | 13_licensing_pricing/13_pricing_reference.md | Fabric PAYG 0.18 USD per CU-hour West US 2 | confirmed | Retail API West US 2 consumption CU meters 0.18 (WebFetch of API, 2026-10-08); azure.microsoft.com pricing page still renders $- for prices | S2700 |
| V3 | 13_licensing_pricing/13_pricing_reference.md | 1-year reservation 938 per CU; 3-year 2,814 per CU | corrected | API: 1-year 938 (since 2023-11-01); 3-year 2814 effective 2026-04-01 = 3 x 938 i.e. total for term, same per-year price; pricing page says reservation saves ~41% for 1 or 3 years | S2700 |
| V3 | 13_licensing_pricing/13_premium_p_sku_retirement.md | P SKUs retire end of each agreement term; grace 30d, throttled 31-90, blocked 91+ | confirmed | Learn decision guide/FAQ/overview current wording; FAQ says expiring EA/MCA customers cannot add or renew P through agreement | S2702 |
| V3 | 13_licensing_pricing/13_premium_p_sku_retirement.md | Final EA date 2028-01-01 | unresolved | No official fixed date; Learn says EA with active term can renew annually until EA term ends | S2702 |
| V3 | 13_licensing_pricing/13_pricing_reference.md | On-Demand meters dated 2026-10-01 | unresolved | 139 'On-Demand Usage CU' meters in westus2 eff 2026-10-01 at 1x/1.3x/2x/3x of 0.18 (Power BI OD 0.54=3x); Learn has no definition; separate Capacity Overage meter 0.54 documented as 3x PAYG (eff 2025-10-01); Spark on-demand billing doc exists | S2705 |
| V3 | 13_licensing_pricing/13_embedded_skus.md | A1-A6 hourly 1.0081..32.2506 USD West US 2 | confirmed | Retail API Power BI Embedded westus2 eff 2017-10-01 identical; no A7/A8 rows; Learn SKU table lists A7/A8 as F512/F1024 equivalents | S2700 |
| V3 | 13_licensing_pricing/13_embedded_skus.md | F SKUs not supported in GCC; supported in GCC High/DoD | confirmed | Learn embedded-capacity note current | S2704 |
| V3 | 13_licensing_pricing/13_who_needs_which_license.md | F64+ (and P) lets Free users with Viewer role view; smaller F, A, EM need Pro/PPU | confirmed | Learn embedded-capacity footnotes and licensing planning table | S2704 |
| V3 | 13_licensing_pricing/13_limits_and_quotas.md | Pro 1 GB/8 per day; PPU 100 GB/48; per-SKU memory, DQ, Direct Lake, dataflow tables; F64 25 GB | confirmed | Learn service-premium-what-is tables match row for row; PPU FAQ confirms 100GB, 40-160 parallelism, export limits | S2707 |
| V3 | 13_licensing_pricing/13_fabric_trial.md | 60 days, F4 or F64, 1 TB OneLake, 7-day retention, max 3 SQL DBs, no Copilot/Private Link | confirmed | Learn fabric-trial current | S2706 |
| V3 | 12_admin_governance_security/12_audit_activity_logs.md | Purview Audit Standard retention 180 days; Power BI records under Premium 180 days | confirmed | Learn: Standard 180d (90d before 2023-10-17); Premium 1-year default only Entra/Exchange/OneDrive/SharePoint for E5-licensed users; others 180d; non-user entities fixed 1 year. Added E5 nuance | S2711 |
| V3 | 12_admin_governance_security/12_audit_activity_logs.md | Activity Events API throttling (gap) | corrected | Gap filled: max 200 requests per hour; same UTC day and within last 28 days; Fabric admin or service principal | S2710 |
| V3 | 12_admin_governance_security/12_object_level_security.md | OLS merge rule across multiple roles (gap) | unresolved | Official SSAS OLS page: RLS+OLS from different roles cannot combine, error at query time; no official rule for conflicting OLS column permissions; community reports unsupported dynamic security configuration error. Added Q&A unsupported and relationship-chain restriction (corrected omission) | S2712 |
| V3 | 12_admin_governance_security/12_sensitivity_labels_purview.md | Sensitivity label licensing: Pro/PPU plus Purview Information Protection license (E5) | corrected | Current Learn enable-labels page states AIP Premium P1 or P2 (standalone or suite) plus Pro/PPU, and Create/Edit permission on item; reworded, flagged conflict | S2714 |
| V3 | 12_admin_governance_security/12_sensitivity_labels_purview.md | Downstream inheritance details (gap) | corrected | Gap filled: 80-item cap, never overwrites manual or less restrictive labels, two modes (user consent default, fully automated) | S2715 |
| V3 | 12_admin_governance_security/12_compliance_encryption.md | Compliance certification list (gap) | corrected | Gap partly filled: Fabric ISO 27001/27017/27018/27701, HIPAA, HITRUST; Power BI in scope for ISO 27001, FedRAMP, HIPAA lists. SOC and per-workload matrix remain Unknown (STP dynamic). Set volatile true | S2716 |
| V3 | 12_admin_governance_security/12_tenant_settings.md | Tenant settings path OneLake catalog > Govern > Configurations > Tenant settings; item recovery 3 to 90 days | confirmed | Path confirmed on several Learn pages; item recovery default on 3 days, 3-90 (one page typo says 7-90); added workspace retention 7-90 default 7, My workspace fixed 30 | S2718 |
| V3 | 12_admin_governance_security/12_tenant_region_multigeo.md | Multi-Geo not with PPU; Embedded supported; China North not; sovereign within cloud; metadata stays home | confirmed | Learn multi-geo page current; added 30-day residual copy and unsupported Metrics/Q&A | S2719 |
| V3 | 12_admin_governance_security/12_service_principals.md | SP settings: Fabric public APIs enabled by default for new customers; create workspaces/connections/pipelines disabled by default | confirmed | Learn developer tenant settings | S2720 |
| V3 | 20_migration/20_ssrs_rdl_to_power_bi.md | Built-in Publish for PBIRS/SSRS 2022; RDL tool for 2012-2019; consolidation under PBIRS from SQL 2025; PBIRS May 2025 needed | corrected | Consolidation and May 2025 confirmed; version scope conflicts inside Learn (planning page: built-in for after-2016; publish page/FAQ: 2022), recorded; PBIRS migration supports SSRS 2008+ | S2722 |
| V3 | 20_migration/20_ssrs_rdl_to_power_bi.md | Unsupported SSRS features (gap) | corrected | Gap filled from paginated reports FAQ and publish article: shared sources/datasets, linked reports, custom fonts/assemblies, document maps, data-driven subscriptions; KPIs, mobile reports, resources not migratable | S2721 |
| V3 | 20_migration/20_excel_to_power_bi.md | Workbooks .xlsx/.xlsm under 1 GB; local workbook upload with refresh unsupported; no cross-tenant sharing of data-model workbooks | confirmed | Learn current; added Publish to Power BI from Excel deprecated | S2724 |
| V3 | 20_migration/20_qlik_to_power_bi.md | QlikView end of life per vendor | corrected | Qlik community lifecycle table (updated 2025-09-26): 12.90 support ends 2026-10-31 (older table said 2026-05-21), 12.100 ends 2027-09-30; tier 3 snippet only, not opened in full; marked volatile | S2725 |
| V3 | 20_migration/20_migration_process.md | Microsoft series: 4 phases, pre-migration plus 5 stages | confirmed | Learn migration overview lists same phases and stages | S2726 |
| V3 | 20_migration/20_tableau_to_power_bi.md | No official Microsoft Tableau/Qlik/Cognos concept maps (gap) | unresolved | Learn migration series is tool-agnostic; no vendor-specific official maps found; MicroStrategy/BO/Looker still not covered | S2726 |
| V3 | 13_licensing_pricing/13_license_types_overview.md | Grace 90 days volume, 30 direct, none for trials; Pro in M365 E5; Pro trial 30 days 25 licenses | corrected | Power BI licensing guide confirms; M365 lifecycle page shows EA monthly/annual 30 days, multi-year 90; added nuance | S2727 |
| V3 | 13_licensing_pricing/13_fabric_capacity_f_skus.md | F SKU facts (billing, buy steps, no autoscale, overage) | corrected | Buy steps confirmed on Learn; added capacity overage default-on 3x, F SKUs only | S2705 |
| V3 | 12_admin_governance_security/12_rls_static_dynamic.md | RLS Viewer-only, union of roles, SP not in roles, M365 groups unsupported, Direct Lake supported | confirmed | Learn RLS page current; added Test as role limits | S2730 |
