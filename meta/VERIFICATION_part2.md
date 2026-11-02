---
id: meta.VERIFICATION2
title: Re-verification log part 2
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
| R1 | 18_ecosystem_tools/18_teams_integration.md | Private and shared channels | corrected | Added; Teams page and June 2026 note | S2823 |
| R1 | 18_ecosystem_tools/18_sharepoint_embedding.md | Prerequisites, licensing, known issues, Enable Copilot checkbox | confirmed | SharePoint embed page | S2824 |
| R1 | 18_ecosystem_tools/18_sharepoint_embedding.md | Workspace browse UI and single-visual embed; air gap support | corrected | Added (August 2026 note and page) | S2824,S2801 |
| R1 | 18_ecosystem_tools/18_analyze_in_excel.md | Prerequisites, 500,000-row export, 2 GB error, hierarchy rule, external users, Mac, field parameters | confirmed | Analyze in Excel page | S2825 |
| R1 | 18_ecosystem_tools/18_dax_studio.md | Current version unverified | corrected | GitHub marks v3.6.1 Latest (04 Sep; year not shown); 3.7.0 pre-releases present | S2826 |
| R1 | 18_ecosystem_tools/18_alm_toolkit_bravo.md | Bravo has no deprecation notice | confirmed | Latest release v1.0.13, 21 January, no archive notice (year not shown) | S2827 |
| R1 | 18_ecosystem_tools/18_alm_toolkit_bravo.md | ALM Toolkit current version, license, requirements | unresolved | Not re-checked | S2827 |
| R1 | references/troubleshooting/19_refresh_error_catalog.md | Imported model 1 GB; 10 GB uncompressed shared; refresh timeout 2 h and 5 h Premium; 4 failures disable schedule | confirmed | Refresh troubleshooting and scheduled refresh pages | S2838,S2839 |
| R1 | references/troubleshooting/19_refresh_error_catalog.md | Entra ID OAuth token lifetime about 1 hour; tile lag 10 to 15 minutes | confirmed | Refresh troubleshooting page | S2838 |
| R1 | references/troubleshooting/19_refresh_error_catalog.md | Refresh quota and inactivity behavior | corrected | Added 8/48 per day row and two-month inactivity pause | S2839 |
| R1 | references/troubleshooting/19_refresh_error_catalog.md | Individual error message strings (capacity limit, 0xC13E0003, container DEAD, etc.) | unresolved | Message wording not re-read this pass | S2838 |
| R2 | 21_certification_learning/21_dp600_exam.md | DP-600 English update 2026-10-19; skills weights 25-30/45-50/25-30; credential page Last Updated 07/21/2026; renewal 12 months | confirmed | Study guide shows skills as of 2026-10-19 with only Query and analyze data as a minor change; no new changes since 10-08 | S2900,S2902 |
| R2 | 21_certification_learning/21_certification_landscape.md | DP-700 skills 30-35% each, update 2026-10-19 (workspace settings and optimize performance minor) | confirmed | Not in stale list; cross-checked against DP-700 study guide, no edit needed | S2901 |
| R2 | 21_certification_learning/21_which_certification.md | Both DP-600 and DP-700 change on 2026-10-19 | confirmed | Both study guides show skills as of October 19, 2026 | S2900,S2901 |
| R2 | 21_certification_learning/21_exam_logistics_renewal.md | Renewal free, 6-month window, extends one year from expiry, unlimited retakes, unproctored open book, fundamentals do not expire | confirmed | Renewal page matches; 700 pass, localized exams +8 weeks and 30 extra minutes match study guide | S2903,S2900 |
| R2 | 21_certification_learning/21_learning_paths.md | Fabric path 8 modules; Power BI path slugs and module counts | corrected | Power BI path slugs were previously unopened; now opened: data-analytics-microsoft 4 modules, model-data-power-bi 6, build-power-bi-visuals-reports 6; Fabric path 8 modules confirmed; limits note updated | S2914,S2915 |
| R2 | 07_report_design/07_bookmarks_navigation.md | Personal bookmarks 20 per report, 2000 total, expire 6 months; Selection pane update behavior | confirmed | Docs match | S2904,S2905 |
| R2 | 07_report_design/07_custom_visuals.md | Group policy EnableCustomVisuals/EnableUncertifiedVisuals default 1 (enable); tenant setting names | confirmed | Admin settings page matches | S2913,S2934 |
| R2 | 08_service/08_scorecards_goals.md | 1000 goals per scorecard, 24 subscriptions per scorecard, none from org app, B2B not supported, Pro/F64 view licensing | confirmed | Goals limits page and subscriptions page match | S2906,S2907 |
| R2 | 08_service/08_org_apps.md | Org apps GA; Fabric Apps preview; supported included types | confirmed | Org app page states generally available; Fabric Apps (preview); maps and real-time dashboards included | S2908 |
| R2 | 08_service/08_item_permissions_sharing.md | 1000 sharing links per report; shared view expires 180 days after last use; M365 groups cannot be used for direct sharing | confirmed | Share pages match; dashboard 100-user input limit not re-read (low risk) | S2909,S2910 |
| R2 | 08_service/08_endorsement.md | Master data tenant setting labeled preview | confirmed | Admin page still names Endorse master data (preview) | S2911,S2912 |
| R2 | references/service/08_fabric_role_capabilities.md | Role capability matrix for Admin/Member/Contributor/Viewer | confirmed | Roles page matches each row (ReadAll excludes Viewer, Git connect Admin only) | S2940 |
| R2 | 09_semantic_models_dataflows/09_semantic_model_basics.md | Default semantic models stopped 2025-09-05; decoupled by 2025-11-30; no auto sync | confirmed | Fabric warehouse semantic models page; Build and free-license claims not re-read | S2921 |
| R2 | references/semantic_models_dataflows/09_enhanced_refresh_parameters.md | maxParallelism 10, retryCount 0, timeout 5h, total under 24h, paused Embedded 6h InProgress | confirmed | Enhanced refresh page matches | S2922 |
| R2 | 10_paginated_reports/10_paginated_limits_unsupported.md | 250 data sources; 600 s default timeout; DirectQuery source 10 min; subscriptions 60 min and 25 MB; 500 concurrent renders | confirmed | FAQ, subscriptions and capacity planning pages match | S2919,S2920,S2923,S2924 |
| R2 | 10_paginated_reports/10_paginated_data_sources.md | Native sources and auth table; AAS OAuth2 irreversible; Direct Lake data source rules unsupported | confirmed | Data sources page matches | S2920,S2919 |
| R2 | 11_fabric_onelake/11_shortcuts.md | 100,000 shortcuts per item; 100 connections; 10 per path; chain depth 5; caching 1-28 days, files over 1 GB not cached | confirmed | Shortcuts page matches | S2916 |
| R2 | 11_fabric_onelake/11_fabric_overview_workloads.md | Workload list including Fabric IQ (preview) | confirmed | Overview page lists the same workloads; Pro/PPU item-license claim not re-read | S2917 |
| R2 | 11_fabric_onelake/11_direct_lake_fallback.md | Only Direct Lake on SQL falls back; OneLake mode refresh fails on guardrail breach | confirmed | Direct Lake overview matches | S2918 |
| R2 | 14_embedding_apis/14_xmla_endpoint.md | Read-only default; no 48/day cap over XMLA; SSMS 18.9, February 2026 release for personal workspace; unsupported model types | confirmed | XMLA page matches | S2925 |
| R2 | references/embedding_apis/14_xmla_tools_security_audit.md | Tool minimum versions (Excel 16.0.13612.10000, SSDT 2.9.14, SSMS 18.9, SqlServer 21.1.18256), audit operation names | confirmed | All match | S2925 |
| R2 | 14_embedding_apis/14_rest_api_overview.md | 429 with Retry-After on per-user throttling; no published quotas | confirmed | REST API landing page throttling text | S2927 |
| R2 | 14_embedding_apis/14_powershell_cli_tooling.md | fabric-cicd Python 3.9-3.13; ms-fabric-cli | corrected | fabric-cicd range confirmed; Fabric CLI needs Python 3.10 or higher (added to file); fab deploy uses fabric-cicd confirmed | S2928,S2929,S2933 |
| R2 | 14_embedding_apis/14_embed_for_organization.md | Free viewers only on P or F64+; A SKU and F below F64 need Pro/PPU; no service principal; R/Python supported | confirmed | Embedded capacity and analytics pages match; note one access-token page says embed for your organization does not support A SKUs while others list A SKUs with Pro/PPU viewers | S2926 |
| R2 | 14_embedding_apis/14_embed_for_customers.md | No end-user license; R/Python unsupported; trial token banner; My workspace unsupported; Direct Lake needs V2 token | confirmed | Embed pages and generate-token page match | S2926,S2939 |
| R2 | 14_embedding_apis/14_custom_visuals_sdk.md | pbiviz tools 6.1.0 certification-audit and certification-fix flags | confirmed | Certified visuals page matches; latest visuals API version not determined | S2934 |
| R2 | 15_devops_lifecycle/15_pbip_format.md | PBIP limits (no sensitivity labels, BOM, CRLF, no OneDrive save, RLS members and IR partitions via API) | confirmed | Matches; added 260-character path limit from Learn | S2932 |
| R2 | 15_devops_lifecycle/15_deployment_rules.md | Rule types by item; supported sources; unsupported scenarios | confirmed | Create rules page matches table, source list and limits | S2935 |
| R2 | 15_devops_lifecycle/15_cicd_patterns.md | fabric-cicd 3.9-3.13; bulk API and pipeline options; preview status of Power BI items | confirmed | fabric-cicd and Git pages match | S2928,S2936 |
| R2 | references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md | Power BI items in pipelines and Git (preview flags); permission matrix | corrected | Lists match on 2026-10-09; added 2026-12-01 label-protected workspace deploy restriction, 2-10 stages, new UI and deployment plan in preview | S2930,S2931,S2936 |
| R2 | 23_patterns_recipes/23_recipe_pbix_to_git.md | Reports on AAS/SSAS/My workspace models excluded from Git; PBIP caveats | confirmed | Git integration and PBIP pages match; tenant Git switch not re-read | S2932,S2936 |
| R2 | 23_patterns_recipes/23_recipe_embed_report_with_rls.md | Service principal must pass identity for RLS items; customData 1024 chars | confirmed | Generate token page matches | S2939 |
| R2 | 23_patterns_recipes/23_recipe_dev_to_prod_release.md | 3 stages default; rules apply on next deploy; data not copied; Select related | confirmed | Pipelines pages match | S2930,S2931,S2935 |
| R2 | 23_patterns_recipes/23_import_vs_directquery_vs_direct_lake.md | Direct Lake OneLake vs SQL; calculated tables preview; calculated columns preview user context | confirmed | Direct Lake page matches | S2918 |
| R2 | 23_patterns_recipes/23_embedding_choice.md | Free viewers need P or F64+; A SKU not supported for secure embed; production needs capacity | confirmed | Embedded capacity page matches | S2926 |
| R2 | 23_patterns_recipes/23_dataflow_vs_semantic_model.md | Dataflow Gen1 legacy, Gen2 recommended for Premium with Fabric, Pro/PPU can keep Gen1 | corrected | Claim confirmed; added that the in-place Dataflows Upgrade Wizard is in preview | S2937,S2938 |
| R2 | 15_devops_lifecycle/15_deployment_pipelines.md | Semantic models without enhanced metadata unsupported since 2026-02-12; 300 items per deployment; PBIR not supported | confirmed | Not in stale list; intro and process pages match, no edit | S2930,S2931 |
| R2 | meta | Desktop OneDrive/SharePoint save-and-share: Desktop builds from March 2026 or earlier lose save/share from October 2026 | unresolved | New deadline item for domain 02 or 18 owners; no October 2026 Desktop update published yet as of 2026-10-09 | S2942,S2943 |
| R2 | meta | Fabric what's new shows no October 2026 GA entries as of 2026-10-09; latest is September 2026 | confirmed | No new GA announcements since 2026-10-07 found | S2941 |
| R3 | 12_admin_governance_security/12_service_principals.md | Developer settings defaults: SP create workspaces disabled for new customers; SP call Fabric public APIs enabled for new customers | confirmed | Developer settings page unchanged | S3000 |
| R3 | 12_admin_governance_security/12_service_principals.md | Admin API settings list; detailed-metadata settings need read-only admin API setting | corrected | Added dependency and Purview DSPM for AI requirement; noted old setting name Allow service principals to use Power BI APIs | S3003 |
| R3 | 12_admin_governance_security/12_service_principals.md | 401 causes; embed limits (My workspace, org-embed, dataflows, AAS group) | corrected | Added token audience, admin-consent permission and ISO 8601 date causes; embed limits confirmed | S3004 |
| R3 | 12_admin_governance_security/12_external_sharing_b2b.md | Invite setting, Guest Inviter role, Pro trial cannot invite, social identities, license matrix, cross-cloud limits, 50-tenant switcher | confirmed | No change on live page | S3002 |
| R3 | 12_admin_governance_security/12_external_sharing_b2b.md | Guest Free license when content on F64 or larger | confirmed | Licensing guide still says F64+ | S3007 |
| R3 | references/admin_governance_security/12_audit_operations.md | All 37 operation names present | confirmed | Found on live operation list | S3006 |
| R3 | references/admin_governance_security/12_audit_operations.md | Friendly names for ExportReport and ApplyChangeToPowerBIModel | corrected | Aligned wording to live list | S3006 |
| R3 | references/admin_governance_security/12_tenant_settings_catalog.md | Setting names by section | corrected | Added Event Schema Sets, Fabric Apps anonymous access, Agent 365 observability, Product Feedback, Teams auto-install, Azure Maps services, edit semantic models, Kusto setting | S3001 |
| R3 | 13_licensing_pricing/13_premium_p_sku_retirement.md | Final EA end date for P SKU | unresolved | Learn gives no fixed date; says EA can renew annually until EA term ends and to confirm with account rep. 2028-01-01 remains third-party only | S3008 |
| R3 | 13_licensing_pricing/13_premium_p_sku_retirement.md | Grace 30 days, throttle days 31-90, block from day 91; no new P SKUs; Pro/PPU/EM/A unaffected | confirmed | Unchanged | S3008 |
| R3 | 13_licensing_pricing/13_pricing_reference.md | Capacity overage meter 0.54 USD at 3x PAYG; Power BI Capacity Usage CU 0.18 West US 2 | confirmed | API read 2026-10-09 (first 100000 chars); overage enabled by default and 3x on Learn | S3009 |
| R3 | 13_licensing_pricing/13_pricing_reference.md | On-Demand Usage CU meters (2026-10-01) | unresolved | Still no Learn definition; Azure bill page points to Retail Prices API; Spark on-demand doc is separate (0.5 CU hour rate) | S3011 |
| R3 | 13_licensing_pricing/13_pricing_reference.md | Fabric Azure pricing page blank price cells | unresolved | Not retried via page render; used API instead | S3009 |
| R3 | 12_admin_governance_security/12_object_level_security.md | OLS multi-role merge rule | unresolved | SSAS page still gives only the RLS+OLS error; OneLake security unions roles but is a different feature | S3012 |
| R3 | 12_admin_governance_security/12_compliance_encryption.md | Compliance list | corrected | Added Power BI in scope for HITRUST, SOC 1, SOC 2, ISO 27017/27001 from healthcare page; Fabric-level SOC still not stated | S3014 |
| R3 | 20_migration/20_tableau_to_power_bi.md | No official Tableau/Qlik/Cognos concept maps | unresolved | Search again found only the tool-agnostic migration series | S3008 |
| V1 | 02_desktop/02_limits.md | Model size 1 GB shared/Pro; Desktop upload 10 GB | confirmed | Service-get-data says shared-capacity 1 GB; large-models page says Desktop upload 10 GB, Pro on reserved capacity 1 GB | S2500 |
| V1 | 02_desktop/02_limits.md | S017 (PPU 100 GB) vs S018 (default 1 GB, large format lifts to capacity size) conflict | corrected | Not a true conflict: 1 GB default applies to small storage format; PPU FAQ lists 100 GB model limit and large storage format is available for PPU; Premium per-capacity limits are 25-400 GB by SKU; small-format hard ceilings F2 1GB ... F64+ 10 GB | S2500,S2501,S2504 |
| V1 | 01_foundations/01_licenses_and_capacity.md | F64 or larger lets Free users view content | confirmed | Implementation planning table and embedded-capacity page both say F64 or larger | S2503 |
| V1 | references/data_modeling/05_direct_lake_guardrails.md | F2-F8 300M rows 3 GB; F64 1,500M rows 25 GB memory | confirmed | service-premium-what-is table: F2/F4/F8 3 GB, 300M rows; F64 25 GB, 1,500M rows; files per table not on this page | S2502 |
