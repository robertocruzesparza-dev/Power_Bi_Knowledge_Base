---
id: 22.fabric_roadmap_pointers
title: Fabric roadmap and release plan pointers
domain: release_roadmap
type: reference
level: beginner
tags: [roadmap, fabric, release, power-bi]
summary: Where Microsoft publishes the Fabric and Power BI roadmap, release plans and blogs, and what each source can and cannot tell you.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S337, S338, S341, S335, S343, S2803, S2845]
references: []
related: [22.release_cadence_and_tracking, 22.deprecations_retirements]
---

# Fabric roadmap and release plan pointers

Purpose: point you to the official planning sources. The roadmap site is a script-driven web app, so its item contents were not extracted. This file lists the sources, not planned features.

## Key facts

- Power BI is part of Microsoft Fabric. The official place for release plans is the Microsoft Fabric Roadmap at roadmap.fabric.microsoft.com (Fact, S337).
- The Power Platform 2024 release wave 2 plan states that Power BI and data integration moved to Microsoft Fabric. Plans for Power BI now live in the Fabric roadmap (Fact, from a docs search result, S343).
- The Fabric Updates blog (blog.fabric.microsoft.com) carries news and features. Community, marketing and case-study posts are on the Microsoft Fabric Blog (Fact, S337).
- On 2026-10-09 the Fabric What's new page listed September 2026 items (for example Fabric IQ in Microsoft 365 Copilot as generally available) and linked to the Fabric September 2026 Feature Summary post (Fact, S2803, S2845).
- The What's new in Microsoft Fabric page is continuously updated with preview and GA status. It also lists features currently in preview, for example Microsoft Fabric Embed, Fabric policies and a Microsoft ODBC driver for Fabric Data Engineering, as of 2026-10-07 (Fact, S337; not re-checked on 2026-10-09 because the page text was truncated).
- The May 2025 monthly notes announced a new Fabric roadmap tool with centralized, near real-time updates (Fact, S336).

## The roadmap site

The page shows filters for planned, recently released, and both planned and released features. It carries a disclaimer that plans may change and may not be delivered (Fact, S338). Use it for direction, not contracts.

## How to use it

1. Open the roadmap and filter to the Power BI or Fabric workload you care about.
2. Compare each planned item's stated timeframe with the monthly notes after that date.
3. Record items you depend on and re-check them each quarter.
4. When something ships, confirm its preview or GA state in the Learn monthly note before using it in production.

## Related governance guidance

Microsoft's adoption roadmap says high-maturity oversight teams review Fabric blog posts and release plans often to plan for changes (Fact, S341).

## Limits and unknowns

- Specific planned features and dates were not extracted. Gap logged: read the roadmap site directly (Unknown).
- Third-party summaries of monthly releases exist (community sites and newsletters). Treat them as community sources and prefer Microsoft posts.

## See also

- [Release cadence and how to track change](22_release_cadence_and_tracking.md)
- [Deprecations and retirements](22_deprecations_retirements.md)
