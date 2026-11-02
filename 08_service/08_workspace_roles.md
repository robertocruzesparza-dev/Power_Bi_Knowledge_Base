---
id: 08.workspace_roles
title: Workspace roles and what each can do
domain: service
type: reference
level: beginner
tags: [workspace, service, security, reference]
summary: The four workspace roles (Admin, Member, Contributor, Viewer) and their Power BI capabilities, with license caveats and RLS behavior.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S921, S920, S958, S960, S940]
references: [../references/service/08_fabric_role_capabilities.md]
related: [08.workspaces, 08.item_permissions_sharing, 08.workspace_apps, 08.license_requirements]
---
## Purpose

Roles decide who can edit, publish, and administer a workspace. You assign them to individuals or to security groups, Microsoft 365 groups, and distribution lists.

## Key facts

- The roles are Admin, Member, Contributor, and Viewer. Fact.
- A user in several groups gets the highest role among them. Nested groups pass the role down. Fact.
- Microsoft Entra service principals can also hold roles for API operations in Fabric. Fact.
- Except viewing and interacting, the capabilities need a Pro or Premium per user (PPU) license. Fact.
- Use the Viewer role to enforce row-level security (RLS) for people who browse a workspace. Fact.
- Members cannot change existing users' roles. An admin must remove the user first, then a member can re-add at the new level. Fact.
- Disabling a user in Microsoft Entra ID does not delete workspace access records. They remain until the user is hard-deleted. Fact.

## Capability matrix

Power BI capabilities (Y means allowed).

| Capability | Admin | Member | Contributor | Viewer |
|---|---|---|---|---|
| Update and delete the workspace | Y | | | |
| Add or remove any user in any role | Y | | | |
| Add members or lower roles | Y | Y | | |
| Publish, unpublish, change permissions on an app | Y | Y | | |
| Update an app | Y | Y | If admin allows | |
| Share items and allow reshare | Y | Y | | |
| Create, edit, delete content | Y | Y | Y | |
| Copy a report; create reports from this workspace's model elsewhere | Y | Y | Y | |
| Schedule refresh through an on-premises gateway | Y | Y | Y | |
| Download a PBIX file | Y | Y | Y | |
| Analyze in Excel | Y | Y | Y | Needs Build permission |
| Subscribe others to reports | Y | Y | Y | |
| Create own subscriptions | Y | Y | Y | Y |
| Manage subscriptions created by others | Y | | | |
| View and interact with items | Y | Y | Y | Y |
| Lineage view | Y | Y | Y | |

Gateway rows also require permissions on the gateway itself. Fact.

## How roles combine

- Contributors can share items only if the app creator selected "Allow users to share the semantic models in this app", or if they hold Reshare on the item.
- In a workspace on capacity (Premium or Fabric F64 and larger), a Viewer can use content without Pro. A user with a higher role there is prompted to start a Pro trial when creating items.
- Consuming Dataflow Gen2 data through the connector needs Admin, Member, or Contributor. Viewer is not enough.
- Guest users with a role keep it even if the tenant setting for guest editing is off.

## Common mistakes

- Giving the Contributor role to consumers. Use Viewer or an app.
- Expecting a Viewer to see only some rows without RLS. Without RLS they see all model data.
- Putting a Viewer in another group with a higher role, which silently raises access and the license need.

## Limits and version notes

- A Pro user can belong to at most 1,000 workspaces. Fact.
- Fabric items add more capabilities per role; see [Fabric role capabilities](../references/service/08_fabric_role_capabilities.md).

## See also

- [Workspaces](08_workspaces.md)
- [Item permissions and sharing](08_item_permissions_sharing.md)
