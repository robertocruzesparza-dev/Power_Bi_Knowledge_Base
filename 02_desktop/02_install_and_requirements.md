---
id: 02.install_and_requirements
title: Install Power BI Desktop and system requirements
domain: desktop
type: how-to
level: beginner
tags: [desktop, how-to, tooling, limits]
summary: How to install Power BI Desktop, the minimum Windows requirements, unsupported setups, and the 64-bit rule.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S002, S006, S2549]
references: [../references/desktop/02_installer_switches.md]
related: [02.store_vs_exe_msi, 02.update_and_release_cadence]
---
## Purpose

Install the free Windows authoring app. Two routes exist: the Microsoft Store app or the downloadable executable. Both install the latest version (S002).

## Key facts

- Fact: Desktop is free (S006).
- Fact: only the latest release is supported. Support will ask you to upgrade (S002).
- Fact: the 32-bit version is no longer supported. Install the 64-bit build (S002).
- Fact: the Report Server Desktop build is a separate installation (S002).

## Steps

Store route:
1. Open the Power BI Desktop page of the Microsoft Store (also reachable from the service: Download icon, then Power BI Desktop).
2. Select Install.

Executable route:
1. Go to the Microsoft Download Center page for Power BI Desktop.
2. Select Download and choose the 64-bit file. Run it as an administrator.
3. Accept the licence terms and finish. A welcome screen appears at first launch.

To check your version: Help ribbon, About, Version line (S002).

## Minimum requirements

| Item | Requirement (S002) |
|---|---|
| OS | Windows 10 or Windows Server 2016 or later; Windows on ARM needs the 2025-09 cumulative update (KB5065789) |
| .NET | 4.7.2 or later |
| Browser engine | Microsoft Edge WebView2 |
| Memory | 2 GB minimum, 4 GB or more recommended |
| Display | At least 1440x900 or 1600x900; text scaling above 100% hides some dialogs |
| CPU | 1 GHz 64-bit (x64) or better |

## Unsupported setups

- Fact (S002): running under a system account fails because WebView2 does not support it. Typical error: "Microsoft Edge can't read and write to its data directory."
- Fact (S002): Citrix published apps and other virtual desktops are unsupported. Azure Virtual Desktop and Windows 365 are supported.
- Fact (S002): Internet Explorer Enhanced Security Configuration breaks sign-in. Prefer a client Windows over Server.
- Fact (S002): side-by-side Store and old MSI installs are unsupported. Uninstall first.

## Common mistakes

- Setting Windows display scaling above 100% and then not seeing a dialog. Reset to 100% (S002).
- Black areas on screen. Fix: Windows setting "Let Windows fix apps that are blurry", then restart (S002).
- Error "We weren't able to restore the saved database to the model" often means an outdated Desktop; update (S002).

## See also

- [Store versus executable](02_store_vs_exe_msi.md)
- [Installer switches](../references/desktop/02_installer_switches.md)
- [Update and release cadence](02_update_and_release_cadence.md)
