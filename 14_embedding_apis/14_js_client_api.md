---
id: 14.js_client_api
title: Power BI JavaScript client API
domain: embedding_apis
type: reference
level: intermediate
tags: [embedding, sdk]
summary: The powerbi-client JavaScript library for embedding and controlling Power BI content from a web page, with its main capabilities.
status: ga
volatile: false
last_verified: 2026-10-07
confidence: moderate
sources: [S1814, S1810]
references: []
related: [14.embed_tokens, 14.embed_for_customers, 14.embed_for_organization]
---
## Purpose

The Power BI client library is a JavaScript and TypeScript library. It renders a report, visual, dashboard, or paginated report inside an HTML element and lets the host page control it.

## Key facts

- Fact: Official docs call it the Power BI embedded analytics Client APIs. Source lives in the `microsoft/PowerBI-JavaScript` repository [S1814].
- Fact: The docs list guides for embedding a report, a single visual, a paginated report, and a dashboard [S1814].
- Fact: A React wrapper and a Jupyter notebook option are documented [S1814].
- Fact: A separate library, Power BI Report Authoring, handles creating and editing visuals in code [S1814].
- Fact: An interactive "playground" lets you test configuration [S1814].
- Unknown: current package version numbers. Check npm before pinning.

## How it works

1. Include the library, then create a service object.
2. Build an embed configuration: item type, ID, embed URL, access token, token type, and settings.
3. Call `embed` on a container element. The library creates an iframe.
4. Listen for events such as loaded, rendered, error, and dataSelected.
5. Call methods on the returned object to apply filters, bookmarks, or settings.

For app owns data, the token type is Embed and the token is an [embed token](14_embed_tokens.md). For user owns data, the token type is Aad and the token is a Microsoft Entra access token (Fact, standard in docs; see [S1814] for the guides).

## Capabilities by area

| Area | What you can do |
|---|---|
| Events | Handle load, render, page change, selection, and errors |
| Tokens | Refresh the access token before expiry |
| Performance | Bootstrap the iframe early so later embeds load faster |
| Filters | Read, set, and remove report, page, and visual filters |
| Settings | Show or hide the filter pane, navigation, and more |
| Authoring | Create, edit, and save reports in an embedded view |
| Bookmarks | Capture and apply bookmarks |
| Layout | Custom layouts and mobile layout |

Source: the table of contents in [S1814].

## Common mistakes

- Not renewing the token. Tokens expire and the visual then fails. The embed token article says to renew before expiry [S1810].
- Passing a user token where an embed token is required, or the reverse.
- Embedding before the user has the right license in the organization scenario.

## Limits and version notes

Behavior depends on the report format and service release. Test with the playground and confirm settings names against the live reference.

## See also

- [Embed tokens](14_embed_tokens.md)
- [Embed for your customers](14_embed_for_customers.md)
- [Custom visuals SDK](14_custom_visuals_sdk.md)
