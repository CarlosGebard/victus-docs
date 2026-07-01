---
id: VICTUS-ADR-002
title: Hybrid Hub-and-Node Documentation Convention
status: accepted
updated_at: 2026-05-27
owners:
  - architecture
related_docs:
  - ../../000-SYSTEM-CONTEXT.md
  - ../../100-ARCHITECTURE.md
  - ../../200-OPERATIONS.md
  - ../../300-CONTRACTS.md
  - ../../decisions/README.md
tags:
  - documentation
  - architecture
  - governance
---

# VICTUS-ADR-002 - Hybrid Hub-and-Node Documentation Convention

## Context

Victus uses multiple repositories with different documentation needs. Agents and humans need a stable first reading layer that works across repositories without forcing every detail into one large index.

Existing `victus-docs` documentation already separates architecture, contracts, ADRs, and agent navigation, but the entrypoints were spread across `docs/**`.

## Decision

Adopt a root-level hybrid Hub-and-Node documentation convention:

```txt
000-SYSTEM-CONTEXT.md
100-ARCHITECTURE.md
200-OPERATIONS.md
300-CONTRACTS.md
decisions/
```

The numbered files act as Maps of Content. They route readers to detailed documents in their owning folders.

Existing detailed documents under `docs/**` remain valid canonical nodes unless a later migration explicitly replaces them.

## Tradeoffs

This creates a clearer first reading path for humans and AI agents.

It also introduces a second navigation layer, so the numbered files must stay lightweight to avoid duplicated documentation drifting from detailed nodes.

## Alternatives Considered

Keep only the existing `docs/**` structure.

This was rejected because it does not match the documentation convention used across the broader project set and makes the first reading path less uniform.

Move all existing documents into the new root structure immediately.

This was rejected because it would create unnecessary link churn and increase the chance of broken references.

## Consequences

Future Victus repositories should expose the root MoC convention before deeper documentation.

Architecture, operations, and contract changes should update the relevant numbered MoC when reader navigation changes.

ADR storage remains under `docs/adr/` for now, with `decisions/` acting as the root decision hub.

## Related Documents

- [System Context](../../000-SYSTEM-CONTEXT.md)
- [Architecture MoC](../../100-ARCHITECTURE.md)
- [Operations MoC](../../200-OPERATIONS.md)
- [Contracts MoC](../../300-CONTRACTS.md)
- [Decision Hub](../../decisions/README.md)
