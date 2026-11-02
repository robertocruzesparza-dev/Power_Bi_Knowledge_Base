---
id: 19.diagnostics_workflow
title: Diagnostics workflow and logs
domain: troubleshooting
type: how-to
level: intermediate
tags: [troubleshooting, monitoring, desktop, gateway]
summary: A step-by-step order for diagnosing Power BI problems and how to collect Desktop traces, service browser traces, gateway logs and refresh history for support.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2126, S2127, S2140, S2123, S2137, S2144]
references: [../references/troubleshooting/19_refresh_error_catalog.md]
related: [19.known_issues_approach, 19.refresh_errors, 19.gateway_errors]
---

# Diagnostics workflow and logs

## Purpose
Find the failing layer first, then pick the right log. Example: a refresh fails; refresh history shows the error, the gateway log shows why.

## Triage order
1. Name the layer: Desktop, publish, service refresh, gateway, visual query, embedding, sign-in.
2. Read the exact error text and any code. Search the reference catalogs: [refresh](../references/troubleshooting/19_refresh_error_catalog.md), [gateway](../references/troubleshooting/19_gateway_error_catalog.md), [embedding](../references/troubleshooting/19_embedding_error_catalog.md).
3. Check the basics: latest Desktop and a supported gateway version [S2122].
4. Collect the right evidence (below), then escalate.

## Evidence by layer
| Layer | Evidence | How |
|---|---|---|
| Desktop | Trace files | File > Options > Diagnostics > Enable tracing; reproduce; open the traces folder. Typical path `%localappdata%\Microsoft\Power BI Desktop\Traces` [S2126, S2127] |
| Desktop | Diagnostics zip | Same page > Collect diagnostic information. Zip may include ErrorsInfo.yaml, DataModelSchema.json, Traces. Only save when support asks [S2126] |
| Mashup traces | Not in the zip | Empty the Traces folder, enable tracing, reproduce, close Desktop, zip the folder [S2126] |
| Service | Browser trace, HAR, console log | Capture per the service diagnostics page; admins attach to support requests in the Power Platform admin center [S2140] |
| Refresh | Refresh history | Dataset Refresh > Refresh history. Shows each automatic retry, with Data and Query Cache phases [S2137] |
| Gateway | Gateway logs | Enable additional logging, repeat the scenario, export logs from the gateway app; repeat on each cluster member if load balancing [S2123] |
| Embedding | Request ID | Log the `RequestId` response header; use Fiddler or browser F12 [S2124] |

## Key facts
- Fact: diagnostics can contain query text, table and column names and filter values, so review before sharing [S2126].
- Fact: Desktop startup problems: turn on tracing while Desktop runs and collect logs [S2144].
- Fact: refresh warnings (status Completed with warnings) are logged in history for service refreshes, but not for XMLA-initiated refreshes; the XMLA response carries them [S2137].

## Common mistakes
- Sending all old trace files. Send only recent ones [S2127].
- Exporting logs from only one member of a gateway cluster.

## See also
- [Known issues approach](19_known_issues_approach.md)
- [Refresh errors](19_refresh_errors.md)
