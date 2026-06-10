# Contract Registry

`docs/contracts/**` is the canonical contract home for the Victus ecosystem.

Canonical contracts live once in `victus-docs`. Repositories do not copy canonical
contract files. A contract is referenced by `contract_id@version`, where
`contract_id` is the stable machine-readable identity and `version` is the
semantic contract version.

Repositories consume or produce contracts by declaring subscriptions in a
repo-local `victus.contracts.yml` file. Repository-local documentation may
explain implementation details, adapters, tests, or operational behavior, but it
must not redefine canonical contracts.

`repos/**` is read-only synchronized context inside this repository. It is useful
for understanding repository documentation state, but it is not the source of
canonical contracts.

Wiki.js is a read-only rendered view of this documentation. It is not a source of
truth for contract definitions, registry data, or subscription ownership.

## Registry Files

| File | Purpose |
|---|---|
| [_registry/contracts.registry.yml](_registry/contracts.registry.yml) | Canonical contract registry |
| [_registry/contract-subscriptions.yml](_registry/contract-subscriptions.yml) | Repository contract subscription registry |
| [_registry/contract-frontmatter-schema.md](_registry/contract-frontmatter-schema.md) | Required frontmatter for future contract documents |

## Active Contracts

| Contract | Identifier | Owner | Status |
|---|---|---|---|
| [Paper](scientific/paper.md) | `victus.scientific.paper@v1` | `victus-docs` | active |
| [StructuredBlock](scientific/structured-block.md) | `victus.scientific.structured_block@v1` | `victus-docs` | active |
| [PaperClassification](scientific/paper-classification.md) | `victus.scientific.paper_classification@v1` | `victus-docs` | draft |
| [ExperimentMap](scientific/experiment-map.md) | `victus.scientific.experiment_map@v1` | `victus-docs` | draft |
| [CanonicalEvidence](scientific/canonical-evidence.md) | `victus.scientific.canonical_evidence@v1` | `victus-docs` | draft |
| [ArtifactManifest](scientific/artifact-manifest.md) | `victus.storage.artifact_manifest@v1` | `victus-docs` | draft |
| [PipelineRun](scientific/pipeline-run.md) | `victus.orchestration.pipeline_run@v1` | `victus-docs` | draft |
| [PipelineEvent](scientific/pipeline-event.md) | `victus.orchestration.pipeline_event@v1` | `victus-docs` | draft |
| [Processing Papers](processing/papers.md) | `victus.processing.papers@v1` | `victus-docs` | draft |
| [Pipeline Runs](processing/pipeline-runs.md) | `victus.processing.pipeline_runs@v1` | `victus-docs` | draft |
| [Stage Runs](processing/stage-runs.md) | `victus.processing.stage_runs@v1` | `victus-docs` | draft |
| [Processing Artifacts](processing/artifacts.md) | `victus.processing.artifacts@v1` | `victus-docs` | draft |
| [Processing Errors](processing/processing-errors.md) | `victus.processing.processing_errors@v1` | `victus-docs` | draft |

## Domain Indexes

| Domain | Purpose |
|---|---|
| [Scientific Contracts](scientific/README.md) | Canonical scientific contract flow and compatibility decisions |
| [Processing Contracts](processing/README.md) | Operational processing registry and pipeline execution contracts |

## Templates

| File | Purpose |
|---|---|
| [_templates/contract-template.md](_templates/contract-template.md) | Template for future canonical contract documents |
| [_templates/repository-subscription-template.yml](_templates/repository-subscription-template.yml) | Template for repo-local `victus.contracts.yml` files |
| [_templates/contract-change-proposal-template.md](_templates/contract-change-proposal-template.md) | Template for proposing canonical contract changes |

## Governance

| File | Purpose |
|---|---|
| [governance/ContractSubscriptionModel.md](governance/ContractSubscriptionModel.md) | Repository subscription model |
| [governance/ContractChangeProcess.md](governance/ContractChangeProcess.md) | Contract change governance |

## Existing Contract Documents

The following documents predate the registry structure and remain canonical until
they are migrated into the registry model:

- [artifacts.md](artifacts.md)
- [repository-documentation-contract.md](repository-documentation-contract.md)
