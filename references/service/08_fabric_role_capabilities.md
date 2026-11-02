---
id: 08.fabric_role_capabilities
title: Fabric item capabilities by workspace role
domain: service
type: reference
level: intermediate
tags: [workspace, fabric, reference]
summary: Reference table of Fabric (non-Power BI) item capabilities for Admin, Member, Contributor, and Viewer workspace roles.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S920, S2940]
references: []
related: [08.workspace_roles]
---
## Purpose

This extends [Workspace roles](../../08_service/08_workspace_roles.md) with Fabric data items. Y means allowed.

## Role table

| Capability | Admin | Member | Contributor | Viewer |
|---|---|---|---|---|
| Update and delete the workspace | Y | | | |
| Add or remove people, including admins | Y | | | |
| Add members or lower roles | Y | Y | | |
| Allow others to reshare items | Y | Y | | |
| Create or modify database, mirroring, and warehouse items | Y | Y | Y | |
| Create workspace identity | Y | | | |
| Connect workspace to a Git repository | Y | | | |
| View content of pipelines, notebooks, Spark job definitions, ML items, eventstreams, KQL items, real-time dashboards | Y | Y | Y | Y |
| Connect to a SQL analytics endpoint of a lakehouse or warehouse | Y | Y | Y | Y |
| Read lakehouse and warehouse data through T-SQL (ReadData) | Y | Y | Y | Y |
| Read data through OneLake APIs, Spark, lakehouse explorer (ReadAll) | Y | Y | Y | |
| Subscribe to OneLake events | Y | Y | Y | |
| Write or delete pipelines, notebooks, Spark jobs, ML items, eventstreams | Y | Y | Y | |
| Write Eventhouses, KQL querysets, real-time dashboards, lakehouse and warehouse data | Y | Y | Y | |
| Run or cancel notebooks, Spark jobs, pipelines | Y | Y | Y | |
| View execution output | Y | Y | Y | Y |
| Schedule refresh via on-premises gateway; edit gateway connection | Y | Y | Y | |

## Footnotes

- Contributors and Viewers can also share items if they hold Reshare permission.
- Reading shortcut data needs extra permissions at the shortcut target.
- Eventhouse operations use a hybrid role model with extra permissions.
- Gateway actions also need gateway permissions, managed separately.
- Business event data is governed by data access roles, not workspace roles.
- For the Items and Job Scheduler REST APIs: Admin, Member, and Contributor can create, modify, start, and cancel; every role can read run status and output.

## See also

- [Workspace roles](../../08_service/08_workspace_roles.md)
