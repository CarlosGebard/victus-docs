---
id: VICTUS-AGENT-ENTRYPOINT
title: Victus Agent Entrypoint
status: draft
updated_at: 2026-05-26

owners:
  - architecture

audience:
  - ai-agents

tags:
  - agents
  - navigation
  - orchestration
---

# Victus Agent Entrypoint

This document defines how AI agents should navigate the Victus ecosystem.

## Initial Reading Order

Agents should read documents in the following order:

1. `docs/index.md`
2. `docs/architecture/context.md`
3. `docs/contracts/index.md`
4. `docs/adr/index.md`

Then continue into the target repository subtree.

## Repository Responsibilities

| Repository | Responsibility |
|---|---|
| `victus-infra` | Infrastructure, networking, storage, deployment foundation |
| `victus-processing` | Ingestion, markdown extraction, chunking, embeddings, claims |
| `victus-rag` | Retrieval, vector search, prompts, API orchestration |

## Agent Rules

Agents must:

- prefer explicit documentation over assumptions
- avoid inventing undocumented architecture
- respect repository boundaries
- prefer contracts over implementation details
- propose ADRs for major architectural changes
- ask for explicit decisions when architecture or contract ownership is unclear
- treat deprecated documents as low-trust sources

## Missing Information Policy

If required information is missing:

1. identify the missing context
2. request documentation updates
3. avoid generating fake implementation details

## Documentation Priority

When conflicts exist:

1. contracts
2. ADRs
3. architecture docs
4. operational docs
5. implementation details

## Repository Navigation

Each repository should expose:

- `README.md`
- `docs/index.md`
- `docs/agent-entrypoint.md`

before deeper navigation.

## Repository Boundary Rule

Agents must not edit source code for other Victus repositories from `victus-docs`.

When repository mirrors are present under `repos/`, treat them as read-only context unless the user explicitly switches to the owning repository.
