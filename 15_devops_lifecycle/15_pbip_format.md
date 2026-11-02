---
id: 15.pbip_format
title: Power BI Project (PBIP) format
domain: devops_lifecycle
type: concept
level: intermediate
tags: [pbip, devops, desktop]
summary: What a Power BI Project folder contains, how to save and open it, how to deploy it, and the main limitations.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1803, S1806, S1821, S2932]
references: []
related: [15.tmdl_format, 15.pbir_format, 15.git_integration]
---
## Purpose

A PBIP saves a report and its semantic model as many small text files instead of one binary PBIX. Text files work with Git, diff tools, code editors, and scripts.

## Key facts

- Fact: Benefits listed by Microsoft: text editing, folder transparency, source control, CI/CD, and programmatic generation [S1803].
- Fact: A PBIP can be converted back to PBIX with Save As in Desktop. Conversion is only possible in Desktop, not by script [S1803].
- Fact: The `.pbip` file is only a pointer to the report folder. It is optional; opening `definition.pbir` also works [S1803].
- Fact: PBIP does not deploy to Azure or SQL Server Analysis Services [S1803].

## Folder layout

```
Project/
  Sales.Report/          report definition (PBIR)
  Sales.SemanticModel/   model definition (TMDL)
  .gitignore
  Sales.pbip
```

The default `.gitignore` excludes `.pbi/localSettings.json` and `.pbi/cache.abf` [S1803]. See [TMDL](15_tmdl_format.md) and [PBIR](15_pbir_format.md) for the inner folders. A `definition.pbir` file links the report to its model by relative path (`byPath`) or by connection (`byConnection`) [S1806].

## Steps

1. In Desktop, choose File, Save As, and pick the Power BI Project type.
2. Keep the root folder path short. Windows limits paths to 260 characters by default [S1803].
3. Initialize Git in the parent folder and commit.
4. Edit in Desktop or in a code editor. Desktop detects outside changes and offers **Apply external changes** [S1806].

## Deploy

Three routes [S1803]:
- Fabric Git integration.
- Fabric APIs (create or update item definitions).
- Desktop **Publish**, which makes a temporary PBIX. It also sends the local data cache, unlike the other routes.

For scripted deployment the `fabric-cicd` library accepts PBIP folders and handles item order and parameters [S1821].

## Common mistakes

- Saving a PBIP into a OneDrive or SharePoint folder directly. Desktop cannot save there directly; synced folders can fail on save [S1803].
- Saving outside files with a byte order mark. Use UTF-8 without BOM [S1803].
- Hand-editing files with undocumented schemas: `report.json` (legacy), `mobileState.json`, `semanticModelDiagramLayout.json`, and `diagramLayout.json` [S1803].
- Forgetting line endings. Desktop writes CRLF. Set Git `autocrlf` [S1803].
- Using `byPath` when deploying reports through Fabric APIs. Those require `byConnection` [S1806].

## Limits

- Sensitivity labels and report linguistic schema are not supported [S1803].
- Not supported in the Power BI Desktop build for Report Server [S1803].
- Row-level security role members and incremental refresh partitions cannot be read or set through the Fabric API [S1803].
- Edits outside Desktop can break opening; the error names the file where possible [S1803].
- Windows limits paths to 260 characters by default, so long table names can break a save. Use a short root folder [S2932].

## See also

- [TMDL format](15_tmdl_format.md)
- [PBIR format](15_pbir_format.md)
- [Fabric Git integration](15_git_integration.md)
