---
id: VICTUS-CONTRACT-PROCESSING-ARTIFACTS
contract_id: victus.processing.artifacts
title: Processing Artifacts
status: draft
version: v1
owner: victus-processing
domain: processing
contract_type: database
stability: experimental
updated_at: 2026-06-09
---

# Processing Artifacts Contract Documentation

## 1. Purpose

Represent any object produced or consumed by the processing pipeline and stored
outside Postgres.

`artifacts` stores references, hashes, types, schemas, and state. It does not
store heavy JSON or binary payloads.

## 2. Identity

### Identity Rules

- Canonical identifier: `artifact_id`
- `artifact_id` is globally unique inside the processing registry.
- `artifact_id` is immutable after creation.
- `storage_uri` locates the external artifact but must not replace
  `artifact_id`.
- `content_hash` identifies artifact content for validation and change
  detection.

### Ownership

`artifacts` is owned by `victus-processing`.

## 3. Schema

### SQL Schema

```sql
CREATE TABLE artifacts (
    artifact_id TEXT PRIMARY KEY,

    paper_id TEXT NOT NULL REFERENCES papers(paper_id),
    pipeline_run_id TEXT REFERENCES pipeline_runs(pipeline_run_id),
    stage_run_id TEXT REFERENCES stage_runs(stage_run_id),

    artifact_type TEXT NOT NULL,

    schema_name TEXT,
    schema_version TEXT,

    storage_uri TEXT NOT NULL,
    content_hash TEXT NOT NULL,

    status TEXT NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    validated_at TIMESTAMPTZ
);
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `artifact_id` | TEXT | Primary identifier for the artifact registry row. |
| `paper_id` | TEXT | Paper associated with the artifact. |
| `pipeline_run_id` | TEXT / NULL | Pipeline run that produced or consumed the artifact. |
| `stage_run_id` | TEXT / NULL | Stage run that produced or consumed the artifact. |
| `artifact_type` | TEXT | Stable artifact type. |
| `schema_name` | TEXT / NULL | Schema name associated with the artifact payload. |
| `schema_version` | TEXT / NULL | Schema version associated with the artifact payload. |
| `storage_uri` | TEXT | External artifact location. |
| `content_hash` | TEXT | Hash of artifact content. |
| `status` | TEXT | Current artifact registry status. |
| `created_at` | TIMESTAMPTZ | Artifact registry creation timestamp. |
| `validated_at` | TIMESTAMPTZ / NULL | Timestamp when the artifact was validated. |

## 5. Responsibilities

### Required Responsibilities

`artifacts` must:

- track externally stored pipeline artifacts
- preserve storage location and content hash
- record artifact type and schema metadata
- link artifacts to paper, pipeline run, and stage run context when available
- support promotion and supersession workflows

### Forbidden Responsibilities

`artifacts` must not store:

- heavy JSON payloads
- binary artifact content
- extracted scientific content inline
- model traces inline
- validation error details

## 6. Validation Rules

- `artifact_id`, `paper_id`, `artifact_type`, `storage_uri`, `content_hash`,
  and `status` are required.
- `paper_id` must reference an existing `papers.paper_id`.
- `pipeline_run_id`, when present, must reference an existing
  `pipeline_runs.pipeline_run_id`.
- `stage_run_id`, when present, must reference an existing
  `stage_runs.stage_run_id`.
- `artifact_type` must be one of the expected types unless the contract is
  extended.
- `status` must be one of the allowed states.
- `validated_at` should be set when `status` is `validated` or `promoted`.

### Expected Artifact Types

- `source_pdf`
- `source_markdown`
- `processed_markdown`
- `markdown_batches`
- `structured_blocks`
- `paper_classification`
- `trimmed_blocks`
- `experiment_map`
- `canonical_evidence_set`
- `evaluation_report`
- `index_payload`
- `langfuse_trace_export`

### Allowed Status Values

- `created`
- `available`
- `validated`
- `promoted`
- `superseded`
- `deprecated`
- `failed_validation`
- `deleted`

## 7. Lifecycle

### Created

Created when an artifact is registered.

### Updated

Updated when the artifact becomes available, validated, promoted, superseded,
deprecated, fails validation, or is deleted.

### Deleted

Logical deletion is represented by `status: deleted`.

### Deprecated

Deprecated when an artifact remains available but should no longer be used for
new processing or consumption.

## 8. Relationships

### Upstream Contracts

- `ProcessingPapers`
- `PipelineRuns`
- `StageRuns`

### Downstream Contracts

- `ProcessingErrors`

### References

- `artifacts.paper_id` -> `papers.paper_id`
- `artifacts.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`
- `artifacts.stage_run_id` -> `stage_runs.stage_run_id`
- `stage_runs.input_artifact_ids[]` -> `artifacts.artifact_id`
- `stage_runs.output_artifact_ids[]` -> `artifacts.artifact_id`

## 9. Operational Notes

Artifact content lives outside Postgres. The registry stores enough metadata to
locate, validate, promote, supersede, or deprecate artifacts.

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable columns, new artifact types, or
new non-breaking status values.

### Major

Breaking schema changes, identity changes, artifact type meaning changes, status
meaning changes, or field removals.
