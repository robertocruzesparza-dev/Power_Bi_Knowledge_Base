---
id: 19.refresh_errors
title: Refresh failures - causes and fixes
domain: troubleshooting
type: troubleshooting
level: intermediate
tags: [troubleshooting, refresh, error-message, limits, capacity]
summary: The main reasons a scheduled or on-demand refresh fails or is disabled, with limits, throttling and out-of-memory guidance.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S2122, S2137, S2138, S2507, S2508, S2557]
references: [../references/troubleshooting/19_refresh_error_catalog.md]
related: [19.gateway_errors, 19.credentials_auth_errors, 19.diagnostics_workflow]
---

# Refresh failures - causes and fixes

## Purpose
Map a refresh symptom to its cause. Full message list: [refresh error catalog](../references/troubleshooting/19_refresh_error_catalog.md).

## Quick facts (volatile)
- Scheduled refresh times out after 2 hours; 5 hours for Premium workspaces [S2122].
- Imported models max 1 GB in the service; shared capacity also limits uncompressed data to 10 GB during refresh; Premium is not subject to these [S2122].
- Four consecutive failures disable the schedule. If an Embedded capacity is switched off, the first failure disables it [S2122].
- Power BI auto-retries; refresh history shows each attempt and splits Data from Query Cache [S2137].
- Dashboard tiles may take 10 to 15 minutes to show new data; repin if they stay stale [S2122].

## Triage table
| Symptom | Likely cause | Fix |
|---|---|---|
| Credentials error after about an hour | Entra ID OAuth token expires in about one hour; long loads fail | Shorten the load; SPO must use the Power BI sign-in account [S2122] |
| Capacity limit exceeded; Node level limit exceeded | Too many concurrent refreshes or node problem | Reschedule, retry; spread schedules [S2122] |
| 0xC13E0003 or "not enough memory" | Per-model memory limit hit | Partition or table refresh, incremental refresh, reduce model, scale-out, bigger SKU [S2122] |
| Fails after moving workspace | New capacity has lower per-model memory limit | Compare limits [S2122] |
| "cannot schedule refresh ... sources that don't support refresh" | Unsupported or dynamic data source | Find the provider in Advanced Editor and compare to supported list [S2138] |
| Container exited with code 0x0000DEAD | Service container fault | Disable schedule and republish [S2122] |
| Dataflow connector "matches no exports" | Connector unsupported in Premium dataflows | Use a non-Premium workspace [S2122] |
| Circular dependency on calculated table | SummarizeColumns change (Sept 2024) | Add dimension tables as filters; apply in one transaction via Tabular Editor [S2122] |
| "connection either timed out or was lost" | Slow fetch from semantic model source | Retry; Table.Buffer the outer-join table [S2122] |

## Common mistakes
- Ignoring "Completed with warnings"; invalid DAX references surface only there [S2137].
- Using XMLA refresh and expecting warnings in history [S2137].

## See also
- [Gateway errors](19_gateway_errors.md)
- [Credentials errors](19_credentials_auth_errors.md)
