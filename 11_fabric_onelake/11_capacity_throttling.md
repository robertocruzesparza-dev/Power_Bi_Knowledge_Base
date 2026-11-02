---
id: 11.capacity_throttling
title: Capacity bursting, smoothing, and throttling
domain: fabric_onelake
type: concept
level: advanced
tags: [capacity, performance, monitoring, limits, fabric]
summary: How Fabric smooths compute, when it throttles interactive and background work, and how to stop throttling.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1242, S2619]
references: []
related: [11.fabric_capacity_and_licensing, 11.direct_lake]
---
## Purpose

Fabric lets a job use more compute than the SKU has (bursting), then repays it over time (smoothing). Throttling starts only when future capacity is used up.

## Key facts

- Fact: A timepoint is 30 seconds. A day holds 2,880. [S1242]
- Fact: Interactive operations are smoothed over at least 5 minutes, up to 64 minutes. Background operations are smoothed over 24 hours. [S1242]
- Fact: Throttling is per capacity. Another capacity can run normally. [S1242]
- Fact: Operations already running are never throttled. Only new requests. [S1242]
- Fact: Microsoft may change the throttling policy. [S1242]

Worked example (from Learn): a 1 CU-hour background job on an F2 adds about 2.1 percent to each timepoint and to the 10-minute and 60-minute limits. An F2 is not throttled by it. [S1242]

## Throttle stages

| Future capacity used | Stage | Effect |
|---|---|---|
| Up to 10 minutes | Overage protection | No throttling |
| 10 to 60 minutes | Interactive delay | New interactive jobs wait 20 seconds |
| 1 to 24 hours | Interactive rejection | New interactive jobs rejected; background still starts |
| Over 24 hours | Background rejection | All new requests rejected |

Source: S1242. Throttling ends when unused capacity repays the carryforward (burndown).

## Detect

- Error status `CapacityLimitExceeded`, message "Your organization's Fabric compute capacity has exceeded its limits. Try again later", or "Cannot load model due to reaching capacity limits". [S1242]
- Fabric Capacity Metrics app: the Throttling chart and System events table on the Compute page. Utilization over 100 percent alone is not throttling. [S1242]
- Slow reports are often item design, not throttling. [S1242]

## Stop throttling

F SKUs: [S1242]

1. Wait. Capacities self-heal.
2. Raise the SKU temporarily to burn down faster.
3. Pause and resume. Pausing bills the accumulated debt; a resume starts at zero.
4. Capacity overage billing, at three times the pay-as-you-go rate, up to a rolling 24-hour threshold the admin sets. Learn calls it opt-in in one sentence and enabled by default at capacity creation in another; check your capacity setting. [S2619]

P SKUs: turn on Autoscale. [S1242]

Scaling across the F256/F512 boundary may feel slower. [S1242]

## Exceptions

- Real-Time Intelligence skips the 20-second delay and starts throttling at the rejection stage. [S1242]
- Warehouse operations are almost all classed as background. [S1242]
- Eventstreams reduce allocated compute instead of rejecting new operations. [S1242]
- Compound throttling protection: a chain of calls is throttled once per capacity. Supported for DirectQuery between semantic models and for DAX from paginated reports. [S1242]
- Spark with Autoscale Billing is pay-as-you-go, with no smoothing. [S1242]

## Common mistakes

- Reading 100 percent utilization as an outage.
- Scheduling jobs apart to avoid spikes. Smoothing already spreads background cost.
- Pausing a busy capacity, which makes content unavailable.

## See also

- [Fabric capacity and licensing](11_fabric_capacity_and_licensing.md)
- [Direct Lake](11_direct_lake.md)
