---
id: victus-rag-architecture
title: Victus RAG Architecture
status: draft
updated_at: 2026-05-26
owners:
  - victus
related_docs:
  - docs/000-SYSTEM-CONTEXT.md
  - docs/200-OPERATIONS.md
  - docs/300-CONTRACTS.md
  - docs/decisions/
related_modules:
  - src/cli.py
  - src/config.py
  - src/retrieval/
  - src/indexing/
  - src/eval/
  - src/telemetry/
tags:
  - retrieval
  - rag
  - evaluation
  - qdrant
---

# Victus RAG Architecture

## Architectural Overview

`victus-rag` is a modular CLI application for retrieval experimentation over scientific
claims.

The system is shaped as a local retrieval and evaluation pipeline. The CLI coordinates
configuration, indexing, retrieval, evaluation, export, and telemetry modules. Persistent
state lives outside the application process in local files, generated artifacts, and Qdrant.

The central architectural unit is the claim. Sparse, dense, and hybrid retrieval paths all
produce ranked claim results that can be queried directly, evaluated locally, evaluated
through BEIR, or emitted as audit telemetry.

```text
CLI
  -> config
  -> indexing / retrieval / evaluation / export / telemetry
  -> local files, artifacts, Qdrant, OpenTelemetry collector
```

## Major Components

### CLI

Path: `src/cli.py`

The CLI owns command parsing and runtime orchestration. It does not own retrieval logic
directly; it dispatches to indexing, retrieval, evaluation, exporter, and telemetry modules.

Inputs:

- command-line arguments
- loaded application configuration
- optional environment values

Outputs:

- console payloads
- generated indexes
- evaluation artifacts
- Qdrant writes
- optional telemetry spans

### Configuration

Paths: `src/config.py`, `config/default.yaml`, `config/beir_generation.yaml`

Configuration defines runtime paths, Qdrant settings, dense retrieval settings, Parquet
column names, query-provider mode, telemetry settings, and synthetic BEIR generation
defaults.

The configuration layer translates YAML into typed application config objects used by the
CLI and downstream modules.

### Sparse Retrieval

Path: `src/retrieval/sparse.py`

Sparse retrieval owns claim loading, local BM25-style index construction, sparse search,
claim serialization, and context matching from available source sections.

Inputs:

- claim JSON files under the configured data directory
- fallback embedded claims Parquet when claim JSON files are unavailable
- optional filtered source context files

Outputs:

- sparse index JSON
- ranked claim results

### Dense Retrieval

Paths: `src/indexing/`, `src/retrieval/dense.py`, `src/retrieval/query_provider.py`

Dense retrieval is split across indexing and querying responsibilities.

Indexing validates embedded Parquet records and upserts claim vectors into Qdrant.
Querying obtains a query vector from the configured query provider and searches the Qdrant
collection.

Query providers are interchangeable:

- local sentence-transformers model
- online HTTP embedding service
- offline query embeddings loaded from Parquet

### Hybrid Retrieval

Path: `src/retrieval/hybrid.py`

Hybrid retrieval composes sparse and dense retrieval results. It expands the candidate pool,
retrieves from both backends, and merges rankings with Reciprocal Rank Fusion.

The hybrid component depends on both the local sparse index and the Qdrant-backed dense
retriever. It owns fusion behavior, not the underlying retrieval backends.

### Evaluation

Paths: `src/eval/`, `src/eval/beir_generation/`

Evaluation has three architectural roles:

- local evaluation over JSON query examples
- BEIR-compatible evaluation adapters and runners
- synthetic BEIR dataset generation

Local evaluation compares ranked claim IDs against relevant claim IDs. BEIR evaluation
adapts sparse, dense, and hybrid retrievers to the BEIR retrieval contract. Synthetic BEIR
generation builds corpus, queries, qrels, manifest, and status files from the claim universe.

### Exporters

Path: `src/exporters/`

Exporters produce derived artifacts from repository data. They are separate from retrieval
and evaluation so export behavior does not become hidden retrieval logic.

### Telemetry

Path: `src/telemetry/`

Telemetry is an optional audit layer for retrieval queries. It wraps retrieval execution
with OpenTelemetry spans and records query metadata plus returned claim documents.

Telemetry does not affect ranking, indexing, evaluation metrics, or generated artifacts.

## System Boundaries

Internal boundaries:

- CLI orchestration is separate from retrieval and evaluation behavior.
- Sparse retrieval is local-file based and independent from Qdrant.
- Dense retrieval depends on Qdrant and a query provider.
- Hybrid retrieval composes sparse and dense outputs without owning either index.
- Evaluation consumes retrievers through search interfaces.
- Telemetry observes retrieval outputs without changing them.

External boundaries:

- Upstream document parsing is outside this repository.
- Upstream claim generation is outside this repository.
- Upstream claim embedding generation is outside this repository.
- Qdrant owns dense vector persistence and vector search execution.
- OpenAI is used only by the synthetic BEIR generation path.
- Phoenix or another OTLP collector owns trace storage and visualization.

## Runtime Flow

### Sparse Query Flow

```text
CLI query sparse
  -> load app config
  -> load sparse index JSON
  -> tokenize query
  -> score indexed claims
  -> return ranked claim results
  -> optionally emit telemetry
```

### Dense Query Flow

```text
CLI query dense
  -> load app config
  -> build query provider
  -> embed query
  -> search Qdrant collection
  -> normalize Qdrant payloads
  -> return ranked claim results
  -> optionally emit telemetry
```

### Hybrid Query Flow

```text
CLI query hybrid
  -> load sparse index
  -> build dense retriever
  -> retrieve sparse candidates
  -> retrieve dense candidates
  -> fuse rankings with RRF
  -> return ranked claim results
  -> optionally emit telemetry
```

### Evaluation Flow

```text
evaluation examples or BEIR dataset
  -> retriever adapter
  -> ranked claim results
  -> metric calculation
  -> metrics, rankings, and failure-analysis artifacts
```

## Artifact and Data Flow

The system moves claim-centered data through distinct stages.

```text
claim JSON / embedded claim Parquet
  -> sparse index JSON
  -> sparse retrieval results
```

```text
embedded claim Parquet
  -> Parquet schema validation
  -> Qdrant collection
  -> dense retrieval results
```

```text
sparse results + dense results
  -> hybrid fusion
  -> hybrid retrieval results
```

```text
embedded claim Parquet + generated queries + qrels
  -> BEIR dataset directory
  -> BEIR evaluation
  -> metrics and analysis artifacts
```

Primary persistence locations:

- `data/claims/` stores claim JSON inputs when available.
- `data/claims_embedded.parquet` stores embedded claim inputs.
- `data/indexes/` stores sparse index artifacts.
- `data/beir/` stores generated BEIR-compatible datasets.
- `artifacts/metrics/` stores evaluation metric payloads.
- `artifacts/runs/` stores rankings and failure-analysis outputs.
- Qdrant stores dense vector points and payloads.

## Quality Attributes

Reproducibility: retrieval and evaluation flows are CLI-driven, config-backed, and artifact-oriented.

Inspectability: generated indexes, datasets, metrics, rankings, manifests, and failure-analysis
files are readable outside the application process.

Modularity: sparse, dense, hybrid, evaluation, export, and telemetry modules have separate
responsibilities and can evolve independently when interfaces remain stable.

Observability: retrieval queries can emit OpenTelemetry spans with query and document-level
audit data.

Recoverability: most local state can be regenerated from source inputs, configuration, and
Qdrant indexing workflows.

Operational simplicity: the architecture relies on local files, a CLI, and a small set of
local services rather than a distributed application runtime.

## External Dependencies

- Qdrant: dense vector storage and vector search.
- OpenAI API: synthetic single-specificity BEIR query generation.
- BEIR: benchmark-compatible retrieval evaluation.
- PyArrow: Parquet schema validation and record loading.
- sentence-transformers: local dense query embedding provider.
- HTTP embedding service: optional external query embedding provider.
- OpenTelemetry OTLP collector: optional retrieval audit trace sink.
- Phoenix: local trace visualization when used as the OTLP collector.
- Docker Compose: local service runtime for Qdrant and Phoenix.

## Documentation Links

- `docs/000-SYSTEM-CONTEXT.md` for repository purpose, scope, vocabulary, and navigation.
- `docs/200-OPERATIONS.md` for operational workflows and validation.
- `docs/300-CONTRACTS.md` for stable CLI, data, telemetry, and artifact expectations.
- `docs/decisions/` for architecture decision records.
