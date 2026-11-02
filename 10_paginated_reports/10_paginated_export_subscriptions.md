---
id: 10.paginated_export_subscriptions
title: Paginated report export formats and subscriptions
domain: paginated_reports
type: reference
level: intermediate
tags: [paginated-report, service, rest-api, limits, tenant-setting]
summary: Export formats in the service and REST API, and how email subscriptions work, with size, time, and recipient limits.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1224, S1226, S1229, S1230, S1227, S2605]
references: []
related: [10.paginated_parameters, 10.paginated_licensing_capacity]
---
## Purpose

Exports render a report into another file type. Subscriptions run an export on a schedule and email the result.

## Export formats

| Format | Type | Where |
|---|---|---|
| PDF, Accessible PDF (PDF/UA) | Hard page break | Service, REST, subscriptions |
| Word (.docx) | Soft page break | Service, REST, subscriptions |
| Excel (.xlsx) | Soft page break | Service, REST, subscriptions |
| PowerPoint (.pptx) | Hard page break | Service, REST, subscriptions |
| CSV | Data only | Service, REST, subscriptions |
| XML | Data only | Service, REST, subscriptions |
| MHTML (web archive) | Soft page break | Service and Report Builder; not in subscriptions |
| Image (TIFF default; also BMP, EMF, GIF, JPEG, PNG) | Hard page break | Report Builder and REST; not in the service menu |

Sources: S1224, S1226, S1229, S1230. Fact: Accessible PDF is supported only in the service, not Report Builder. [S1229]

Hard-break formats paginate by physical page size. Preview uses HTML soft-break rules, so page counts can change on export. [S1229]

## Subscriptions

Steps (Power BI service): [S1226]

1. Open the paginated report and choose Subscribe.
2. Add recipients and choose frequency, time zone, start and end date.
3. Choose the attachment type. Optionally add a preview image.
4. Set parameter values: current or default. Save.

Rules: [S1226]

- Creating subscriptions needs a tenant switch plus Pro or PPU, or a workspace on Premium capacity. Subscribing others needs Pro or PPU plus Contributor or higher.
- No "After data refresh" option for paginated reports. Each run reads fresh data.
- The report attachment reflects data based on the subscription creator's permissions. RLS data shown follows the owner.
- B2B guests can only subscribe themselves.
- External recipients need a workspace on paid non-PPU capacity. Trial and PPU workspaces cannot send externally.
- Dynamic subscriptions (data-driven) are in preview.
- Run now limits per user per hour: 10 trial, 15 default, 20 PPU, 25 Premium or Fabric.

## Admin switches

A Fabric admin enables: Create email subscriptions, and the export switches for Excel, CSV, PowerPoint or PDF, MHTML, Word, and XML (Tenant settings, Export and sharing). Attachment formats are limited by these switches. [S1226]

## Limits

| Limit | Value |
|---|---|
| Attachment size | 25 MB maximum |
| Report execution in a subscription | 60 minutes |
| Subscriptions per paginated report | unlimited (reports: 24 per report) |
| Concurrent renders per capacity workload | 500 |

Sources: S1226, S1227 (concurrency).

Sensitivity labels apply to attachments, not to email text or preview images. Turn off Preview image to avoid exposing labeled data. [S1226]

## Common mistakes

- Expecting an After-refresh trigger.
- Subscribing an external address from a PPU workspace.
- Letting a long report pass 60 minutes and fail with a timeout.

## See also

- [Parameters](10_paginated_parameters.md)
- [Licensing and capacity](10_paginated_licensing_capacity.md)
