---
id: 17.key_influencers
title: Key influencers visual
domain: ai_features
type: how-to
level: intermediate
tags: [ai-visual, visual, troubleshooting, limits]
summary: How the key influencers visual ranks drivers of a metric, how to set it up, its statistics, limits, and the common error messages.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2104]
references: []
related: [17.decomposition_tree, 17.anomaly_detection]
---

## Table of Contents

- [Purpose](#purpose)
- [Setup](#setup)
- [How it works](#how-it-works)
- [Limits](#limits)
- [Errors and fixes](#errors-and-fixes)

# Key influencers visual

## Purpose
It shows which factors drive a metric. Example: which fields make a customer rating "Low"? Consumers were 2.57 times more likely to rate low in the Microsoft sample [S2104].

## Setup
1. Add the Key influencers visual.
2. Put the metric in Analyze. Put candidate drivers in Explain by.
3. Leave Expand by empty unless the metric is a measure or summarized field; it sets the analysis level without adding drivers.
4. Pick the value to explain (for example Low). The Top segments tab shows combinations of factors.
5. Optional: enable counts in the Analysis card to see how much data each influencer covers.

## How it works
- Fact: categorical targets use logistic regression via ML.NET; numeric targets use linear regression; segments use a decision tree [S2104].
- Fact: significance uses a Wald test with p-value 0.05 [S2104].
- Fact: the analysis runs at the row level of the Analyze field's table. Explain by fields must be attributes at that level (aggregate or pivot one-to-many fields) [S2104].
- Fact: continuous drivers non-linear to the target are binned into at most five bins [S2104].
- Fact: for a numeric unsummarized field choose Categorical or Continuous analysis type in Format [S2104].
- Fact: the analysis uses a sample of 10,000 data points [S2104].

## Limits
- No DirectQuery, no Live connection to Analysis Services, no Publish to web, no SharePoint Online embedding [S2104].
- Needs .NET Framework 4.6 or higher [S2104].
- Not supported for a categorical metric if Discourage Implicit Measures is true (for example with calculation groups) [S2104].

## Errors and fixes
| Message | Cause | Fix |
|---|---|---|
| No influencers or segments found | Metric also in Explain by; too many sparse categories; no real correlation | Remove metric from Explain by; try Continuous analysis |
| Not enough data | Fewer than about 100 observations of the target state or 10 of the comparison state | Add data or change the question |
| Field not uniquely related to the table | Driver is at finer grain than the metric | Aggregate to metric level or pivot |
| Measures weren't included | Metric table has no unique identifier | Add a key or index column |
| More than 10 unique values | Too many categories | Group values or use Continuous |
Source: S2104.

## Common mistakes
- Reading influencers as proof of cause. They are statistical associations.
- Adding an ID column to Explain by; use Expand by instead.

## See also
- [Decomposition tree](17_decomposition_tree.md)
- [Narrative visual](17_smart_narratives.md)
