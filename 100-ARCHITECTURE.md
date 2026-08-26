---
id: VICTUS-MOC-100-ARCHITECTURE
title: Victus Architecture
status: active
updated_at: 2026-08-25
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags:
  - moc
  - architecture
  - navigation
---

# 100 - Architecture

This Map of Content routes architecture readers to the current high-trust architecture documents for Victus.

## Architecture Authority

`victus-docs` is the architecture authority for cross-repository system context, boundaries, and governance.

Repository-local implementation architecture belongs in the owning repository.

## Core Architecture Documents

| Document | Purpose |
|---|---|
| [System Context](000-SYSTEM-CONTEXT.md) | Ecosystem scope, documentation convention, and repository boundaries |
| [Artifact Contract Hub](docs/contracts/artifacts.md) | Canonical artifact graph and artifact governance |
| [AGENTS.md](AGENTS.md) | AI-agent reading order and execution rules |

## Architecture Principles

Victus prioritizes:

- deterministic systems
- explicit contracts
- traceable reasoning
- modular ownership
- low hidden context
- reproducible behavior

## Documentation Flow

Documentation has one authoring path and one backup path:

```txt
Wiki.js (authoring authority)
-> Git target / wiki-production (one-way versioned backup)
```

Wiki.js owns documentation mutations. The Git target is not imported back into
Wiki.js, so there is no competing source of truth or Git merge path in the
publishing architecture.

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
[docs/contracts/artifacts.md](docs/contracts/artifacts.md).

## Decision Links

Architecture decisions are indexed from [decisions/](decisions/) and currently stored under [docs/adr/](docs/adr/).

Breaking architecture changes require:

- ADR
- affected contract update
- owning repository implementation update
- migration notes when persisted data or downstream consumers are affected

The documentation authority decision is recorded in
[VICTUS-ADR-003](docs/adr/VICTUS-ADR-003-wikijs-authoring-and-git-backup.md).
