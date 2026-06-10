---
id: VICTUS-MOC-200-OPERATIONS
title: Victus Operations
status: active
updated_at: 2026-05-27
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
| [README.md](01-Projects/victus/victus-docs/README.md) | Human-facing repository overview |
| [AGENTS.md](01-Projects/victus/victus-docs/AGENTS.md) | Agent-facing repository rules |
