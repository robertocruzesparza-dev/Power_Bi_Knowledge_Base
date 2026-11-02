---
id: 01.report_server_and_deployment_options
title: Report Server and deployment options
domain: foundations
type: comparison
level: intermediate
tags: [report-server, service, desktop, licensing, comparison]
summary: Compares the cloud service with Power BI Report Server, including the separate Desktop build and licensing rules for each.
status: mixed
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S013, S002, S033, S029, S2805, S2806, S2807, S3024, S3025]
references: []
related: [01.product_family_and_components, 01.licenses_and_capacity]
---
## Purpose

Some organisations keep reports on their own servers. Power BI Report Server supports that. This file shows how it differs from the cloud service.

## Key facts

- Fact: Power BI Report Server is an on-premises server with a web portal. It hosts Power BI reports (.pbix), paginated reports (.rdl), mobile reports, KPIs, and (before the January 2026 release removed Office Online Server support) Excel workbooks (S013, S3024).
- Fact: it is a superset of SQL Server Reporting Services (S013).
- Fact: you author for it with a separate Desktop build optimised for Report Server (S013, S002).
- Fact: a hybrid deployment is possible with an F64 reserved instance (S013).
- Fact (checked 2026-11-02): the newest release on Learn is Power BI Report Server September 2026, version 1.27.9794.1532 (build 15.0.1122.101), released 2026-10-26, with Desktop for Report Server 2.158.1602.0 (S3024, S3025).

## Comparison

| Aspect | Power BI service | Power BI Report Server |
|---|---|---|
| Hosting | Microsoft cloud | Your servers or Azure VMs |
| Authoring app | Latest Desktop (monthly) | Report Server Desktop build (three times a year: January, May, September, per S2806) |
| Preview features | Available in Desktop | Not available in the Report Server build (S033) |
| Power BI projects (PBIP) | Supported | Not supported (S004) |
| Dashboards, dataflows, Copilot | Yes (S017) | No; the portal organises reports and KPIs (S013) |
| Licensing | Per-user and capacity | Core-based; see below |

## Choosing a Desktop build

- Fact: the Report Server Desktop build installs separately and can run side by side with the standard build (S002).
- Fact: Microsoft lists two strategies for authors who publish to both targets (S033). Option 1: use only the Report Server build; new features arrive about every four months. Option 2: run both builds side by side.
- Inference: Option 2 gives newer features for the cloud but needs care so that a file saved in the newer build does not break on the server.

## Common mistakes

- Opening a Report Server file in the latest Desktop, saving, and then failing to publish to the server. Match the build to the target.
- Expecting preview features or PBIP projects with the Report Server build (S033, S004).

## Limits and version notes

- Volatile licensing. Fact (S013): Report Server runs under core-based licensing, available through Fabric F64+ reserved instances and SQL Server licensing paths. It is included with Premium P SKUs, not EM SKUs, and not with F SKUs below F64 reserved.
- Fact (S013): with an F64+ reserved instance, a Pro license is needed to publish both paginated and Power BI reports to Report Server. Viewing does not need Pro.
- Fact (S2807): with SQL Server 2025, Report Server may run on the licensed server up to the number of core licenses (minimum four per operating system environment) or in Azure with one core license per virtual core. For SQL Server Enterprise versions before 2025, use rights need active Software Assurance and end when it expires. For SQL Server editions, Pro is needed only to publish Power BI reports, not paginated reports.
- Verify details in the licensing domain before purchase.

## See also

- [Product family](01_product_family_and_components.md)
- [Licenses and capacity](01_licenses_and_capacity.md)
- [Desktop install and versions](../02_desktop/02_install_and_requirements.md)
