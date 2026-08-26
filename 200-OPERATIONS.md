---
id: VICTUS-MOC-200-OPERATIONS
title: Victus Operations
status: active
updated_at: 2026-08-25
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags:
  - moc
  - operations
  - navigation
---

# 200 - Operations

This repository is documentation-first. It does not own runtime services, deployment code, or repository-local operational commands.

Wiki.js documentation synchronization is intentionally one-way: Wiki.js writes
the Git backup; Git never imports documentation back into Wiki.js.

## Operational Scope

`victus-docs` owns operational guidance for:

- maintaining canonical documentation
- validating documentation changes
- preserving repository boundaries
- guiding AI-agent navigation
- keeping synchronized repository context read-only

Runtime operations for infrastructure, processing, and RAG services belong in the owning repositories.

## Local Validation

Useful checks for documentation changes:

```bash
git status --short
find . -path './repos' -prune -o -type f -name '*.md' -print
```

Before claiming completion:

- inspect changed files
- confirm links point to existing local targets
- confirm no synchronized mirror files were changed

## Repository Mirrors

Synchronized repository context must be treated as read-only from this repository:

- `repos/victus-infra/`
- `repos/victus-processing/`
- `repos/victus-rag/`

If implementation source or repository-local runbooks need changes, switch to the owning repository.

## Operational Documents

| Document | Purpose |
|---|---|
| [README.md](README.md) | Human-facing repository overview |
| [AGENTS.md](AGENTS.md) | Agent-facing repository rules |
| [Wiki.js Git backup runbook](docs/runbooks/wikijs-git-backup.md) | Configure, validate, and recover the one-way Wiki.js backup |
