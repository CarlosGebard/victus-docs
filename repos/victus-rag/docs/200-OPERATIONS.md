---
id: victus-rag-operations
title: Victus RAG Operations
status: draft
updated_at: 2026-05-26
owners:
  - victus
related_services:
  - qdrant
  - phoenix
  - openai-api
related_docs:
  - docs/000-SYSTEM-CONTEXT.md
  - docs/100-ARCHITECTURE.md
  - docs/300-CONTRACTS.md
  - docs/decisions/
tags:
  - operations
  - cli
  - qdrant
  - telemetry
  - evaluation
---

# Victus RAG Operations

## Operational Overview

`victus-rag` is operated through the `victus-rag` CLI.

Typical operational work includes:

- syncing the Python environment
- starting local services when dense retrieval or telemetry is needed
- building sparse and dense indexes
- running sparse, dense, and hybrid queries
- running local and BEIR evaluations
- generating BEIR-compatible datasets
- inspecting metrics, rankings, traces, and generated artifacts

The system is currently operated as a local CLI workflow. It does not expose a production
service or deployment runtime.

## Runtime Environments

### Local CLI

The primary runtime is a local shell with Python, `uv`, repository files, and optional
Docker Compose services.

Use this environment for:

- sparse indexing and sparse queries
- dense indexing and dense queries
- hybrid queries
- local evaluation
- BEIR evaluation
- synthetic BEIR dataset generation
- telemetry smoke checks

### Local Services

Qdrant is required for:

- dense indexing
- dense queries
- hybrid queries
- dense and hybrid evaluation
- synthetic BEIR multi-relevance query generation

Phoenix is optional and used as an OpenTelemetry collector and trace UI.

### Offline File Runtime

Some workflows rely only on local files:

- sparse indexing from claim JSON or embedded claims Parquet
- sparse queries after the sparse index exists
- local evaluation with an existing sparse index
- artifact inspection

### External API Runtime

Synthetic BEIR single-specificity generation uses the OpenAI API. This path requires
`OPENAI_API_KEY` in the environment or repository `.env`.

## Execution Workflows

### Environment Sync

```bash
uv sync
```

Inspect the CLI:

```bash
uv run victus-rag --help
```

### Sparse Retrieval

Build the sparse index:

```bash
uv run victus-rag index sparse
```

Run a sparse query:

```bash
uv run victus-rag query sparse --query "mediterranean diet metabolic syndrome" --top-k 5
```

### Dense Retrieval

Start Qdrant:

```bash
docker compose up -d qdrant
docker compose ps
```

Index embedded claims into Qdrant:

```bash
uv run victus-rag index qdrant --parquet-path data/claims_embedded.parquet
```

Run a dense query:

```bash
uv run victus-rag query dense --query "mediterranean diet metabolic syndrome" --top-k 5
```

Limit local embedder CPU threads when needed:

```bash
uv run victus-rag query dense \
  --query "mediterranean diet metabolic syndrome" \
  --cpu-threads 4 \
  --cpu-interop-threads 1
```

### Hybrid Retrieval

Hybrid retrieval requires both a sparse index and a populated Qdrant collection.

```bash
uv run victus-rag query hybrid --query "mediterranean diet metabolic syndrome" --top-k 5
```

### Local Evaluation

```bash
uv run victus-rag eval sparse --top-k 5
uv run victus-rag eval dense --top-k 5
uv run victus-rag eval hybrid --top-k 5
```

### Synthetic BEIR Dataset Generation

Generation requires:

- embedded claims Parquet
- `OPENAI_API_KEY`
- Qdrant running and indexed for multi-relevance queries

```bash
uv run victus-rag eval generate-beir --overwrite
```

### BEIR Evaluation

```bash
uv run victus-rag eval sparse-beir
uv run victus-rag eval dense-beir
uv run victus-rag eval hybrid-beir
```

### Claims CSV Export

```bash
uv run victus-rag export claims-csv
```

## Configuration

Runtime configuration is loaded from:

```text
config/default.yaml
```

Synthetic BEIR generation defaults are loaded from:

```text
config/beir_generation.yaml
```

The CLI loads `.env` from the repository root before executing commands.

Required environment variables:

- `OPENAI_API_KEY` for synthetic BEIR single-specificity query generation.

Important runtime configuration areas:

- `paths`: data, index, BEIR, evaluation, and artifact locations.
- `qdrant`: Qdrant URL and collection.
- `dense`: embedded claim/query Parquet locations and vector settings.
- `query_provider`: local, HTTP, or offline Parquet query embedding mode.
- `telemetry`: OTLP endpoint, dataset name, and trace enablement.

Configuration schema details belong in `docs/300-CONTRACTS.md`.

## Observability

### Console Output

CLI commands print runtime results or JSON payloads directly to stdout.

Use help commands to inspect available flags:

```bash
uv run victus-rag query sparse --help
uv run victus-rag query dense --help
uv run victus-rag query hybrid --help
uv run victus-rag eval generate-beir --help
```

### Generated Artifacts

Default artifact root:

```text
artifacts/
```

BEIR metrics and run artifacts are written under:

```text
artifacts/metrics/
artifacts/runs/
```

Generated BEIR datasets are written under:

```text
data/beir/
```

Sparse indexes are written under:

```text
data/indexes/
```

### Telemetry

Start Phoenix:

```bash
docker compose up -d phoenix
docker compose ps
```

Phoenix UI:

```text
http://localhost:6006
```

OTLP gRPC endpoint:

```text
http://localhost:4317
```

Run an audited retrieval query:

```bash
uv run victus-rag query sparse \
  --query "diet metabolic syndrome" \
  --top-k 1 \
  --telemetry \
  --dataset-name claims-v1
```

Expected result:

- CLI returns normal retrieval output.
- Phoenix shows a `rag.query` trace.
- Retrieved document attributes include claim text.

## Validation

Run lightweight validation before handing off changes:

```bash
uv run python -m compileall src
uv run victus-rag --help
uv run victus-rag index qdrant --help
uv run victus-rag query sparse --help
uv run victus-rag query dense --help
uv run victus-rag query hybrid --help
```

There is no committed test suite in the current repository state.

Runtime validation requiring services should only be used when those services are available:

- dense and hybrid retrieval require Qdrant
- telemetry validation requires Phoenix or another OTLP collector
- synthetic BEIR generation requires OpenAI API access

## Failure and Recovery

### Missing Sparse Index

Rebuild the sparse index:

```bash
uv run victus-rag index sparse
```

### Qdrant Unavailable

Inspect local service state:

```bash
docker compose ps
docker compose logs qdrant
```

Restart Qdrant when needed:

```bash
docker compose up -d qdrant
```

### Qdrant Collection Needs Rebuild

Recreate the collection from embedded claims:

```bash
uv run victus-rag index qdrant --parquet-path data/claims_embedded.parquet --recreate
```

### Invalid Embedded Parquet

Validate the configured Parquet contract:

```bash
uv run python -c "from src.config import load_app_config; from src.indexing.parquet_contract import validate_embedded_parquet_schema; c=load_app_config(); validate_embedded_parquet_schema(c.dense.claims_parquet_path, c.parquet_contract)"
```

### Missing Offline Query Embeddings

Use a local or HTTP query provider, or provide the configured query embeddings Parquet file.

The relevant config area is:

```yaml
query_provider:
  mode: LOCAL_SENTENCE_TRANSFORMERS
```

### BEIR Generation Partial Failure

Inspect:

```text
data/beir/<dataset>/generation_status.json
```

If the output directory exists and should be regenerated, rerun with:

```bash
uv run victus-rag eval generate-beir --overwrite
```

### Telemetry Missing In Phoenix

Inspect service state:

```bash
docker compose ps
docker compose logs phoenix
```

Emit a minimal trace:

```bash
uv run victus-rag query sparse --query "diet metabolic syndrome" --top-k 1 --telemetry
```

If running inside a sandboxed environment, local OTLP traffic to `localhost:4317` may be
blocked. Run the audited query from the host shell.

## Troubleshooting

Dependency import failures:

- Run `uv sync`.
- Re-run the failing command through `uv run`.

OpenAI authentication failures:

- Confirm `OPENAI_API_KEY` is present in `.env` or exported in the shell.
- Confirm synthetic BEIR generation is the workflow being executed.

Dense query model load failures:

- Confirm `sentence-transformers` dependencies are installed.
- Use CPU thread limits if local embedding consumes too many resources.
- Switch to `ONLINE_HTTP` or `OFFLINE_PARQUET` query provider when appropriate.

Empty or invalid query failures:

- Provide a non-empty query with usable alphanumeric tokens.

No compatible relevant IDs during evaluation:

- Confirm the evaluation file references claim IDs present in the active sparse index or Qdrant collection.
- Rebuild the required index from the same source dataset used by the evaluation file.

## Operational Boundaries

This document owns:

- runtime workflows
- local service procedures
- validation commands
- configuration usage
- observability procedures
- failure recovery
- troubleshooting guidance

This document does not own:

- system architecture
- stable data/interface contracts
- historical decisions
- implementation walkthroughs
- repository onboarding

## Related Documentation

- `docs/000-SYSTEM-CONTEXT.md` for repository purpose, scope, and vocabulary.
- `docs/100-ARCHITECTURE.md` for system shape and component interaction.
- `docs/300-CONTRACTS.md` for stable interfaces, guarantees, and artifact expectations.
- `docs/runbooks/` for focused operational procedures.
- `docs/decisions/` for architecture and compatibility decisions.
