---
id: 06.ref_functions_statistical_relationship
title: DAX statistical and relationship functions catalog
domain: dax
type: reference
level: intermediate
tags: [dax, dax-function, relationship, catalog]
summary: Catalog of DAX statistical functions (ranking, percentile, distributions) and the four relationship functions, verified against Microsoft Learn.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: high
sources: [S657, S658]
references: []
related: [06.patterns, 05.filter_direction_ambiguity]
---

# DAX statistical and relationship functions catalog

Fact: Names come from Microsoft Learn category pages read on 2026-10-07 (S657, S658).

## Relationship functions (S658)
| Function | Purpose |
|---|---|
| RELATED | Value from the one side of a relationship; needs row context |
| RELATEDTABLE | Rows from the many side related to the current row |
| USERELATIONSHIP | Uses a named inactive relationship for one calculation |
| CROSSFILTER | Sets filter direction (one, both, none) for one calculation |

Fact: RELATED cannot read the one side across a limited relationship (see [relationships](../../05_data_modeling/05_relationships_cardinality.md)).

## Ranking and sampling
- RANKX: rank of a value for each row of a table; the usual ranking tool in measures.
- RANK.EQ: rank of a number in a list of numbers.
- SAMPLE: N sampled rows of a table.
- Newer window-function options (RANK, ROWNUMBER) are in the [filter catalog](06_functions_filter.md).

## Central tendency and spread
| Function | Purpose |
|---|---|
| MEDIAN, MEDIANX | Median of a column, or of an expression per row |
| GEOMEAN, GEOMEANX | Geometric mean |
| PERCENTILE.INC, PERCENTILE.EXC | Percentile of a column (inclusive or exclusive of 0 and 1) |
| PERCENTILEX.INC, PERCENTILEX.EXC | Percentile of an expression per row |
| STDEV.S, STDEV.P, STDEVX.S, STDEVX.P | Standard deviation of a sample or whole population |
| VAR.S, VAR.P, VARX.S, VARX.P | Variance of a sample or whole population |

## Regression and counting
- LINEST and LINESTX: least squares straight-line fit.
- COMBIN, COMBINA, PERMUT: counts of combinations and permutations.
- CONFIDENCE.NORM, CONFIDENCE.T: confidence interval.

## Distributions
BETA.DIST, BETA.INV, CHISQ.DIST, CHISQ.DIST.RT, CHISQ.INV, CHISQ.INV.RT, EXPON.DIST, NORM.DIST, NORM.INV, NORM.S.DIST, NORM.S.INV, POISSON.DIST, T.DIST, T.DIST.2T, T.DIST.RT, T.INV, T.INV.2t.

## Not catalogued here
Fact: DAX also has financial, parent and child, and other categories. This KB does not list them; see the Learn function reference (S640). Parent and child functions (such as PATH) are used to flatten a parent-child hierarchy into columns (S603).
