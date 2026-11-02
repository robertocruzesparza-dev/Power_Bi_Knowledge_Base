---
id: 18.external_tools_overview
title: External tools for Power BI Desktop
domain: ecosystem_tools
type: concept
level: intermediate
tags: [ecosystem, desktop, semantic-model, xmla]
summary: How external tools such as DAX Studio, Tabular Editor and ALM Toolkit connect to Power BI Desktop, how to register them, and what is unsupported.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2114]
references: []
related: [18.dax_studio, 18.tabular_editor, 18.alm_toolkit_bravo]
---

# External tools for Power BI Desktop

## Purpose
Community and vendor tools extend Desktop for modeling, DAX tuning and deployment. Example: launch DAX Studio from the External Tools ribbon and it connects to the open model automatically [S2114].

## Key facts
- Fact: when Desktop opens a file it starts a local Analysis Services engine on a random port with a GUID model name. The ribbon passes server, port and model name to the tool [S2114].
- Fact: categories are semantic modeling (DAX Studio, ALM Toolkit, Tabular Editor, Metadata Translator), data analysis, miscellaneous, custom [S2114].
- Fact: tools register through a *.pbitool.json file in `C:\Program Files (x86)\Common Files\Microsoft Shared\Power BI Desktop\External Tools`. DAX Studio and ALM Toolkit create it on install [S2114].
- Fact: Microsoft supports only the public APIs; third-party tools are supported by their owners. Microsoft helps if you can reproduce the issue with Microsoft tools such as SQL Server Management Studio (SSMS) [S2114].
- Fact: admins can disable the ribbon with the registry value `EnableExternalTools` (0 disables) [S2114].

## Cautions
- Write operations are supported but changes outside Desktop can cause unexpected behavior or, rarely, model inconsistency [S2114].
- Editing a template (PBIT) file is not supported; sending processing commands to a model loaded in Desktop is not supported [S2114].
- Not supported in Desktop for Power BI Report Server [S2114].

## Common mistakes
- Treating the Desktop port as stable; it changes every session.
- Expecting Microsoft support for third-party tool bugs.

## See also
- [DAX Studio](18_dax_studio.md)
- [Tabular Editor](18_tabular_editor.md)
- [ALM Toolkit and Bravo](18_alm_toolkit_bravo.md)
