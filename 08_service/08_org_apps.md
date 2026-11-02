---
id: 08.org_apps
title: Org apps (Fabric item) versus workspace apps
domain: service
type: comparison
level: intermediate
tags: [app, fabric, service, comparison]
summary: What org apps are, how they differ from workspace apps, included item types, and documented limitations as of October 2026.
status: mixed
volatile: true
last_verified: 2026-10-09
confidence: moderate
sources: [S925, S926, S924, S2908]
references: []
related: [08.workspace_apps, 08.distribution_decision_guide]
---
## Purpose

Org apps are a newer way to package content, implemented as a Fabric item. They are generally available and live beside workspace apps.

## Key facts

- You can create several org apps per workspace. Fact.
- Included items stay in the same workspace. Supported types: Power BI reports, paginated reports, Fabric notebooks, Fabric Apps (preview), maps, and real-time dashboards. Fact.
- Dashboards and scorecards cannot be included. Fact.
- Granting access to an org app gives at least read access to the included items. For reports, users also gain read access to the underlying semantic models, even in another workspace. Fact.
- Audiences are child items of the org app, so audience access can be managed without entering edit mode. Fact.
- Users do not install an org app. It appears in item lists such as Recent on Home, in the OneLake catalog, and on the Apps page. Fact.

## Comparison

| Topic | Org app | Workspace app |
|---|---|---|
| Apps per workspace | Several | One |
| Versioning | Not versioned; Save makes changes visible at once | Versioned; changes appear at Update app |
| Install by user | Not needed | Install from Apps page or link |
| Removing a user | Revokes org-app-based access, including semantic model access | Model access must be revoked manually |
| Paginated report model access | Granted automatically | Managed manually |
| Cross-workspace model access | Can be granted automatically | Managed manually |
| Who can share | Users with share permission on the item | Specific workspace roles |
| Direct link to included items | Users with app access can view items by direct link | Items outside the app need separate access |

## Limitations

- Not all report toolbar features exist in org apps; comments are an example. Fact.
- Email subscriptions work for Power BI reports in org apps with some differences. They are not supported for paginated reports in org apps. Fact.
- Audience tabs are not supported in the Power BI mobile apps. Fact.
- The navigation sidebar stays visible by default; Focus mode hides it. Fact.
- For an included Fabric App, access to the app's own data items is not managed by the org app. Fact.
- The Home page "My apps" list shows only workspace apps. Use the Apps page to see every app type. Fact.

## Status notes

- Org apps: generally available. Fabric Apps: preview. Template apps remain a separate type. Fact.
- Some screens still show older terms such as "App". The new Apps page labels types Org app, Workspace app, App (Fabric App), and Template app. Fact.
- Whether Microsoft will retire workspace apps is not stated in the pages read. Unknown.

## See also

- [Workspace apps](08_workspace_apps.md)
- [Distribution decision guide](08_distribution_decision_guide.md)
