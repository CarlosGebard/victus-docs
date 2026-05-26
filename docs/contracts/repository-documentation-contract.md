---
id: VICTUS-CONTRACT-REPOSITORY-DOCS
title: Repository Documentation Contract
status: draft
updated_at: 2026-05-25
audience:
  - humans
  - ai-agents
---

# Repository Documentation Contract

Every Victus repository must be understandable as an independent unit.

## Required Files

Each repository should include:

- `README.md`
- `docs/index.md`
- `docs/architecture.md`
- `docs/contracts.md`
- `docs/operations.md`
- `docs/agent-entrypoint.md`

## Rules

- The repository must explain its own purpose.
- The repository must define its boundaries.
- The repository must expose its inputs and outputs.
- The repository must document its runtime dependencies.
- The repository must link to related Victus repositories.
- The repository must not depend on hidden context.
- Implementation details stay inside the owning repository.
- Global architecture lives in `victus-docs`.

## Agent Reading Order

Agents should read:

1. `README.md`
2. `docs/index.md`
3. `docs/agent-entrypoint.md`
4. `docs/architecture.md`
5. `docs/contracts.md`
6. `docs/operations.md`
