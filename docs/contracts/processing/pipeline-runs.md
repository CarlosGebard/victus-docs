---
id: VICTUS-CONTRACT-PROCESSING-PIPELINE-RUNS
contract_id: victus.processing.pipeline_runs
title: Pipeline Runs
status: draft
version: v1
owner: victus-processing
domain: processing
contract_type: database
stability: experimental
updated_at: 2026-06-09
---

# Pipeline Runs Contract Documentation

## 1. Purpose

Represent a complete pipeline execution for a paper.

`pipeline_runs` allows multiple executions to coexist for the same paper. A new
run must not silently overwrite previous runs.

## 2. Identity

### Identity Rules

- Canonical identifier: `pipeline_run_id`
- `pipeline_run_id` is globally unique inside the processing registry.
- `pipeline_run_id` is immutable after creation.
- `paper_id` links the run to the processable paper.

### Ownership

`pipeline_runs` is owned by `victus-processing`.

## 3. Schema

### SQL Schema

```sql
CREATE TABLE pipeline_runs (
    pipeline_run_id TEXT PRIMARY KEY,

    paper_id TEXT NOT NULL REFERENCES papers(paper_id),

    pipeline_name TEXT NOT NULL,
    pipeline_version TEXT NOT NULL,
    pipeline_profile TEXT NOT NULL,

    status TEXT NOT NULL,

    triggered_by TEXT,
    parent_run_id TEXT REFERENCES pipeline_runs(pipeline_run_id),

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    started_at TIMESTAMPTZ,
    finished_at TIMESTAMPTZ
);
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `pipeline_run_id` | TEXT | Primary identifier for the pipeline run. |
| `paper_id` | TEXT | Paper being processed by the run. |
| `pipeline_name` | TEXT | Pipeline name. |
| `pipeline_version` | TEXT | Version of the pipeline definition. |
| `pipeline_profile` | TEXT | Execution profile used by the run. |
| `status` | TEXT | Current run status. |
| `triggered_by` | TEXT / NULL | Actor or process that triggered the run. |
| `parent_run_id` | TEXT / NULL | Parent run when this run derives from another run. |
| `created_at` | TIMESTAMPTZ | Run creation timestamp. |
| `started_at` | TIMESTAMPTZ / NULL | Run start timestamp. |
| `finished_at` | TIMESTAMPTZ / NULL | Run finish timestamp. |

## 5. Responsibilities

### Required Responsibilities

`pipeline_runs` must:

- track complete pipeline executions
- preserve multiple executions for the same paper
- capture pipeline version and profile
- support parent-child run relationships
- provide the parent context for stage runs and artifacts

### Forbidden Responsibilities

`pipeline_runs` must not store:

- per-stage debugging details
- heavy artifact payloads
- extracted scientific content
- model traces
- error details beyond run status

## 6. Validation Rules

- `pipeline_run_id`, `paper_id`, `pipeline_name`, `pipeline_version`,
  `pipeline_profile`, and `status` are required.
- `paper_id` must reference an existing `papers.paper_id`.
- `parent_run_id`, when present, must reference an existing
  `pipeline_runs.pipeline_run_id`.
- `status` must be one of the allowed states.
- `started_at` must not be set before `created_at`.
- `finished_at` must not be set before `started_at` when both are present.

### Allowed Status Values

- `created`
- `running`
- `completed`
- `completed_with_warnings`
- `failed`
- `cancelled`
- `superseded`

## 7. Lifecycle

### Created

Created when a pipeline execution is registered.

### Updated

Updated as execution starts, completes, fails, is cancelled, or is superseded.

### Deleted

Not deleted under normal operation.

### Deprecated

Superseded by marking the run `superseded`, not by overwriting it.

## 8. Relationships

### Upstream Contracts

- `ProcessingPapers`

### Downstream Contracts

- `StageRuns`
- `ProcessingArtifacts`
- `ProcessingErrors`

### References

- `pipeline_runs.paper_id` -> `papers.paper_id`
- `pipeline_runs.parent_run_id` -> `pipeline_runs.pipeline_run_id`
- `stage_runs.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`
- `artifacts.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`
- `processing_errors.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`

## 9. Operational Notes

Pipeline runs are append-friendly execution records. Promotion of a new run over
an older run must be explicit.

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable columns or new non-breaking
status values.

### Major

Breaking schema changes, identity changes, status meaning changes, or field
removals.
