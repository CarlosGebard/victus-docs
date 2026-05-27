---
id: VICTUS-MOC-300-CONTRACTS
title: Victus Contracts
status: active
updated_at: 2026-05-27
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags:
  - moc
  - contracts
  - navigation
---

# 300 - Contracts

Contracts define stable, explicit system boundaries across the Victus ecosystem.

This Map of Content routes contract readers to the current contract nodes.

## Contract Authority

Canonical cross-repository contracts live in `victus-docs`.

Implementation details belong in repository-local documentation owned by the relevant repository.

## Core Contract Documents

| Document | Purpose |
|---|---|
| [Artifact Contract Hub](docs/contracts/artifacts.md) | Canonical artifact graph and governance |
| [Repository Documentation Contract](docs/contracts/repository-documentation-contract.md) | Documentation expectations for ecosystem repositories |

## Current Contract Areas

- repository documentation
- artifacts
- events
- claims schemas
- storage layouts
- API boundaries

Some contract areas are listed as planned or pending until the relevant decision and owner-specific details are documented.

## Contract Rules

Contracts should:

- describe stable expectations
- avoid implementation-specific details
- expose ownership clearly
- remain readable by humans and AI agents
- be referenced by affected architecture documents

Breaking contract changes require an ADR and updates to affected contract documents.
