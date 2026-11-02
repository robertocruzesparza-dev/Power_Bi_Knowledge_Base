---
id: 14.custom_visuals_sdk
title: Custom visuals SDK (pbiviz)
domain: embedding_apis
type: how-to
level: advanced
tags: [custom-visual, sdk]
summary: How developers build, test, and package Power BI custom visuals with the pbiviz tools, and what certification requires.
status: ga
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S1815, S1816, S1817, S2934]
references: []
related: [14.js_client_api]
---
## Purpose

A custom visual is a TypeScript and JavaScript package that draws data in a way the built-in visuals cannot. It ships as one `.pbiviz` file. Developers build it with the open-source `powerbi-visuals-tools` package.

## Key facts

- Fact: Prerequisites are Node.js, the `pbiviz` tool, a code editor such as Visual Studio Code, and a Power BI Pro or Premium Per User (PPU) account [S1815].
- Fact: Install the tool with `npm i -g powerbi-visuals-tools@latest` [S1815].
- Fact: The developer visual for live testing exists only in the Power BI service, not Desktop or mobile. The packaged visual works everywhere [S1815].
- Fact: Distribution options are AppSource (public), the organizational store, or a private `.pbiviz` file [S1806].
- Fact: Only private visuals are stored in a report's `CustomVisuals` folder in a project; AppSource and organizational visuals load automatically [S1806].

## Setup steps

1. Install Node.js (long-term support version) and restart.
2. Install `pbiviz` with npm.
3. Enable developer mode in Power BI service settings.
4. Create a project: `pbiviz new <name>`.
5. Run `pbiviz start` from the project root. The local server needs an SSL certificate; see Microsoft's certificate guide [S1815].
6. Add the developer visual to a report in the service and test with data.
7. Build the package: `pbiviz package`.

## Project layout

`pbiviz new` creates these items [S1817]:

| Item | Role |
|---|---|
| `src/visual.ts` | Main visual code |
| `src/settings.ts` | Visual property definitions |
| `style/visual.less` | Styles |
| `capabilities.json` | Data roles, data view mappings, formatting objects |
| `pbiviz.json` | Visual metadata |
| `assets/icon.png` | 20 by 20 pixel PNG icon |
| `package.json`, `tsconfig.json` | Node and TypeScript setup |

## Certification

Certified visuals are reviewed by Microsoft for security and quality. Requirements in the docs include [S1816]:

- `typescript`, `eslint`, and `eslint-plugin-powerbi-visuals` in `package.json`, plus a lint command.
- A `package-lock.json` and `tsconfig.json`.
- `npm install`, `pbiviz package`, `npm audit` (no high or moderate warnings), and ESLint must run clean.
- Use the latest `powerbi-visuals-tools`.
- From tools version 6.1.0, `pbiviz package --certification-audit` flags unsafe `fetch`, `XMLHttpRequest`, and `eval` calls. `--certification-fix` removes them from libraries you cannot edit. Remove them from your own code by hand [S1816].

## Common mistakes

- Expecting the developer visual in Desktop.
- Skipping the SSL certificate step, then seeing no connection to the service [S1815].
- Using `eval` or network calls and failing certification.

## Limits and version notes

Tooling versions, certification rules, and supported API versions change often. Treat the lists above as a snapshot dated 2026-10-09. The tenant setting **Allow visuals created by the Power BI SDK** controls whether report authors may use private visuals [S1842].

## See also

- [JS client API](14_js_client_api.md)
- [Power BI project formats](../15_devops_lifecycle/15_pbip_format.md)
