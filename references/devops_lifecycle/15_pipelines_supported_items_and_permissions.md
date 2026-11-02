---
id: 15.ref_pipelines_items_permissions
title: Pipelines reference - supported items and permissions
domain: devops_lifecycle
type: reference
level: intermediate
tags: [deployment-pipeline, reference, limits]
summary: Reference lists of Power BI item types supported by deployment pipelines and Git, plus the permission matrix for pipeline actions.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1802, S1804, S1823, S1819, S2930, S2931, S2936]
references: []
related: [15.deployment_pipelines, 15.git_integration]
---
## Power BI items in pipelines

As listed on 2026-10-07 [S1802]. The full list also includes many Fabric item types (lakehouse, notebook, pipeline, warehouse, eventstream, and more).

| Item | Status in the list |
|---|---|
| Dashboard | Preview |
| Dataflow (Gen1) | Preview |
| Dataflow Gen2 | Listed without preview tag |
| Org app | Preview |
| Paginated report | Preview |
| Report (on supported semantic models) | Preview |
| Semantic model from a PBIX, not a push dataset | Preview |

## Power BI items in Git integration

As listed on 2026-10-07 [S1804].

| Item | Status | Exceptions |
|---|---|---|
| Report | Preview | Not for reports on Azure or SQL Server Analysis Services models, or on models in My workspace |
| Semantic model | Preview | Not for push datasets, live connections to Analysis Services, or model v1 |
| Paginated report | Preview | None noted |
| Metrics set | Preview | None noted |
| Org app | Preview | None noted |

Unsupported items in a connected workspace are ignored, not deleted [S1804].

## Pipeline permission matrix

From [S1823].

| Action | Required |
|---|---|
| View pipeline list | No license (Free user) |
| Create pipeline | Pro, PPU, or Premium license |
| Delete pipeline; add or remove users; manage settings; view history | Pipeline admin |
| Assign workspace to stage | Pipeline admin and workspace admin |
| Deploy to empty stage | Pipeline admin and source workspace contributor |
| Deploy to next stage | Pipeline admin and contributor on both workspaces |
| View or set a rule | Pipeline admin, target workspace contributor or above, and owner of the item |
| Compare stages | Pipeline admin and contributor or above on both |

## Notes

- Pipelines have one permission level: Admin. Microsoft 365 groups cannot be pipeline admins [S1823].
- In the GCC cloud, deployers must be at least Member on both workspaces. Contributor deployment is not supported yet [S1823].
- Dataflow deploys require item ownership. When the tenant owner-only switch is on, semantic model deploys require ownership too [S1823].
- The deploying user becomes owner of cloned models and the only admin of a newly created stage workspace [S1823].
- From 2026-12-01, users without read-write permission on all workspace items cannot deploy to, or assign, a workspace that holds items protected by sensitivity labels with protection policies. Checked 2026-10-09 [S2931].
- Pipelines hold two to 10 stages. The new pipeline user interface and deployment plans are in preview as of 2026-10-09 [S2930].
