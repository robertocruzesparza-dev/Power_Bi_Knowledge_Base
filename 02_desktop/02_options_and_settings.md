---
id: 02.options_and_settings
title: Desktop Options and settings
domain: desktop
type: reference
level: intermediate
tags: [desktop, reference, power-query, security, tooling]
summary: Where the Options dialog lives, its Global versus Current file split, and the verified settings for privacy, data load, diagnostics and query limits.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S014, S030, S031, S032, S033, S036, S029, S2833, S2836, S2837]
references: []
related: [02.preview_features, 02.limits]
---
## Purpose

Open the Options dialog with File, Options and settings, Options. It has a Global section (applies to all files) and a Current file section (stored with the file). This file lists settings Microsoft documents; it is not a full catalog.

## Key facts

- Fact: Many settings cannot be set by group policy or registry; preview toggles are among the user-controlled ones (S033).
- Fact: Data source settings (credentials and privacy levels) are under File, Options and settings, Data source settings (S036).
- Unknown: a complete current list of all Options pages; the Learn pages describe them one by one.

## Verified settings

| Setting | Where | Detail |
|---|---|---|
| Privacy (global or current file) | Options, Privacy | Chooses whether privacy levels are enforced (S036) |
| Parallel loading of tables | Options, Data Load, Global | Max simultaneous evaluations (default: logical CPU cores) and memory per evaluation (default 432 MB) (S030) |
| Diagnostics tracing | Options, Diagnostics, Global | Enable tracing, then Collect diagnostic information; saves a PBIDesktopDiagnosticInfo zip to Documents by default (S031) |
| Query Diagnostics without admin | Options, Diagnostics | Option "Enable in Query Editor" (S036) |
| Query limit simulation | Options, Current file, Report settings | Auto, Shared, Premium, SSAS, AAS, custom, none (S014) |
| Copy object names | Options, Report settings, Report objects | Adds "Copy object name" to right-click menus; useful for PBIR files (S029) |
| Preview features | Options, Preview features | See [preview features](02_preview_features.md) |
| Privacy firewall partitions | Options, Preview features | Enabled by default from the July 2026 build (S032) |

## Steps: simulate service query limits

1. Open Options, then Current file, then Report settings.
2. Find Query limit simulations.
3. Choose a capacity type. Auto picks the host if known, else Shared.
4. Check the timeout and memory shown under the list.

Limits by host (S014): Shared 225 s and 1 GB; Premium 225 s and 10 GB; SSAS 600 s and 1 GB; AAS 600 s and 10 GB. Custom value 0 means no limit.

## Common mistakes

- Leaving old reports on "no query limits". Reports made before the feature default to none, so visuals may pass in Desktop but fail when published (S014).
- Leaving tracing on. Diagnostics files may contain customer content such as source paths and parameter values (S036).
- Raising memory per evaluation above 90% of RAM; Microsoft advises against it (S030).

## Limits and version notes

- Fact: query limit simulation applies to Report view queries, not Data or Model view (S014).
- Fact: parallelism settings affect only your machine, not the service (S030).

## See also

- [Preview features](02_preview_features.md)
- [Limits](02_limits.md)
- Power Query domain: ../04_power_query_m/
