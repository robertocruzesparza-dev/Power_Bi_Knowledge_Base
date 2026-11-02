---
id: 12.service_principals
title: Service principals in Power BI and Fabric
domain: admin_governance_security
type: how-to
level: advanced
tags: [security, admin, rest-api, embedding]
summary: How to enable service principals for APIs, admin APIs and embedding, with the tenant settings, group scoping, limits and common 401 causes.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1519, S1525, S1528, S1529, S1546, S1548, S3000, S3003, S3004, S3005]
references: []
related: [12.tenant_settings, 12.audit_activity_logs, 12.rls_static_dynamic]
---
## Purpose

A service principal is an app identity in Microsoft Entra ID. Automation and embedded apps use it instead of a person's login.

## Key facts

- Fact: Several separate tenant settings control service principals. Enabling one does not enable another [S1546].
- Fact: Each setting takes security groups. Put the service principal in a group, then add that group to the setting [S1528].
- Fact: Service principals can call Fabric public APIs that have a Fabric permission model. This setting is enabled by default for new customers [S1528].
- Fact: Service principals can create workspaces, connections and deployment pipelines is a separate setting, disabled by default for new customers [S1528].
- Fact: Read-only admin API access shows user names, emails and model metadata for the whole tenant. Control it tightly [S1528].
- Fact: The two detailed-metadata settings apply to service principals only when the read-only admin APIs setting is also enabled. Both admin API settings are also required for Microsoft Purview Data Security Posture Management (DSPM) for AI data risk assessments of Fabric [S3003].
- Fact: A service principal cannot sign in to the Power BI portal [S1529]. It cannot be put in an RLS role [S1519].

## Settings to know

| Setting | Section |
|---|---|
| Service principals can call Fabric public APIs | Developer |
| Service principals can create workspaces, connections, and deployment pipelines | Developer |
| Allow service principals to create and use profiles | Developer |
| Embed content in apps | Developer |
| Service principals can access read-only admin APIs | Admin API |
| Service principals can access admin APIs used for updates | Admin API |
| Enhance admin API responses with detailed metadata / DAX and mashup expressions | Admin API |

Source: S1525, S1528, S3000, S3003.

Older pages still call the Fabric public APIs setting "Allow service principals to use Power BI APIs" (user APIs) [S3004, S3005]. Treat both names as the same setting.

## Steps: set up for admin API reading

1. Register an app in Entra ID. Do not grant Azure API permissions for this purpose [S1548].
2. Create a security group such as "Power BI admin service principals". Add the service principal.
3. In tenant settings, add the group to the read-only admin APIs setting.
4. Optionally add it to the detailed metadata settings.
5. Test with a simple admin call and set a secret-rotation process.

## Steps: workspace automation

1. Enable Service principals can call Fabric public APIs for a group.
2. Add the service principal as Member or Admin on the workspace.

## Embedding notes

- My workspace is not supported with service principals. A capacity is required for production [S1529].
- "Embed for your organization" apps cannot use a service principal; dataflow management is not supported [S1529].
- Profiles give per-customer isolation in multitenant apps. They exist only in Power BI, not in Entra ID [S1528].
- Per-user RLS needs `EffectiveIdentity` in the embed token [S1519].

## Common mistakes

- 401 on admin APIs: only the user API setting is on, or the principal is not in the setting's group [S1546].
- 401 persists: check the token audience is the Power BI resource (`https://analysis.windows.net/powerbi/api` in the global cloud), the app has no admin-consent application permissions, and Activity Events dates are ISO 8601 UTC [S3005].
- Granting the broad group "entire organization". Service principals inherit every setting they are allowed for [S1529].
- A service principal with Azure Analysis Services needs direct instance permission; a group containing it does not work [S1529].

## Limits and version notes

Defaults differ for new versus old tenants. Check the live tenant settings.

## See also

- [Tenant settings](12_tenant_settings.md)
- [Audit and activity logs](12_audit_activity_logs.md)
