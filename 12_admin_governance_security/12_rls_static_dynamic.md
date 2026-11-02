---
id: 12.rls_static_dynamic
title: Row-level security (static and dynamic)
domain: admin_governance_security
type: how-to
level: intermediate
tags: [rls, security, semantic-model]
summary: How to define, assign and test static and dynamic row-level security roles in Power BI, with limits and B2B pitfalls.
status: ga
volatile: false
last_verified: 2026-10-08
confidence: high
sources: [S1519, S2730]
references: []
related: [12.object_level_security, 12.external_sharing_b2b, 12.service_principals]
---
## Purpose

Row-level security (RLS) hides rows from some users of a semantic model. Roles hold DAX filters. A row is visible only if the filter returns TRUE.

## Key facts

- Fact: RLS applies only to the workspace Viewer role. Admin, Member and Contributor can edit the model, so RLS does not apply to them [S1519].
- Fact: Viewers with Build permission are still restricted, including in Analyze in Excel [S1519].
- Fact: A user in several roles sees the union of the roles [S1519].
- Fact: Service principals cannot be added to RLS roles. RLS is not applied when a service principal is the final effective identity [S1519].
- Fact: Microsoft 365 groups cannot be role members. Use Entra security, mail-enabled or distribution groups [S1519].
- Fact: Test as role does not work for DirectQuery models with single sign-on, paginated reports, or embedded service-principal flows. It uses your own identity, so validate guests with a real guest account [S2730].
- Fact: RLS works on Import, DirectQuery and Direct Lake models. Live connections to Analysis Services use the on-premises model's security [S1519].

## How it works

Static RLS fixes a value in the filter. Dynamic RLS compares a column with the signed-in user.

| Kind | Example filter | Use |
|---|---|---|
| Static | `[Region] = "West"` | One role per audience |
| Dynamic, UPN | `[UserEmail] = USERPRINCIPALNAME()` | One role, mapping table |
| Dynamic, name | `[UserDomain] = USERNAME()` | Domain accounts |
| Dynamic, embedded | `[AppRole] = CUSTOMDATA()` | App passes a string |

Source: S1519. In Desktop, `USERNAME()` returns DOMAIN\user. In the service it returns the user principal name (UPN) [S1519].

## Steps

1. In Power BI Desktop, open Modeling, then Manage roles.
2. Create a role. Role names cannot contain commas.
3. Pick a table and write the filter in the default or DAX editor. Use commas as argument separators in every locale.
4. Save and publish.
5. In the service, open the model's More options, then Security. Add members to each role.
6. Choose Test as role to check results [S1519].

## Worked example

A Sales table has Region, Product and Amount. The role "West" has filter `[Region] = "West"`. Of five rows, a West member sees two. Tables not covered by the filter still show all rows unless relationships carry the filter.

## Common mistakes

- Testing as an Admin. Admins see everything.
- Expecting RLS to hide columns. Use object-level security instead [S1519].
- Using `USERELATIONSHIP()` in measures with RLS. It may cause errors [S1519].
- Forgetting a bi-directional relationship needs "Apply security filter in both directions" for dynamic patterns. It can slow queries [S1519].
- Embedded apps using a service principal. `USERPRINCIPALNAME()` then returns the app ID or empty. Pass `EffectiveIdentity` in the embed token [S1519].

## Limits and version notes

- Roles created in the service before Desktop must be recreated in Desktop [S1519].
- Test as role does not work for DirectQuery with single sign-on, for paginated reports, or for Q&A, Quick insights and Copilot [S1519].
- Test as role uses your own identity, so it cannot simulate a B2B guest [S1519].
- B2B guests: `USERPRINCIPALNAME()` may return an email or a `#EXT#` form. Verify with a card visual and a real guest before launch [S1519]. See [External sharing and B2B](12_external_sharing_b2b.md).
- Users not in any role see no data, because RLS is enforced with no matching role [S1519].

## See also

- [Object-level security](12_object_level_security.md)
- [Service principals](12_service_principals.md)
