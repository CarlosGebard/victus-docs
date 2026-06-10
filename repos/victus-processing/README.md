# victus-processing

Local paper-processing pipeline for the Victus ecosystem.

This repository turns scientific-paper inputs into metadata, normalized PDFs,
structured PDF-processing artifacts, and canonical evidence outputs. It owns the local
processing workflow and the `data/` artifact layout used between stages.

[Español](01-Projects/victus/victus-docs/repos/victus-processing/docs/README.es.md)

## Quick Start

Prerequisites:

- Python 3.12
- `uv`
- API keys for the stages you plan to run

Install and inspect the CLI:

```bash
uv sync
uv run victus-processing --help
```

Create the local data layout:

```bash
uv run victus-processing data-layout create
```

Run the main local flow:

```bash
uv run victus-processing metadata-extraction explore --mode broad-nutrition
uv run victus-processing metadata-to-pdf normalize-pdfs
uv run victus-processing pdf-processing run
uv run victus-processing evidence-extraction run
```

## Validate

```bash
uv run pytest tests/test_cli_smoke.py -q
```

## Documentation

- [System Context](01-Projects/victus/victus-docs/repos/victus-processing/docs/000-SYSTEM-CONTEXT.md)
- [Architecture](01-Projects/victus/victus-docs/repos/victus-processing/docs/100-ARCHITECTURE.md)
- [Contracts](01-Projects/victus/victus-docs/repos/victus-processing/docs/300-CONTRACTS.md)
- [Operations](01-Projects/victus/victus-docs/repos/victus-processing/docs/200-OPERATIONS.md)
- [CLI](01-Projects/victus/victus-docs/repos/victus-processing/docs/operations/cli.md)
- [Runbooks](docs/operations/runbooks/)

## Responsibilities

This repository owns:

- local paper-processing CLI commands;
- metadata discovery and candidate state;
- PDF normalization into active processing inputs;
- Docling/LLM PDF processing artifacts;
- LLM canonical evidence extraction outputs via LiteLLM;
- local runtime contracts under `data/`.

This repository does not cover:

- analytics products;
- RAG indexing or vector stores;
- production deployment infrastructure;
- external PDF retrieval services;
- external API availability, billing, or model behavior.
