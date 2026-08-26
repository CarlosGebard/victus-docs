# Wiki.js One-Way Backup Plan

## Goal

Make Wiki.js the sole documentation authoring source and retain Git only as a
one-way, versioned backup on `wiki-production`.

## Scope

- Remove the GitHub Actions export/import workflow and its helper scripts.
- Record Wiki.js as the documentation authority and Git as backup only.
- Provide a runbook to configure and validate the Wiki.js Git target.

## Assumptions

- Wiki.js content and its database are the authoring authority.
- The Git target is the dedicated `wiki-production` branch.
- Wiki.js uses `Push to target`, never `Pull from target` or bi-directional
  synchronization.
- `repos/**` remains read-only synchronized context.

## Steps

1. Remove the obsolete Git-to-Wiki.js pipeline. Complete.
2. Record the authority change in architecture, contract, and ADR documentation. Complete.
3. Configure the Wiki.js storage target manually and perform a Force Sync. Pending operator action.

## Validation

- Validate Markdown links and ensure the obsolete workflow and scripts are absent.
- In Wiki.js, use Force Sync and verify the new commit appears on
  `wiki-production`.

## Risks

- The manual Wiki.js configuration is outside this repository and must be
  completed by an operator with access to the Wiki.js administration interface.
- Git backups do not replace database backups for Wiki.js.
