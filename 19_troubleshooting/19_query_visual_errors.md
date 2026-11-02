---
id: 19.query_visual_errors
title: Visual query and resource errors
domain: troubleshooting
type: troubleshooting
level: intermediate
tags: [troubleshooting, performance, limits, error-message, dax]
summary: Why a visual shows exceeded-resources or memory errors, the query timeout and memory limits per capacity type, and how to test them in Desktop.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S2128, S2129, S2130, S2509, S2510]
references: []
related: [19.refresh_errors, 19.diagnostics_workflow]
---

# Visual query and resource errors

## Purpose
Explain errors that appear only after publishing. Example: a matrix works in Desktop but fails in the service with "This visual has exceeded the available resources".

## Query limits by host (volatile)
| Host | Timeout | Memory limit |
|---|---|---|
| Shared capacity | 225 s | 1 GB |
| Premium | 225 s | 10 GB |
| SQL Server Analysis Services | 600 s | 1 GB |
| Azure Analysis Services | 600 s | 10 GB |
Source: S2128. Desktop does not apply these to local models by default.

## Test before publishing
File > Options > Current file > Report settings > Query limit simulations. Choose Auto, a capacity type, custom limits, or none (0 means no limit). Auto falls back to shared-capacity limits when it cannot tell [S2128]. Older reports default to no limits [S2128].

## Error messages
- "This visual has exceeded the available resources. Try filtering to decrease the amount of data displayed." Add filters, remove fields, aggregate, split visuals, or optimize the model [S2129].
- "We are not able to identify the following fields" means a field was renamed or deleted; remove it and repin [S2129].
- "Couldn't retrieve the data for this visual. Please try again later" is usually transient [S2129].
- "Resource governing: This operation was canceled because there wasn't enough memory..." includes consumed memory, memory limit and database size. If consumed is 0 and database size exceeds the limit, the model is too big for that SKU to start the command [S2130].
- Effective command limit equals SKU allowance minus memory already used by the model, optionally lowered by `DbpropMsmdRequestMemoryLimit` [S2130].

## Common mistakes
- Trusting Desktop performance as proof the visual works in shared capacity.
- Retrying a memory error forever; transient ones clear quickly, persistent ones need model changes [S2130].

## Not verified
DAX syntax and calculation error catalog: not covered in this pass. See gaps.

## See also
- [Refresh errors](19_refresh_errors.md)
