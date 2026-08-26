---
id: VICTUS-MOC-300-CONTRACTS
title: Victus Contracts
status: active
updated_at: 2026-06-09
owners:
  - architecture
audience:
  - humans
  - ai-agents
tags: moc, contracts, navigation
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

Wiki.js is a read-only rendered view, not a source of truth.

## Core Contract Documents

| Document | Purpose |
|---|---|
| [Contract Registry](/docs/contracts/README) | Canonical contract registry entrypoint |
| [Contracts Registry](docs/contracts/_registry/contracts.registry.yml) | Canonical contract registry |
| [Contract Subscriptions](docs/contracts/_registry/contract-subscriptions.yml) | Repository contract subscription registry |
| [Contract Subscription Model](/docs/contracts/governance/ContractSubscriptionModel) | Governance model for explicit repository subscriptions |
| [Contract Change Process](/docs/contracts/governance/ContractChangeProcess) | Governance process for patch, minor, and major contract changes |
| [Scientific Contracts](/docs/contracts/scientific/README) | Scientific contract flow and compatibility decisions |
| [Paper](/docs/contracts/scientific/paper) | Canonical scientific publication identity contract |
| [StructuredBlock](/docs/contracts/scientific/structured-block) | Canonical preserved source context unit |
| [PaperClassification](/docs/contracts/scientific/paper-classification) | Draft paper-level evidence routing classification |
| [ExperimentMap](/docs/contracts/scientific/experiment-map) | Draft result-centered block grouping artifact |
| [CanonicalEvidence](/docs/contracts/scientific/canonical-evidence) | Draft canonical scientific result contract |
| [ArtifactManifest](/docs/contracts/scientific/artifact-manifest) | Draft physical artifact manifest and lineage record |
| [PipelineRun](/docs/contracts/scientific/pipeline-run) | Draft canonical pipeline execution record |
| [PipelineEvent](/docs/contracts/scientific/pipeline-event) | Draft append-only pipeline event record |
| [Processing Contracts](/docs/contracts/processing/README) | Operational processing registry and pipeline execution contracts |
| [Artifact Contract Hub](/docs/contracts/artifacts) | Canonical artifact graph and governance |
| [Repository Documentation Contract](/docs/contracts/repository-documentation-contract) | Documentation expectations for ecosystem repositories |

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
