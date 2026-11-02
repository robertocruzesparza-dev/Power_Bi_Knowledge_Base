---
id: 06.best_practices
title: DAX style and performance best practices
domain: dax
type: decision
level: intermediate
tags: [dax, best-practice, optimization, anti-pattern]
summary: Practical rules for writing readable, fast DAX, with sources and the reasoning behind each rule.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S661, S660, S662, S651, S604]
references: []
related: [06.measures_columns_variables, 16.optimization_checklist]
---

# DAX style and performance best practices

## Purpose
Short rules that prevent most wrong-number and slow-measure problems.

## Rules
| Rule | Why | Source |
|---|---|---|
| Use SELECTEDVALUE, not IF + HASONEVALUE + VALUES | Same result, shorter, more efficient | S662 |
| Use DIVIDE for ratios | Handles zero denominators | S648 |
| Prefer REMOVEFILTERS to ALL as a modifier | States intent; Microsoft recommends it | S651 |
| Switch filter direction in a measure with CROSSFILTER | Avoids permanent bi-directional cost | S604 |
| Use VAR for repeated subexpressions | One evaluation, easier debugging | S652, S661 |
| Merge alternatives into one CALCULATE filter | Fewer storage engine requests | S661 |
| Do not call measures in wide calculated columns | Context transition filters all columns | S660 |
| Use explicit measures | Reusable, formattable, work with calculation groups | S616 |
| Keep fact columns narrow; hide keys | Smaller model, cleaner field list | see 16 domain |

## Formula engine and storage engine
Fact (S661): Separate filter contexts on the same column can send sequential requests to the storage engine; newer engines batch some. Combining logic into one CALCULATE can reduce requests. Re-test after engine upgrades. Inference: this is why consolidating many one-account measures into grouped measures helps in profit-and-loss models.

## Style
1. One measure per business idea; name it for the user.
2. Format with consistent indentation; one argument per line when long.
3. Put base measures in a Measures table or the fact table and organize in display folders.
4. Comment non-obvious logic.
5. Avoid hardcoded values; use parameter tables.

## Anti-patterns
- Calculated columns for values that depend on filters.
- FILTER over an entire large table when a column predicate works.
- Nested IFs when SWITCH is clearer.
- IFERROR everywhere.
- Time shifts built from extra offset columns on the date table; Microsoft says they bloat models (S628).
- Using bi-directional relationships by default.

## Steps to tune a slow measure
1. Capture it with Performance Analyzer ([guide](../16_performance/16_performance_analyzer.md)).
2. Run the copied query in DAX Studio with Server Timings ([guide](../16_performance/16_dax_studio_vertipaq.md)).
3. If the storage engine dominates, reduce columns or cardinality, or fix relationships.
4. If the formula engine dominates, simplify iterators, remove nested measure calls, use VAR.
5. Re-measure with a cold cache.

## See also
- [Optimization checklist](../16_performance/16_optimization_checklist.md)
- [Patterns](06_patterns.md)
