---
id: VICTUS-ADR-003
title: Wiki.js Authoring with One-Way Git Backup
status: accepted
updated_at: 2026-08-25
owners:
  - architecture
related_docs:
  - ../../000-SYSTEM-CONTEXT.md
  - ../../100-ARCHITECTURE.md
  - ../../200-OPERATIONS.md
  - ../runbooks/wikijs-git-backup.md
tags:
  - documentation
  - wikijs
  - operations
---

# VICTUS-ADR-003: Wiki.js Authoring with One-Way Git Backup

## Context

The previous Git-to-Wiki.js export pipeline maintained a generated branch,
rewrote documents, and invoked the Wiki.js API. It created two competing
authoring paths and failed without causing the workflow to fail.

## Decision

Wiki.js is the sole source for authoring Victus documentation. Its Git storage
target pushes documentation to the dedicated `wiki-production` branch as a
one-way versioned backup.

The repository does not run a GitHub Actions export or import workflow. Git
must not pull content into, or otherwise mutate, Wiki.js.

## Tradeoffs

This removes generated branches, API-triggered imports, merge divergence, and
the need to coordinate two write paths. It also means Wiki.js database
availability and backups are essential because Git is no longer the authoring
authority.

## Alternatives Considered

Bidirectional Git synchronization was rejected because it makes conflict
resolution and ownership ambiguous. Keeping Git as the authoring source was
rejected because the intended editing experience is Wiki.js.

## Consequences

Operators must configure the Git storage target in `Push to target` mode and
perform a Force Sync after configuration. Documentation changes are made in
Wiki.js; Git is used for backup and recovery only.

## Related Documents

- [System Context](../../000-SYSTEM-CONTEXT.md)
- [Architecture MoC](../../100-ARCHITECTURE.md)
- [Wiki.js Git backup runbook](../runbooks/wikijs-git-backup.md)
