---
id: 03.connector_lifecycle_changes
title: Connector deprecations and driver changes
domain: data_sources
type: reference
level: intermediate
tags: [connector, release, data-source, limits]
summary: Connectors and drivers that were deprecated, retired or changed between 2024 and 2026, with dates and what to do.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S304, S335, S336, S2545, S2546]
references: []
related: [22.deprecations_retirements, 03.connector_catalog_guide]
---

# Connector deprecations and driver changes

Purpose: warn you before a connector or driver you rely on stops working.

## Key facts

| Item | Change | Date | Action |
|---|---|---|---|
| IBM Netezza | Built-in Simba ODBC driver deprecated; IBM Netezza ODBC driver is GA | Notice March 2026, deprecation April 2026 | Install the IBM driver; keep the connector |
| Vertica | Simba Vertica ODBC driver deprecation began | February 2026 | Install the Vertica ODBC driver |
| QuickBooks Online | Connector retired, no new connections, old ones may stop | After March 2026 | Use another route to the data |
| QuickBooks Online (beta) | Deprecation announced | June 2025 | Same |
| Service Excel and CSV import (legacy) | Entry points removed May 31, 2026; old models stop refreshing July 31, 2026 and stop loading August 31, 2026 | 2026 | Rebuild the model with the current experience |
| Government cloud sources | Organizational account no longer works from non-government Power BI | After March 31, 2024 | Use the government Power BI environment |

All rows: Fact from S304, S335 or S336.

## Other connector changes in the monthly notes

- Snowflake: new connector implementation in preview from January 2025, with updates through April 2025 (S336).
- Oracle: built-in driver in preview, April 2025. Vertica user-installed ODBC driver in preview, April 2025 (S336).
- Microsoft Entra ID authentication for PostgreSQL Flexible Server: August 2025 (S336).
- Impala connector 2.0 on the Arrow Database Connectivity driver: preview, August 2025 (S336).
- Export query results from Power Query to Dataflows Gen2 and lakehouses: October 2025 update (S336).
- New Power Query Get Data experience in Desktop: preview from May 2026 (S336, S317).

## How to check a connector you depend on

1. Open its Learn page and read the Release State line and any notes.
2. Search the monthly update archive for the connector name.
3. Test in a copy of the model before updating Desktop or the gateway.

## Common mistakes

- Updating Desktop on a Vertica or Netezza model without installing the vendor ODBC driver.
- Assuming a Preview connector in Desktop is available in the service.

## See also

- [All deprecations and retirements](../22_release_roadmap/22_deprecations_retirements.md)
