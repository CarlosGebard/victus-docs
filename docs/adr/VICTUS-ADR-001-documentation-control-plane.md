---
id: VICTUS-ADR-001
title: Documentation Control Plane
status: accepted
updated_at: 2026-05-26
owners:
  - architecture
audience:
  - humans
  - ai-agents
related_docs:
  - ../architecture/context.md
  - ../contracts/index.md
  - ../contracts/artifacts.md
tags:
  - adr
  - documentation
  - governance
---

# VICTUS-ADR-001: Documentation Control Plane

## Context

Victus is a multi-repository scientific knowledge platform. Its architecture depends on clear repository boundaries, stable artifacts, deterministic retrieval behavior, and traceable scientific reasoning.

The documentation layer must be readable by humans and AI agents without relying on hidden context.

## Decision

`victus-docs` is the canonical documentation control plane for the Victus ecosystem.

It owns:

- global architecture context
- cross-repository contracts
- architecture decision records
- AI-agent navigation rules
- documentation governance

Owning repositories retain their implementation details. Source code must not be edited from `victus-docs`.

Repository mirrors or git subtrees may be added under `repos/` later as read-only context sources.

## Consequences

- Global contracts live in `victus-docs/docs/contracts/`.
- Implementation-specific documentation lives in the owning repository.
- Breaking artifact or contract changes require an ADR and contract updates.
- AI agents must prefer contracts and ADRs over inferred implementation behavior.

## Non-Goals

- `victus-docs` does not replace repository-local documentation.
- `victus-docs` does not own source code changes for other repositories.
- `victus-docs` does not document repository implementation details before mirrors or source context exist.
