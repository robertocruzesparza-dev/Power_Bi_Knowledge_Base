---
id: 22.release_cadence_and_tracking
title: Release cadence and how to track change
domain: release_roadmap
type: how-to
level: beginner
tags: [release, roadmap, governance, monitoring]
summary: How often Power BI components ship, where Microsoft publishes changes, and a routine to stay current without reading everything.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S313, S335, S336, S337, S338, S341, S2800, S2801, S2802, S3016, S3018, S3026]
references: []
related: [22.fabric_roadmap_pointers, 22.deprecations_retirements, 22.gateway_release_history]
---

# Release cadence and how to track change

Purpose: give you a repeatable way to learn what changed and what is coming.

## Cadence (Fact unless noted)

- Power BI Desktop ships a new version every month. Older builds are not serviced, and files saved in a newer build may not open in older ones (S336).
- The service updates continuously; the monthly notes list service items beside Desktop items (S335, S336).
- The on-premises data gateway ships monthly, and Microsoft supports only the last six releases (S305, S313).
- Microsoft Fabric publishes new features monthly (S341).
- No December Desktop update appears in the 2024 and 2025 archive (S336).
- The Download Center build on 2026-11-02 was 2.159.883.0, published 2026-10-15 (S3018); the What's new page shows the October 2026 update as the newest monthly summary (S3016). On 2026-10-09 the build was 2.158.1304.0 (S2802) and the What's new page still showed August 2026 (S2801), so Learn can lag the download by days to weeks.
- The Desktop change log (bug-fix builds) listed no entry after the March 2026 quick fix 1 build (version 2.152.1057.0) when read on 2026-11-02 (S3026).

## Where changes are published

| Need | Place |
|---|---|
| Current month summary | Learn page "What's new in Power BI?" (S335) |
| Prior months | Learn page "Previous monthly updates to Power BI Desktop and the Power BI service" (S336) |
| Full feature lists with videos | Monthly "Power BI Feature Summary" blog post, linked from each month's Learn page (S335) |
| Desktop bug fixes | Power BI Desktop change log on Learn (S335) |
| Gateway versions | Learn page "On-premises data gateway monthly updates" (S313) |
| Fabric-wide news | Microsoft Fabric Updates blog and the What's new in Microsoft Fabric page (S337) |
| Planned features | Microsoft Fabric Roadmap site (S337, S338) |
| Mobile apps | "What's new in the mobile apps for Power BI" (linked from S336) |

## Routine

1. Weekly: skim the Fabric Updates blog titles.
2. Monthly, after the new release: read the Learn "What's new" page, focusing on General and Data connectivity sections for deprecations.
3. Monthly: update Desktop on authoring machines and gateways to a supported build.
4. Quarterly: check the roadmap for planned features that affect your plans, and update your tenant-setting review.
5. Keep a change log of deprecations with owners and dates (see [deprecations](22_deprecations_retirements.md)).

Microsoft's own adoption guidance rates staying current as a maturity trait. Administrators who review blog posts and release plans often can plan for change (S341).

## Reading a roadmap item

Release plans describe functionality that may not have shipped. Delivery timelines and projected functionality are subject to change or may not be released (Fact, S338 disclaimer). Treat roadmap dates as intent, not commitment.

## Common mistakes

- Treating a preview feature as production ready. Desktop preview features must often be enabled under Options > Preview features.
- Missing deprecations in the General section.
- Letting gateways drift more than six releases behind.

## See also

- [Fabric roadmap pointers](22_fabric_roadmap_pointers.md)
- [Gateway release history](22_gateway_release_history.md)
- [Release history 2026](22_release_history_2026.md)
