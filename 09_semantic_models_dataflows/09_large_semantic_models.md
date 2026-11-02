---
id: 09.large_semantic_models
title: Large semantic model storage format
domain: semantic_models_dataflows
type: reference
level: advanced
tags: [semantic-model, capacity, limits, xmla]
summary: How the large semantic model storage format works, how to enable it, size limits, eviction, and restrictions.
status: ga
volatile: true
last_verified: 2026-10-08
confidence: high
sources: [S1201, S1212, S1208, S2618]
references: []
related: [09.semantic_model_refresh, 11.fabric_capacity_and_licensing]
---
## Purpose

The default size limit for an imported semantic model is 1 GB. The large storage format lifts that limit on paid capacity. Use it for big Import models or for any model you write to through XMLA tools.

## Key facts

- Fact: Default model size limit is 1 GB. With the large format, the limit equals the capacity size, or the maximum set by the capacity admin. [S1201]
- Fact: The setting works on Fabric F SKUs, Premium P SKUs, Embedded A SKUs, Premium Per User (PPU), and Pro workspaces on Reserved Capacity for Pro Workspaces. Pro workspaces keep a 1 GB limit. [S1201]
- Fact: The Desktop upload limit stays 10 GB. Models can grow past that in the service on refresh. [S1201]
- Fact: Push semantic models do not support the large format. [S1201]
- Fact: The default segment size becomes 8 million rows, matching Azure Analysis Services. [S1201]
- Fact: Pro workspaces do not support XMLA write operations. [S1201]
- Fact: In the small storage format, the admin Max Offline Semantic model Size is also capped by a SKU ceiling: F2 1 GB, F4 2 GB, F8 3 GB, F16 5 GB, F32 6 GB, F64 and larger 10 GB. The ceiling does not apply to the large format. [S2618]

## Enable it

1. Publish the model to a workspace on paid capacity.
2. Open semantic model Settings, expand Large semantic model storage format, set On, and Apply.
3. Run a refresh to load history. Use incremental refresh for big tables.

To make it the default for new models, open Workspace settings, then Premium, then Default storage format. You cannot set this default through the REST API. [S1201]

PowerShell option: `Set-PowerBIDataset -Id <id> -TargetStorageMode PremiumFiles`. The module is MicrosoftPowerBIMgmt. You need capacity admin and workspace admin rights. [S1201]

## Memory behavior

- Eviction: Power BI removes idle models from memory so total model size can exceed the SKU memory. One model must still fit the SKU limit. A reload after eviction can cause a delay. [S1201]
- On-demand load pages data in as queries need it. It is on by default for large models. [S1201]
- Check size with Dynamic Management Views (DMVs) over XMLA. Sum DICTIONARY_SIZE and USED_SIZE. [S1201]
- A model near half the capacity memory can run out of memory during refresh. Refresh in parts with enhanced refresh or XMLA. [S1201, S1212]
- If eviction hits a running refresh, error 0xC11C0020 can occur. Rerun the refresh. [S1212]

## Limits and version notes

- Large models are only available in Azure regions that support Azure Premium Files Storage. The Learn page lists them. [S1201]
- A workspace holding a large model cannot move to a capacity in another region. [S1201]
- Not available for US Government DoD customers. [S1201]
- Power BI Premium P SKUs are being retired in favor of F SKUs. See [Fabric capacity and licensing](../11_fabric_onelake/11_fabric_capacity_and_licensing.md). [S1208]

## See also

- [Semantic model refresh](09_semantic_model_refresh.md)
- [Semantic model basics](09_semantic_model_basics.md)
