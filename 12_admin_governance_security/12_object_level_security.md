---
id: 12.object_level_security
title: Object-level security (OLS)
domain: admin_governance_security
type: how-to
level: advanced
tags: [ols, security, semantic-model, tmdl]
summary: How to hide tables and columns from report viewers with object-level security using TMDL view or Tabular Editor, and what it cannot do.
status: ga
volatile: false
last_verified: 2026-10-08
confidence: high
sources: [S1520, S1519, S2712, S2713, S3012, S3013]
references: []
related: [12.rls_static_dynamic]
---
## Purpose

Object-level security (OLS) hides whole tables or columns, including their names and metadata. For a restricted viewer the object behaves as if it does not exist [S1520].

## Key facts

- Fact: OLS lives in model roles, like row-level security (RLS) [S1520].
- Fact: Permission values are `none` (hidden) and `read` (visible) [S1520].
- Fact: OLS applies only to workspace Viewers. Admin, Member and Contributor roles bypass it [S1520].
- Fact: Models with OLS do not support Quick insights, Smart narrative visuals or the Excel Data Types gallery [S1520].
- Fact: Visuals that use a hidden field show a "field cannot be found" error [S1520].
- Fact: Securing a table is blocked at design time if it breaks a relationship chain (A to B to C). Measures that reference a secured object are restricted automatically. Q&A visuals are also unsupported on OLS models [S2712].
- Fact: RLS cannot hide columns; use OLS for that [S1519].

## Steps with TMDL view

1. Open TMDL view and start a new script tab.
2. Write a `createOrReplace` script. The role needs `modelPermission: read`.
3. Hide a table with `tablePermission Customers` and `metadataPermission: none`.
4. Hide one column with `columnPermission Address` inside the table block.
5. Preview, then Apply, then publish.
6. In the service, open Security on the model and add members to the role [S1520].

```
createOrReplace
    role CategoriesOLS
        modelPermission: read
        tablePermission Customers
            columnPermission Address
                metadataPermission: none
```

## Steps with Tabular Editor

1. Create roles in Desktop, then open External tools and Tabular Editor.
2. Expand Roles, pick the role and open Table Permissions.
3. Set the table or column permission to None.
4. Save, return to Desktop, publish, and assign members [S1520].

## Common mistakes

- Mixing RLS and OLS across roles. Official: RLS and OLS cannot be combined from different roles, and a user in such a combination gets an error at query time [S2712].
- Putting a user in several roles that disagree about one column (None in one, Read in another). The official page gives no merge rule for this case (Unknown). Community threads report an error about an unsupported dynamic security configuration; treat as community, not official [S2713]. Keep each user in one role or test with a real viewer. Rechecked 2026-10-09: still no official merge rule for semantic models [S3012]. Do not borrow the OneLake security model, which unions roles and is a separate feature [S3013].
- Hiding a column that a measure needs. Check dependencies first.

## Limits and version notes

More restrictions are listed in the Analysis Services OLS article linked from [S1520]. Pair OLS with RLS when a table has sensitive rows and columns.

## See also

- [Row-level security](12_rls_static_dynamic.md)
