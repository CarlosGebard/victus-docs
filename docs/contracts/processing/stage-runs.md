---
id: VICTUS-CONTRACT-PROCESSING-STAGE-RUNS
contract_id: victus.processing.stage_runs
title: Stage Runs
status: draft
version: v1
owner: victus-processing
domain: processing
contract_type: database
stability: experimental
updated_at: 2026-06-09
---

# Stage Runs Contract Documentation

## 1. Purpose

Represent the execution of a specific stage within a pipeline run.

`stage_runs` is the central processing debugging table. It identifies exactly
where a pipeline run failed, succeeded, skipped, or became blocked.

## 2. Identity

### Identity Rules

- Canonical identifier: `stage_run_id`
- `stage_run_id` is globally unique inside the processing registry.
- `stage_run_id` is immutable after creation.
- `pipeline_run_id` links the stage run to its complete pipeline execution.
- `paper_id` denormalizes the paper relationship for debugging and querying.

### Ownership

`stage_runs` is owned by `victus-processing`.

## 3. Schema

### SQL Schema

```sql
CREATE TABLE stage_runs (
    stage_run_id TEXT PRIMARY KEY,

    pipeline_run_id TEXT NOT NULL REFERENCES pipeline_runs(pipeline_run_id),
    paper_id TEXT NOT NULL REFERENCES papers(paper_id),

    stage_name TEXT NOT NULL,
    stage_order INTEGER NOT NULL,

    status TEXT NOT NULL,

    input_artifact_ids TEXT[] NOT NULL DEFAULT '{}',
    output_artifact_ids TEXT[] NOT NULL DEFAULT '{}',

    error_id TEXT,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    started_at TIMESTAMPTZ,
    finished_at TIMESTAMPTZ
);
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `stage_run_id` | TEXT | Primary identifier for the stage execution. |
| `pipeline_run_id` | TEXT | Parent pipeline run. |
| `paper_id` | TEXT | Paper being processed. |
| `stage_name` | TEXT | Stable stage name. |
| `stage_order` | INTEGER | Stage order within the pipeline run. |
| `status` | TEXT | Current stage execution status. |
| `input_artifact_ids` | TEXT[] | Artifact ids consumed by this stage. |
| `output_artifact_ids` | TEXT[] | Artifact ids produced by this stage. |
| `error_id` | TEXT / NULL | Primary processing error for this stage, when present. |
| `created_at` | TIMESTAMPTZ | Stage run creation timestamp. |
| `started_at` | TIMESTAMPTZ / NULL | Stage run start timestamp. |
| `finished_at` | TIMESTAMPTZ / NULL | Stage run finish timestamp. |

## 5. Responsibilities

### Required Responsibilities

`stage_runs` must:

- track execution state for each pipeline stage
- preserve stage ordering
- record consumed and produced artifact identifiers
- point to the primary error through `error_id`
- support debugging at stage granularity

### Forbidden Responsibilities

`stage_runs` must not store:

- full error detail payloads
- heavy artifacts
- scientific extraction payloads
- model traces
- storage object content

## 6. Validation Rules

- `stage_run_id`, `pipeline_run_id`, `paper_id`, `stage_name`, `stage_order`,
  and `status` are required.
- `pipeline_run_id` must reference an existing
  `pipeline_runs.pipeline_run_id`.
- `paper_id` must reference an existing `papers.paper_id`.
- `status` must be one of the allowed states.
- `input_artifact_ids` and `output_artifact_ids` must always be arrays.
- `stage_order` must be non-negative.
- `started_at` must not be set before `created_at`.
- `finished_at` must not be set before `started_at` when both are present.

### Expected Stage Names

- `metadata_resolution`
- `pdf_ingestion`
- `pdf_to_markdown`
- `markdown_batching`
- `structured_block_extraction`
- `paper_classification`
- `scientific_block_trimming`
- `experiment_mapping`
- `canonical_evidence_extraction`
- `artifact_packaging`
- `promotion`
- `indexing`

### Allowed Status Values

- `pending`
- `running`
- `succeeded`
- `succeeded_with_warnings`
- `failed`
- `skipped`
- `blocked`
- `cancelled`

## 7. Lifecycle

### Created

Created when the stage is planned or registered for a pipeline run.

### Updated

Updated as the stage starts, finishes, fails, is skipped, is blocked, or is
cancelled.

### Deleted

Not deleted under normal operation.

### Deprecated

Deprecated only through a future contract version or superseded pipeline model.

## 8. Relationships

### Upstream Contracts

- `ProcessingPapers`
- `PipelineRuns`

### Downstream Contracts

- `ProcessingArtifacts`
- `ProcessingErrors`

### References

- `stage_runs.pipeline_run_id` -> `pipeline_runs.pipeline_run_id`
- `stage_runs.paper_id` -> `papers.paper_id`
- `stage_runs.error_id` -> `processing_errors.error_id`
- `artifacts.stage_run_id` -> `stage_runs.stage_run_id`
- `processing_errors.stage_run_id` -> `stage_runs.stage_run_id`

## 9. Operational Notes

`stage_runs` is the first table to inspect when debugging a failed pipeline
execution. Detailed error payloads belong in `processing_errors`.

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable columns, new stage names, or new
non-breaking status values.

### Major

Breaking schema changes, identity changes, stage meaning changes, status meaning
changes, or field removals.
