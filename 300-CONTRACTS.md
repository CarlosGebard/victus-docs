---
id: VICTUS-MOC-300-CONTRACTS
title: Victus Contracts
status: active
updated_at: 2026-08-25
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags:
  - moc
  - contracts
  - navigation
---

# 300 - Contracts

Contracts define stable, explicit system boundaries across the Victus ecosystem.

This Map of Content routes contract readers to the current contract nodes.

## Contract Authority

Canonical cross-repository contracts live only in `victus-docs`.

Repositories do not copy canonical contracts. They subscribe to contracts through
repo-local `victus.contracts.yml` files using `contract_id@version`.

Implementation details belong in repository-local documentation owned by the
relevant repository.

`repos/**` is read-only synchronized context, not the source of canonical
contracts inside `victus-docs`.

Wiki.js is the authoring source for the rendered documentation, including
contract documentation. Git receives a one-way versioned backup on the
`wiki-production` branch and must not be used to import or author Wiki.js
content.

## Core Contract Documents

| Document | Purpose |
|---|---|
| [Contract Registry](docs/contracts/README.md) | Canonical contract registry entrypoint |
| [Contracts Registry](docs/contracts/_registry/contracts.registry.yml) | Canonical contract registry |
| [Contract Subscriptions](docs/contracts/_registry/contract-subscriptions.yml) | Repository contract subscription registry |
| [Contract Subscription Model](docs/contracts/governance/ContractSubscriptionModel.md) | Governance model for explicit repository subscriptions |
| [Contract Change Process](docs/contracts/governance/ContractChangeProcess.md) | Governance process for patch, minor, and major contract changes |
| [Scientific Contracts](docs/contracts/scientific/README.md) | Scientific contract flow and compatibility decisions |
| [Paper](docs/contracts/scientific/paper.md) | Canonical scientific publication identity contract |
| [StructuredBlock](docs/contracts/scientific/structured-block.md) | Canonical preserved source context unit |
| [PaperClassification](docs/contracts/scientific/paper-classification.md) | Draft paper-level evidence routing classification |
| [ExperimentMap](docs/contracts/scientific/experiment-map.md) | Draft result-centered block grouping artifact |
| [CanonicalEvidence](docs/contracts/scientific/canonical-evidence.md) | Draft canonical scientific result contract |
| [ArtifactManifest](docs/contracts/scientific/artifact-manifest.md) | Draft physical artifact manifest and lineage record |
| [PipelineRun](docs/contracts/scientific/pipeline-run.md) | Draft canonical pipeline execution record |
| [PipelineEvent](docs/contracts/scientific/pipeline-event.md) | Draft append-only pipeline event record |
| [Processing Contracts](docs/contracts/processing/README.md) | Operational processing registry and pipeline execution contracts |
| [Artifact Contract Hub](docs/contracts/artifacts.md) | Canonical artifact graph and governance |
| [Repository Documentation Contract](docs/contracts/repository-documentation-contract.md) | Documentation expectations for ecosystem repositories |

## Current Contract Areas

- repository documentation
- artifacts
- scientific evidence
- retrieval
- provenance
- storage layouts
- API boundaries

Some contract areas are listed as planned or pending until the relevant decision and owner-specific details are documented.

## Contract Rules

Contracts should:

- describe stable expectations
- avoid implementation-specific details
- expose ownership clearly
- remain readable by humans and AI agents
- be referenced by affected architecture documents

Breaking contract changes require an ADR and updates to affected contract documents.

Do not create real domain contracts until the domain contract has an owner,
subscription need, and approved design.

`StructuredBlock` replaces legacy `Section Block` terminology.
`CanonicalEvidence` replaces the previous `Claim` contract concept; Victus does
not define `Claim` as a system contract.
