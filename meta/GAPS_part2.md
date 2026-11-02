---
id: meta.GAPS2
title: Known gaps part 2
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
| W6 | migration | Official Microsoft Tableau, Qlik, Cognos concept maps | None found; used consultancies and labeled inference | Microsoft partner migration accelerators; Power BI migration series stage articles (not fetched individually) |
| W6 | migration | MicroStrategy, Business Objects, SAP BO, Looker migration | Not researched | Search vendor and Microsoft Fabric community sources |
| W6 | migration | Unsupported SSRS features in Power BI paginated reports | Not fetched | learn.microsoft.com/power-bi/paginated-reports/paginated-reports-faq |
| W7 | embedding_apis | Exact Power BI REST API rate limit numbers | Learn page states only 429 and Retry-After, no quotas | Power BI REST API reference throttling notes, Chris Webb or Data Goblins posts |
| W7 | embedding_apis | JavaScript client package version, event list, and settings names | Only landing page read, not the API reference | microsoft.github.io/PowerBI-JavaScript and npm powerbi-client |
| W7 | embedding_apis | Custom visuals API version table and AppSource publish steps | Only setup and certification snippets read | Learn: visual-api, office-store, power-bi-custom-visuals |
| W7 | embedding_apis | Service principal profiles and multitenancy design | embed-multi-tenancy page not read | Learn: embed-multi-tenancy, embed-service-principal-certificate |
| W7 | embedding_apis | Fabric REST API endpoint catalog (core, items, git, deployment pipelines) | Scope was Power BI REST; Fabric API groups not enumerated | Learn: rest/api/fabric |
| W7 | devops_lifecycle | ALM Toolkit workflow, versions, Direct Lake support | Only one official paragraph; tool site not read | alm-toolkit.com, SQLBI, Tabular Editor docs |
| W7 | devops_lifecycle | Deployment pipelines: item properties not copied, deployment plan preview details, new UI | Not fetched in full | Learn: understand-the-deployment-process, deployment-plan-overview |
| W7 | devops_lifecycle | Git integration: conflict resolution, branching strategies, granular commit preview | Only the process page read | Learn: conflict-resolution, manage-branches, granular-compare |
| W7 | devops_lifecycle | Tabular Editor CLI and Best Practice Analyzer in CI pipelines; Azure DevOps YAML examples | Community/expert sources not consulted | Tabular Editor docs, SQLBI, Data Goblins |
| W7 | devops_lifecycle | Variable libraries in CI/CD for Power BI | Mentioned only in passing | Learn: variable-library-overview |
| W7 | patterns_recipes | RLS vs OLS vs workspace isolation under Direct Lake | Only the overview page read | Learn: direct-lake-security-integration, direct-lake-fixed-identity |
| W7 | patterns_recipes | Pricing-based license break-even (Pro vs F64) | Prices intentionally excluded; volatile | Power BI pricing page, Azure pricing calculator |
| W7 | patterns_recipes | Expert opinion on storage mode and dataflow choices | Official docs only | SQLBI, RADACAD, Guy in a Cube |
| W8 | ai_features | Copilot supported region list and per-surface region gaps (two pages list different regions) | Region lists conflict between overview and prep-data pages | learn.microsoft.com/fabric/admin/region-availability and Copilot FAQ |
| W8 | ai_features | Q&A retirement details and Copilot replacement guidance | Deprecating Power BI Q&A page not fetched | go.microsoft.com/fwlink/?LinkId=2379220 |
| W8 | ai_features | Copilot FAQ, DAX query Copilot, web modeling, measure descriptions, subscription summaries not given own files | Time/budget | learn.microsoft.com/power-bi/create-reports/copilot-faq-fabric and dax/dax-copilot |
| W8 | ecosystem_tools | Excel cube functions (CUBEVALUE etc) over Power BI models | No page verified | Microsoft Support Excel cube functions plus Chris Webb / SQLBI posts |
| W8 | ecosystem_tools | DAX Studio current version, license, requirements | Project pages only partly readable | daxstudio.org/docs/license, requirements, GitHub releases |
| W8 | ecosystem_tools | Tabular Editor 3 prices | Pricing page showed no numbers | tabulareditor.com/pricing live |
| W8 | ecosystem_tools | Power Automate flows triggering refresh, Power Apps writeback patterns, Metadata Translator, Teams notifications | Not covered | Power Automate docs for Power BI connector |
| W8 | troubleshooting | DAX syntax and calculation error catalog | Not researched | Microsoft DAX docs, SQLBI, community |
| W8 | troubleshooting | Known issues list (Fabric support site) and monthly known issues | Not fetched | support.fabric.microsoft.com known issues |
| W8 | troubleshooting | Paginated report, Report Server and mobile errors; tile error catalog full list | Not covered | refresh-troubleshooting-tile-errors page |
