---
id: 08.workspaces
title: Workspaces in the Power BI service
domain: service
type: concept
level: beginner
tags: [workspace, service, fabric]
summary: What workspaces are, their settings, folders, item limits, workspace type, and contact list, as documented for Fabric and Power BI.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S948, S949, S950, S951, S921, S957, S2608, S2609]
references: []
related: [08.workspace_roles, 08.service_overview, 08.license_requirements]
---
## Purpose

A workspace is a shared container where people collaborate on reports, semantic models, dashboards, and Fabric items. Workspaces also sit on OneLake as separately secured containers.

## Key facts

- Every user also has "My workspace" for personal content. Fact.
- By default new workspaces use the organization's shared capacity. They can be assigned to another capacity or a per-user license mode in settings. Fact.
- Workspace type has two groups: Power BI workspace types and Fabric workspace types. Fact.
- A workspace can hold up to 1,000 Fabric and Power BI items, parents and children together. Lower item-type limits still apply. Fact (volatile).
- A user with a Pro license can be a member of at most 1,000 workspaces. Fact (volatile).
- A tenant setting decides who may create workspaces: everyone, nobody, or specific security groups. Fact.
- Workspace admins can pin workspaces, set a contact list, link a Microsoft 365 group for a SharePoint library, and connect Git. Fact.

## Workspace settings

| Setting | What it does |
|---|---|
| Name, description, image | Help users identify the subject area and owner |
| Contact list | Users or groups who receive system notices about the workspace; the creator is the default contact |
| License mode (workspace type) | Pro, Premium per user, capacity, or Fabric; changeable later with some migration effort |
| Default storage format | Large semantic model format on capacity |
| Template app workspace | Special type for template apps; cannot be reverted to a normal workspace |
| SharePoint | Link a Microsoft 365 group; permissions are not synchronized with workspace roles |
| Azure connections | Dataflow storage in Azure Data Lake Gen2; Log Analytics connection for activity data |

Downgrading a capacity workspace to Pro first requires removing non-Power BI Fabric items. Fact.

## Folders

- Admin, Member, and Contributor can create, rename, move, and delete folders. Viewer can only view them. Fact.
- Folders inherit workspace permissions. Fact.
- You can nest folders up to 10 levels. Fact.
- Report names must be unique across the entire workspace, whatever folder they sit in. Publishing a same-named report goes to the existing report's location. Fact.
- Git integration does not support workspace folders, and folders are not supported in template app workspaces. Fact (as documented; may change).

## Steps to create a workspace

1. Start the create-workspace dialog from the workspace list. Exact button labels vary by release.
2. Enter a name and description.
3. Expand Advanced to set the contact list and workspace type.
4. Apply, then add users or groups with roles (see [Workspace roles](08_workspace_roles.md)).

## Common mistakes

- Putting everything in one workspace. Split development, test, and production content.
- Giving consumers workspace access when an app would do.
- Assuming a Microsoft 365 group's membership grants workspace roles. It does not.

## Limits and version notes

Item and workspace-count limits are volatile. Recheck the admin portal workspace article before planning a large estate.

## See also

- [Workspace roles](08_workspace_roles.md)
- [License requirements](08_license_requirements.md)
