---
id: 08.scheduled_refresh
title: Scheduled refresh in the Power BI service
domain: service
type: how-to
level: intermediate
tags: [refresh, service, gateway, limits]
summary: How to configure scheduled and on-demand refresh of a semantic model in the service, with frequency limits, timeouts, and auto-disable rules.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S922, S923, S959, S931, S2604]
references: []
related: [08.data_alerts, 08.subscriptions, 08.lineage_impact_analysis, 08.license_requirements]
---
## Purpose

Import-mode semantic models hold a copy of the data. A schedule refreshes that copy. Gateways, credentials, and capacity limits decide whether it succeeds.

## Key facts

- Refresh updates the semantic model and, for Import and composite models, the dashboard tiles. Fact.
- DirectQuery and live connections rarely need refresh, but some metadata such as role security can still need processing. Fact.
- A gateway is needed when the source is not reachable over a direct network connection. Fact.
- With a standard on-premises gateway, credentials are defined by the gateway admin. With a personal gateway you enter them. Fact.
- The service starts a refresh within about 15 minutes of the slot; a delay of up to one hour can occur. It may start up to five minutes early. Fact.
- There is no monthly refresh interval in the UI. Use Power Automate or Fabric pipelines for monthly cadence. Fact.
- Refresh failure emails go to the owner; on-demand and programmatic refreshes do not send them. Fact.

## Limits by license

| Item | Pro (shared capacity) | PPU, Premium, Fabric capacity |
|---|---|---|
| Scheduled refreshes per day | 8 | 48 |
| API-triggered refreshes | Count against the same daily 8 | No fixed numeric limit; governed by capacity resources |
| Maximum refresh duration | 2 hours | 5 hours; XMLA endpoint refresh can exceed this |
| XMLA read-write endpoint | No | Yes |

Manual UI "Refresh now" does not count toward the 8 scheduled refreshes. Fact. With XMLA read-write, programmatic refresh via TMSL or PowerShell is effectively unlimited, within capacity limits. Fact.

## Steps to schedule refresh

1. Open the workspace and select the semantic model.
2. Choose Refresh, then Schedule refresh.
3. Under Gateway and cloud connections, pick the gateway or cloud connection.
4. Check data source credentials.
5. Turn on Configure a refresh schedule and add time slots in your time zone.
6. Optionally send failure notices to contacts, then apply.

## Automatic pauses and disables

- After two months with no one opening any report or dashboard on the model (including through an app or embed), the schedule pauses and the owner is emailed. Opening any dependent report resumes it; re-enable if needed. Fact.
- After four consecutive failures, or an unrecoverable error such as invalid credentials, the schedule is deactivated. The threshold cannot be changed. Fact.
- To re-enable: fix the cause, set the schedule slider back to On, and apply. Fact.

## Troubleshooting

1. Open Refresh history to see status, duration, and error text.
2. Check the gateway is online in Gateway and cloud connections.
3. Re-enter expired credentials.
4. If duration nears the cap, use incremental refresh or move to capacity.
5. On-premises SharePoint refresh supports only Anonymous, Basic, and Windows (NTLM or Kerberos) authentication, not ADFS or forms-based. Fact.

## Common mistakes

- Scheduling 8 refreshes on Pro and then also calling the API.
- Running a refresh and an email subscription at the same time, so the snapshot shows old data.
- Ignoring the inactivity pause on rarely used models.

## Limits and version notes

Numbers are volatile. The refresh-data article was updated 2026-10-01 and the scheduled refresh article 2026-05-06. The semantic model settings pane is in preview and may move menu items.

## See also

- [Subscriptions](08_subscriptions.md)
- [License requirements](08_license_requirements.md)
