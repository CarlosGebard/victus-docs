---
id: VICTUS-CONTRACT-REPOSITORY-DOCS
title: Repository Documentation Contract
status: active
updated_at: 2026-05-27
audience:
  - humans
  - ai-agents
---

# Repository Documentation Contract

Every Victus repository must be understandable as an independent unit.

## Required Files

Each repository should include:

- `README.md`
- `000-SYSTEM-CONTEXT.md`
- `100-ARCHITECTURE.md`
- `200-OPERATIONS.md`
- `300-CONTRACTS.md`
- `decisions/`

Depending on complexity, repositories may also include:

- `docs/architecture/`
- `docs/contracts/`
- `docs/operations/`
- `docs/adr/`
- `docs/api/`
- `docs/pipelines/`
- `docs/runbooks/`

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
2. `000-SYSTEM-CONTEXT.md`
3. `100-ARCHITECTURE.md`
4. `300-CONTRACTS.md`
5. `200-OPERATIONS.md`
6. `decisions/`
