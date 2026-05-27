---
id: VICTUS-CONTRACT-ARTIFACTS
title: Victus Artifact Contract Hub
status: active
updated_at: 2026-05-27
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
| PDF Source | Source Artifact | stable input concept | `victus-docs` | [Processing Data Layout](../../repos/victus-processing/docs/contracts/data-layout.md) |
| Normalized Paper | Intermediate Artifact | candidate contract | `victus-docs` | [Processing Architecture](../../repos/victus-processing/docs/100-ARCHITECTURE.md) |
| Markdown Document | Intermediate Artifact | candidate contract | `victus-docs` | [Processing Data Layout](../../repos/victus-processing/docs/contracts/data-layout.md) |
| Section Block | Intermediate Artifact | internal | owning repository | [Processing Architecture](../../repos/victus-processing/docs/100-ARCHITECTURE.md) |
| Chunk | Contract Artifact | stable shared artifact | `victus-docs` | [Processing Contracts](../../repos/victus-processing/docs/300-CONTRACTS.md) |
| Claim | Contract Artifact | stable shared artifact | `victus-docs` | [Processing Contracts](../../repos/victus-processing/docs/300-CONTRACTS.md), [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) |
| Embedding | Contract Artifact | stable shared artifact | `victus-docs` | [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) |
| Retrieval Result | Contract Artifact | stable shared artifact | `victus-docs` | [RAG Contracts](../../repos/victus-rag/docs/300-CONTRACTS.md) |
| User Answer | Product Artifact | stable output concept | `victus-docs` | pending |

## Stability Rules

- `Section Block` is an internal intermediate artifact.
- `Chunk` is a stable retrieval artifact shared across repositories.
- Shared artifacts require stable identifiers.
- Artifact IDs must remain stable across migrations.
- Artifact versioning belongs in metadata, not in the semantic ID.

Correct:

```yaml
id: VICTUS-ARTIFACT-CLAIM
version: 1
```

Avoid:

```txt
VICTUS-ARTIFACT-CLAIM-V1
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
