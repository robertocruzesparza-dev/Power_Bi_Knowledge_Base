---
id: 02.ui_tour
title: Desktop user interface tour
domain: desktop
type: concept
level: beginner
tags: [desktop, report, data-modeling, dax, tmdl]
summary: Walks through the Desktop window in words: ribbon, canvas, panes, and the Report, Table, Model, DAX query and TMDL views.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S006, S021, S022, S023, S024, S025, S028, S035, S2801, S2841]
references: []
related: [02.options_and_settings, 02.keyboard_and_automation]
---
## Purpose

Describe the screen so you can follow any tutorial without the software open.

## Window layout

- Ribbon across the top with tabs such as Home, Insert, Modeling, View (S006).
- Report canvas in the centre, where visuals are placed (S006).
- Fields or Data pane on the right, listing tables and fields (S006).
- Visualizations pane near it, for chart type and field wells such as Values, Axis, Legend (S006).
- A theme selector (light, dark, system) and a Settings entry that opens Options (S006).
- A view switcher as icons along the left edge (S025).
- Footer and sign-in area at bottom and top right (S035 in the accessibility focus order).

## Views

| View | Purpose | Notes |
|---|---|---|
| Report | Build pages and visuals | Default view (S025) |
| Table | Inspect loaded data, add DAX measures and columns via the formula bar | Hidden if all sources use DirectQuery (S024) |
| Model | Diagram of tables and relationships | Warns above 75 tables; use a custom layout (S023) |
| DAX query | Write and run DAX queries (EVALUATE, optional DEFINE) | Queries do not create model objects (S021) |
| TMDL | Script and edit model metadata as code | GA in Desktop, preview on web (S022) |

Fact (S021): when live connected to a published model, you cannot view or edit model measures in DAX query view, but you can create report measures.

## Power Query Editor

Opened by Transform Data. It is a separate window for connecting, shaping, and loading data. Close and Apply returns to the main window (S006, S025).

## New layout with on-object interaction

Fact (S028): a preview feature moves build and format controls onto the visual. If your Desktop shows no Visualizations pane, this layout is on. Turn it off or on in Options, Preview features, then restart.

## Common mistakes

- Looking for the Table view icon in a DirectQuery-only file (S024).
- Following screenshots that do not match. The layout depends on preview toggles and monthly updates (S028).
- Assuming DAX query view edits the model. Use the Update model action for that (S021).

## Limits and version notes

- Volatile: the interface changes monthly. Fact: modern visual defaults and the Theme pane reached general availability in the August 2026 update (S010).

## See also

- [Options and settings](02_options_and_settings.md)
- [Preview features](02_preview_features.md)
- [Keyboard and automation](02_keyboard_and_automation.md)
