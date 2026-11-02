---
id: 14.embed_for_organization
title: Embed for your organization (user owns data)
domain: embedding_apis
type: concept
level: intermediate
tags: [embedding, service, licensing]
summary: How the user-owns-data embedding model works, who it suits, license rules for viewers, and where it differs from app-owns-data.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1801, S1812, S1813, S2926]
references: []
related: [14.embed_for_customers, 14.embed_service_principal_capacity, 14.js_client_api]
---
## Purpose

"Embed for your organization" is also called user owns data. An internal app asks each employee to sign in with Microsoft Entra ID. The app then shows only the content that person can already open in the Power BI service.

## Key facts

- Fact: Users authenticate interactively against Microsoft Entra ID [S1801].
- Fact: Each app user needs a Power BI license, except when content sits on a P capacity or an F64 or larger capacity, where Free-license viewers can consume apps and shared content [S1813].
- Fact: On an A SKU, or an F SKU smaller than F64, each viewer needs Pro or Premium Per User (PPU) [S1813].
- Fact: Service principals cannot be used in this model [S1812].
- Fact: R and Python visuals are supported, subject to regional restrictions [S1801].
- Fact: Embedding in Microsoft Teams, SharePoint Online, and PowerPoint follows the same viewer license rule [S1813].

## Comparison

| Topic | For your organization | For your customers |
|---|---|---|
| Also called | User owns data | App owns data |
| Audience | Internal users | External users |
| App sign-in | Entra ID | Your own method |
| Viewer license | Required below F64/P | Not required |
| Identity used to call | The signed-in user | Service principal or master user |
| R and Python visuals | Supported | Not supported |

Source: [S1801, S1813].

## How it works

1. The app uses the Microsoft Authentication Library (MSAL) to sign the user in and get an Entra access token.
2. The app passes that access token, type Aad, to the [JavaScript client](14_js_client_api.md) with the report ID and embed URL.
3. Power BI applies the user's own permissions and any RLS roles assigned to that user.
4. No embed token is generated. [Embed tokens](14_embed_tokens.md) are only for app-owns-data.

## Common mistakes

- Trying a service principal here. It will not work [S1812].
- Assuming an A SKU lets free users view. It does not; Pro or PPU is still required [S1813].
- Forgetting that content creators who publish to a workspace need Pro or PPU [S1813].

## Limits and version notes

Capacity sizes and license rules change with Microsoft's Premium-to-Fabric consolidation. Per-capacity Premium P SKUs are being retired for new purchases in favor of F SKUs [S1832]. Check [S1813] before purchase decisions.

## See also

- [Embed for your customers](14_embed_for_customers.md)
- [Capacity and service principal setup](14_embed_service_principal_capacity.md)
- [License choice](../23_patterns_recipes/23_license_choice.md)
