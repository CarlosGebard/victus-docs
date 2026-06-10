---
id: VICTUS-CONTRACT-PROCESSING-ERRORS
contract_id: victus.processing.processing_errors
title: Processing Errors
status: draft
version: v1
owner: victus-processing
domain: processing
contract_type: database
stability: experimental
updated_at: 2026-06-09
---

# Processing Errors Contract Documentation

## 1. Purpose

Represent traceable processing pipeline errors.

`processing_errors` allows failures to be audited without overloading
`stage_runs`. `stage_runs.error_id` points to the primary error for a failed or
blocked stage.

## 2. Identity

### Identity Rules

- Canonical identifier: `error_id`
- `error_id` is globally unique inside the processing registry.
- `error_id` is immutable after creation.
- Errors may reference paper, pipeline run, and stage run context when known.

### Ownership

`processing_errors` is owned by `victus-processing`.

## 3. Schema

### SQL Schema

```sql
CREATE TABLE processing_errors (
    error_id TEXT PRIMARY KEY,

    paper_id TEXT REFERENCES papers(paper_id),
    pipeline_run_id TEXT REFERENCES pipeline_runs(pipeline_run_id),
    stage_run_id TEXT REFERENCES stage_runs(stage_run_id),

    error_type TEXT NOT NULL,
    error_code TEXT,

    message TEXT NOT NULL,
    details_json JSONB,

    retryable BOOLEAN NOT NULL DEFAULT false,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `error_id` | TEXT | Primary identifier for the processing error. |
| `paper_id` | TEXT / NULL | Paper associated with the error when known. |
| `pipeline_run_id` | TEXT / NULL | Pipeline run associated with the error when known. |
| `stage_run_id` | TEXT / NULL | Stage run associated with the error when known. |
| `error_type` | TEXT | Stable error type classification. |
| `error_code` | TEXT / NULL | More specific machine-readable error code. |
| `message` | TEXT | Human-readable error message. |
| `details_json` | JSONB / NULL | Structured diagnostic details. |
| `retryable` | BOOLEAN | Whether retry may succeed without contract or data changes. |
| `created_at` | TIMESTAMPTZ | Error creation timestamp. |

## 5. Responsibilities

### Required Responsibilities

`processing_errors` must:

- preserve traceable failure records
- classify errors by stable error type
- preserve human-readable error messages
- allow structured diagnostic details
- support retry decisions through `retryable`

### Forbidden Responsibilities

`processing_errors` must not store:

- stage status
- artifact payloads
- model traces as primary storage
- replacement records for `stage_runs`
- scientific extraction payloads

## 6. Validation Rules

- `error_id`, `error_type`, `message`, `retryable`, and `created_at` are
  required.
- `paper_id`, when present, must reference an existing `papers.paper_id`.
- `pipeline_run_id`, when present, must reference an existing
  `pipeline_runs.pipeline_run_id`.
- `stage_run_id`, when present, must reference an existing
  `stage_runs.stage_run_id`.
- `error_type` must be one of the allowed values.
- `message` must not be empty.
- `details_json` must be valid JSON when present.

### Allowed Error Types

- `validation_error`
- `model_error`
- `parser_error`
- `storage_error`
- `schema_error`
- `timeout`
- `dependency_missing`
- `manual_stop`
- `unknown`

## 7. Lifecycle

### Created

Created when a pipeline, stage, validation, storage, model, parser, dependency,
or manual-stop error is observed.

### Updated

Errors are append-oriented and should not be materially rewritten.

### Deleted

Not deleted under normal operation.

### Deprecated

Deprecated only by future contract version or error taxonomy migration.

## 8. Relationships

### Upstream Contracts

- `ProcessingPapers`
- `PipelineRuns`
- `StageRuns`

### Downstream Contracts

None.

### References

- `processing_errors.paper_id` -> `papers.paper_id`
- `processing_errors.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`
- `processing_errors.stage_run_id` -> `stage_runs.stage_run_id`
- `stage_runs.error_id` -> `processing_errors.error_id`

## 9. Operational Notes

`processing_errors` records diagnostic detail. The authoritative stage state
remains in `stage_runs`.

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable columns, new error types, or
additional diagnostic fields.

### Major

Breaking schema changes, identity changes, error type meaning changes, or field
removals.
