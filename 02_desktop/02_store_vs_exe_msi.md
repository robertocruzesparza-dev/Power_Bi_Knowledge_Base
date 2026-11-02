---
id: 02.store_vs_exe_msi
title: Store app versus executable (and the MSI)
domain: desktop
type: comparison
level: intermediate
tags: [desktop, comparison, decision-guide, tooling]
summary: Compares installing Desktop from the Microsoft Store, from the downloadable executable, and from an extracted MSI.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S002, S033, S2804, S2805]
references: [../references/desktop/02_installer_switches.md]
related: [02.install_and_requirements, 02.update_and_release_cadence]
---
## Purpose

Pick the install route that fits your people. Individuals usually want the Store. IT teams with deployment tools may want the executable.

## Comparison

| Aspect | Microsoft Store | Executable (.exe) | MSI |
|---|---|---|---|
| Updates | Automatic in background | Manual, or notification | Manual |
| Download size per update | Only changed parts | Full installer | Full |
| Admin rights to install | Not needed | Needed | Needed |
| IT rollout | Microsoft Store for Business | Command-line switches | Extract from .exe yourself |
| Languages | All; detected at each launch | All in one package | Same package |
| Settings copied from .exe install | No; reconnect sources and credentials | n/a | n/a |
| Status | Supported | Supported | The old official MSI is deprecated (S002) |

All rows from S002.

## How to choose

- Individual or analyst: Store. It stays current without effort.
- Locked-down PC with no Store access: executable.
- Software-distribution tool that demands MSI: extract it with WiX (see [reference](../references/desktop/02_installer_switches.md)). Fact: this is a non-Microsoft route.
- Need a fixed older version: download from the monthly archive. Newer files cannot be opened by older builds (S002).
- Need a Report Server build: separate installer (S002, S033).

## Common mistakes

- Installing Store and an old MSI side by side. Unsupported; uninstall one (S002).
- Switching from .exe to Store and assuming recent files and credentials carry over. They do not (S002).
- The SAP connector may need driver files moved to Windows\System32 under the Store build (S002).
- Pinning a version for the whole team but forgetting the Store auto-updates. Inference: use the executable and the DisableUpdateNotification value when you must freeze a version.

## Limits and version notes

- Fact: the 32-bit build is unsupported (S002, S2804).
- Fact: Desktop is supported on Azure Virtual Desktop and Windows 365. Citrix and other virtual desktop setups are not supported (S2804).
- Fact: Microsoft says only the latest version is supported, so freezing versions has support risk (S002).
- Fact: Microsoft advises using preview features only to evaluate, not for mission-critical work (S033).

## See also

- [Install and requirements](02_install_and_requirements.md)
- [Update and release cadence](02_update_and_release_cadence.md)
