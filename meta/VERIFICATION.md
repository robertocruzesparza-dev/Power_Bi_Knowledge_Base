---
id: meta.VERIFICATION
title: Re-verification log part 1
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
| R1 | 22_release_roadmap/22_gateway_release_history.md | Gateway builds Sep 3000.334, Aug 3000.330, Jul 3000.326, Jun 3000.322, May 3000.318, Apr 3000.314 | confirmed | Learn page on 2026-10-09 lists the same six builds; September still newest, no October build yet | S2800 |
| R1 | 22_release_roadmap/22_gateway_release_history.md | Only last six gateway releases supported | confirmed | Learn page text and gateway FAQ | S2800 |
| R1 | 22_release_roadmap/22_release_cadence_and_tracking.md | Desktop monthly cadence, older builds not serviced | confirmed | Download and What's new pages state monthly and latest-only support | S2801,S2804 |
| R1 | 22_release_roadmap/22_release_cadence_and_tracking.md | Newest monthly summary on Learn is August 2026 | confirmed | Still August 2026 on 2026-10-09; no September or October Power BI summary found | S2801,S2843 |
| R1 | 22_release_roadmap/22_release_history_2026.md | Sep 2026 Desktop build 2.158.1304.0 | confirmed | Download Center shows 2.158.1304.0 published 10/7/2026 | S2802 |
| R1 | 22_release_roadmap/22_release_history_2026.md | No official Power BI September 2026 feature summary | confirmed | Not on Learn; web search finds none; Fabric September 2026 summary does exist (new finding, added) | S2801,S2843,S2845 |
| R1 | 22_release_roadmap/22_release_history_2026.md | Aug 2026 highlights (modern defaults GA, date picker GA, donut center value GA, matrix column expand GA, OneLake URLs GA, refresh options, Direct Lake calculated columns preview) | confirmed | Match the August 2026 What's new table | S2801 |
| R1 | 22_release_roadmap/22_release_history_2026.md | May to Jul 2026 versions 2.154.1260, 2.155.756.0, 2.156.951.0 and Mar 2026 2.152.882.0 | confirmed | Archive snippets show same version strings | S2844 |
| R1 | 22_release_roadmap/22_release_history_2024_2025.md | Jul 2025 2.145.1105.0, Aug 2025 2.146.705.0, Sep 2025 2.147.909.0 | confirmed | Archive snippets; other 2024-2025 rows spot-checked only via snippets (Nov 2025 features confirmed) | S2844 |
| R1 | 22_release_roadmap/22_release_history_2024_2025.md | Remaining 2024-2025 version numbers (Oct 2024 to Jun 2025, Oct 2025) | unresolved | Full archive fetch too large to parse; not re-read this pass | S2844 |
| R1 | 22_release_roadmap/22_fabric_roadmap_pointers.md | Fabric What's new lists previews: Fabric Embed, Fabric policies, ODBC driver for Fabric Data Engineering | unresolved | Page text truncated after 100000 characters; claim marked not re-checked in file | S2803 |
| R1 | 22_release_roadmap/22_fabric_roadmap_pointers.md | Fabric What's new is the continuously updated GA and preview list | corrected | Added September 2026 items and Fabric September 2026 Feature Summary link | S2803,S2845 |
| R1 | 22_release_roadmap/22_deprecations_retirements.md | Q&A retirement Feb 2027 vs Dec 2026 | confirmed | Learn Q&A page updated 2026-09-10 says February 2027 | S2820 |
| R1 | 22_release_roadmap/22_deprecations_retirements.md | Snowflake username and password sign-in deprecation | corrected | New row added: connector page says it will be deprecated, no date; ODBC to ADBC transition | S2810 |
| R1 | 22_release_roadmap/22_deprecations_retirements.md | Old file picker: Desktop March 2026 and older lose OneDrive/SharePoint save from October 2026 | confirmed | Present in August 2026 What's new and the OneDrive integration page | S2801,S2842 |
| R1 | 01_foundations/01_report_server_and_deployment_options.md | Report Server Desktop cadence about three times per year | corrected | Now stated as January, May, September | S2806 |
| R1 | 01_foundations/01_report_server_and_deployment_options.md | Report Server licensing: F64+ reserved, P SKUs yes, EM no, F below F64 no, Pro to publish | confirmed | Get started page | S2807 |
| R1 | 01_foundations/01_report_server_and_deployment_options.md | SQL Server licensing path details | corrected | Added SQL Server 2025 core rules and pre-2025 Software Assurance rule | S2807 |
| R1 | 01_foundations/01_report_server_and_deployment_options.md | No preview features, no PBIP in Report Server Desktop; separate side-by-side install | confirmed | Install and compare pages (PBIP not re-checked) | S2805,S2806 |
| R1 | 01_foundations/01_power_bi_and_fabric.md | Fabric workload list incl. Fabric IQ (preview), Data Factory 200+ connectors, OneLake on ADLS Gen2 | confirmed | Overview page re-read | S2808 |
| R1 | 01_foundations/01_power_bi_and_fabric.md | Aug 2026 Direct Lake calculated columns preview | confirmed | August 2026 What's new | S2801 |
| R1 | 01_foundations/01_power_bi_and_fabric.md | Fabric not available in sovereign clouds (S026); Fabric free license auto-assigned | unresolved | Not re-checked; Copilot overview says Copilot unsupported in sovereign clouds only | S2817 |
| R1 | 02_desktop/02_store_vs_exe_msi.md | Store vs exe differences, 32-bit unsupported, MSI deprecated, side-by-side unsupported | confirmed | Download page | S2804 |
| R1 | 02_desktop/02_store_vs_exe_msi.md | Virtualization support | corrected | Added Azure Virtual Desktop and Windows 365 supported, Citrix not | S2804 |
| R1 | references/desktop/02_installer_switches.md | All switches, properties, WiX Dark.exe extraction, DisableUpdateNotification registry value | confirmed | Identical to Learn page | S2804 |
| R1 | 02_desktop/02_options_and_settings.md | Parallel loading defaults (CPU cores, 432 MB) and registry keys | confirmed | Evaluation configuration page | S2836 |
| R1 | 02_desktop/02_options_and_settings.md | Query limit simulation limits (225 s 1 GB shared, 225 s 10 GB Premium, 600 s SSAS/AAS) | confirmed | Query limits page | S2833 |
| R1 | 02_desktop/02_options_and_settings.md | Privacy firewall partitions setting under Global Preview features, on by default July 2026 | confirmed | Setting page | S2837 |
| R1 | 02_desktop/02_preview_features.md | On-object interaction still preview; Aug 2026 statuses; OneDrive/SharePoint save on by default | confirmed | Preview pages and August What's new | S2801,S2842 |
| R1 | 02_desktop/02_preview_features.md | Whether August-preview items reached GA in September | unresolved | No Power BI September summary published yet | S2843 |
| R1 | 02_desktop/02_desktop_vs_service.md | Pro model size 1 GB, PPU 100 GB, refresh 8 or 48 per day | confirmed | Service description and PPU FAQ | S2840 |
| R1 | 02_desktop/02_desktop_vs_service.md | TMDL view GA in Desktop, preview on web | confirmed | TMDL view page | S2841 |
| R1 | 02_desktop/02_ui_tour.md | TMDL GA in Desktop, preview on web; modern defaults and Theme pane GA Aug 2026 | confirmed | TMDL page and August What's new | S2841,S2801 |
| R1 | 02_desktop/02_ui_tour.md | Model view warns above 75 tables | unresolved | Not re-checked this pass | S2841 |
| R1 | 03_data_sources/03_connector_catalog_guide.md | About 190 connectors in official index | corrected | Live index has 194 rows | S2809 |
| R1 | 03_data_sources/03_connector_catalog_guide.md | About 120 entries have own reference page | corrected | Count of rows with a link is about 170 (Learn or partner site) | S2809 |
| R1 | 03_data_sources/03_connector_catalog_guide.md | Gov cloud org-account note after March 31 2024; matches-no-exports known issue | confirmed | Both notes still on index | S2809 |
| R1 | references/data_sources/03_connector_catalog_part1.md | Names and SM/DF1/DF2 flags for connectors A to D | confirmed | Script compare of all 194 rows with live index: zero flag differences, one naming variant (CloudBlue PSA) | S2809 |
| R1 | references/data_sources/03_connector_catalog_part2.md | Names and flags for middle range | confirmed | Same script compare | S2809 |
| R1 | references/data_sources/03_connector_catalog_part3.md | Names and flags for remaining range | confirmed | Same script compare | S2809 |
| R1 | references/data_sources/03_connector_capability_details.md | Snowflake: GA, auth kinds, Import and DirectQuery | corrected | Added service principal, username/password deprecation, ADBC default | S2810 |
| R1 | references/data_sources/03_connector_capability_details.md | Oracle: GA, auth, Import and DirectQuery | corrected | Added built-in managed driver default for Import since June 2026, DirectQuery preview, no personal gateway | S2813 |
| R1 | references/data_sources/03_connector_capability_details.md | Azure Data Explorer: Preview, Entra ID, Import and DirectQuery | confirmed | Connector page | S2811 |
| R1 | references/data_sources/03_connector_capability_details.md | SQL Server: GA, four auth kinds, Import and DirectQuery | confirmed | Connector page | S2812 |
| R1 | references/data_sources/03_connector_capability_details.md | Other ~120 connector rows (release state, auth kinds) | unresolved | Only four pages re-checked; rest not re-read | S2809 |
| R1 | 03_data_sources/03_data_sources_overview.md | New Get Data experience in Desktop is a preview (File > Options > Preview features) | confirmed | May 2026 archive snippet lists new Get Data experience preview | S2844 |
| R1 | 03_data_sources/03_authentication_and_credentials.md | Gateway caches credentials, changed credentials may take about 5 hours | confirmed | Gateway considerations | S2814 |
| R1 | 03_data_sources/03_authentication_and_credentials.md | VNet gateway OAuth2 tokens not refreshed mid-stream | corrected | Applies to Dataflow Gen1 only; Gen2, semantic models, pipelines refresh mid-stream | S2815 |
| R1 | 03_data_sources/03_authentication_and_credentials.md | Snowflake auth list | corrected | Added key pair and service principal; password deprecation noted | S2810 |
| R1 | 04_power_query_m/04_data_privacy_firewall.md | Firewall partition rule; July 2026 Desktop setting enabled by default | confirmed | Learn firewall pages | S2837 |
| R1 | 06_dax/06_function_catalog.md | Over 250 DAX functions | confirmed | DAX function reference | S2831 |
| R1 | references/dax/06_functions_time_intelligence.md | All 40 time intelligence function names | confirmed | Name-by-name against Learn category page | S2828 |
| R1 | references/dax/06_functions_information.md | Information function names incl. TEXTCONTAINS, TEXTSIMILARITY, NAMEOF, TABLEOF | confirmed | Name-by-name against Learn category page; TEXTCONTAINS/TEXTSIMILARITY listed as new Sept 2026 | S2829,S2832 |
| R1 | references/dax/06_functions_filter.md | Filter, window and visual-calculation function names | confirmed | Name-by-name against Learn category page | S2830 |
| R1 | 06_dax/06_window_visual_calcs.md | Visual calculations availability | corrected | Now states GA in May 2026 update | S2844 |
| R1 | 16_performance/16_directquery_tuning.md | 1,000,000-row limit; Premium can raise it | confirmed | DirectQuery pages | S2834,S2835 |
| R1 | 16_performance/16_directquery_tuning.md | Default 10 connections per source; Pro and Report Server 10 active; Premium by SKU | confirmed | DirectQuery in Power BI page | S2835 |
| R1 | 16_performance/16_directquery_tuning.md | Query timeout | corrected | Added four minutes (225 s) timeout fact | S2834 |
| R1 | 17_ai_features/17_smart_narratives.md | Custom mode 4 summaries per visual, 16 per page; Copilot prompt limit 10,000 characters | confirmed | Smart narrative page | S2822 |
| R1 | 17_ai_features/17_smart_narratives.md | Copilot narrative limits (paid dedicated capacity to author, no edit, no key influencers, bookmark rules) | confirmed | Copilot narrative page | S2821 |
| R1 | 17_ai_features/17_smart_narratives.md | Embedding support for Copilot narrative | corrected | Added app-owns-data supported in preview; other scenarios supported | S2821 |
| R1 | 17_ai_features/17_copilot_privacy_data.md | Geography table (US, EU, UK, other regions) and cross-geo setting | confirmed | Copilot in Fabric overview | S2817 |
| R1 | 17_ai_features/17_copilot_privacy_data.md | Chat history kept 28 days for notebooks and data agents | confirmed | Same page | S2817 |
| R1 | 17_ai_features/17_copilot_privacy_data.md | Data use and non-storage statements | confirmed | Copilot privacy page; abuse-monitoring retention removed | S2816 |
| R1 | 17_ai_features/17_copilot_privacy_data.md | OpenAI as a Microsoft Subprocessor option and no trial SKU | corrected | New tenant opt-in setting and trial restriction added | S2816,S2817 |
| R1 | references/ai_features/17_ai_feature_status_matrix.md | Fabric data agent GA vs preview | corrected | Concept page says GA (updated 2026-09-29); release-status page still Preview; 25 rows by 25 columns cap added | S2819,S2818 |
| R1 | references/ai_features/17_ai_feature_status_matrix.md | Q&A retiring Feb 2027 | confirmed | Learn Q&A page | S2820 |
| R1 | references/ai_features/17_ai_feature_status_matrix.md | Copilot Data Factory GA; notebooks and Data Warehouse Preview; Power BI reports GA | confirmed | Release status page | S2818 |
| R1 | references/ai_features/17_ai_feature_status_matrix.md | Standalone Copilot agent preview, prep data for AI preview, app-scoped Copilot preview | unresolved | App-scoped Copilot is labelled preview in overview; standalone and prep-for-AI not re-checked | S2817 |
| R1 | 18_ecosystem_tools/18_teams_integration.md | Embeddable items, Viewer role, URL filters unsupported, national clouds, cross-tenant links | confirmed | Teams embed page | S2823 |
