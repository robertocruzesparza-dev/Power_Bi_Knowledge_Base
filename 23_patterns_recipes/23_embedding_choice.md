---
id: 23.embedding_choice
title: Choosing an embedding approach
domain: patterns_recipes
type: decision
level: intermediate
tags: [embedding, decision-guide, licensing, capacity]
summary: A decision guide for picking secure embed, embed for your organization, or embed for your customers, with licensing consequences.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1801, S1813, S1810, S1812, S2926]
references: []
related: [14.embed_for_customers, 14.embed_for_organization, 23.license_choice, 23.rls_pattern_choice]
---
## Purpose

Power BI offers three ways to show reports outside the portal. They differ in who signs in, who pays for licenses, and how much code you write.

## Key facts

- Fact: Secure embed is the no-code option. It uses a URL or iframe for any portal. Viewers need a proper Power BI license and cannot edit or save [S1801].
- Fact: Embed for your organization needs viewers to sign in with Entra ID [S1801].
- Fact: Embed for your customers lets your app authenticate for everyone. Viewers need no Power BI license [S1801].
- Fact: Production use of either developer solution needs a capacity [S1801, S1813].

## Decision flow

1. Do you only need a report inside an existing portal page, and are all viewers licensed Power BI users? Use secure embed [S1801].
2. Are all viewers employees with Entra accounts? Use embed for your organization. Check the license rule for your capacity size.
3. Are viewers customers or partners without Power BI licenses? Use embed for your customers.
4. Do you need R or Python visuals? Embed for your organization [S1801].
5. Embedding in Teams, SharePoint Online, or PowerPoint? These Microsoft 365 apps follow the organization rule [S1813].

## Comparison

| Aspect | Secure embed | For your organization | For your customers |
|---|---|---|---|
| Code needed | None | Yes | Yes |
| Viewer sign-in | Power BI | Entra ID | Your app |
| Viewer license | Required | Required below F64/P | None |
| Service principal | Not applicable | No | Yes |
| Editing in page | No | Possible | Possible with token option |
| A SKU | Not supported | Yes | Yes |

Source: [S1801, S1812, S1813]. "Editing" row: Inference from the allowEdit token option [S1810].

License detail [S1813]: free viewers work only on P capacities or F64 and larger. On smaller F SKUs or any A SKU, each viewer needs Pro or Premium Per User (PPU), for the organization scenario.

Cost note: an A SKU is billed hourly and can be paused. F SKUs offer pay as you go. See [license choice](23_license_choice.md) for the viewer-license break-even idea.

## Common mistakes

- Choosing "for your organization" for an external audience. Guests then need licenses.
- Choosing "for your customers" and skipping RLS planning. See [RLS pattern choice](23_rls_pattern_choice.md).
- Expecting trial tokens in production.
- Selecting an A SKU for secure embed. It is not supported [S1813].

## Limits and version notes

SKU names and the retirement of P SKUs for new purchases change the options; recheck [S1813] and [S1832].

## See also

- [Embed for your customers](../14_embedding_apis/14_embed_for_customers.md)
- [Embed for your organization](../14_embedding_apis/14_embed_for_organization.md)
- [Embed tokens](../14_embedding_apis/14_embed_tokens.md)
