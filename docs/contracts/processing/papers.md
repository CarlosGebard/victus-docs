---
id: VICTUS-CONTRACT-PROCESSING-PAPERS
contract_id: victus.processing.papers
title: Processing Papers
status: draft
version: v1
owner: victus-processing
domain: processing
contract_type: database
stability: experimental
updated_at: 2026-06-09
---

# Processing Papers Contract Documentation

## 1. Purpose

Represent the operational and canonical processing identity of a paper inside
`victus-processing`.

`papers` tracks the general processable state of a paper. It does not state
which artifacts exist for that paper.

## 2. Identity

### Identity Rules

- Canonical identifier: `paper_id`
- `paper_id` is the primary key for processing registry rows.
- `paper_id` must reference the same paper identity used by scientific
  contracts when the paper has been resolved.
- `paper_id` must not be derived from storage paths as its source of truth.

### Ownership

`papers` is owned by `victus-processing`.

## 3. Schema

### SQL Schema

```sql
CREATE TABLE papers (
    paper_id TEXT PRIMARY KEY,

    status TEXT NOT NULL,

    doi TEXT,
    title TEXT,
    source_fingerprint TEXT,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deprecated_at TIMESTAMPTZ
);
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `paper_id` | TEXT | Primary processing registry identifier for the paper. |
| `status` | TEXT | Current general processable state of the paper. |
| `doi` | TEXT / NULL | DOI when available. |
| `title` | TEXT / NULL | Paper title when available. |
| `source_fingerprint` | TEXT / NULL | Source-level fingerprint used for reconciliation or deduplication. |
| `created_at` | TIMESTAMPTZ | Registry row creation timestamp. |
| `updated_at` | TIMESTAMPTZ | Last registry row update timestamp. |
| `deprecated_at` | TIMESTAMPTZ / NULL | Timestamp when this paper registry row was deprecated. |

## 5. Responsibilities

### Required Responsibilities

`papers` must:

- track one processable paper entity
- expose the general processing state for the paper
- support deduplication and reconciliation through metadata fields
- provide the parent identity for pipeline runs

### Forbidden Responsibilities

`papers` must not store:

- artifact existence
- artifact storage locations
- pipeline execution history
- per-stage debugging state
- heavy scientific payloads
- extracted scientific content

## 6. Validation Rules

- `paper_id` and `status` are required.
- `paper_id` must be unique.
- `status` must be one of the allowed states.
- `doi`, `title`, `source_fingerprint`, and `deprecated_at` may be `null`.
- `deprecated_at` must be set when `status` is `deprecated`.
- `updated_at` must change when the row is materially updated.

### Allowed Status Values

- `registered`
- `ingested`
- `processing`
- `processed`
- `partially_processed`
- `failed`
- `deprecated`

## 7. Lifecycle

### Created

Created when a paper is registered for processing.

### Updated

Updated when the paper advances through processing state or metadata is
corrected.

### Deleted

Not deleted under normal operation.

### Deprecated

Deprecated when the processing registry entry is superseded or should no longer
be used.

## 8. Relationships

### Upstream Contracts

- `Paper`

### Downstream Contracts

- `PipelineRuns`
- `StageRuns`
- `ProcessingArtifacts`
- `ProcessingErrors`

### References

- `pipeline_runs.paper_id` -> `papers.paper_id`
- `stage_runs.paper_id` -> `papers.paper_id`
- `artifacts.paper_id` -> `papers.paper_id`
- `processing_errors.paper_id` -> `papers.paper_id`

## 9. Operational Notes

`papers` is a registry table, not an artifact inventory. Artifact availability
must be determined from `artifacts`.

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable columns or new non-breaking
status values.

### Major

Breaking schema changes, identity changes, status meaning changes, or field
removals.
