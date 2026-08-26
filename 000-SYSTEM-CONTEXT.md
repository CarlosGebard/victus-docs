---
id: VICTUS-MOC-000-SYSTEM-CONTEXT
title: Victus System Context
status: active
updated_at: 2026-06-09
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags: moc, system-context, navigation
---

# 000 - System Context

Victus is a modular scientific knowledge platform for nutrition and food-related health evidence.

This repository is the documentation control plane for the Victus ecosystem. It owns global architecture, shared contracts, architecture decisions, and AI-agent navigation.

## Documentation Convention

Victus documentation follows a hybrid Hub-and-Node model:

```txt
000-SYSTEM-CONTEXT.md
100-ARCHITECTURE.md
200-OPERATIONS.md
300-CONTRACTS.md
decisions/
```

The numbered files are Maps of Content. Detailed documents remain in their owning folders and are linked from these hubs.

## Start Here

| Reader | First document | Next document |
|---|---|---|
| Human | [README.md](/README) | [100-ARCHITECTURE.md](/100-ARCHITECTURE) |
| AI agent | [AGENTS.md](/AGENTS) | [100-ARCHITECTURE.md](/100-ARCHITECTURE) |
| Architecture reviewer | [100-ARCHITECTURE.md](/100-ARCHITECTURE) | [decisions/](decisions/) |
| Contract reviewer | [300-CONTRACTS.md](/300-CONTRACTS) | [docs/contracts/artifacts.md](/docs/contracts/artifacts) |

## System Scope

Victus is organized around:

- scientific paper ingestion
- Markdown extraction and normalization
- structured block generation
- canonical evidence extraction
- embeddings and retrieval
- deterministic RAG
- traceable scientific reasoning
- agent-readable documentation

## Repository Boundaries

| Repository | Responsibility |
|---|---|
| `victus-docs` | Global documentation, contracts, ADRs, and agent-readable navigation |
| `victus-infra` | Infrastructure, networking, storage, secrets, observability, and deployment foundation |
| `victus-processing` | Paper ingestion, extraction, structured blocks, canonical evidence, and embeddings |
| `victus-rag` | Retrieval, vector database integration, API orchestration, prompts, and answers |

Implementation details and source changes belong in the owning repositories.

## Repository Jumps

Agents can use synchronized repository documentation as read-only context:

| Repository | Mirror entrypoint | System context | Architecture | Operations | Contracts |
|---|---|---|---|---|---|
| `victus-infra` | [README](/repos/victus-infra/README) | [000](/repos/victus-infra/docs/000-SYSTEM-CONTEXT) | [100](/repos/victus-infra/docs/100-ARCHITECTURE) | [200](/repos/victus-infra/docs/200-OPERATIONS) | [300](/repos/victus-infra/docs/300-CONTRACTS) |
| `victus-processing` | [README](/repos/victus-processing/README) | [000](/repos/victus-processing/docs/000-SYSTEM-CONTEXT) | [100](/repos/victus-processing/docs/100-ARCHITECTURE) | [200](/repos/victus-processing/docs/200-OPERATIONS) | [300](/repos/victus-processing/docs/300-CONTRACTS) |
| `victus-rag` | [README](/repos/victus-rag/README) | [000](/repos/victus-rag/docs/000-SYSTEM-CONTEXT) | [100](/repos/victus-rag/docs/100-ARCHITECTURE) | [200](/repos/victus-rag/docs/200-OPERATIONS) | [300](/repos/victus-rag/docs/300-CONTRACTS) |

These mirrors are navigation and context only. Changes must happen in the owning repository.

## Canonical Nodes

- [Architecture MoC](/100-ARCHITECTURE)
- [Operations MoC](/200-OPERATIONS)
- [Contracts MoC](/300-CONTRACTS)
- [Artifact contract hub](/docs/contracts/artifacts)
- [Repository documentation contract](/docs/contracts/repository-documentation-contract)
- [ADR index](/docs/adr/index)
