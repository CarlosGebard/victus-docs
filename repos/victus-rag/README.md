# victus-rag

[Español](docs/localization/README.es.md)

Retrieval experimentation CLI for scientific claims.

`victus-rag` is a CLI-first RAG retrieval lab for indexing, querying, and evaluating
sparse, dense, and hybrid retrieval strategies. It does not generate final answers; it
focuses on retrieval behavior, metrics, auditability, and local artifacts.

## Quick Start

```bash
uv sync
uv run victus-rag --help
uv run victus-rag index sparse
uv run victus-rag query sparse --query "mediterranean diet metabolic syndrome" --top-k 5
```

Dense retrieval requires Qdrant and embedded claim vectors:

```bash
docker compose up -d qdrant
uv run victus-rag index qdrant --parquet-path data/claims_embedded.parquet
uv run victus-rag query dense --query "mediterranean diet metabolic syndrome" --top-k 5
```

## Validation

```bash
uv run python -m compileall src
uv run victus-rag --help
uv run victus-rag index qdrant --help
```

## Documentation

- [System Context](docs/000-SYSTEM-CONTEXT.md)
- [Architecture](docs/100-ARCHITECTURE.md)
- [Operations](docs/200-OPERATIONS.md)
- [Contracts](docs/300-CONTRACTS.md)
- [Decisions](docs/decisions/)
- [Runbooks](docs/runbooks/)

## Responsibilities

This repository owns:

- sparse, dense, and hybrid retrieval workflows
- claim-level indexing and querying
- local and BEIR-compatible evaluation
- retrieval metrics, rankings, failure-analysis artifacts, and optional telemetry
- CLI configuration for local execution

This repository does not own:

- PDF parsing or upstream document ingestion
- upstream claim generation
- corpus embedding generation or model training
- production serving or deployment orchestration
- final answer generation
