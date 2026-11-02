---
id: 02.preview_features
title: Preview features in Desktop
domain: desktop
type: how-to
level: intermediate
tags: [desktop, how-to, release, best-practice]
summary: How to turn preview features on or off, the risks, and examples seen in 2026 with their current status.
status: preview
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S010, S011, S027, S028, S032, S033, S034, S037, S040, S2801, S2842, S3016, S3017]
references: []
related: [02.options_and_settings, 02.update_and_release_cadence]
---
## Purpose

Preview features let you try new capability early. They can change or vanish. Use them for learning, not for production.

## Key facts

- Fact: Microsoft recommends preview features only to evaluate and learn. They are subject to change, have limited support, and may not work the same in the service (S033).
- Fact: connectors marked Beta or Preview have limited support (S040).
- Fact: the Report Server Desktop build has no preview features (S033).
- Fact: the toggles save per user. Many need a restart (S028).

## Steps

1. Select File, Options and settings, Options.
2. Under Global, select Preview features.
3. Tick or clear the feature.
4. Restart Desktop.

## Examples and status

| Feature | Status as of last check | Note |
|---|---|---|
| On-object interaction | Preview | Moves build and format onto the visual (S028) |
| Relationship pane editing | Preview | Edit relationships in Properties pane (S037) |
| Publish dialogs support folder selection | Preview | Publish into workspace folders (S034) |
| Save to and Share to OneDrive and SharePoint | Enabled by default | Builds from March 2026 or older lose it from October 2026 (S027, S010, S3017) |
| Gantt chart visual | Preview (October 2026) | Core visual for task durations, progress and milestones; enable under Preview features and restart Desktop (S3016) |
| List slicer dropdown option | Preview (October 2026) | Dropdown mode with selection pills; Show selected first in list and button slicers (S3016) |
| Modern visual defaults, Theme pane | GA in August 2026 | Was preview in March 2026 (S011, S010) |
| Direct Lake calculated columns | Preview (August 2026) | S010 |
| Desktop Bridge for agents | Preview (June 2026) | S011 |
| Privacy firewall partitions | On by default since July 2026 build | Can still be turned off (S032) |

Unverified: whether the August 2026 preview items (Direct Lake calculated columns, Desktop Bridge) reached general availability by September or October 2026. The October 2026 What's new page does not list them as GA (S3016).

## Common mistakes

- Enabling many previews, then wondering why screenshots do not match docs (S028).
- Publishing a report built with a preview feature and finding the service behaves differently (S033).
- Assuming "enabled by default" means "not preview". Check the feature page.

## Limits and version notes

- Volatile. Status moves monthly. Check the monthly update page and the feature's own Learn page.
- Fact: the pane arrangement dialog first appeared with the December 2023 build for on-object users (S028).

## See also

- [Options and settings](02_options_and_settings.md)
- [Update cadence](02_update_and_release_cadence.md)
