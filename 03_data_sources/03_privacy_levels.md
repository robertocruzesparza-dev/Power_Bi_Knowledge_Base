---
id: 03.privacy_levels
title: Privacy levels and the Data Privacy Firewall
domain: data_sources
type: concept
level: intermediate
tags: [data-source, power-query, security, query-folding, gateway]
summary: What None, Private, Organizational and Public mean, how they limit data combining and folding, and where to set them.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S312, S314, S315, S316, S342, S2550]
references: []
related: [04.data_privacy_firewall, 03.authentication_and_credentials, 04.query_folding]
---

# Privacy levels and the Data Privacy Firewall

Purpose: explain why Power Query sometimes blocks or slows a query that combines two sources, and how to set levels safely.

## Key facts

- Each source is classified None, Private, Organizational or Public (Fact, S314).
- Private: sensitive data. It cannot fold into any other source, even another Private one.
- Organizational: can fold into Private and other Organizational sources, but not into Public ones. Typical for internal databases.
- Public: non-sensitive data visible to anyone, such as a census file from a government site.
- None: no setting. Use only in controlled development.
- The Data Privacy Firewall enforces this. A query that mixes levels may be blocked or forced to buffer data, which stops folding (Fact, S314, S315).

## Why it matters: an example

You filter an Azure SQL table by a value read from an Excel workbook. The fastest plan sends a WHERE clause with that value to the database. A database admin could see the value in a trace. If the workbook is Private, Power Query instead downloads the whole table and filters locally. That is slower but safer (Fact, S342).

## Where to set levels

- Data modelers in Power BI Desktop.
- Semantic model owners in the service, for cloud sources.
- Gateway data source owners, for gateway sources. The gateway setting applies only to scheduled refresh, not DirectQuery (Fact, S312, S342).

## Fast Combine

The option "Ignore the Privacy Levels and potentially improve performance" is also called Fast Combine. It is off by default, does not apply to published semantic models in the service, and Microsoft advises against it (Fact, S314). The personal gateway article has a separate section on using Fast Combine with that gateway (Fact, S306).

## Recent change

Power BI Desktop introduced a setting in the July 2026 version that lets a query reference another query and also access a data source when privacy levels are compatible. It is on by default from that version and matches service behavior. It sits under Options > Preview features, and turning it off restores the older blocking behavior (Fact, S316).

## Common mistakes

- Marking everything Public to silence errors. That risks leaking data.
- Marking a source Private and expecting folding when it is combined with another source.
- Expecting the Desktop-only ignore setting to carry into the service.

## See also

- [Data Privacy Firewall errors in Power Query](../04_power_query_m/04_data_privacy_firewall.md)
- [Authentication and credentials](03_authentication_and_credentials.md)
