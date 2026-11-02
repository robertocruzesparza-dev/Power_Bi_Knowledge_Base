---
id: 08.endorsement
title: Endorsement: promoted, certified, and master data
domain: service
type: concept
level: intermediate
tags: [governance, service, fabric, semantic-model]
summary: The three endorsement badges, who can apply each, admin setup, and discoverability, as documented for Fabric and Power BI.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S936, S937, S938, S939, S958, S2911, S2912]
references: []
related: [08.lineage_impact_analysis, 08.workspace_roles, 08.org_apps]
---
## Purpose

Endorsement marks trusted content so users find the right items. Endorsed items carry a badge and can rank first in lists and searches.

## Key facts

- Three badges exist: Promoted, Certified, and Master data. Fact.
- Almost all Fabric and Power BI items can be promoted or certified; Power BI dashboards cannot. Fact.
- Master data applies only to items that contain data, such as lakehouses and semantic models. Fact.
- Free-license users cannot add endorsements. Fact.

## Badge comparison

| Badge | Meaning | Who applies |
|---|---|---|
| Promoted | Creators think the item is ready for reuse | Item owner or anyone with write permission |
| Certified | An authorized reviewer confirms it meets organization quality standards | Only members of groups the Fabric admin names |
| Master data | Core, single-source-of-truth data such as customer lists | Only authorized users with write permission on the item |

## Admin setup

- Certification: the admin enables the tenant setting, lists security groups (not individual users) allowed to certify, and may link a certification policy URL. Domain admins can be allowed to override tenant certification settings. Fact.
- Master data: tenant setting "Endorse master data" is labeled preview. The admin chooses the entire organization or specific groups, with exclusions. Fact.
- Discoverability: owners can make promoted or certified semantic models discoverable by users without access, who can then request access. Needs tenant settings. Fact.
- Guidance: delegate certification to domain admins so data owners certify items they have tested. Fact (Microsoft guidance).

## Steps to promote or request certification

1. Open the workspace and the item's settings.
2. Expand the Endorsement section.
3. Choose Promoted and apply. If Certified or Master data is greyed out, you are not authorized.
4. Use the "How do I get content certified" link to find your organization's process. If the link only returns you to the note, contact the Fabric admin.

## Common mistakes

- Certifying items nobody tested. Certification only helps if reviewers hold a standard.
- Trying to endorse a dashboard. Endorse the underlying report or model instead.

## Limits and version notes

The master data setting is preview, so wording and rules can change. Name and email of the certifier show with the badge. Fact.

## See also

- [Lineage and impact analysis](08_lineage_impact_analysis.md)
- [Org apps](08_org_apps.md)
