---
id: 04.data_privacy_firewall
title: Data Privacy Firewall and Formula.Firewall errors
domain: power_query_m
type: troubleshooting
level: advanced
tags: [power-query, query-folding, troubleshooting, error-message, security]
summary: How the Data Privacy Firewall partitions queries, why Formula.Firewall errors occur, and the July 2026 Desktop setting that relaxes one case.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S314, S315, S316, S326, S2837]
references: []
related: [03.privacy_levels, 04.errors_and_fixes, 04.query_folding]
---

# Data Privacy Firewall and Formula.Firewall errors

Purpose: explain the firewall rule behind the common Formula.Firewall error, so you can restructure a query instead of weakening privacy.

## Key facts

- The firewall splits a query into partitions. A partition that references another partition goes through a call named `Value.Firewall`, which can deny the request or buffer the data. Buffering stops further folding to the original source (Fact, S315).
- Core rule: a partition may either access compatible data sources or reference other partitions, not both (Fact, S315).
- Compatible means data may flow both ways. Only two combinations qualify: both sources Public, or both Organizational. Private with anything, or Public with Organizational, is not compatible (Fact, S315).
- When the error appears, the message mentions Formula.Firewall and that a query references other queries or steps and so cannot access a data source directly (Fact, S326 gives the error name; message wording not re-read).

## Typical cause

Query A reads a value, for example a date from a table. Query B calls `Web.Contents` or `Sql.Database` and uses A's value in the request. B both references a partition and accesses a source.

## Fixes, safest first

1. Set correct privacy levels on all sources. If they are compatible (both Organizational), the pattern is allowed in the service and, from July 2026, in Desktop.
2. Restructure: do the lookup and the data fetch in one query, or fetch all data first and filter inside Power Query.
3. Pass the value as a function argument or a query parameter instead of a referenced query.
4. Update Power BI Desktop to the July 2026 build or later.
5. Last resort for local testing only: relax or ignore privacy levels. This option can leak data, does not apply to published semantic models, and Microsoft advises against it (Fact, S314).

## Desktop setting added in July 2026 (Fact, S316)

"Allow data privacy firewall partitions that reference other partitions to also access data sources" lives under File > Options and settings > Options > GLOBAL > Preview features. It is enabled by default from the July 2026 Desktop version and matches the behavior of Power Query Online, gateways and the service. When disabled, Desktop keeps the older rule and blocks such queries even when levels are compatible. Example it permits: one query returns a value that another uses to build a web request, SQL statement or file path.

## Common mistakes

- Setting every source to Public.
- Debugging only in Desktop. Older Desktop builds are stricter than the service, so a query may fail in Desktop and work after publishing, or the reverse if levels differ (Inference from S316).

## See also

- [Privacy levels](../03_data_sources/03_privacy_levels.md)
- [Errors and fixes](04_errors_and_fixes.md)
