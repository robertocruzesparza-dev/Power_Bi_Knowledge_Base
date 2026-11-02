---
id: 12.audit_activity_logs
title: Audit and activity logs
domain: admin_governance_security
type: how-to
level: intermediate
tags: [audit, monitoring, admin, rest-api]
summary: How to read Power BI and Fabric user activity through the Purview audit log and the Activity Events REST API, with retention and paging rules.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1522, S1523, S1524, S2710, S2711]
references: [../references/admin_governance_security/12_audit_operations.md]
related: [12.governance_frameworks, 12.service_principals, 12.sensitivity_labels_purview]
---
## Purpose

The activity log records who did what to which item: viewed a report, exported data, changed a label, shared a dashboard. Admins use it for compliance, usage reports and adoption tracking.

## Key facts

- Fact: Most events appear within 30 minutes. A lag of up to 60 minutes can occur [S1522].
- Fact: You must be a Fabric administrator to read the activity log through Power BI APIs [S1522].
- Fact: The Activity Events API returns one day of data per request. Start and end must fall on the same UTC day and within the last 28 days [S1522, S2710].
- Fact: The Activity Events API allows a maximum of 200 requests per hour. Each continuation-token page counts as a request [S2710].
- Fact: A response holds about 5,000 to 10,000 entries plus a continuation token. Keep calling until no token is returned. A response can hold a token and zero events [S1522].
- Fact: The Fabric audit log is not a complete source for OneLake data-plane activity. Use OneLake diagnostics for that [S1524].

## Two ways to get events

| Method | Use when |
|---|---|
| Microsoft Purview audit search (portal) | Ad hoc investigation across Microsoft 365 services; CSV export |
| ActivityEvents REST API or `Get-PowerBIActivityEvent` | Scheduled export to a lake or database for reports |

The PowerShell cmdlet handles continuation tokens for you and has the same one-day rule [S1522]. Another route is the Office 365 Management Activity API for SIEM tools [S1523].

## Steps for the REST API

1. Install the MicrosoftPowerBIMgmt module, or use Cloud Shell.
2. Sign in with `Login-PowerBI`.
3. Call `Get-PowerBIActivityEvent` with start `2026-01-31T00:00:00` and end `2026-01-31T23:59:59`, optionally with `-ActivityType ViewDashboard`.
4. Convert the JSON and store it. Repeat per day [S1522].
5. For unattended jobs, use a service principal in a group allowed for read-only admin APIs. See [Service principals](12_service_principals.md).

## Retention

- Fact: Purview Audit (Standard) keeps records 180 days. Records made before 2023-10-17 kept 90 days [S1523].
- Fact: Audit (Premium) keeps Exchange, SharePoint, OneDrive and Entra records for one year by default. Other records, including Power BI, keep 180 days unless a retention policy extends them. The one-year default applies only to users with an E5-level or Purview audit license; other and guest users keep 180 days [S1523, S2711].
- Fact: Retention policies can reach one year, and up to 10 years with an add-on license [S1523].
- Fact: Export to your own store if you need longer history or custom reports.

## Common mistakes

- Querying a two-day range and getting an error.
- Stopping when a page returns no events but a token [S1522].
- Not exporting daily, then losing history after 180 days.
- Assuming every operation is logged for every item type. Check the [operation reference](../references/admin_governance_security/12_audit_operations.md).

## Limits and version notes

The Activity Events API cap is 200 requests per hour (verified 2026-10-08 in the REST reference [S2710]). Whether a 429 response carries a Retry-After header is not documented there (Unknown). Plan loops so one day needs few pages. Activity logging is not supported for Microsoft Cloud Deutschland [S2710]. Some fields such as capacity ID are null when a report is viewed from an app [S1524].

## See also

- [Operation reference](../references/admin_governance_security/12_audit_operations.md)
- [Governance frameworks](12_governance_frameworks.md)
