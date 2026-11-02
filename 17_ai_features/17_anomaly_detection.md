---
id: 17.anomaly_detection
title: Anomaly detection on line charts
domain: ai_features
type: how-to
level: intermediate
tags: [ai-visual, visual, limits]
summary: How to turn on anomaly detection for a line chart, tune sensitivity, read explanations, and what blocks the feature.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2106]
references: []
related: [17.key_influencers, 17.decomposition_tree]
---

# Anomaly detection on line charts

## Purpose
Mark points outside the expected range in a time series and suggest reasons. Example: revenue of 5,187 on August 30 against an expected range of 2,447 to 3,423 [S2106].

## Steps
1. Select a line chart with a date on the Axis.
2. On the Analytics tab of the Visualizations pane, open Anomalies and add them.
3. Adjust sensitivity: higher flags smaller deviations, lower is more selective [S2106].
4. Select an anomaly to see explanations. Drop fields into Explain by to restrict the search [S2106].

## Key facts
- Fact: explanation strength is the deviation of a component series (for example one seller) divided by the deviation of the total [S2106].
- Fact: the algorithm is based on the Azure Anomaly Detector (SR-CNN) approach [S2106].
- Fact: you can format anomaly shape, size, color and the expected range band [S2106].

## Limits
- Only line charts with time series on the Axis [S2106].
- No legends, multiple values or secondary values [S2106].
- At least four data points [S2106].
- Forecast, min, max, average, median and percentile lines do not work with it [S2106].
- Not supported: DirectQuery over SAP, Report Server, Live connection to Analysis Services [S2106].
- Explanations fail with Show value as; hierarchy drill-down is unsupported [S2106].

## Common mistakes
- Adding a legend field, which disables detection.

## See also
- [Key influencers](17_key_influencers.md)
- [Decomposition tree](17_decomposition_tree.md)
