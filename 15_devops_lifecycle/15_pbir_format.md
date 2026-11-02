---
id: 15.pbir_format
title: Power BI enhanced report format (PBIR)
domain: devops_lifecycle
type: reference
level: advanced
tags: [pbir, report, devops]
summary: The PBIR folder structure for reports, naming rules, conversion from PBIR-Legacy, and service size limits.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1806, S1803, S2616]
references: []
related: [15.pbip_format, 15.tmdl_format, 15.git_integration]
---
## Purpose

PBIR stores each report page, visual, and bookmark as its own JSON file. Two developers editing different visuals touch different files, so merges rarely conflict. PBIR-Legacy kept the whole report in one `report.json`.

## Key facts

- Fact: PBIR is generally available and the default report format [S1806].
- Fact: Every PBIR file has a public JSON schema, so editors such as Visual Studio Code validate edits [S1806].
- Fact: `definition.pbir` version 4.0 or higher can hold either format. Version 1.0 requires PBIR-Legacy [S1806].
- Fact: Fabric Git integration and Fabric REST APIs export reports as PBIR [S1806].
- Fact: Data values used in filters or slicer selections persist in the files, for example a filter on Company equals Contoso. Treat the repo as data-sensitive [S1806].

## Folder structure

Inside `definition\` [S1806]:

| Path | Required | Content |
|---|---|---|
| `report.json` | Yes | Report-level filters and formatting |
| `version.json` | Yes | PBIR version |
| `pages\pages.json` | No | Page order, active page |
| `pages\<page>\page.json` | Yes | Page filters and formatting |
| `pages\<page>\visuals\<visual>\visual.json` | Yes | Position, formatting, query |
| `...\mobile.json` | No | Mobile layout of a visual |
| `bookmarks\*.bookmark.json` | No | Bookmark state |
| `reportExtensions.json` | No | Report-level measures |

## Naming rules

- New objects get 20-character identifiers as names. Existing names are kept when converting a project [S1806].
- A name may use letters, digits, underscores, and hyphens only. Other names are ignored as private files [S1806].
- Restart Desktop after renaming files. Page binding names must be unique per report [S1806].
- Enable **Copy object names** under Report settings to find the folder of a clicked visual [S1806].
- Annotations (name-value pairs) are allowed on report, page, and visual. Desktop ignores them, so scripts can use them [S1806].

## Conversion from PBIR-Legacy

Editing and saving a legacy report converts it automatically. Desktop keeps a backup for 30 days. The service keeps one for 28 days, and **Restore as PBIR-Legacy** appears in report settings. A restore does not stop the next conversion [S1806].

## Limits

Service limits [S1806]: 1,000 pages per report; 1,000 visuals per page; 1,000 resource package files; 300 MB for all resource files; 300 MB for all report files.

## Common mistakes

- Copying a bookmark file without its pages and visuals. Invalid targets are removed.
- Copying a page with a duplicate page binding name.
- Hand-editing before saving in Desktop. Unsaved changes are overwritten on apply [S1806].
- Expecting visual automatic filters to be persisted before the filter pane has been opened once [S1806].

## See also

- [PBIP format](15_pbip_format.md)
- [TMDL format](15_tmdl_format.md)
- [Fabric Git integration](15_git_integration.md)
