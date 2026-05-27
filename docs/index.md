---
id: VICTUS-DOCS-INDEX
title: Victus Documentation Index
status: draft
updated_at: 2026-05-25

owners:
  - architecture

audience:
  - humans
  - ai-agents

tags:
  - documentation
  - index
  - architecture
---

# Victus Documentation

Victus is a modular platform for ingesting, processing, structuring, and retrieving scientific knowledge about nutrition and food-related health.

This repository is the canonical documentation control plane for the Victus ecosystem.

## First Read

| Reader | Start with | Then read |
|---|---|---|
| Human | [Repository README](../README.md) | [Architecture Context](architecture/context.md) |
| AI agent | [Agent Entrypoint](agents/entrypoint.md) | [Contracts Index](contracts/index.md) |
| Architecture reviewer | [Architecture Context](architecture/context.md) | [ADR Index](adr/index.md) |
| Contract reviewer | [Contracts Index](contracts/index.md) | [Artifact Contract Hub](contracts/artifacts.md) |

## Canonical Areas

| Area | Path | Purpose |
|---|---|---|
| Agents | [agents/](agents/) | Agent reading order, rules, and navigation |
| Architecture | [architecture/](architecture/) | System context, principles, and boundaries |
| Contracts | [contracts/](contracts/) | Stable cross-repository expectations |
| ADRs | [adr/](adr/) | Accepted architecture decisions |
| Repository mirrors | [repos/](../repos/) | Documentation context for ecosystem repositories |

## Core Repositories

| Repository | Responsibility |
|---|---|
| `victus-docs` | Global architecture, contracts, decisions, planning, and agent-readable documentation |
| `victus-infra` | Infrastructure, networking, storage, secrets, observability, and deployment foundation |
| `victus-processing` | Paper ingestion, PDF/Markdown extraction, chunking, claims extraction, and embeddings |
| `victus-rag` | Retrieval, vector database integration, API orchestration, prompts, and user-facing answers |

## Repository Boundary

`victus-docs` owns global documentation only.

Implementation details and source changes belong in the owning repositories. Content under `repos/**` is synchronized context and should be treated as read-only from this repository.

## Documentation Model

Victus documentation follows four document styles:

| Style | Purpose |
|---|---|
| Architecture | Explain system context, boundaries, tradeoffs, and design intent |
| Contracts | Define stable interfaces, schemas, artifacts, events, and responsibilities |
| Operations | Provide practical commands, runbooks, deployment notes, and debugging flows |
| Agents | Provide explicit reading paths and execution rules for AI agents |

## Current High-Trust Documents

- [Victus Architecture Context](architecture/context.md)
- [Victus Contracts Index](contracts/index.md)
- [Victus Artifact Contract Hub](contracts/artifacts.md)
- [Victus ADR Index](adr/index.md)
- [Victus Agent Entrypoint](agents/entrypoint.md)

## Machine Reading Rules

AI agents must start from:

```txt
docs/agents/entrypoint.md
```

## Governance

Architecture decisions live in `docs/adr/`.

Canonical cross-repository contracts live in `docs/contracts/`.

Repository implementation details remain in the owning repositories.
