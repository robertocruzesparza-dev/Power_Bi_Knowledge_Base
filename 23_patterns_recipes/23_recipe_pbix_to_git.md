---
id: 23.recipe_pbix_to_git
title: Recipe - move a PBIX report into Git
domain: patterns_recipes
type: how-to
level: intermediate
tags: [pbip, git-integration, devops, how-to]
summary: Steps to convert a PBIX into a PBIP project, commit it, and connect a Fabric workspace to the repository.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1803, S1806, S1819, S1804, S2932, S2936]
references: []
related: [15.pbip_format, 15.git_integration, 15.pbir_format]
---
## Goal

Replace a binary PBIX with text files under version control, and let a workspace sync with the repo.

## Before you start

- An admin has enabled Git integration in the tenant [S1819].
- You can create a Git repository in Azure DevOps or GitHub (cloud) [S1804].
- Your report does not depend on a model in My workspace or Analysis Services. Those reports are excluded [S1804].
- The report does not rely on sensitivity labels in the project. Labels are not supported in PBIP [S1803].

## Steps

1. Create a short local folder, for example `C:\src\sales`. Long paths can break saves [S1803].
2. Open the PBIX in Power BI Desktop. Choose File, Save As, and the Power BI Project type, and save into the folder.
3. Initialize Git in that folder. Keep the generated `.gitignore`, which excludes `localSettings.json` and `cache.abf` [S1803].
4. Set `core.autocrlf` as advised, because Desktop writes CRLF line endings [S1803].
5. Commit and push to a branch.
6. In the Fabric workspace, an admin opens Workspace settings, Git integration, and connects to the repo, branch, and folder. If the workspace is empty, content syncs from Git [S1819].
7. Developers use branches. Each can branch out to a private workspace [S1819].
8. Edit in Desktop or Visual Studio Code. Desktop offers **Apply external changes** when files change [S1806].
9. Commit from Desktop tooling or the service source control panel; update the workspace from Git.

## Checks

- The repo shows `Sales.SemanticModel` and `Sales.Report` folders.
- `definition.pbir` points to the model with `byPath` [S1806].
- The workspace shows a Git status of Synced.

## Common mistakes

- Pushing the cache file. Check the `.gitignore` [S1803].
- Using the service to export a PBIX after Git deployment and expecting an exact copy [S1819].
- Treating the repo as free of data values. Filter values persist in report files [S1806].
- Both sides have content at first connect: choose the sync direction carefully, because updating the workspace overwrites it [S1819].

## See also

- [PBIP format](../15_devops_lifecycle/15_pbip_format.md)
- [Fabric Git integration](../15_devops_lifecycle/15_git_integration.md)
- [PBIR format](../15_devops_lifecycle/15_pbir_format.md)
