---
id: 08.license_requirements
title: License requirements for service tasks
domain: service
type: reference
level: beginner
tags: [licensing, service, limits, comparison]
summary: Which Free, Pro, and PPU licenses and capacity types are needed to view, share, publish, subscribe, and refresh in the Power BI service.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S957, S958, S961, S959, S921, S924, S2610]
references: []
related: [08.workspace_roles, 08.workspace_apps, 08.scheduled_refresh, 08.distribution_decision_guide]
---
## Purpose

The license a person holds, plus the type of capacity that hosts a workspace, decide what that person can do. Prices and SKU details live in the licensing domain, not here.

## Key facts

- Per-user licenses are Free (Fabric free), Pro, and Premium per user (PPU). The service gives you the experience of your best license. Fact.
- A free user can create personal content in My workspace and cannot share it or publish to other workspaces. Fact.
- In a workspace on Premium capacity or Fabric F64 or larger, free users can view content shared with them. Smaller F SKUs need a paid license for viewers. Fact.
- PPU content is visible only to other PPU users unless it sits on a capacity workspace. Fact.
- A user can hold more than one license. Fact.

## Task matrix

| Task | Free | Pro | PPU | Notes |
|---|---|---|---|---|
| Author in My workspace | Yes | Yes | Yes | |
| View shared content on F64+ or Premium capacity | Yes | Yes | Yes | Viewer role or app access |
| View shared content on shared capacity | No | Yes | Yes | Both sides need Pro |
| Publish to another workspace | No | Yes | Yes | Error "Only users with Power BI Pro licenses can publish" if missing |
| Create or update an app | No | Yes | Yes | |
| Share items | No | Yes | Yes | |
| Create dashboards in a workspace | No | Yes | Yes | |
| Subscribe others | No | Yes | Yes | Plus Contributor or higher |
| Author scorecards | My workspace only | Yes | Yes | |
| Promote or certify | No | Yes | Yes | |
| Lineage view | No | Yes | Yes | Plus Admin, Member, Contributor |

Pro and PPU rows are marked from the Microsoft pages cited; a few cells are inference where the page says only "paid license".

## Pro, PPU, and capacity compared

| Consideration | Pro workspace | PPU workspace | Fabric capacity workspace |
|---|---|---|---|
| Maximum semantic model size | 1 GB | 100 GB | Varies by SKU |
| Scheduled refreshes per day | 8 | 48 | 48 |
| XMLA read-write | No | Yes | Yes |
| Deployment pipelines | No | Yes | Yes |
| Dedicated compute | No | No | Yes |
| View without a paid per-user license | No | No | Yes, on F64 or larger |

The Microsoft planning guide states these values. Capacity features vary by SKU and need tenant or capacity settings. Fact.

## Common mistakes

- Assuming an F32 capacity lets free users view reports. Only F64 or larger qualifies.
- Adding a free user as Contributor and expecting edit rights. Higher roles still need Pro or PPU.
- Sharing PPU workspace content with Pro users.

## Limits and version notes

- The Premium P-SKU capacity subscriptions are being consolidated into Fabric F SKUs per Microsoft notes. Details of that change belong to the licensing domain.
- US Government cloud does not offer a Free license. Fact.

## See also

- [Workspace roles](08_workspace_roles.md)
- [Distribution decision guide](08_distribution_decision_guide.md)
