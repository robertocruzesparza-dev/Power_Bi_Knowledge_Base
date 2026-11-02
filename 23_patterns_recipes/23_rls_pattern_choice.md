---
id: 23.rls_pattern_choice
title: Choosing a row-level security pattern
domain: patterns_recipes
type: decision
level: intermediate
tags: [rls, security, decision-guide, embedding]
summary: When to use static roles, dynamic roles, custom data, or workspace isolation for row-level security, including embedding cases.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S1836, S1837, S1810, S1827, S1808]
references: []
related: [14.embed_tokens, 23.embedding_choice, 23.workspace_design]
---
## Purpose

Row-level security (RLS) hides rows from some users. The pattern you choose decides how many roles you maintain and whether embedded apps can pass identity.

## Key facts

- Fact: A role is a set of DAX filter rules. Users are assigned to roles in the Power BI service, not in Desktop [S1836].
- Fact: RLS applies to workspace Viewers. Admin, Member, and Contributor can edit the model, so RLS does not apply to them [S1836].
- Fact: Static rules use constants such as `[Region] = "West"`. Dynamic rules use `USERPRINCIPALNAME()`, `USERNAME()`, or `CUSTOMDATA()` with a mapping table [S1836].
- Fact: Microsoft calls dynamic RLS the most common approach, because one role serves everyone [S1836].
- Fact: Service principals cannot be added as role members through XMLA [S1808].
- Fact: Roles that have no rules give access to all rows, useful for admins [S1836].

## Pattern table

| Pattern | Use when | Cost |
|---|---|---|
| Static roles | Few groups, rules rarely change | Many roles as groups grow |
| Dynamic with `USERPRINCIPALNAME()` | Each user signs in to Power BI | A mapping table to maintain |
| Dynamic with `CUSTOMDATA()` | Embedded app owns identity | App must pass a string; mainly embedded use [S1836] |
| Embedded `username()` as the key | App owns data, one role for all | Username is any string the app chooses [S1837] |
| Workspace isolation per customer | Strong tenant separation, many customers | Many workspaces; Microsoft's recommended default for multi-tenancy [S1810] |

## Decision flow

1. Internal users who sign in to Power BI: dynamic RLS with `USERPRINCIPALNAME()` and a mapping table. Assign Entra security groups to the role [S1836].
2. External customers in an embedded app: choose workspace isolation if you can manage many workspaces. Otherwise use RLS with an effective identity in the embed token [S1810].
3. Static roles only when the set of audiences is small and stable. For static embedding, the token carries the role; the username can be any string [S1837].
4. Direct Lake models: use semantic-model RLS with a fixed-identity cloud connection. SQL-endpoint RLS is not applied by Direct Lake on OneLake [S1827].

## Testing

- **Test as role** in the service uses your own identity. For dynamic RLS it shows your UPN, not the simulated user's [S1836].
- Validate B2B guests by signing in as the guest. The format returned by `USERPRINCIPALNAME()` may differ from the email [S1836].
- With a service principal, `USERPRINCIPALNAME()` returns the application ID or an empty string, not an end user [S1836].

## Common mistakes

- Storing emails in the mapping table when the UPN differs.
- Leaving report authors as Contributor and wondering why RLS does not filter.
- Forgetting that a service principal must supply an identity for RLS items [S1810].
- Using master-user shortcuts that skip the identity and expose everything [S1810].

## Limits

Role names in embed tokens: up to 50 roles per identity, 50 characters each [S1809]. DirectQuery with SSO does not support Test as role [S1836].

## See also

- [Embed tokens](../14_embedding_apis/14_embed_tokens.md)
- [Embedding choice](23_embedding_choice.md)
- [Workspace design](23_workspace_design.md)
