---
id: 02.update_and_release_cadence
title: Desktop updates, release cadence, and version rules
domain: desktop
type: concept
level: intermediate
tags: [desktop, release, tooling, report-server]
summary: Monthly Desktop releases, the latest-only support rule, how to hold or freeze updates, and the separate Report Server cadence.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S002, S010, S011, S033, S027, S2556, S2518, S3016, S3017, S3018]
references: []
related: [02.install_and_requirements, 02.store_vs_exe_msi, 02.preview_features]
---
## Purpose

Desktop changes every month. Knowing the rules prevents surprise file-format and support problems. There are no user-selectable "channels" for the standard build; there is one monthly stream plus a separate Report Server build.

## Key facts

- Fact: Microsoft releases Desktop monthly. Only the latest version is supported (S002).
- Fact: older versions cannot open files saved by newer ones. Opening a newer file in an old build and saving can lose data tied to new features (S010).
- Fact: only English builds of previous versions are archived (S010).
- Fact: a change log tracks bug fixes between monthly releases (S010).
- Fact (re-verified 2026-11-02): the Microsoft Download Center lists Desktop version 2.159.883.0, published 2026-10-15. That is the October 2026 release, and the Learn "What's new" page now shows the October 2026 update as current (S3016, S3018). The previous Download Center build, 2.158.1304.0 (published 2026-10-07), was the September 2026 release (minor 158 follows July 156 and August 157), and Learn now carries a September 2026 section for it (S2556, S2518, S3017). The August build number (2.157.x) is still unverified.

## Recent versions

| Release | Version | Notable item (S011, S010) |
|---|---|---|
| March 2026 | 2.152.882.0 | Translytical task flows GA; modern visual defaults preview |
| April 2026 | 2.153.910.0 | Fixed-size layout for cards and slicers |
| May 2026 | 2.154.1260 | Visual calculations GA; new Get Data experience preview |
| June 2026 | 2.155.756.0 | Desktop Bridge preview; PBIR default-on rollout update |
| August 2026 | 2.157.x (exact build unverified) | Modern visual defaults GA; calculated columns on Direct Lake preview |
| September 2026 | 2.158.1304.0 | Agentic authoring, Microsoft 365 Copilot integration, new Power Query editor (S3017, S2518) |
| October 2026 | 2.159.883.0 | Gantt chart and dropdown list slicer in preview; Power BI Report skill can add custom visuals (GA) (S3016, S3018) |

## Holding back updates

- Fact: set DisableUpdateNotification to 1 in the registry to silence notices (S002). Details in the [reference](../references/desktop/02_installer_switches.md).
- Fact: or pass DISABLE_UPDATE_NOTIFICATION=1 at install (S002).
- Fact: Store installs update automatically (S002).
- Inference: freezing carries support risk because Microsoft supports only the latest build.

## Report Server cadence

Fact: the Report Server build follows the server release cadence, usually three times per year, and offers no preview features (S033).

## Common mistakes

- A team on mixed versions. Files saved by the newest build may not open for others (S010).
- Ignoring deprecation notices. Example: since October 2026, builds from March 2026 or earlier cannot save or share to OneDrive and SharePoint (S010, S027, S3017).

## Limits and version notes

- Volatile: check the monthly update page for the current version.
- Fact: the Windows on ARM requirement of the 2025-09 cumulative update is stated in the install guidance (S002).

## See also

- [Preview features](02_preview_features.md)
- [Store vs executable](02_store_vs_exe_msi.md)
- Release domain: ../22_release_roadmap/
