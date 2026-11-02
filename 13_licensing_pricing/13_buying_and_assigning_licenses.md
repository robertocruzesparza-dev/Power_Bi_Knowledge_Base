---
id: 13.buying_and_assigning_licenses
title: Buying and assigning licenses
domain: licensing_pricing
type: how-to
level: beginner
tags: [licensing, admin, how-to]
summary: Steps for admins to buy Pro or PPU, assign licenses, control self-service sign-up and purchase, and understand expiry grace periods.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1503, S1510, S2727]
references: []
related: [13.license_types_overview, 13.pricing_reference, 12.tenant_settings]
---
## Purpose

This page shows how an administrator obtains and manages per-user licenses. Capacity purchase is in [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md).

## Key facts

- Fact: To buy or assign licenses you need the Billing admin role. License and User admins can manage licenses after purchase [S1510].
- Fact: Pro and PPU can be bought self-service or in the Microsoft 365 admin center, by credit card or invoice through a reseller [S1503, S1510].
- Fact: Each Microsoft 365 E5 license includes one Power BI Pro license [S1510].
- Fact: Before you give Pro or PPU to guest users, check your agreement terms with your Microsoft account team [S1510].

## Steps: buy in Microsoft 365 admin center

1. Sign in as an admin at the Microsoft 365 admin center.
2. Select Home, then Subscriptions, then Add more products.
3. Search for Power BI and pick Pro or Premium Per User.
4. Choose quantity and monthly or yearly billing, then Buy.
5. Check Billing, then Your products [S1510].

## Steps: assign

1. In Billing, select Licenses, then the Power BI product.
2. Assign to users or groups. In Microsoft Entra ID you can use Licenses, All products, then Assign [S1510].
3. View a user's licenses under Users, then Active users.

## Self-service controls

Self-service sign-up lets users get a license on first sign-in. Self-service purchase lets them buy one. Turning off purchase blocks sharing, exporting and creating workspaces for collaboration [S1510].

Disable self-service when procurement, training or enterprise pricing must be enforced. Keep it when decentralized groups need to try Power BI [S1510]. A Cloud Solution Provider may control these settings for you [S1510].

The tenant setting that governs trials is Users can try Microsoft Fabric paid features. See [Tenant settings](../12_admin_governance_security/12_tenant_settings.md).

## Expiry and grace periods

| Purchase type | Grace period |
|---|---|
| Volume license | 90 days |
| Direct purchase | 30 days |
| Trial | none |

Source: S1510, rechecked [S2727]. A free 30-day Pro trial includes up to 25 licenses and bills when it ends [S1510].

## Common mistakes

- Letting Free users self-upgrade without budget approval.
- Forgetting that CSP-bought tenants may have self-service blocked [S1510].

## Limits and version notes

Self-service purchase is for commercial cloud customers only [S1510]. Prices are in [Pricing reference](13_pricing_reference.md).

## See also

- [Who needs which license](13_who_needs_which_license.md)
