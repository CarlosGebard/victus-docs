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
| [_registry/contract-frontmatter-schema.md](/docs/contracts/_registry/contract-frontmatter-schema) | Required frontmatter for future contract documents |

## Active Contracts

| Contract | Identifier | Owner | Status |
|---|---|---|---|
| [Paper](/docs/contracts/scientific/paper) | `victus.scientific.paper@v1` | `victus-docs` | active |
| [StructuredBlock](/docs/contracts/scientific/structured-block) | `victus.scientific.structured_block@v1` | `victus-docs` | active |
| [PaperClassification](/docs/contracts/scientific/paper-classification) | `victus.scientific.paper_classification@v1` | `victus-docs` | draft |
| [ExperimentMap](/docs/contracts/scientific/experiment-map) | `victus.scientific.experiment_map@v1` | `victus-docs` | draft |
| [CanonicalEvidence](/docs/contracts/scientific/canonical-evidence) | `victus.scientific.canonical_evidence@v1` | `victus-docs` | draft |
| [ArtifactManifest](/docs/contracts/scientific/artifact-manifest) | `victus.storage.artifact_manifest@v1` | `victus-docs` | draft |
| [PipelineRun](/docs/contracts/scientific/pipeline-run) | `victus.orchestration.pipeline_run@v1` | `victus-docs` | draft |
| [PipelineEvent](/docs/contracts/scientific/pipeline-event) | `victus.orchestration.pipeline_event@v1` | `victus-docs` | draft |
| [Processing Papers](/docs/contracts/processing/papers) | `victus.processing.papers@v1` | `victus-docs` | draft |
| [Pipeline Runs](/docs/contracts/processing/pipeline-runs) | `victus.processing.pipeline_runs@v1` | `victus-docs` | draft |
| [Stage Runs](/docs/contracts/processing/stage-runs) | `victus.processing.stage_runs@v1` | `victus-docs` | draft |
| [Processing Artifacts](/docs/contracts/processing/artifacts) | `victus.processing.artifacts@v1` | `victus-docs` | draft |
| [Processing Errors](/docs/contracts/processing/processing-errors) | `victus.processing.processing_errors@v1` | `victus-docs` | draft |

## Domain Indexes

| Domain | Purpose |
|---|---|
| [Scientific Contracts](/docs/contracts/scientific/README) | Canonical scientific contract flow and compatibility decisions |
| [Processing Contracts](/docs/contracts/processing/README) | Operational processing registry and pipeline execution contracts |

## Templates

| File | Purpose |
|---|---|
| [_templates/contract-template.md](/docs/contracts/_templates/contract-template) | Template for future canonical contract documents |
| [_templates/repository-subscription-template.yml](_templates/repository-subscription-template.yml) | Template for repo-local `victus.contracts.yml` files |
| [_templates/contract-change-proposal-template.md](/docs/contracts/_templates/contract-change-proposal-template) | Template for proposing canonical contract changes |

## Governance

| File | Purpose |
|---|---|
| [governance/ContractSubscriptionModel.md](/docs/contracts/governance/ContractSubscriptionModel) | Repository subscription model |
| [governance/ContractChangeProcess.md](/docs/contracts/governance/ContractChangeProcess) | Contract change governance |

## Existing Contract Documents

The following documents predate the registry structure and remain canonical until
they are migrated into the registry model:

- [artifacts.md](/docs/contracts/artifacts)
- [repository-documentation-contract.md](/docs/contracts/repository-documentation-contract)
