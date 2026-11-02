---
id: 14.embed_service_principal_capacity
title: Embedding setup - service principal and capacity
domain: embedding_apis
type: how-to
level: intermediate
tags: [embedding, capacity, licensing, security]
summary: Steps to authorize a service principal for Power BI embedding, plus which capacity SKUs support each embedding scenario.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1812, S1813, S1801, S2610]
references: []
related: [14.embed_for_customers, 14.embed_for_organization, 14.embed_tokens]
---
## Purpose

Two setups block most first embedding projects: giving the app an identity, and putting content on a capacity. This file covers both.

## Service principal setup

A service principal is the identity of a Microsoft Entra app. It signs in with an application ID plus a secret or a certificate [S1812].

1. Create the Entra app and a secret or certificate. Microsoft recommends certificates for back-end services.
2. Do not add API permissions to the app. They are never used and can cause confusing errors [S1812].
3. Create a Microsoft Entra security group. Add the service principal to it. Skip the group only if you want to enable the whole organization.
4. A Power BI admin opens Tenant settings, Developer settings. Turn on **Embed content in apps** and **Allow service principals to use Power BI APIs**, for the group [S1812].
5. Add the service principal, or the group, to each workspace as Member or Admin [S1812].
6. Optionally script step 5 with the Groups add-user API or the `Add-PowerBIWorkspaceUser` cmdlet with `-PrincipalType App`.

Service principals inherit every tenant setting enabled for them. To limit exposure, enable settings only for specific groups, or exclude the service-principal group from settings it does not need [S1812].

## Capacity and SKUs

Production embedding needs a capacity. A, EM, P, and F SKUs all support embed for customers and embed for your organization [S1813].

| Aspect | A SKU | EM | P | F |
|---|---|---|---|---|
| Offer | Azure | Office | Office | Azure (Fabric) |
| Billing | Hourly | Monthly | Monthly or yearly | Pay as you go per second, or reserved |
| Pause and resume | Yes | No | No | Yes |
| Secure URL embed | No | Yes | Yes | Yes |

Source: [S1813]; F billing from the Premium migration FAQ [S1832].

Size map (Fact, from [S1813]): F8 matches EM1/A1, F16 matches EM2/A2, F32 matches EM3/A3, F64 matches P1/A4, and so on up to F1024 with P5/A8.

Other facts:
- A Pro or PPU account is needed to publish content. A service principal can publish without one via the Post Import In Group API [S1813].
- F SKUs are not supported in the GCC cloud. EM and P are. GCC High and DoD support Azure embedded capacities [S1813].
- Fabric trial capacities are F4 or F64 for the trial period [S1813].
- Viewer licensing: see [embed for your organization](14_embed_for_organization.md).

## Common mistakes

- Treating a service principal as a user. It cannot sign in to the portal [S1812].
- Granting access via a group when the data source is Azure Analysis Services. The principal itself needs the permission; a group does not work [S1812].
- Choosing an A SKU and expecting free viewers in the organization scenario [S1813].

## Limits and version notes

- Dataflow management is not supported with service principals [S1812].
- Not all read-only admin APIs work with a service principal. Enable the separate admin tenant setting [S1812].
- SKU lists and prices change. Confirm on the live page before buying.

## See also

- [Embed for your customers](14_embed_for_customers.md)
- [Embed tokens](14_embed_tokens.md)
- [License choice](../23_patterns_recipes/23_license_choice.md)
