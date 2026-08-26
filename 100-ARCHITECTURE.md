---
id: VICTUS-MOC-100-ARCHITECTURE
title: Victus Architecture
status: active
updated_at: 2026-06-09
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags: moc, architecture, navigation
---

# 100 - Architecture

This Map of Content routes architecture readers to the current high-trust architecture documents for Victus.

## Architecture Authority

`victus-docs` is the architecture authority for cross-repository system context, boundaries, and governance.

Repository-local implementation architecture belongs in the owning repository.

## Core Architecture Documents

| Document | Purpose |
|---|---|
| [System Context](/000-SYSTEM-CONTEXT) | Ecosystem scope, documentation convention, and repository boundaries |
| [Artifact Contract Hub](/docs/contracts/artifacts) | Canonical artifact graph and artifact governance |
| [AGENTS.md](/AGENTS) | AI-agent reading order and execution rules |

## Architecture Principles

Victus prioritizes:

- deterministic systems
- explicit contracts
- traceable reasoning
- modular ownership
- low hidden context
- reproducible behavior

## Artifact Flow

```txt
Paper
-> StructuredBlock
-> ExperimentMap
-> CanonicalEvidence
-> Embedding
-> Retrieval
-> Agent Reasoning
-> User Answer
```

The detailed artifact contract lives in
[docs/contracts/artifacts.md](/docs/contracts/artifacts).

## Decision Links

Architecture decisions are indexed from [decisions/](decisions/) and currently stored under [docs/adr/](docs/adr/).

Breaking architecture changes require:

- ADR
- affected contract update
- owning repository implementation update
- migration notes when persisted data or downstream consumers are affected
