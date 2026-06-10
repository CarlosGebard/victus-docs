---
id: VICTUS-CONTRACT-ARTIFACTS
title: Victus Artifact Contract Hub
status: active
updated_at: 2026-06-09
owners:
  - architecture
audience:
  - humans
  - ai-agents
related_docs:
  - ../../100-ARCHITECTURE.md
  - ../adr/VICTUS-ADR-001-documentation-control-plane.md
tags:
  - contracts
  - artifacts
  - governance
---

# Victus Artifact Contract Hub

This document defines the canonical artifact graph and governance rules for Victus.

Artifact-specific implementation details live in the owning repositories. This file acts as the central contract hub and links to repository-local contract documents mirrored under `repos/`.

## Artifact Graph

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

## Artifact Classes

| Class | Purpose |
|---|---|
| Source Artifact | External or original input accepted by Victus |
| Intermediate Artifact | Internal transformation product |
| Contract Artifact | Stable artifact shared across repositories |
| Product Artifact | User-facing or API-facing output |

## Canonical Artifacts

| Artifact | Class | Stability | Canonical owner | Repository-local details |
|---|---|---|---|---|
| Paper | Contract Artifact | active foundation | `victus-docs` | [Paper](scientific/paper.md) |
| StructuredBlock | Contract Artifact | active foundation | `victus-docs` | [StructuredBlock](scientific/structured-block.md) |
| ExperimentMap | Contract Artifact | draft | `victus-docs` | [ExperimentMap](scientific/experiment-map.md) |
| CanonicalEvidence | Contract Artifact | draft | `victus-docs` | [CanonicalEvidence](scientific/canonical-evidence.md) |
| Embedding | Contract Artifact | stable shared artifact | `victus-docs` | [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) |
| Retrieval | Contract Artifact | stable shared artifact | `victus-docs` | [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) |
| User Answer | Product Artifact | stable output concept | `victus-docs` | pending |

## Stability Rules

- `StructuredBlock` replaces legacy `Section Block` terminology.
- `CanonicalEvidence` replaces the previous `Claim` contract concept.
- Victus does not define `Claim` as a system contract.
- `paper.md`, `paper.processed.json`, and `paper.final.json` are operational
  pipeline artifacts, not canonical scientific contracts.
- `paper.final.json` may be a repository-local implementation of
  `StructuredBlock[]`.
- Shared artifacts require stable identifiers.
- Artifact IDs must remain stable across migrations.
- Artifact versioning belongs in metadata, not in the semantic ID.

Correct:

```yaml
id: VICTUS-ARTIFACT-CANONICAL-EVIDENCE
version: 1
```

Avoid:

```txt
VICTUS-ARTIFACT-CANONICAL-EVIDENCE-V1
```

## Governance

Canonical artifact contracts live in `victus-docs/docs/contracts/`.

Implementation details live in the owning repositories.

Breaking artifact changes require:

- ADR
- contract update
- implementation update in owning repositories
- migration notes when persisted data or downstream consumers are affected

## Repository Contract Links

| Repository | Contract document | Contract scope |
|---|---|---|
| `victus-processing` | [Processing Contracts](../../repos/victus-processing/docs/300-CONTRACTS.md) | processing artifacts, paths, identities, stage handoffs |
| `victus-processing` | [Processing Data Layout](../../repos/victus-processing/docs/contracts/data-layout.md) | local runtime artifact layout and stage outputs |
| `victus-rag` | [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) | embedded Parquet inputs, Qdrant payloads, retrieval results, BEIR/evaluation artifacts |

## Known Gaps

The `User Answer` artifact does not yet have a repository-local contract mirror.
