---
id: 13.pricing_reference
title: Power BI and Fabric pricing reference
domain: licensing_pricing
type: reference
level: beginner
tags: [pricing, licensing, capacity]
summary: Retail prices for Pro, PPU, Fabric F SKUs and Embedded A SKUs as looked up on 2026-10-07, with region and currency caveats.
status: ga
volatile: true
last_verified: 2026-11-02
confidence: moderate
sources: [S1503, S1504, S1505, S1506, S1516, S1517, S2700, S2701, S2705, S2728, S2729, S3009, S3010, S3011, S3020]
references: []
related: [13.fabric_capacity_f_skus, 13.embedded_skus, 13.who_needs_which_license]
---
## Purpose

This page records list prices seen on 2026-10-07. Prices change. Always confirm on the official page before you budget.

## Key facts

- Fact: Pro costs 14.00 USD per user per month, billed yearly. PPU costs 24.00 USD per user per month, billed yearly. Source is the en-US pricing page [S1503], rechecked on microsoft.com on 2026-10-08 [S2701].
- Fact: These Pro and PPU prices took effect on 2025-04-01 after an announcement on 2024-11-12. Existing customers kept old prices until renewal. Education, nonprofit and government cloud prices were stated as unaffected [S1517].
- Fact: The Azure Fabric pricing page rendered blank price cells to our fetch. We used the Azure Retail Prices API instead [S1504, S1505].
- Fact: The Pro-to-PPU step-up add-on is listed at 14.00 USD per user per month, yearly [S1503].
- Fact (rechecked 2026-11-02): the Microsoft Power BI pricing page still shows Pro at 14.00 and PPU at 24.00 USD per user per month, paid yearly, the 14.00 step-up add-on, 8 and 48 refreshes per day, 1 GB and 100 GB model memory, and a 40.5 percent saving for a yearly Fabric reservation [S3020]. The Azure Retail Prices API figures below were not re-queried on 2026-11-02 (Unverified).

## Per-user prices

| Plan | Price (USD, en-US page) | Billing | Model memory | Refreshes per day |
|---|---|---|---|---|
| Free | 0 | none | not listed | not listed |
| Pro | 14.00 per user per month | yearly | 1 GB | 8 |
| PPU | 24.00 per user per month | yearly | 100 GB | 48 |

Source: S1503. Pro storage is 10 GB per license; the tenant storage cap is 100 TB [S1503].

## Fabric F SKU prices

Pay-as-you-go rate in West US 2, USD, from the retail API: 0.18 USD per CU per hour [S1505]. Hourly figures below multiply that rate by CUs. Monthly figures assume 730 hours. Both are our arithmetic (Inference).

| SKU | CUs | PAYG per hour | PAYG per month (730 h) | 1-year reservation per year |
|---|---|---|---|---|
| F2 | 2 | 0.36 | 262.80 | 1,876 |
| F4 | 4 | 0.72 | 525.60 | 3,752 |
| F8 | 8 | 1.44 | 1,051.20 | 7,504 |
| F16 | 16 | 2.88 | 2,102.40 | 15,008 |
| F32 | 32 | 5.76 | 4,204.80 | 30,016 |
| F64 | 64 | 11.52 | 8,409.60 | 60,032 |
| F128 | 128 | 23.04 | 16,819.20 | 120,064 |
| F256 | 256 | 46.08 | 33,638.40 | 240,128 |
| F512 | 512 | 92.16 | 67,276.80 | 480,256 |
| F1024 | 1,024 | 184.32 | 134,553.60 | 960,512 |

The API lists a Fabric Capacity Reservation at 938 USD per CU for a one-year term (start 2023-11-01) and 2,814 USD per CU for a three-year term (start 2026-04-01) [S2700]. The three-year figure is exactly three times the one-year figure, so it reads as a term total with no extra discount per year (Inference). The pricing page says a one- or three-year reservation saves about 41 percent versus pay-as-you-go [S2728]. The pricing page claims about 40.5 percent saving for a one-year reservation versus pay-as-you-go [S1503]. Our arithmetic (938 divided by 1,576.8) agrees. Storage, networking and OneLake are billed separately: hot storage 0.023 USD per GB per month in West US 2 [S1505].

## Regional variation

PAYG rate per CU per hour, USD, from the same API on the same day [S1505]:

| Region | USD per CU-hour |
|---|---|
| West US 2 | 0.18 |
| UK South | 0.21 |
| Japan East | 0.21 |
| Australia East | 0.21 |
| West Europe | 0.22 |
| Brazil South | 0.28 |

Inference: the meter named "Power BI Capacity Usage" carries the F SKU rate. It matches the 0.18 figure widely quoted for the US.

## Caveats

- Region: price depends on the Azure region of the capacity, not the tenant home region [S1501].
- Currency: the API returned no EUR rows for the regions tested. Use the Azure pricing calculator for local currency [S1504].
- Capacity overage: Azure bills overage through the separate meter "Capacity Overage Capacity Usage CU" at three times the pay-as-you-go rate (0.54 USD in West US 2). Overage is on by default for new F capacities and has a rolling 24-hour CU threshold [S2705, S2700].
- New meters: on 2026-10-08 the API listed 139 "On-Demand Usage CU" meters for West US 2, all starting 2026-10-01, for example Power BI OD 0.54, Data Warehouse 0.234, Dataflows Standard 0.216, Spark Memory Optimized 0.18 USD per CU-hour. Learn does not define them (Unknown); rechecked 2026-10-09: the Azure bill page says to use the Retail Prices API for the full meter list [S3011], and a 2026-10-09 API read again showed Capacity Overage at 0.54 from 2025-10-01 and Power BI Capacity Usage CU at 0.18 [S3009]. Inference: the rates are 1x, 1.2x, 1.3x or 3x of 0.18, so they look like per-workload rates for billing outside the capacity pool, similar to the documented on-demand Spark billing [S2700, S2729].
- Marketing pages say prices are for marketing purposes and vary by currency, country and region [S1503].
- Taxes, EA discounts and CSP margins are not included.

## Common mistakes

- Multiplying hourly rate by 24 x 30 for a paused capacity. Paused time is not billed for compute [S1515].
- Comparing Pro at list price with F64 reservation without counting authors, who still need Pro [S1503].

## See also

- [Fabric capacity F SKUs](13_fabric_capacity_f_skus.md)
- [Embedded A SKUs](13_embedded_skus.md)
