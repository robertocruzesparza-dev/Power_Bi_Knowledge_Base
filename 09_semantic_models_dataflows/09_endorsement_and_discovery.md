---
id: 09.endorsement_and_discovery
title: Endorsement and semantic model discovery
domain: semantic_models_dataflows
type: concept
level: beginner
tags: [governance, semantic-model, service, workspace]
summary: Promoted, Certified, and Master data badges, who can apply them, which items qualify, and how users find endorsed models.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1210, S1211, S1213, S1219]
references: []
related: [09.semantic_model_basics]
---
## Purpose

Endorsement marks trusted content so people can find it. It labels items; it does not change data or security.

## Key facts

| Badge | Meaning | Who can apply |
|---|---|---|
| Promoted | Creators think the item is ready to share and reuse. | Anyone with write permission on the item |
| Certified | An authorized reviewer says it meets organization quality standards. | Only reviewers named by a Fabric admin |
| Master data | Core, single-source-of-truth data such as customer lists. | Only reviewers named by a Fabric admin; data items only |

- Fact: Any Fabric or Power BI item except Power BI dashboards can be promoted or certified. [S1210]
- Fact: Master data applies only to items that hold data, such as lakehouses and semantic models. [S1210]
- Fact: Certification must be enabled and configured by an admin. Others can request it. [S1211]
- Fact: Endorsed items get badges, search priority, and sort options, including in Excel. [S1210]

## Steps

Promote a semantic model:

1. Open the item's settings (More options, then Settings).
2. Expand Endorsement and choose Promoted.
3. Add a clear description. It shows in tooltips and the details page.
4. Select Apply. [S1211]

If you see Make discoverable, users without access can find the model and request access. That needs the discoverability tenant setting. [S1211]

## Finding endorsed models

- Power BI service: open the OneLake catalog and filter Endorsed in your org.
- Power BI Desktop: Get data, then Power BI semantic models.
- A Certified tooltip shows who certified the model. [S1213]

Creating a report from a found model makes a live connection. The model stays in its home workspace, and RLS still applies. [S1213]

## Common mistakes

- Certifying content without review. Certification is a responsibility, per the docs. [S1211]
- Leaving the description empty. Users then cannot judge fit.
- Endorsing the report but not the model behind it. Endorse both when both are ready.

## Limits and version notes

Dataflow Gen1 can be endorsed. Dataflow Gen2 Save As does not copy endorsements. [S1219]

## See also

- [Semantic model basics](09_semantic_model_basics.md)
