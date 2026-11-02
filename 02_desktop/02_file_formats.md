---
id: 02.file_formats
title: File formats - PBIX, PBIT, PBIP, PBIR, TMDL
domain: desktop
type: comparison
level: intermediate
tags: [desktop, pbip, pbir, tmdl, comparison, devops]
summary: What each Desktop file type contains, when to use it, how to convert between them, and PBIP and PBIR limitations.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S004, S005, S029, S019, S2538, S2539]
references: []
related: [02.limits, 02.desktop_vs_service]
---
## Purpose

Choose the right file type. Use PBIX for simple work, PBIT to share a starting point, and PBIP when you need Git or code editing.

## Comparison

| Format | Holds | Data included? | Use for |
|---|---|---|---|
| PBIX | Report, model, and data in one file | Yes | Everyday authoring, publishing |
| PBIT | Pages, visuals, model definition, queries, parameters (S005) | No | Reusable template; prompts for parameters on open |
| PBIP | Pointer file to a project folder | Cache is local only | Source control, CI/CD, code editing (S004) |
| PBIR | Report definition as many small JSON files (S029) | n/a | Readable diffs, copy pages and visuals |
| TMDL | Semantic model definition as text (S004) | n/a | Scripting and editing the model |

## PBIP folder layout

Fact (S004): saving as a project creates a root folder with a .pbip file, a Name.Report folder, a Name.SemanticModel folder, and a .gitignore (if none exists). The .gitignore excludes .pbi/localSettings.json and .pbi/cache.abf. The Report folder holds definition.pbir; the model folder holds definition.pbism.
Fact (S029): PBIR stores each page, visual, and bookmark in its own file under a definition folder.

## Convert and open

- PBIX to PBIP and back: File, Save as, in Desktop only. No programmatic conversion (S004).
- Create a template: File, Export, Power BI template. Open with double-click or File, Import (S005).
- Open a project by opening the .pbip or the report's .pbir file (S004).
- PBIR status: Fact (S029) it is generally available and the default report format. Editing a PBIR-Legacy report converts it silently, after a backup (30 days in Desktop, 28 days in the service).

## Common mistakes

- Editing undocumented files outside Desktop. Unsupported: report.json, mobileState.json, semanticModelDiagramLayout.json, diagramLayout.json (S004).
- Long folder paths. Windows' 260-character limit can break saves; use a short root (S004).
- Saving PBIP directly to OneDrive or SharePoint; unsupported, sync issues possible (S004).
- Saving external edits with a BOM. Use UTF-8 without BOM (S004).
- Expecting no data in PBIT filters. Filter and slicer values persist as metadata (S005, S029).

## Limits and version notes

- Fact (S004): not supported in PBIP: sensitivity labels, report page synonyms (linguistic schema), and the Report Server Desktop build. Row-level security members and incremental refresh partitions cannot be set via the Fabric REST API.
- Fact (S004): a PBIP cannot be deployed to Azure or SQL Server Analysis Services.
- Fact (S029): service limits on PBIR: 1,000 pages per report, 1,000 visuals per page, 300 MB for report files.
- Fact (S004): publishing from Desktop uses a temporary PBIX that includes the local data cache; Git and API deployment send metadata only.
- Downloading a PBIX from the service has limits (S019): see [limits](02_limits.md).

## See also

- [Limits](02_limits.md)
- [Desktop vs service](02_desktop_vs_service.md)
- Lifecycle domain: ../15_devops_lifecycle/
