---
id: victus-rag-contracts
title: Victus RAG Contracts
status: draft
updated_at: 2026-05-26
owners:
  - victus
related_components:
  - src/cli.py
  - src/config.py
  - src/indexing/
  - src/retrieval/
  - src/eval/
  - src/telemetry/
related_docs:
  - docs/000-SYSTEM-CONTEXT.md
  - docs/100-ARCHITECTURE.md
  - docs/200-OPERATIONS.md
  - docs/decisions/
tags:
  - contracts
  - retrieval
  - parquet
  - qdrant
  - beir
---

# Victus RAG Contracts

## Purpose

This document defines stable system guarantees for `victus-rag`.

These contracts govern the interfaces and artifacts that retrieval, indexing, evaluation,
telemetry, and generated datasets depend on. Future changes should preserve these
guarantees or explicitly document a compatibility break.

## Scope

Covered contracts:

- CLI command surface
- application configuration shape
- embedded Parquet inputs
- Qdrant point payloads
- retrieval result payloads
- local evaluation input and output expectations
- BEIR dataset generation artifacts
- BEIR evaluation artifacts
- retrieval telemetry attributes
- failure behavior for validation and missing dependencies

Out of scope:

- upstream PDF parsing contracts
- upstream claim extraction contracts
- upstream corpus embedding generation contracts
- production API contracts
- answer-generation contracts

## Global Guarantees

- The claim is the primary retrieval unit.
- Claim identifiers must remain stable across indexing, retrieval, evaluation, BEIR data,
  Qdrant payloads, and telemetry.
- Sparse, dense, and hybrid retrieval must return ranked claim results.
- Retrieval commands must not generate final natural-language answers.
- Evaluation must compare retrieved claim IDs against relevant claim IDs.
- Generated artifacts must be inspectable as local files.
- Optional telemetry must observe retrieval output without changing ranking behavior.

## CLI Contract

The repository exposes the `victus-rag` CLI entrypoint.

Stable top-level command groups:

- `index`
- `query`
- `eval`
- `export`

Stable retrieval modes:

- `query sparse`
- `query dense`
- `query hybrid`

Stable indexing modes:

- `index sparse`
- `index qdrant`

Stable evaluation modes:

- `eval sparse`
- `eval dense`
- `eval hybrid`
- `eval generate-beir`
- `eval sparse-beir`
- `eval dense-beir`
- `eval hybrid-beir`

Stable export mode:

- `export claims-csv`

The CLI may add flags or commands over time. Existing command names should not be renamed
without an explicit compatibility decision.

## Configuration Contract

Default application configuration lives at:

```text
config/default.yaml
```

Synthetic BEIR generation configuration lives at:

```text
config/beir_generation.yaml
```

Stable top-level configuration sections:

- `paths`
- `qdrant`
- `dense`
- `parquet_contract`
- `query_provider`
- `telemetry`

Stable BEIR generation keys:

- `output_dir`
- `total_queries`
- `single_specificity_count`
- `multi_relevance_count`
- `seed`
- `split`
- `openai_model`
- `llm_temperature`
- `llm_claim_batch_size`
- `single_prompt_file`

Configuration values may be overridden by CLI flags where supported. YAML sections must be
objects/mappings when present.

## Embedded Parquet Contract

Embedded claim Parquet files must contain the configured id, text, and embedding columns.

Default claim columns:

- `claim_id`: string or large string
- `claim_text`: string or large string
- `embedding`: list of float32 or float64 values

Optional metadata behavior:

- If `metadata_column` is configured, that column must be a struct.
- If `metadata_column` is empty, all non-id, non-text, and non-embedding columns are copied
  into metadata.

Record-level invariants:

- Each emitted record must have a non-empty embedding.
- Embedding values are converted to floats before indexing.
- Dense indexing requires all embeddings in a Qdrant collection load to have the same vector
  dimension.

## Qdrant Payload Contract

Dense indexing writes one Qdrant point per embedded claim record.

Point ID guarantee:

- The Qdrant point ID is a deterministic UUIDv5 derived from the external claim ID.

Payload guarantees:

- `external_id` identifies the claim.
- `claim_text` stores the claim text.
- `source_path` is present and defaults to `source_file` or an empty string.
- `source_locator` is present and defaults to the external claim ID.
- `paper_id` is present and is derived from existing payload metadata, the claim ID, or a
  document identifier fallback.
- Additional metadata fields from the Parquet record may be preserved in the payload.

Dense retrieval must be able to normalize legacy payloads that contain enough information
to recover an `external_id`.

## Retrieval Result Contract

Retrieval payloads must include:

- `query`
- `top_k`
- `result_count`
- `results`

Each result must include:

- `rank`
- `score`
- `external_id`
- `unit_type`
- `paper_id`
- `source_path`
- `source_locator`
- `snippet`
- `claim_text`
- `metadata`

Sparse and hybrid results include grounding data when available:

- `support_section`
- `evidence_span`
- `context_matches`

Sparse results include matched-term explanations.

Dense results include the backend collection and query-provider context in the parent
payload.

Hybrid results include component scores and ranks for sparse and dense sources.

Invariants:

- `unit_type` for retrieval results is `claim`.
- `rank` is one-based.
- `result_count` reflects the number of returned results.
- `external_id` is the primary identifier used by evaluation and telemetry.

## Local Evaluation Contract

Local evaluation input is JSON loaded from the configured evaluation path.

Accepted query fields:

- query ID: `query_id` or `id`
- query text: `query` or `query_text`
- relevant IDs: `relevant_doc_ids` or `relevant_ids`

Evaluation examples may include:

- `category`
- `difficulty`
- `metadata`

Relevant IDs are canonicalized when they use supported claim identifier forms.

Local evaluation output includes:

- evaluation type
- `top_k`
- query count
- hit rate at k
- mean recall at k
- MRR at k
- per-query retrieved and relevant IDs

Invariant:

- Every evaluated query must have at least one relevant claim ID compatible with the indexed
  retrieval backend.

## Synthetic BEIR Dataset Contract

Synthetic BEIR generation produces a BEIR-compatible dataset directory.

Required files:

- `corpus.jsonl`
- `queries.jsonl`
- `qrels/<split>.tsv`
- `manifest.json`
- `generation_status.json`

Corpus rows must contain:

- `_id`
- `title`
- `text`
- `metadata`

Query rows must contain:

- `_id`
- `text`

Qrels must be tab-separated and include the header:

```text
query-id	corpus-id	score
```

Generation invariants:

- `single_specificity_count + multi_relevance_count` must equal `total_queries`.
- Single-specificity generation must produce exactly one query per sampled claim.
- Generated single-specificity target IDs must exactly match the sampled claim IDs.
- Multi-relevance generation writes three qrels per query.
- Dense retrieval IDs used for multi-relevance qrels must exist in the corpus.
- Existing non-empty output directories must not be overwritten unless overwrite behavior is
  explicitly requested.

Current configured defaults:

- `total_queries`: 187
- `single_specificity_count`: 180
- `multi_relevance_count`: 7
- `split`: `test`
- `openai_model`: `gpt-5-mini-2025-08-07`
- `llm_claim_batch_size`: 30

## BEIR Evaluation Artifact Contract

BEIR evaluation writes metrics and optional run artifacts under the configured artifacts
directory.

Stable artifact families:

- `artifacts/metrics/`
- `artifacts/runs/`

Metrics payloads include:

- evaluation type
- BEIR directory
- split
- k values
- query count
- corpus size
- metrics for nDCG, MAP, recall, precision, and MRR

Optional run artifacts:

- rankings JSON
- failure-analysis JSONL

Failure-analysis rows include:

- query ID
- query text
- relevant document IDs
- top retrieved document IDs
- scored top retrieved records
- first relevant rank when found

## Telemetry Contract

Retrieval telemetry is optional.

When enabled, retrieval commands emit an OpenTelemetry span named:

```text
rag.query
```

Required span attributes:

- `app.pipeline_stage`
- `dataset.name`
- `user.query.length_words`
- `input.value`
- `openinference.span.kind`
- `retrieval.backend`
- `retrieval.top_k`
- `retrieval.result_count`

Optional backend attributes:

- `retrieval.collection`
- `retrieval.query_provider`
- `retrieval.dense_model_name`

Retrieved document attributes use indexed document keys:

```text
retrieval.documents.<index>.document.rank
retrieval.documents.<index>.document.score
retrieval.documents.<index>.document.id
retrieval.documents.<index>.document.content
retrieval.documents.<index>.document.source_locator
retrieval.documents.<index>.document.metadata
retrieval.documents.<index>.document.grounding
```

Telemetry invariants:

- Telemetry must not change retrieval ranking or result payloads.
- The number of recorded documents is capped by `telemetry.max_documents`.
- `document.content` records claim text for auditability.

## Failure Expectations

Validation failures should fail fast with explicit messages.

Expected failure categories:

- missing required Parquet file
- missing required Parquet columns
- invalid Parquet column types
- empty embeddings
- inconsistent embedding dimensions
- unsupported Qdrant distance
- unavailable Qdrant during dense operations
- missing sparse index during sparse or hybrid operations
- empty or untokenizable queries
- missing local dependencies such as PyArrow, BEIR, OpenTelemetry, OpenAI, or sentence-transformers
- invalid BEIR generation counts
- LLM responses whose generated target IDs do not match sampled claim IDs
- non-empty BEIR output directory without explicit overwrite behavior

Partial BEIR generation writes `generation_status.json` with failure context when generation
fails after the writer has been initialized.

## Compatibility Expectations

Future changes should preserve:

- existing CLI command names
- claim-level retrieval as the primary unit
- stable `external_id` usage across components
- embedded Parquet id/text/embedding semantics
- Qdrant payload recoverability for `external_id` and `claim_text`
- retrieval result fields used by evaluation and telemetry
- BEIR-compatible output file names and qrels layout
- telemetry span name and core retrieval attributes

Any change that breaks these expectations should be treated as a compatibility break and
recorded in `docs/decisions/`.

## Related Documents

- `docs/000-SYSTEM-CONTEXT.md` for repository purpose, scope, and vocabulary.
- `docs/100-ARCHITECTURE.md` for system shape and component interaction.
- `docs/200-OPERATIONS.md` for operational workflows and validation.
- `docs/decisions/` for compatibility-breaking or architecture-level decisions.
