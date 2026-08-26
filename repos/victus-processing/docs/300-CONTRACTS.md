---
id: VICTUS-PROCESSING-CONTRACTS
title: Victus Processing Contracts
status: source-of-truth
updated_at: 2026-06-19
related_docs:
  - VICTUS-PROCESSING-SYSTEM-CONTEXT
  - VICTUS-PROCESSING-ARCHITECTURE
tags: contracts, invariants, artifacts
---

# Contracts

This hub is the source of truth for stable guarantees that future changes must
preserve.

Contracts are high-trust documentation. Agents should treat them as
compatibility boundaries before changing paths, artifacts, identities, schemas,
or stage handoffs.

## Contract Layout

Contracts are split by source and responsibility:

- `docs/contracts/fundamental/`: ecosystem-level contracts synchronized from
  `victus-docs`. These define shared Victus interfaces and preserve the central
  contract repository subdirectory layout.
- `docs/contracts/local/`: repository-specific contracts owned here.

## Fundamental Contracts

- [Paper](/repos/victus-processing/docs/contracts/fundamental/scientific/paper)
- [Structured Block](/repos/victus-processing/docs/contracts/fundamental/scientific/structured-block)
- [Paper Classification](/repos/victus-processing/docs/contracts/fundamental/scientific/paper-classification)
- [Experiment Map](/repos/victus-processing/docs/contracts/fundamental/scientific/experiment-map)
- [Canonical Evidence](/repos/victus-processing/docs/contracts/fundamental/scientific/canonical-evidence)
- [Pipeline Run](/repos/victus-processing/docs/contracts/fundamental/scientific/pipeline-run)
- [Pipeline Event](/repos/victus-processing/docs/contracts/fundamental/scientific/pipeline-event)
- [Storage Layout](/repos/victus-processing/docs/contracts/fundamental/processing/README)
- [Artifact Manifest](/repos/victus-processing/docs/contracts/fundamental/scientific/artifact-manifest)
- [Contracts Lock](contracts/fundamental/contracts.lock.json)

## Local Contracts

- [Data Layout](/repos/victus-processing/docs/contracts/local/data-layout): stable local artifact
  locations, identities, stage inputs, stage outputs, and failure expectations.
- [Metadata Extraction](/repos/victus-processing/docs/operations/pipeline/metadata-extraction): operation, LLM selection
  contract, `paper_metadata.jsonl` schema, and dedupe rules.
- [Stage Handoffs](/repos/victus-processing/docs/contracts/local/stage-handoffs): boundaries between
  metadata, bibliography export, manual PDF intake, PDF processing, trimming,
  experiment mapping, and canonical evidence extraction.
- [Artifact Schemas](/repos/victus-processing/docs/contracts/local/artifact-schemas): durable JSON/JSONL
  shapes consumed or produced by the current pipeline.
- [Artifact Inventory](/repos/victus-processing/docs/contracts/local/artifact-inventory): complete artifact
  list with the inputs consumed to create each artifact.
- [Paper Pipeline State](/repos/victus-processing/docs/contracts/local/paper-pipeline-state): PostgreSQL
  lifecycle state for one paper stage attempt.
- [Paper Processing State](/repos/victus-processing/docs/contracts/fundamental/scientific/paper-processing-state): derived
  PostgreSQL dashboard state by paper.

## Contract Scope

Contracts cover:

- local runtime artifact boundaries;
- stage handoff locations;
- stable identity terms;
- block identity and field-level semantics;
- required validation expectations;
- compatibility boundaries between processing stages;
- config and environment resolution that affects paths or models;
- public CLI command names used by operators and agents;
- schema-level expectations for current durable artifacts and PostgreSQL state;
- experiment map and canonical evidence schema expectations.
- paper classification gate expectations.
- testing workspace artifact expectations.

Contracts do not cover:

- implementation details;
- operational procedures;
- architecture rationale;
- external vendor guarantees.
- downstream analytics schemas outside this repository.

## Status Rule

Documentation with `status: source-of-truth` is authoritative as of its own
`updated_at` value. If code and docs disagree, stop and reconcile the contract
before making behavior-changing edits.

## Related Documents

- [System Context](/repos/victus-processing/docs/000-SYSTEM-CONTEXT)
- [Architecture](/repos/victus-processing/docs/100-ARCHITECTURE)
- [Operations](/repos/victus-processing/docs/200-OPERATIONS)
