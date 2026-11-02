---
id: 19.publishing_errors
title: Publishing errors from Desktop
domain: troubleshooting
type: troubleshooting
level: beginner
tags: [troubleshooting, desktop, service, error-message, tenant-setting]
summary: Common failures when publishing from Power BI Desktop to the service and their fixes, including size limits and blocked republish.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2125]
references: []
related: [19.credentials_auth_errors, 19.diagnostics_workflow]
---

# Publishing errors from Desktop

## Purpose
Fix publish failures in a fixed order.

## General checklist
1. Use the latest Desktop [S2125].
2. Allow Power BI URLs through firewall, proxy and antivirus [S2125].
3. Check connectivity [S2125].
4. Clear cache: File > Options > Data Load > Clear Cache [S2125].
5. Clear cached credentials: File > Options > Data source settings > Clear Permissions [S2125].
6. Confirm permissions on the target workspace and model, and sign in to the service [S2125].

## Specific errors
| Error or symptom | Cause | Fix |
|---|---|---|
| "The remote server returned an error: (400) Bad Request" | Pro licence and model over 1 GB | PPU or Premium capacity [S2125] |
| "Unable to write data to the transport connection..." | Network | Different network, cloud VM, upload via OneDrive or SharePoint, shrink file [S2125] |
| Cannot publish to a different workspace | Tenant setting "Use semantic models across workspaces" off | Ask admin [S2125] |
| Cannot republish | Tenant setting "Block republish and disable package refresh" on | Ask admin [S2125] |
| "A report has already been published with this name" | Live-connected report with same name as the original, would overwrite the model | Publish the original, or rename [S2125] |
| Duplicate reports after publishing | Unstable network | Delete duplicates [S2125] |

## Common mistakes
- Renaming the live-connected report to the original name.

## See also
- [Credentials and sign-in](19_credentials_auth_errors.md)
