---
id: 09.enhanced_refresh_parameters_ref
title: Enhanced refresh REST API parameters
domain: semantic_models_dataflows
type: reference
level: advanced
tags: [rest-api, refresh, semantic-model]
summary: Request body parameters, defaults, and rules for the enhanced refresh call on Power BI semantic models.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: high
sources: [S1212, S2922]
references: []
related: [09.semantic_model_refresh]
---

# Enhanced refresh parameters

Call: `POST https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes`. The response Location header holds the `requestId`. Poll with GET on the same collection. Cancel with DELETE. [S1212]

Requirements: a model in Premium, PPU, or Embedded capacity, the group and dataset IDs, and the Dataset.ReadWrite.All scope. The token can be a user or a service principal, with audience `https://api.powerbi.com`. [S1212]

| Parameter | Default | Meaning |
|---|---|---|
| type | automatic | Matches TMSL refresh types: full, clearValues, calculate, dataOnly, automatic, defragment. The add type is not supported. |
| commitMode | transactional | transactional commits at the end. partialBatch commits each object. |
| maxParallelism | 10 | Maximum parallel threads for processing. |
| retryCount | 0 | Retries before failing. |
| timeout | 5 hours | Per attempt. Format hh:mm:ss. Total with retries must stay under 24 hours. |
| objects | whole model | Array of table, or table plus partition. |
| applyRefreshPolicy | true | Applies the incremental refresh policy. With partialBatch it must be false. |

Sample body (values are examples):

```json
{ "type": "Full", "commitMode": "transactional", "maxParallelism": 2,
  "retryCount": 2, "timeout": "02:00:00",
  "objects": [ { "table": "DimCustomer", "partition": "DimCustomer" }, { "table": "DimDate" } ] }
```

Notes:

- A paused Embedded capacity keeps an enhanced refresh InProgress for up to six hours. It resumes if capacity returns in time. [S1212]
- A retry can push total time past one attempt's time-out. With retryCount 1, a 4-hour failure plus a 3-hour success is 7 hours. [S1212]
- Fabric pipelines have a Semantic model refresh activity with the same options: max parallelism, retry count, time-out, and commit mode. It works only for models you own. [S1212]
