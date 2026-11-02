---
id: 23.recipe_embed_report_with_rls
title: Recipe - embed a report for external customers with RLS
domain: patterns_recipes
type: how-to
level: advanced
tags: [embedding, rls, rest-api, how-to]
summary: Steps to embed a report for external customers with a service principal and a row-level security identity in the embed token.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1809, S1810, S1812, S1813, S1837, S2939]
references: []
related: [14.embed_for_customers, 14.embed_tokens, 23.rls_pattern_choice]
---
## Goal

Show each customer only its rows, with no Power BI license for the customer.

## Before you start

- A workspace on a capacity, containing the report and semantic model [S1813].
- A service principal set up as in [embedding setup](../14_embedding_apis/14_embed_service_principal_capacity.md) [S1812].
- A dynamic RLS role in the model, for example `CustomerDynamic` with the rule `[CustomerCode] = USERNAME()` (Pattern from [S1837]).

## Steps

1. Publish the model with the role. Do not add users to the role: embedding passes identity in the token [S1837].
2. In your back end, authenticate as the service principal and call Generate Token.
3. Include the report, the dataset, and an identity with the customer code as the username, the role, and the dataset ID [S1809, S1837].
4. Return the token, token ID, and embed URL to the browser. Never send the secret.
5. Embed with the [JavaScript client](../14_embedding_apis/14_js_client_api.md) using token type Embed.
6. Renew the token before it expires [S1810].
7. Log the `tokenId` for audit correlation [S1809].

## Worked token request

```json
{
  "reports": [{ "id": "<report-id>" }],
  "datasets": [{ "id": "<dataset-id>" }],
  "identities": [{
    "username": "ACME",
    "roles": ["CustomerDynamic"],
    "datasets": ["<dataset-id>"]
  }],
  "lifetimeInMinutes": 30
}
```

`ACME` is the customer code the rule compares with. With dynamic roles the username acts as the filter value [S1837].

## Checks

- Request a token for `ACME`, then for `GLOBEX`. Confirm totals differ.
- Request one without an identity as the service principal. It should fail, since a service principal must pass an identity for RLS items [S1810].

## Common mistakes

- Putting the filter in a static role and passing a different username. Static roles ignore the username [S1837].
- Building one token for several customers.
- Using a master user shortcut in production.

## See also

- [Embed tokens](../14_embedding_apis/14_embed_tokens.md)
- [RLS pattern choice](23_rls_pattern_choice.md)
- [Embedding choice](23_embedding_choice.md)
