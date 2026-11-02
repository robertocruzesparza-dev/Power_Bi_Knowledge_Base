---
id: 14.embed_for_customers
title: Embed for your customers (app owns data)
domain: embedding_apis
type: concept
level: intermediate
tags: [embedding, rest-api, security]
summary: How the app-owns-data embedding model works, who it suits, how it authenticates, and what it requires.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1801, S1812, S1813, S1810, S2926, S2939]
references: []
related: [14.embed_for_organization, 14.embed_tokens, 14.embed_service_principal_capacity]
---
## Purpose

"Embed for your customers" is also called app owns data. A software vendor's web app shows Power BI content to its own users. Those users never sign in to Power BI and need no Power BI license.

## Key facts

- Fact: The app authenticates non-interactively, with a service principal or a master user account [S1801].
- Fact: App users sign in with the app's own method, not Microsoft Entra ID [S1801].
- Fact: App users need no Power BI license [S1801, S1813].
- Fact: R and Python visuals are not supported in this model [S1801].
- Fact: Production use needs a capacity (A, EM, P, or F SKU). Trial tokens are for development only and show a "Free trial version" banner [S1801, S1813].
- Fact: Microsoft recommends a service principal over a master user. A master user is a normal licensed account that the app signs in as.

## How it works

1. The back end holds a credential (service principal secret or certificate).
2. The back end calls the Generate Token API with the items to show and, if needed, a row-level security (RLS) identity [S1810].
3. The back end gives the embed token and the report's embed URL to the browser.
4. The browser uses the [JavaScript client](14_js_client_api.md) to render the report inside a page element.
5. The app renews the token before it expires [S1810].

## Steps

1. Create a Microsoft Entra app and a client secret or certificate.
2. Create a Microsoft Entra security group and add the service principal.
3. In the admin portal, turn on **Embed content in apps** and **Allow service principals to use Power BI APIs** for that group [S1812].
4. Add the service principal to the workspace as Member or Admin [S1812].
5. Put the workspace on a capacity.
6. Generate tokens and embed. See [embed tokens](14_embed_tokens.md).

## Multi-customer isolation

Two approaches exist for serving many customers: workspace-based isolation (one workspace per customer, with service principal profiles) and RLS-based isolation (one shared model, filtered per customer). Microsoft recommends workspace-based isolation with profiles [S1810]. See the [RLS pattern choice](../23_patterns_recipes/23_rls_pattern_choice.md) for a comparison.

## Common mistakes

- Using My workspace. It is not supported with service principals, and tokens cannot be made for it [S1810, S1812].
- Shipping with a trial token and leaving the banner in production.
- Forgetting an RLS identity. A service principal must always provide an identity for any item whose model has RLS [S1810].
- Leaving a client secret in front-end code. Keep secrets on the server and prefer certificates [S1812].

## Limits and version notes

Embedding Direct Lake models needs a V2 embed token, and a service principal needs a fixed-identity cloud connection [S1827]. Service principal profiles are not supported for Direct Lake [S1827].

## See also

- [Embed for your organization](14_embed_for_organization.md)
- [Embed tokens](14_embed_tokens.md)
- [Embedding choice](../23_patterns_recipes/23_embedding_choice.md)
