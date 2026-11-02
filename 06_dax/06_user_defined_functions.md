---
id: 06.user_defined_functions
title: DAX user-defined functions
domain: dax
type: how-to
level: advanced
tags: [dax, dax-function, desktop, tmdl]
summary: Explains DAX user-defined functions (UDFs): syntax, parameter types, where to define them, and the conflicting status statements in Microsoft docs.
status: mixed
volatile: true
last_verified: 2026-10-08
confidence: moderate
sources: [S654, S655, S659, S653, S2529, S2530]
references: []
related: [06.best_practices, 06.dax_basics]
---

# DAX user-defined functions

## Purpose
A UDF packages reusable DAX logic with parameters. Write once, call from measures, calculated columns, visual calculations, or other UDFs (S654).

## Key facts
- Fact: UDFs use a FUNCTION keyword, take scalar, table, and reference parameters, and can have default expressions (S654, S659).
- Fact: UDFs need database compatibility level 1702 or higher (S654).
- Fact: They are first-class model objects, listed under Functions in Model explorer (S654).
- Fact: You define them in DAX query view, TMDL view, or Model view, and edit them in web modeling (S659).
- Status (conflict): The June 2026 Desktop update and the best-practices page say UDFs are generally available (GA) from the June 2026 release (S654, S655). The DAX glossary still says preview (S653). The release notes are newer; treat GA as likely, and verify.

## Syntax (S659)
```dax
DEFINE
    /// AddTax takes in amount and returns amount including tax
    FUNCTION AddTax = ( amount : NUMERIC ) => amount * 1.1
EVALUATE
{ AddTax ( 10 ) }
```
TMDL form: `function AddTax = (amount : NUMERIC) => amount * 1.1`.

## Parameter typing (S654, from the FUNCTION statement page)
| Piece | Allowed values |
|---|---|
| Type | ANYVAL, SCALAR, TABLE, ANYREF, CALENDARREF, COLUMNREF, MEASUREREF, TABLEREF |
| Scalar subtype | BOOLEAN, DATETIME, DECIMAL, DOUBLE, INT64, NUMERIC, STRING, VARIANT |
| Passing mode | VAL (eager) or EXPR (lazy) |
Default expression makes the parameter optional. Type hints for calendar, column, measure, and table references were added in March 2026 (S655).

## Steps
1. Open DAX query view and write the DEFINE FUNCTION block.
2. Run EVALUATE to test.
3. Select Update model with changes.
4. Call it from a measure like any function.
5. Review with INFO.USERDEFINEDFUNCTIONS in a query (S655).

## Release notes worth knowing (S655)
- Mar 2026: automatic dependency tracking on rename; /// documentation tags; up to 256 parameters (from 12).
- Apr 2026: NAMEOF accepts optional component and escape arguments.
- Jun 2026: GA wording and optional parameters.

## Common mistakes
- Using a reserved word such as measure as a parameter name.
- Hiding business rules in UDFs without documenting them.
- Forgetting the compatibility level upgrade is one-way for older clients (verify before upgrading shared models).

## See also
- [DAX best practices](06_best_practices.md)
