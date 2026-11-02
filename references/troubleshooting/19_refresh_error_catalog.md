---
id: 19.refresh_error_catalog
title: Refresh error and limit catalog
domain: troubleshooting
type: reference
level: intermediate
tags: [troubleshooting, refresh, error-message, limits, reference]
summary: Catalog of documented refresh errors, messages and limits in the Power BI service with cause and fix, verified from Microsoft Learn.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S2122, S2137, S2138, S2129, S2838, S2839]
references: []
related: [19.refresh_errors]
---

# Refresh error and limit catalog

| Message or code | Cause | Fix | Source |
|---|---|---|---|
| You've exceeded the capacity limit for semantic model refreshes. Try again when fewer semantic models are being processed. | Premium throttling of concurrent refreshes | Reschedule, space refreshes, retry | S2122 |
| Capacity level limit exceeded. | Too many refreshes for purchased capacity | Retry or reschedule | S2122 |
| Node level limit exceeded. | Node-level system error | Retry or reschedule | S2122 |
| Query memory limit exceeded | Memory governance | Partition-level refresh, reduce model | S2122 |
| This operation was canceled because there wasn't enough memory to finish running it. | Memory governance | As above; scale-out; larger SKU | S2122 |
| 0xC13E0003 | Memory pressure cancellation | As above | S2122 |
| Container exited unexpectedly with code 0x0000DEAD | Service container fault | Disable schedule, republish | S2122 |
| Processing Error: The following system error occurred: Type Mismatch | M script or old Desktop | Fix M, update Desktop | S2122 |
| GatewayNotReachable (setting credentials) | Outdated gateway | Install latest gateway | S2122 |
| Expression.Error: The import "connector" matches no exports | Connector unsupported in Premium dataflows | Use non-Premium workspace | S2122 |
| Gateway version isn't supported (dataflow) | Gateway older than last six versions | Update gateway | S2122 |
| You cannot schedule refresh for this semantic model because it gets data from sources that currently don't support refresh. | Unsupported source | Check provider against supported list | S2138 |
| Evaluation resulted in a stack overflow | Non-terminating recursive M | Add end condition or iterate | S2143 |
| Evaluation ran out of memory | Large in-memory table operations | Reduce Table.Buffer use or data | S2143 |

## Limits table
| Limit | Value | Source |
|---|---|---|
| Imported model size in service | 1 GB | S2122 |
| Uncompressed data during refresh, shared capacity | 10 GB | S2122 |
| Scheduled refresh timeout | 2 hours; 5 hours in Premium | S2122, S2838 |
| Scheduled refreshes per day | 8 for Pro; 48 for PPU, Premium and Fabric capacity | S2839 |
| Consecutive failures before schedule disabled | 4 | S2122 |
| Entra ID OAuth token lifetime | about 1 hour | S2122 |
| Tile update lag after refresh | 10 to 15 minutes | S2122 |

## Other behavior
- ANY-type column with TRUE or FALSE can become -1 or 0 in the service [S2122].
- Web.Page based Web connector models updated after 18 Nov 2016 need a gateway [S2122].
- Scheduled refresh pauses after two months with no views of the model's reports; the owner gets an email [S2839].
- Refresh history lists each retry; Data and Query Cache are separate phases [S2137].
- Tile errors have their own catalog [S2129].
