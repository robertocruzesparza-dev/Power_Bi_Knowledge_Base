---
id: 22.gateway_release_history
title: On-premises data gateway release history
domain: release_roadmap
type: reference
level: intermediate
tags: [gateway, release, monitoring]
summary: Recent monthly on-premises data gateway builds from May to October 2026 and the six-release support rule.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: high
sources: [S305, S313, S2800, S3019]
references: []
related: [03.gateway_install_network_ha, 22.release_cadence_and_tracking]
---

# On-premises data gateway release history

Purpose: tell you which gateway builds are current and supported.

## Key facts

- The gateway has a new release every month (Fact, S305).
- Microsoft actively supports only the last six releases (Fact, S305).
- Each release offers a standard installer and a personal-mode installer (Fact, S313).
- The Learn page lists six builds. Older builds are not listed there, so earlier history is unknown (Fact, S313).

## Builds listed on 2026-11-02 (Fact, S3019; earlier reads S313, S2800)

| Release | Build number |
|---|---|
| October 2026 | 3000.338 |
| September 2026 | 3000.334 |
| August 2026 | 3000.330 |
| July 2026 | 3000.326 |
| June 2026 | 3000.322 |
| May 2026 | 3000.318 |

Each month adds four to the minor number in this sample (Inference).

On 2026-11-02 the page lists October 2026 (3000.338) as the newest build and April 2026 (3000.314) has dropped off the supported list (Fact, S3019). On 2026-10-09 September 2026 (3000.334) was still the newest (S2800). The September download links are now labelled "September 2026 version", so the earlier label slip is fixed.

## What to do

1. Find your gateway version in the gateway app.
2. If it is older than May 2026, update now.
3. Update all cluster members to the same build (Fact, S309).
4. For Fabric items that use the gateway, update to the latest version so feature changes propagate (Fact, S313).

## Past compatibility notice

Dataflows using a gateway older than April 2021 might fail from March 15, 2023 (Fact, S305).

## Per-release feature lists

Each month links to a "List of features released" section on the Learn page. Open the page for details (Unknown here; not extracted).

## See also

- [Gateway install, network and clusters](../03_data_sources/03_gateway_install_network_ha.md)
- [Release cadence and tracking](22_release_cadence_and_tracking.md)
