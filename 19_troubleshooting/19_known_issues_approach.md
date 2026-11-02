---
id: 19.known_issues_approach
title: Approach to known issues and support
domain: troubleshooting
type: decision
level: beginner
tags: [troubleshooting, best-practice]
summary: How to decide whether a problem is a documented limit, a known issue, a configuration fault or a case for a support ticket.
status: n/a
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S2122, S2123, S2114, S2126]
references: []
related: [19.diagnostics_workflow]
---

# Approach to known issues and support

## Purpose
Avoid chasing a "bug" that is a documented limit. This file is a method, not a list of current incidents.

## Decision steps
1. Is it a documented limit? Many failures are limits: 1 GB model for Pro, 2-hour refresh timeout in shared capacity, 5 hours in Premium [S2122, S2125]. Check the feature's "Considerations and limitations" section first.
2. Is it a version problem? Microsoft supports only the last six gateway versions [S2122]. Update Desktop and gateway.
3. Is it configuration? Server and database names must match between Desktop and the gateway data source, and the user must be on the data source Users list [S2123].
4. Is it transient? Memory and connection errors often clear on retry; Power BI also retries automatically [S2122, S2137].
5. Does it reproduce in a Microsoft tool? For external-tool issues, Microsoft helps only if you can reproduce in Microsoft tools such as SSMS [S2114].
6. Still open: collect evidence ([workflow](19_diagnostics_workflow.md)) and open a support ticket, or ask the community [S2122, S2123].

## Where known issues are published
- Unverified in this pass: the Microsoft Fabric/Power BI "known issues" list and the monthly feature summary. Check the Fabric support site and release blog; see gaps.

## Label discipline
- Treat community fixes as community. Prefer official pages when they disagree, and record dates.

## Common mistakes
- Retrying a scheduled refresh endlessly: after four consecutive failures Power BI disables the schedule [S2122].
- Assuming a fix from an old forum post still applies after a service update.

## See also
- [Diagnostics workflow](19_diagnostics_workflow.md)
