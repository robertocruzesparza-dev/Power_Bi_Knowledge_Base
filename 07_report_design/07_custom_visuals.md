---
id: 07.custom_visuals
title: Custom visuals, certification, and admin controls
domain: report_design
type: concept
level: intermediate
tags: [custom-visual, visual, admin, tenant-setting]
summary: Where custom visuals come from, what certified means, tenant and group-policy controls, the organizational store, and known limitations.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S966, S967, S968, S969, S931, S2913, S2934]
references: []
related: [07.visual_catalog, 07.accessibility, 07.design_principles]
---
## Purpose

Custom visuals add chart types beyond the built-in set. They also add risk, because a visual receives the data queried by its report.

## Key facts

- Custom visuals ship as `.pbiviz` packages built with the Power BI visuals SDK. Fact.
- A visual can contain code with security or privacy risks. Trust the author before importing. Fact.
- Certified visuals are AppSource visuals that passed Microsoft code requirements and tests, including a check that they do not call external services. Microsoft is not the author of non-Microsoft visuals. Fact.
- Some paid AppSource visuals use licenses you buy and then assign in the Microsoft 365 admin center. Fact.
- Licensed visuals are not enforced in report server, sovereign clouds, app-owns-data embedding, and publish to web. Fact.

## Sources of custom visuals

| Source | Notes |
|---|---|
| AppSource | Free and paid; each has a downloadable sample report; certified ones are marked |
| `.pbiviz` file | Import from a local computer; subject to tenant setting |
| Organizational store | Admin-approved list shown on the My organization tab of Get more visuals |

## Admin controls

Settings live in the Fabric admin portal under the Power BI visuals tenant settings. Fact.

| Setting | Effect |
|---|---|
| Allow visuals created using the Power BI SDK | Lets chosen users add AppSource and file visuals; off by default for these sources |
| Add and use certified visuals only | Blocks uncertified visuals in the service; off by default; does not affect organizational store visuals |
| Allow downloads from custom visuals | Visuals may download summarized data and configuration with user consent |
| AppSource custom visuals SSO | Visuals can get Microsoft Entra tokens containing name and email; off by default |
| Allow access to the browser's local storage | Visuals can store data in the browser |

Tenant settings affect only the service. For Desktop use group policy: `EnableCustomVisuals` and `EnableUncertifiedVisuals` under Software\Policies\Microsoft\Power BI Desktop (0 disables, 1 enables, default 1). Fact.

## Organizational store

- Admins add visuals from AppSource (auto-updated) or from a file, choose whether each is available, and can disable instead of delete. Fact.
- Organizational visuals auto-deploy to Desktop and are not supported in Power BI Report Server. Fact.
- Deleting a visual from the repository breaks reports that use it. Deletion is irreversible; use Disable. Fact.
- Organizational visuals cannot be exported to PowerPoint or shown in subscription emails. Only certified visuals imported directly from the marketplace support those. Fact.
- Visio, Mapbox, Power Automate, and Charticulator visuals will not render from the repository; add them from AppSource instead. Fact.

A balanced approach from Microsoft planning guidance: allow certified visuals only, and use organizational visuals for approved exceptions. Fact.

## Common mistakes

- Using an uncertified visual and then finding it missing from subscription emails or PowerPoint exports.
- Blocking uncertified visuals in the service but not in Desktop. Authors build reports that fail after publishing.
- Letting each author download their own version. Use the store to align versions.

## Limits and version notes

Uncertified visuals generally do not render in email subscriptions. Check each visual's bookmark and accessibility support before relying on it.

## See also

- [Built-in visual catalog](07_visual_catalog.md)
- [Accessibility](07_accessibility.md)
