---
id: 12.external_sharing_b2b
title: External sharing and Entra B2B guests
domain: admin_governance_security
type: how-to
level: intermediate
tags: [security, governance, licensing, tenant-setting]
summary: How to share Power BI content with external guests through Microsoft Entra B2B, the tenant settings, license rules, limits and RLS pitfalls.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1510, S1519, S1525, S1530, S1549, S3002, S3007]
references: []
related: [12.rls_static_dynamic, 12.tenant_settings, 13.who_needs_which_license]
---
## Purpose

Microsoft Entra business-to-business (B2B) lets you invite outside people as guests. They sign in with their own identity and see only what you share.

## Key facts

- Fact: Inviting guests needs the "Invite external users to your organization" tenant setting and the Entra Guest Inviter role. A Pro trial user cannot invite guests [S1530].
- Fact: Most email addresses work, including personal ones like gmail.com. These social identities have more limits [S1530].
- Fact: To block guests entirely, use a Microsoft Entra Conditional Access policy. Turning off the invite setting does not remove existing guests [S1530].
- Fact: Another option is in-place semantic model sharing. Guests use the model from their own tenant. It needs the setting Guest users can work with shared semantic models in their own tenants [S1549].
- Fact: Guests on a different cloud cannot bring their own license, and cross-cloud sharing with security groups does not work [S1530].

## Settings

Under Export and sharing [S1525]:

- Guest users can access Microsoft Fabric
- Users can invite guest users to collaborate through item sharing and permissions
- Guest users can browse and access Fabric content
- Users can see guest users in lists of suggested people
- B2B guest users can set up and be subscribed to email subscriptions
- Users can send email subscriptions to external users
- External data sharing; Users can accept external data shares

## License rules

- The sharer needs Pro or PPU [S1510].
- The guest needs Pro or PPU (their own or yours), or a Free license when content is on F64 or larger [S1510, S3007].
- Consumers with Pro can see Pro and capacity workspaces but not PPU workspaces. PPU consumers can see all three. Free consumers see only capacity-workspace content shared by licensed providers [S1530].
- Check your agreement terms before assigning paid licenses to guests [S1510].

## Steps

1. Enable the invite setting for a security group.
2. Decide the license route: capacity workspace, assigned license or guest's own license.
3. Invite the guest, or let sharing invite them.
4. Give the guest the Tenant URL (Help, About Power BI) so they can sign in to your tenant [S1530].
5. Share to a security group to avoid per-user email invitations.
6. Test with a real guest account.

## Common mistakes

- Using an Entra security group with guests for RLS. Add guests directly by email instead, or use dynamic RLS [S1519].
- Assuming `USERPRINCIPALNAME()` matches the email. Guests may appear as `#EXT#` or `Live#...` forms. Verify [S1519, S1530].
- Applying Purview Information Protection to external member accounts. Not supported [S1530].
- Expecting guests to use Desktop publishing, gateways, Analyze in Excel or org-wide apps [S1530].

## Limits and version notes

Social-identity guests cannot use the Power BI mobile apps and are limited to browser consumption [S1530]. Details of the "From external orgs" home tab and tenant switcher (up to 50 tenants listed) are in S1530 and S3002. Rechecked 2026-10-09: no rule changed. If you disable "Guest users can browse and access Fabric content", guests keep roles and permissions already granted [S3002].

## See also

- [Row-level security](12_rls_static_dynamic.md)
- [Who needs which license](../13_licensing_pricing/13_who_needs_which_license.md)
