---
id: 17.decomposition_tree
title: Decomposition tree visual
domain: ai_features
type: how-to
level: beginner
tags: [ai-visual, visual, drill, limits]
summary: How the decomposition tree breaks a measure down by dimensions, how AI splits find high and low values, locking, and limits.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S2105, S2145]
references: []
related: [17.key_influencers, 17.anomaly_detection]
---

# Decomposition tree visual

## Purpose
Explore a measure across dimensions in any order and find root causes. Example: percent of products on backorder, split by product type and plant [S2105].

## Key facts
- Fact: inputs are Analyze (must be a measure or aggregate) and Explain by (one or more dimensions) [S2105].
- Fact: the plus sign beside a node chooses the next field to drill into [S2105].
- Fact: AI splits are marked with a light bulb. High Value and Low Value find the field giving the highest or lowest measure [S2105].
- Fact: Absolute mode finds the largest value; Relative mode finds values that stand out against other values in the column [S2105].
- Fact: AI levels recalculate when you pick another node or cross-filter [S2105].
- Fact: an AI level can follow an AI level, but a manual level after an AI level turns the AI level into a normal one [S2105].
- Fact: creators can lock levels so consumers cannot change them. Locked levels cannot sit after unlocked ones [S2105].

## Limits
- Fact: maximum 50 levels, 5,000 data points at once, top 10 shown per level [S2105].
- Fact: not supported with on-premises Analysis Services [S2105].
- Fact: AI splits are not supported with Azure Analysis Services, Report Server, Publish to web, or complex measures [S2105].
- Fact: not supported inside Q&A [S2105]. Visual calculations do not work with it either [S2145].

## Common mistakes
- Using a column as Analyze without aggregating it.
- Expecting stable AI splits after cross-filtering; the chosen column can change.

## See also
- [Key influencers](17_key_influencers.md)
- [Anomaly detection](17_anomaly_detection.md)
