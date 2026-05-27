---
id: VICTUS-ARCH-CONTEXT
title: Victus Architecture Context
status: draft
updated_at: 2026-05-26
owners:
  - architecture
audience:
  - humans
  - ai-agents
related_docs:
  - ../contracts/index.md
  - ../contracts/artifacts.md
  - ../adr/index.md
tags:
  - architecture
  - context
  - governance
---

# Victus Architecture Context

Victus is a modular scientific knowledge platform for nutrition and food-related health evidence.

The system direction is:

- ingestion of scientific papers
- extraction of structured claims
- embeddings and retrieval
- deterministic RAG
- traceable scientific reasoning
- AI-agent-readable architecture

## Architecture Principles

Victus prioritizes:

- deterministic systems
- explicit contracts
- traceable reasoning
- modular ownership
- low hidden context
- reproducible behavior

Victus avoids:

- opaque automation
- hidden assumptions
- architecture drift
- undocumented behavior
- source edits across repository boundaries

## Documentation as Architecture

The documentation system is a first-class architecture layer.

`victus-docs` acts as:

- canonical documentation control plane
- architecture authority
- contract authority
- AI-agent navigation root

Source code changes must happen in the owning repositories, not from `victus-docs`.

## Repository Model

Victus is a multi-repository ecosystem.

Known repository roles:

| Repository | Role |
|---|---|
| `victus-docs` | Global architecture, contracts, ADRs, and agent-readable navigation |
| `victus-infra` | Infrastructure foundation |
| `victus-processing` | Scientific document processing pipeline |
| `victus-rag` | Retrieval and answer-generation layer |

Implementation details for non-documentation repositories are intentionally not documented here until repository mirrors are added.

## Artifact Flow

The high-level artifact graph is:

```txt
PDF Source
-> Normalized Paper
-> Markdown Document
-> Section Block
-> Chunk
-> Claim
-> Embedding
-> Retrieval Result
-> User Answer
```

The canonical artifact contract hub is [Victus Artifact Contract Hub](../contracts/artifacts.md).

## Decision Governance

Architecture decisions live in `docs/adr/`.

Breaking changes to shared architecture or artifacts require:

- ADR
- contract update
- implementation update in the owning repository
- migration notes when persisted data or downstream consumers are affected

## Agent Governance

AI agents are first-class consumers of Victus documentation.

Agents must:

- start from `docs/agents/entrypoint.md`
- prefer explicit docs over assumptions
- use contracts over implementation details
- ask for missing decisions instead of inventing behavior
- respect repository boundaries
