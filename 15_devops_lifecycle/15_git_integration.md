---
id: 15.git_integration
title: Fabric Git integration
domain: devops_lifecycle
type: concept
level: intermediate
tags: [git-integration, devops, workspace]
summary: How a Fabric workspace connects to Azure DevOps or GitHub, which roles can do what, branching options, and key limits.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1804, S1819, S1822, S2615]
references: [../references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md]
related: [15.pbip_format, 15.cicd_patterns, 15.deployment_pipelines]
---
## Purpose

Git integration links one workspace to one branch and folder of a Git repository. You commit workspace changes to Git and update the workspace from Git. This gives version history, branches, and pull requests for Power BI items.

## Key facts

- Fact: Supported providers are Azure DevOps (cloud only), GitHub, and GitHub Enterprise (cloud only) [S1804].
- Fact: An administrator must enable Git integration in the tenant [S1819].
- Fact: Power BI items covered include reports, semantic models, paginated reports, metrics sets, and org apps, mostly marked preview [S1804]. See the [item reference](../references/devops_lifecycle/15_pipelines_supported_items_and_permissions.md).
- Fact: Unsupported items stay in the workspace and are ignored by Git sync [S1804].
- Fact: Folder structure is mirrored, up to 10 levels. Empty folders are not copied [S1819].
- Fact: Items are stored as definition files. Semantic models use TMDL or BIM, and reports use PBIR or PBIR-Legacy. See [PBIP format](15_pbip_format.md).

## How it works

**Connect and sync.** Only a workspace admin connects. On first sync, if only one side has content, it is copied to the other. If both have content, you pick a direction. Updating the workspace from Git overwrites workspace content, so the tool asks you to confirm [S1819].

**Commit and update.** Commit pushes selected changed items. Update always pulls the whole branch to the latest commit. You cannot commit and update at once. Update is blocked when the same item changed on both sides until you resolve the conflict [S1819].

**Branching.** Options in the source control panel: branch out to another workspace (a private workspace per developer), checkout a new branch (admin), and switch branch. Workspace setting **Allow users with at least Contributor role to change Git branch** lets Contributors with write access switch branches [S1819].

**Git status.** Each item shows Synced, Conflict, Unsupported, Uncommitted changes, or Update required [S1819].

## Roles and permissions

| Operation | Workspace role |
|---|---|
| Connect, disconnect, sync | Admin |
| Commit or update | Contributor with write access to all items (and item owner if the tenant switch requires it) |
| See Git status | Admin, Member, Contributor |
| Viewer | No Git actions |

Git side: Azure Repos needs Read to connect and sync, plus Contribute for commits. GitHub fine-grained tokens need Contents Read, and Read and write to commit [S1819].

Each user signs in to Git individually. Do not share one GitHub personal access token across users [S1819].

## Steps

1. Admin opens Workspace settings, Git integration, picks the provider, repo, branch, and folder, then connects.
2. Choose the sync direction if both sides have content.
3. A developer edits items. The source control icon shows a count.
4. Select changes, add a comment, and commit.
5. To take others' work, choose Update.

## Common mistakes

- Committing straight to a protected branch. Branch policy must allow it, or use checkout branch and a pull request [S1819].
- Connecting a workspace with folders to a repo without them, then updating first. The Git structure overwrites the workspace folders [S1819].
- Using the service to download a PBIX after Git deployment. Results are unreliable; use Desktop [S1819].
- Refreshing a model with the enhanced refresh API and being surprised by a Git diff after each refresh [S1819].

## Limits and version notes

- 1,000 items per workspace. Sync fails above that [S1819].
- File size 25 MB. Branch name 244 characters. Full path 250 characters [S1819].
- Commit size: 25 MB for Azure DevOps with a service principal, 125 MB with a user account; 50 MB combined on GitHub [S1819].
- Not supported: submodules, sovereign clouds, B2B, template-app workspaces, My workspace, and models connected to Analysis Services [S1819].
- Sensitivity labels are not supported in export unless the admin allows exporting without labels [S1819].
- From 2026-12-01, users without read-write permission on workspace items cannot use Git integration [S1819].
- Git service principal support exists with the Azure DevOps provider [S1822].

## See also

- [PBIP format](15_pbip_format.md)
- [CI/CD patterns](15_cicd_patterns.md)
- [Deployment pipelines](15_deployment_pipelines.md)
