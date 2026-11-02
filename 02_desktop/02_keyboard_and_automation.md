---
id: 02.keyboard_and_automation
title: Keyboard shortcuts and automation basics
domain: desktop
type: reference
level: intermediate
tags: [desktop, accessibility, cheatsheet, automation, tooling]
summary: Frequently used Desktop keyboard shortcuts, KeyTips, silent install and project-file automation routes.
status: mixed
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S002, S004, S012, S035]
references: []
related: [02.ui_tour, 02.file_formats]
---
## Purpose

Move faster and script what can be scripted. Press Shift and question mark inside Desktop to see Microsoft's own list (S012).

## Shortcuts

| Action | Keys (S012 unless noted) |
|---|---|
| Move focus between sections | Ctrl+F6 |
| Move focus forward or back in a section | Tab, Shift+Tab |
| Select or clear an object | Enter or Space |
| Multi-select | Ctrl+Space |
| Show ribbon KeyTips | Alt |
| Open context menu | Shift+F10 |
| Zoom canvas in or out | Ctrl+Plus, Ctrl+Minus |
| Expand all or collapse all tables in Data pane | Alt+Shift+9, Alt+Shift+1 |
| Activate Selection pane | F6 |
| Hide or show selected object | Ctrl+Shift+S |
| Move object forward or back in layers | Ctrl+Shift+F, Ctrl+Shift+B |
| Accessible Show data table | Alt+Shift+F11 (S035) |
| Show visuals as tables (preview at the time) | Ctrl+Shift+F11 (S035) |
| Model view: focus relationship line of a card | Ctrl+Alt+R |

Unverified: shortcuts for DAX query view and TMDL view; the pages read did not list them.

## Ribbon KeyTips

Press Alt to show letter boxes over ribbon commands. Press a letter to open a tab, then more letters for groups. Esc steps back. Alt again hides them (S035). Example: Alt then M opens Modeling.

## Automation routes

| Goal | Route | Source |
|---|---|---|
| Unattended install | Executable with -quiet and properties | S002 |
| Change many reports or measures | Edit PBIP/PBIR/TMDL text files by script | S004 |
| Programmatic model edits | Tabular Object Model library against project files, or external tools | S004 |
| Convert PBIX to PBIP | Not scriptable; File, Save as only | S004 |
| Deploy projects | Fabric Git integration, Fabric APIs, or Desktop publish | S004 |
| Agent-driven authoring | Desktop Bridge, preview since June 2026 | S011 |

## Common mistakes

- Using screen-reader tips without opening the reader first. Open it before files in Desktop (S012 notes).
- Editing project files with an editor that adds a BOM or changes line endings. Use UTF-8 without BOM; configure Git autocrlf because Desktop writes CRLF (S004).

## Limits and version notes

- Keyboard behaviour also applies in the Q&A Explorer, Getting Started, File menu, About, and restore dialogs (S012).
- Desktop Bridge is preview and may change; its documentation lives under the developer agentic pages (S011).

## See also

- [UI tour](02_ui_tour.md)
- [Install switches](../references/desktop/02_installer_switches.md)
- DevOps domain: ../15_devops_lifecycle/
