---
id: 02.ref_installer_switches
title: Desktop installer command-line switches and registry
domain: desktop
type: reference
level: intermediate
tags: [desktop, reference, automation, admin]
summary: Silent-install switches, properties, MSI extraction, and the registry value that disables update notifications.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S002, S2804]
references: []
related: [02.install_and_requirements, 02.store_vs_exe_msi]
---
# Installer switches (reference)

Fact (S002): the executable accepts these switches.

| Switch | Behaviour |
|---|---|
| -q, -quiet, -s, -silent | Silent install |
| -passive | Progress bar only |
| -norestart | Suppress restart |
| -forcerestart | Restart without prompt |
| -promptrestart | Prompt if restart needed (default) |
| -l or -log, then a file | Write install log |
| -uninstall | Uninstall |
| -repair | Repair, or install if absent |
| -package, -update | Install (default) |

## Properties (property=value)

| Property | Meaning |
|---|---|
| ACCEPT_EULA | 1 accepts the licence |
| ENABLECXP | 1 joins the customer experience program |
| INSTALLDESKTOPSHORTCUT | 1 adds a desktop shortcut |
| INSTALLLOCATION | Install path |
| LANGUAGE | Locale such as en-US or de-DE; default is the Windows language |
| DISABLE_UPDATE_NOTIFICATION | 1 turns off update notices |

Example (S002): `PBIDesktopSetup_x64.exe -quiet LANGUAGE=de-DE ACCEPT_EULA=1`

## Extract an MSI

Fact (S002): if a tool needs an .msi, extract it from the .exe with the non-Microsoft WiX Toolset: `Dark.exe <installer path> -x <output folder>`. The MSI files appear in an AttachedContainer folder. Moving from an .exe install to an extracted MSI is unsupported without uninstalling first. WiX options may change; check its documentation.

## Disable update notifications by registry

Fact (S002): under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft Power BI Desktop add a REG_DWORD named DisableUpdateNotification with value 1, then restart.

## Related settings

Fact (S030): Power Query parallelism and memory-per-evaluation can also be set by registry DWORD values for organisation-wide control.
