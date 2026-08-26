---
id: victus-rag-system-context
title: Victus RAG System Context
status: draft
updated_at: 2026-05-26
owners:
  - victus
---

# Victus RAG System Context

## Purpose

`victus-rag` is a CLI-first retrieval laboratory for scientific claims.

The repository exists to build, query, evaluate, and audit retrieval behavior across
sparse, dense, and hybrid retrieval strategies. It focuses on retrieval quality,
evaluation datasets, ranking artifacts, and operationally inspectable outputs.

It does not generate final answers. Its system role is to provide a controlled retrieval
layer that can be measured before it is connected to downstream answer-generation systems.

## System Goals

- Support reproducible retrieval experiments over scientific claims.
- Keep sparse, dense, and hybrid retrieval paths explicit and independently testable.
- Treat data contracts and artifact outputs as stable system boundaries.
- Prefer CLI workflows that can be run locally and inspected directly.
- Make evaluation behavior auditable through local metrics, BEIR-compatible datasets,
  ranking artifacts, and optional telemetry traces.
- Keep infrastructure simple: local files for artifacts, Qdrant for vector search,
  and Docker Compose for local services.

## Non-Goals

- This repository does not own PDF parsing or source document ingestion.
- This repository does not own embedding model training.
- This repository does not serve a production API.
- This repository does not generate natural-language answers.
- This repository does not orchestrate production deployments.

## Repository Scope

`victus-rag` owns:

- claim-level sparse indexing from JSON or Parquet inputs
- dense claim indexing into Qdrant from embedded Parquet inputs
- dense query embedding through local, HTTP, or offline Parquet providers
- hybrid retrieval through reciprocal rank fusion
- local retrieval evaluation over JSON query sets
- BEIR-compatible synthetic dataset generation and BEIR evaluation
- retrieval artifacts such as metrics, rankings, and failure-analysis files
- optional OpenTelemetry retrieval audit traces
- CLI commands and configuration for the workflows above

Out of scope:

- upstream document extraction
- upstream claim generation
- upstream embedding generation for the claim corpus
- production serving and user-facing applications
- answer synthesis, citation formatting, or LLM response generation

## Documentation Map

This repository uses a Hub-and-Node Markdown structure with top-level Maps of Content.

```text
docs/
├── 000-SYSTEM-CONTEXT.md  -> repository purpose, scope, vocabulary, navigation
├── 100-ARCHITECTURE.md    -> system shape, components, runtime/data flows
├── 200-OPERATIONS.md      -> local operations, validation, runbooks, troubleshooting
├── 300-CONTRACTS.md       -> stable interfaces, data guarantees, artifact expectations
└── decisions/             -> architecture decision records
```

Planned supporting areas:

- `docs/retrieval/` for sparse, dense, and hybrid retrieval modules.
- `docs/evaluation/` for local evaluation, BEIR, and synthetic dataset generation.
- `docs/runbooks/` for operational procedures.
- `docs/decisions/` for architecture decision records.

## Core Concepts

- Claim: the primary retrieval unit. A claim is an atomic scientific statement with a stable identifier and text.
- Sparse retrieval: local BM25-style search over claim text.
- Dense retrieval: vector search over embedded claims stored in Qdrant.
- Hybrid retrieval: Reciprocal Rank Fusion over sparse and dense result sets.
- Query provider: the component that produces dense vectors for user or evaluation queries.
- Parquet contract: the configured schema expected for embedded claim or query data.
- BEIR dataset: a benchmark-compatible corpus, query set, and qrels directory used for retrieval evaluation.
- Artifact: a generated output such as sparse indexes, metrics, rankings, failure-analysis files, or BEIR datasets.
- Telemetry trace: optional OpenTelemetry span data emitted during retrieval for audit and inspection.

## Repository Structure

```text
src/        -> CLI and application code
config/     -> runtime and generation configuration
docs/       -> system documentation
data/       -> local input data and generated retrieval datasets
artifacts/  -> generated metrics, rankings, and analysis outputs
```

Important code areas:

```text
src/retrieval/             -> sparse, dense, hybrid, and query-provider logic
src/indexing/              -> Parquet validation and Qdrant upsert
src/eval/                  -> local and BEIR evaluation
src/eval/beir_generation/  -> synthetic BEIR dataset generation
src/exporters/             -> derived data exports
src/telemetry/             -> optional OTLP retrieval tracing
```

## Design Principles

- Retrieval first: measure retrieval behavior before adding answer generation.
- Explicit contracts: data schemas, payloads, and artifact expectations should be documented.
- Small workflows: CLI commands should remain understandable and independently runnable.
- Local reproducibility: default workflows should run from local config, local files, and local services.
- Auditable outputs: evaluations should produce inspectable artifacts, not only console summaries.
- Stable identifiers: claim IDs and document IDs must remain consistent across indexing, retrieval, and evaluation.
- Clear boundaries: upstream data preparation and downstream answer generation stay outside this repository.
- Agent-friendly navigation: documentation should help humans and AI agents find the right deeper document quickly.

## Reading Path

Start here to understand the repository boundary and vocabulary.

Then read:

1. `docs/100-ARCHITECTURE.md` for component and flow structure.
2. `docs/300-CONTRACTS.md` for stable data and interface guarantees.
3. `docs/200-OPERATIONS.md` and `docs/runbooks/` for execution and troubleshooting.
4. `docs/decisions/` for architectural reasoning.
