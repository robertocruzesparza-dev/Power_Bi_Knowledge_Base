---
id: meta.GAPS
title: Known gaps part 1
domain: meta
type: reference
level: intermediate
tags: [metadata, reference]
summary: Unfilled coverage gaps by domain, with reasons and where to look next.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: []
references: []
related: []
---

# Known gaps

Each row is a gap logged during research on 2026-10-07. Verifiers filled some of them on 2026-10-08; see the re-verification log. Treat every domain as incomplete where listed.

Parts: [part 1](GAPS.md) | [part 2](GAPS_part2.md)

| Worker | Domain | Missing | Why | Look next |
|---|---|---|---|---|
| W1 | foundations | No expert or community sources (SQLBI, Guy in a Cube, RADACAD) consulted | Budget spent on official pages; all sources tier 1 | Search SQLBI and Guy in a Cube for Desktop vs service pitfalls |
| W1 | desktop | Full list of Options dialog pages not catalogued | Learn has no single page | Read each Options page in Desktop or Learn per area |
| W1 | desktop | Keyboard shortcuts for DAX query view and TMDL view not found | Not on the shortcut page read | Check DAX query view and TMDL view Learn pages |
| W1 | desktop | September 2026 Desktop release and current version number not verified | Latest-update page showed August 2026 | Check desktop-latest-update and change log |
| W1 | desktop | Power BI Desktop Bridge details not read | Preview, only in release notes | learn.microsoft.com/power-bi/developer/agentic |
| W1 | foundations | Power BI mobile apps details and Goals/Scorecards only mentioned | Out of scope depth | Domain 07 and 08 |
| W1 | desktop | Desktop group policy and registry settings beyond update notifications and evaluation settings | Not researched | Implementation planning user tools page |
| W1 | desktop | Whether Desktop 100 GB PPU model upload and 10 GB upload limit statements reconcile | S017 vs S018 differ | Fabric capacity limits pages |
| W2 | data_sources | SAP HANA, SAP BW, Spark, Web, Oracle connector pages not in capability details (slug lookups failed) | Learn pages use unknown slugs; only about 120 connector pages parsed | Open each connector page via https://learn.microsoft.com/en-us/power-query/connectors/ and add auth plus DirectQuery lines |
| W2 | data_sources | Partner connectors (about 70) have no Learn page, so DirectQuery and auth are unknown | Partner-documented | Check each partner site |
| W2 | data_sources | Gateway troubleshooting (common errors, logs, monitoring, performance counters) not covered | Budget | Learn data-integration/gateway troubleshooting pages |
| W2 | data_sources | Data source and SSO setup steps for Kerberos, SAML, Entra SSO not detailed | Budget | Learn gateway SSO articles |
| W2 | data_sources | MySQL DirectQuery conflict: DirectQuery article discusses MySQL, connector page lists Import only | Conflicting official pages | Test in current Desktop |
| W2 | power_query_m | Query diagnostics, step folding examples, Power Query Online dataflow differences not covered | Budget | Learn power-query/query-diagnostics and folding examples |
| W2 | power_query_m | Cube, accessing-data, error-handling and expression function categories not cataloged | Budget | Learn powerquery-m function reference |
| W2 | power_query_m | M reference pages for case sensitivity, operators and type system not re-read | Budget | Learn powerquery-m/m-spec-lexical-structure |
| W2 | release_roadmap | Official Power BI September 2026 feature summary not found | Search returned only Message Center mirror | Check Power BI blog and Fabric community update blog |
| W2 | release_roadmap | Fabric roadmap site item contents not extracted (JavaScript app) | Fetch returns shell only | Browse roadmap.fabric.microsoft.com or use its export |
| W2 | release_roadmap | Monthly history before October 2024 and December 2025 omission not explained | Out of 24-month scope | Archive page earlier sections |
| W2 | release_roadmap | Per-release gateway feature lists not extracted | Budget | Gateway monthly updates page |
| W3 | data_modeling | Parent-child hierarchies, field parameters, what-if parameters, many-to-many bridge worked examples not covered | time budget | Learn: parent and child DAX functions; field parameters page |
| W3 | data_modeling | Large semantic model storage format, model size limits per SKU not covered | volatile, belongs with licensing | Learn: service-premium-large-models; licensing domain |
| W3 | data_modeling | Automatic aggregations configuration steps and fine tuning not detailed | snippet-level only | Learn: aggregations-auto-configure |
| W3 | data_modeling | Calculation group selection expressions, dynamic format strings, and Tabular Editor authoring not detailed | snippet-level only | Learn: calculation-groups; Tabular Editor docs |
| W3 | data_modeling | Direct Lake automatic updates, security, and DirectLakeBehavior values not detailed | snippet-level | Learn: direct-lake-how-it-works, direct-lake-manage |
| W3 | dax | Financial and parent-child function categories not catalogued | time budget | Learn: financial-functions-dax, parent-and-child-functions-dax |
| W3 | dax | Exact signatures for window functions, TOTALYTD year-end argument, and SUMMARIZECOLUMNS not verified | catalog lists names only | Learn function pages |
| W3 | dax | SQLBI and DAX Patterns coverage thin (two articles read) | time budget | sqlbi.com/articles, daxpatterns.com |
| W3 | dax | DAX query syntax (EVALUATE, DEFINE, ORDER BY, INFO functions) not given its own file | time budget | Learn: dax-queries |
| W3 | dax | Time zone behavior of NOW and TODAY in the service stated as inference | unverified | Learn NOW function page; RADACAD |
| W3 | performance | Query caching, query parallelization, large model format, and Log Analytics semantic model events not covered | time budget | Learn: power-bi-query-caching, azure-log-analytics |
| W3 | performance | Best Practice Analyzer and Tabular Editor performance rules not covered | time budget | Tabular Editor docs; Microsoft best practice rules |
| W3 | performance | Refresh performance (Power Query folding diagnostics, refresh timeouts) only linked, not covered | belongs to W2 domain | 04_power_query_m |
| W4 | certification_learning | Pre-2026-10-19 skills lists for DP-600 and DP-700, and full DP-700 page read | Study guides show only the post-update list; DP-700 came from a search snippet | Re-fetch study-guides/dp-600 and dp-700 after 2026-10-19; check the Microsoft Learn exam pages |
| W4 | certification_learning | Official exam prices by country | Exam pages show no price; only a third-party US price (165 USD) found | Microsoft Learn schedule-through-Pearson-VUE flow or the exam pricing page |
| W4 | certification_learning | Other Fabric or Power Platform exams (for example PL-200, PL-600, AI-related Fabric exams) and Applied Skills | Only PL-300, DP-600, DP-700, DP-900, DP-203 checked | credentials/browse filtered by product Power BI and Fabric |
| W4 | certification_learning | Guy in a Cube and Fabric Community site details | Site pages did not load (empty page, HTTP 403) | YouTube channel About page; community.fabric.microsoft.com in a browser |
| W4 | service | Fabric Activator alert details for reports and GA date | Only a snippet of the preview article read | Fabric Activator docs and Fabric roadmap |
| W4 | service | Semantic model settings pane (preview) menu changes and Power BI Home changes | Only mentioned in passing | What's new in Power BI service pages for 2026 |
| W4 | service | Deployment pipelines, Git, and gateway administration for content delivery | Out of W4 scope; belong to devops and data source domains | 15_devops_lifecycle and 03_data_sources |
| W4 | service | Metrics hub versus Goals naming history | Docs still use metrics in URLs | Power BI blog archive |
| W4 | report_design | Per-visual property reference (formatting options per visual type) | Only overview and cross-cutting features covered | Individual visual docs and the Report Theme JSON schema on GitHub |
| W4 | report_design | New card visual and new slicer GA status and migration | Only mentioned in troubleshooting article | Desktop monthly updates 2025 and 2026 |
| W4 | report_design | Cross-report drillthrough workspace requirement | Current doc says same workspace and service only; older articles may differ | desktop-drillthrough article history and a hands-on test |
| W4 | report_design | Q&A retirement date conflict (December 2026 versus February 2027) | Two official pages disagree | Deprecating Power BI Q&A link (go.microsoft.com/fwlink/?LinkId=2379220) and Power BI blog |
| W4 | report_design | Translytical task flows, field parameters, visual calculations depth | Only mentioned in overviews | Their own docs; may belong to 17_ai_features or 06_dax |
| W5 | semantic_models_dataflows | Gen1 dataflow admin settings, linked tables, BYOL storage detail not researched in depth | time budget | Learn power-query/dataflows pages, tenant settings |
| W5 | semantic_models_dataflows | Semantic model settings pane (preview), query caching, scale-out, automatic aggregations not covered | time budget | Learn power-bi/connect-data and enterprise pages |
| W5 | semantic_models_dataflows | Dataflow Gen2 pricing and CU consumption rates not captured | volatile pricing page not fetched | Learn fabric/data-factory/pricing-dataflows-gen2 |
| W5 | semantic_models_dataflows | Dataflow Gen2 data destinations and managed settings details | not fetched | Learn dataflow-gen2-data-destinations-and-managed-settings |
| W5 | paginated_reports | Dynamic (data-driven) subscriptions preview, URL parameters, Report Builder UI walkthrough, RDL element reference not researched | time budget | Learn power-bi-dynamic-report-subscriptions, report-builder-url-parameters |
| W5 | paginated_reports | SSRS to Power BI migration (RDL migration tool, SSRS 2022 publish) only mentioned | time budget | Learn guidance/migrate-ssrs-reports-to-power-bi |
| W5 | paginated_reports | Gateway setup for paginated reports and Kerberos SSO steps | not researched | Learn gateway articles |
| W5 | fabric_onelake | Workload-specific limits (Spark, Real-Time Intelligence, Activator) not covered | scope focus on the Power BI path | Learn fabric/data-engineering, real-time-intelligence |
| W5 | fabric_onelake | OneLake security roles detail, table maintenance and V-Order guidance | not fetched | Learn onelake/security, fabric/fundamentals/table-maintenance-optimization |
| W5 | fabric_onelake | F SKU prices, reservation discounts, overage billing rates | volatile, not looked up | Azure Fabric pricing page |
| W5 | fabric_onelake | Direct Lake security integration and fixed identity setup steps | not fetched | Learn direct-lake-security-integration, direct-lake-fixed-identity |
| W5 | fabric_onelake | Semantic link and Fabric REST API for semantic models | not covered | Learn python/api/semantic-link-sempy |
| W6 | admin_governance_security | Compliance certification list (ISO, SOC, HIPAA etc.) not captured | Trust Center pages are dynamic; no stable doc fetched | Microsoft Trust Center and Service Trust Portal; learn.microsoft.com/compliance/regulatory/offering-home |
| W6 | admin_governance_security | Activity Events API throttling limit not verified | Not in fetched snippets | learn.microsoft.com/rest/api/power-bi/admin/get-activity-events |
| W6 | admin_governance_security | OLS behavior when a user is in multiple roles with conflicting column permissions | Page read did not say | learn.microsoft.com/analysis-services/tabular-models/object-level-security |
| W6 | admin_governance_security | Fabric region availability and Fabric-specific item-level security (OneLake security, workspace roles, item permissions) | Out of assigned scope depth; only RLS/OLS covered | learn.microsoft.com/fabric/security/security-overview and permission-model pages |
| W6 | admin_governance_security | Private Link, workspace network rules, DLP and Defender for Cloud Apps session policies | Only listed as tenant settings | learn.microsoft.com/fabric/security/security-private-links-overview |
| W6 | admin_governance_security | Sensitivity label downstream inheritance and change-enforcement details, bulk label APIs | Only overview snippets read | learn.microsoft.com/fabric/governance/service-security-sensitivity-label-downstream-inheritance |
| W6 | admin_governance_security | Power BI blog primary announcements (HTTP 403 on fetch) | Blog blocked WebFetch | powerbi.microsoft.com/blog and Fabric blog via browser |
| W6 | licensing_pricing | Meaning of new On-Demand meters dated 2026-10-01 in the Azure retail price API | No doc found | Fabric blog, Azure pricing page, release notes |
| W6 | licensing_pricing | Currency-localized prices (EUR, GBP) and sovereign cloud prices | Retail API returned no EUR rows for tested regions | azure.microsoft.com pricing calculator |
| W6 | licensing_pricing | Final P SKU end date for EA customers | No fixed date on official pages; one consultancy cites 2028-01-01 unverified | Microsoft account team; licensing news page (blocked, returned error) |
| W6 | licensing_pricing | Fabric capacity smoothing, throttling and surge protection numbers | Belongs to performance domain | learn.microsoft.com/fabric/enterprise/throttling and surge-protection |
| W6 | licensing_pricing | Education, nonprofit and government pricing | Only mentioned as available | Microsoft academic and nonprofit pricing pages |
