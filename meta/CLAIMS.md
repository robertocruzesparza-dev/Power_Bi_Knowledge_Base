---
id: meta.CLAIMS
title: High-impact volatile claims part 1
domain: meta
type: reference
level: intermediate
tags: [metadata, reference]
summary: Highest-impact volatile claims queued for re-verification.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: []
---

# High-impact volatile claims

Claims to re-check against official sources before each release of this KB.

Parts: [part 1](CLAIMS.md) | [part 2](CLAIMS_part2.md)

| Worker | File | Claim | Source |
|---|---|---|---|
| W1 | 02_desktop/02_install_and_requirements.md | Only the latest Desktop release is supported; 32-bit build unsupported | S002 |
| W1 | 02_desktop/02_install_and_requirements.md | Min requirements: Windows 10 or Server 2016+, .NET 4.7.2, 2 GB RAM min | S002 |
| W1 | 01_foundations/01_licenses_and_capacity.md | F64 or larger lets Free users with Viewer role view Power BI content | S009 |
| W1 | 01_foundations/01_licenses_and_capacity.md | P SKUs retire at end of agreement term; 30 day grace, throttle 31-90, block 91+ | S026 |
| W1 | references/foundations/01_fabric_sku_table.md | F SKU capacity unit and P/A SKU mapping (F64=P1=64 CU) | S009 |
| W1 | 02_desktop/02_limits.md | Model size limit 1 GB shared/Pro; Desktop upload 10 GB | S015 |
| W1 | 02_desktop/02_limits.md | Scheduled refresh timeout 2 h shared, 5 h Premium; disabled after 4 failures | S016 |
| W1 | 02_desktop/02_limits.md | Visual query limits: 225 s timeout; 1 GB shared, 10 GB Premium memory | S014 |
| W1 | 02_desktop/02_file_formats.md | PBIR is GA and default report format; PBIP excludes sensitivity labels | S029 |
| W1 | 02_desktop/02_update_and_release_cadence.md | Desktop versions 2.152.882.0 (Mar 2026) to 2.155.756.0 (Jun 2026); Aug 2026 latest seen | S011 |
| W2 | 03_data_sources/03_gateway_types_compared.md | Gateway cluster and source limit is 1,000 data sources; Microsoft supports last six gateway releases | S305 |
| W2 | 03_data_sources/03_gateway_types_compared.md | VNet gateway available for P, F and A4+ SKUs; F8 and above recommended | S307 |
| W2 | 03_data_sources/03_gateway_install_network_ha.md | Clusters hold up to 10 members; outbound ports 80, 443, 433, 5671-5672, 9350-9354 | S309 |
| W2 | 03_data_sources/03_gateway_install_network_ha.md | Newest gateway build is September 2026, 3000.334 | S313 |
| W2 | 03_data_sources/03_import_directquery_support.md | Scheduled refresh 8 per day shared, 48 per day Premium, PPU, Fabric | S318 |
| W2 | 03_data_sources/03_connector_lifecycle_changes.md | Legacy service Excel/CSV import: refresh stops July 31, 2026, loading stops August 31, 2026 | S336 |
| W2 | 22_release_roadmap/22_deprecations_retirements.md | Power BI Q&A deprecated December 2026 | S336 |
| W2 | 22_release_roadmap/22_deprecations_retirements.md | Desktop March 2026 and older cannot save to OneDrive or SharePoint from October 2026 | S335 |
| W2 | 03_data_sources/03_privacy_levels.md | July 2026 Desktop firewall partitions setting on by default | S316 |
| W2 | 03_data_sources/03_gateway_sso_and_data_sources.md | SSO supported source list (Entra, Kerberos, SAML) | S311 |
| W3 | references/data_modeling/05_direct_lake_guardrails.md | Direct Lake guardrails per SKU (F64: 5,000 files, 1,500M rows, 25 GB memory; F2 to F8: 300M rows, 3 GB) | S611 |
| W3 | 05_data_modeling/05_direct_lake.md | Direct Lake on OneLake is recommended for new models and has no DirectQuery fallback; calculated columns are preview | S612 |
| W3 | 05_data_modeling/05_storage_modes.md | DirectQuery 1,000,000 row intermediate limit and default 10 connections per source | S622 |
| W3 | 06_dax/06_time_intelligence.md | Calendar-based time intelligence is a preview behind Enhanced DAX Time Intelligence | S628 |
| W3 | 06_dax/06_user_defined_functions.md | DAX UDFs generally available from June 2026 release; compatibility level 1702 required | S654 |
| W3 | 05_data_modeling/05_incremental_refresh_basics.md | Real-time DirectQuery partition requires Premium; compatibility levels 1550 and 1565 | S618 |
| W3 | 05_data_modeling/05_aggregations.md | Automatic aggregations: Premium or PPU or Embedded; 60 minute training limit; up to 48 refreshes per day | S624 |
| W3 | 16_performance/16_capacity_metrics_app.md | Throttling windows 10 minutes, 60 minutes, 24 hours; interactive delay 20 seconds | S673 |
| W3 | 16_performance/16_model_size_reduction.md | Shared capacity model size 1 GB statement and 10x compression guidance | S671 |
| W3 | 05_data_modeling/05_date_tables_hierarchies.md | Scorecard hierarchies retirement date April 15 2026 (docs warning) | S629 |
| W4 | 08_service/08_scheduled_refresh.md | Pro allows 8 scheduled refreshes per day; PPU, Premium, and Fabric capacity allow 48 | S922 |
| W4 | 08_service/08_scheduled_refresh.md | Shared capacity refresh must finish within 2 hours; Premium maximum is 5 hours | S923 |
| W4 | 08_service/08_scheduled_refresh.md | Schedule deactivates after four consecutive failures; pauses after two months of inactivity | S922 |
| W4 | 08_service/08_workspace_apps.md | One workspace app per workspace; 25 audiences; 10,000 users and groups; 1,000 per audience; 200 dashboards | S924 |
| W4 | 08_service/08_subscriptions.md | Limit of 24 subscriptions per Power BI report or dashboard; instant email caps 10/15/20/25 per hour | S930 |
| W4 | 08_service/08_data_alerts.md | Up to 250 alerts across all models; alerts only on gauge, KPI, and card tiles | S933 |
| W4 | 08_service/08_license_requirements.md | Free users can view content only on Premium or Fabric F64 or larger capacity | S957 |
| W4 | 08_service/08_workspaces.md | Workspace limit of 1,000 items; Pro user limit of 1,000 workspaces | S950 |
| W4 | 07_report_design/07_visual_catalog.md | Q&A visual deprecation December 2026 (overview) versus February 2027 (Q&A pages) | S963 |
| W4 | 21_certification_learning/21_pl300_exam.md | PL-300 skills as of 2026-04-20; 100 minutes; passing score 700; 12-month renewal | S901 |
| W4 | 21_certification_learning/21_dp600_exam.md | DP-600 English update on 2026-10-19; weights 25-30, 45-50, 25-30 | S905 |
| W5 | 09_semantic_models_dataflows/09_semantic_model_refresh.md | Shared capacity allows 8 scheduled refreshes/day; Premium, PPU, Fabric allow 48/day | S1204 |
| W5 | 09_semantic_models_dataflows/09_semantic_model_refresh.md | Scheduled refresh disabled after 4 consecutive failures; time-out 2 h shared and 5 h Premium | S1206 |
| W5 | 09_semantic_models_dataflows/09_large_semantic_models.md | Default model size limit 1 GB; large format limit equals capacity size or admin maximum | S1201 |
| W5 | 09_semantic_models_dataflows/09_datamarts_status.md | Datamarts no longer supported since 2025-11-01; new datamart creation redirects to warehouse since 2025-06-01 | S1207 |
| W5 | 09_semantic_models_dataflows/09_dataflows_gen1_vs_gen2.md | Dataflow Gen1 is legacy with no new investment; new Gen2 items are CI/CD only since April 2026 | S1216 |
| W5 | 09_semantic_models_dataflows/09_dataflow_gen2_refresh_limits.md | Gen2 limits: 300 refreshes per 24h (150 non-CI/CD), 8 h per query, 24 h per refresh, 50 queries | S1218 |
| W5 | 10_paginated_reports/10_paginated_licensing_capacity.md | Free users view paginated reports only on F64+/P1+ with Viewer role; Pro or PPU needed to publish to other workspaces | S1224 |
| W5 | 10_paginated_reports/10_paginated_export_subscriptions.md | Subscription attachment max 25 MB, 60 min execution limit, Run-now limits by tier | S1226 |
| W5 | 11_fabric_onelake/11_direct_lake.md | Direct Lake needs Fabric F SKU; guardrails by SKU (F64: 5,000 files, 1,500M rows, 25 GB memory) | S1203 |
| W5 | 11_fabric_onelake/11_fabric_capacity_and_licensing.md | P SKUs retired at end of agreement term; 30-day grace, throttle day 31, rejected day 91 | S1209 |
| W5 | 11_fabric_onelake/11_mirroring.md | Free mirroring storage 1 TB per CU purchased; default retention 1 day for new mirrored databases | S1240 |
| W5 | 11_fabric_onelake/11_capacity_throttling.md | Throttle stages: 10 min overage protection, 20 s delay to 60 min, interactive rejection to 24 h | S1242 |
| W6 | 13_licensing_pricing/13_pricing_reference.md | Power BI Pro is 14.00 USD and PPU is 24.00 USD per user per month, billed yearly (en-US page) | S1503 |
| W6 | 13_licensing_pricing/13_pricing_reference.md | Fabric F SKU pay-as-you-go is 0.18 USD per CU-hour in West US 2 (UK/Japan/Australia 0.21, West Europe 0.22, Brazil South 0.28) | S1505 |
| W6 | 13_licensing_pricing/13_pricing_reference.md | Fabric one-year reservation 938 USD per CU, three-year 2,814 USD per CU; about 40.5 percent saving | S1505 |
| W6 | 13_licensing_pricing/13_embedded_skus.md | A1 to A6 hourly USD 1.0081, 2.0081, 4.0242, 8.0565, 16.121, 32.2506 | S1506 |
| W6 | 13_licensing_pricing/13_premium_p_sku_retirement.md | P SKUs retire at end of each agreement term; grace 30 days, throttled days 31-90, blocked from day 91 | S1509 |
| W6 | 13_licensing_pricing/13_who_needs_which_license.md | F64 or larger (and P) lets Free users with Viewer role view Power BI content; smaller F, A, EM need Pro or PPU | S1501 |
| W6 | 13_licensing_pricing/13_limits_and_quotas.md | Pro 1 GB model/8 refreshes per day; PPU 100 GB/48 refreshes; F64 max memory 25 GB | S1508 |
| W6 | 13_licensing_pricing/13_fabric_trial.md | Fabric trial lasts 60 days, F4 or F64, 1 TB OneLake, 7-day recovery after expiry | S1511 |
| W6 | 12_admin_governance_security/12_audit_activity_logs.md | Purview Audit Standard retention is 180 days; Power BI records under Premium also 180 days by default | S1523 |
| W6 | 12_admin_governance_security/12_tenant_settings.md | Tenant settings path is OneLake catalog > Govern > Configurations > Tenant settings; item recovery 3 to 90 days | S1525 |
| W7 | 15_devops_lifecycle/15_deployment_pipelines.md | Pipelines have 2 to 10 stages; default is 3 | S1802 |
| W7 | 15_devops_lifecycle/15_deployment_pipelines.md | Semantic models not upgraded to enhanced metadata unsupported in pipelines from 2026-02-12 | S1802 |
| W7 | 15_devops_lifecycle/15_git_integration.md | Workspace limit 1,000 items; file size 25 MB; commit limits 25 MB (ADO SP), 125 MB (ADO user), 50 MB (GitHub) | S1819 |
| W7 | 15_devops_lifecycle/15_git_integration.md | From 2026-12-01 users without read-write permission on items cannot use Git integration | S1819 |
| W7 | 15_devops_lifecycle/15_pbir_format.md | PBIR limits: 1,000 pages, 1,000 visuals per page, 300 MB report files; PBIR is GA and default | S1806 |
| W7 | 14_embedding_apis/14_embed_tokens.md | GenerateToken V2 limits: 50 reports, 50 datasets, 50 target workspaces | S1809 |
| W7 | 14_embedding_apis/14_embed_service_principal_capacity.md | Free-license viewers only on P SKUs or F64 and larger; A SKUs and smaller F need Pro or PPU | S1813 |
