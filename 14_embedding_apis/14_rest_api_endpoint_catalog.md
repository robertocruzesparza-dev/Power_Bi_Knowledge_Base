---
id: 14.rest_api_endpoint_catalog
title: Power BI REST API operation groups
domain: embedding_apis
type: reference
level: intermediate
tags: [rest-api, catalog, reference]
summary: Catalog of the Power BI REST API operation groups with typical uses and notes on which groups matter for embedding and DevOps.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S1811, S1809, S1825, S1843, S1813, S2614]
references: []
related: [14.rest_api_overview, 14.embed_tokens, 15.deployment_pipelines]
---
## Purpose

This file lists the operation groups in the official Power BI REST reference. It is a map, not a copy of every endpoint. Open the live reference for parameters.

## Operation groups

The list of groups comes from the official reference page [S1811].

| Group | What it covers |
|---|---|
| Admin | Tenant-wide reads and actions: workspaces, activity events, scanner metadata |
| Apps | List and read Power BI apps |
| Available Features | Which features the caller can use |
| Capacities | Capacity details and workspace assignment |
| Dashboards | Dashboards and tiles |
| Dataflow Storage Accounts | Bring-your-own storage for dataflows |
| Dataflows | Dataflow definitions, refresh, transactions |
| Datasets | Semantic model refresh, parameters, data sources, execute queries |
| Embed Token | Generate tokens for embedding |
| Gateways | Gateway clusters and data sources |
| Groups | Workspaces and workspace users |
| Imports | Publish a PBIX or other file into a workspace |
| Pipelines | Deployment pipelines: create, assign, deploy |
| Push Datasets | Row-push semantic models |
| Reports | Reports, clone, rebind, export |
| Template Apps | Template app install tickets |
| Users | User-level information |

The reference calls "datasets" what the product now calls semantic models. Endpoint names keep the older word.

## Operations worth knowing

- Generate Token (Embed Token group): one call for several reports and semantic models. It is only for app-owns-data scenarios [S1809]. See [embed tokens](14_embed_tokens.md).
- Deploy All and Selective Deploy (Pipelines): promote content between stages. Options include backward deployment and app update [S1825]. See [deployment pipelines](../15_devops_lifecycle/15_deployment_pipelines.md).
- Post Import In Group (Imports): publishes a file, and works with a service principal for publishing without a Pro license [S1813].
- Groups Add Group User: adds a service principal or group to a workspace.
- Execute Queries (Datasets): runs DAX against a semantic model. Check current limits on the live page: unverified here.

## Limits and version notes

- Fact: The primary Learn page on real-time streaming (checked 2026-10-08) says creation of push, streaming, PubNub streaming semantic models and streaming tiles stays enabled until 2027-10-31. After that date new ones cannot be created, and existing ones are unaffected [S2614].
- Conflict: an older tutorial note (S1843) says creation stopped on 2024-10-31 and existing models retire on 2027-10-31, subject to change. The primary page is newer and more specific, so treat it as correct. Unresolved: the retirement blog post was not readable.
- Fact: Azure Stream Analytics jobs with a Power BI output cannot be created from 2027-10-31, and existing jobs with that output are stopped [S2614].
- Fact: push semantic models allow 1 request of up to 16 MB and 1 million rows per hour. Streaming models allow 5 requests of 15 KB. Microsoft recommends Real-Time Intelligence in Fabric [S2614].
- The Workspace Collections API is deprecated and replaced by Power BI Embedded.
- Throttling returns 429. See [REST API overview](14_rest_api_overview.md).

## See also

- [REST API overview](14_rest_api_overview.md)
- [Embed tokens](14_embed_tokens.md)
- [PowerShell and CLI tooling](14_powershell_cli_tooling.md)
