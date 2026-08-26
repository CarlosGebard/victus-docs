---
id: VICTUS-RUNBOOK-WIKIJS-GIT-BACKUP
title: Wiki.js One-Way Git Backup
status: active
updated_at: 2026-08-25
owners:
  - architecture
related_docs:
  - ../../200-OPERATIONS.md
  - ../adr/VICTUS-ADR-003-wikijs-authoring-and-git-backup.md
tags:
  - wikijs
  - git
  - backup
---

# Wiki.js One-Way Git Backup

## Purpose

Keep a versioned backup of Wiki.js documentation in Git without creating a
second authoring path.

## Required Wiki.js Configuration

In **Administration → Storage → Git**, configure one target:

| Setting | Value |
|---|---|
| Repository URI | `https://github.com/victus-fit/victus-docs.git` |
| Branch | `wiki-production` |
| Authentication | GitHub PAT with repository contents write access, or a write-enabled SSH deploy key |
| Verify SSL Certificate | Enabled |
| Sync Direction | `Push to target` |

Do not use `Pull from target` or `Bi-directional` mode. Do not point this
target to `main`.

## Initial Validation

1. Save the target with **Apply Changes**.
2. Confirm the Git storage status is green.
3. Run **Force Sync**.
4. Confirm a new commit appears on `wiki-production` in GitHub.
5. Make a small non-sensitive edit in Wiki.js, wait for the configured sync
   schedule or run **Force Sync**, then confirm it appears in that branch.

## Recovery

If a sync fails, first inspect the Git storage status and verify that the PAT
or deploy key can write to `victus-fit/victus-docs`.

If Wiki.js reports an unrelated local Git history, back up the Wiki.js database,
use **Purge Local Repository**, and run **Force Sync** again. Purging the local
repository does not remove the remote Git backup, but it should only be done
after the database backup is confirmed.

Never recover by enabling pull or bi-directional synchronization: that can
overwrite Wiki.js-authored content.

## Boundaries

Wiki.js and its database are the documentation authority. The Git branch is a
backup and history mechanism; it does not replace database backups.
