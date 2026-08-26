# Scientific Contracts

Scientific contracts define canonical scientific objects and relationships in
Victus. They do not define repository-local runtime files, prompt internals,
storage paths, or model execution details.

## Conceptual Flow

```text
Paper
  -> PaperClassification
  -> StructuredBlock
  -> ExperimentMap
  -> CanonicalEvidence
  -> ArtifactManifest
  -> PipelineRun
  -> PipelineEvent
  -> Embedding
  -> Retrieval
  -> Agent Reasoning
  -> User Answer
```

## Contract Index

| Order | Contract | Identifier | Status | Role |
|---|---|---|---|---|
| 1 | [Paper](/docs/contracts/scientific/paper) | `victus.scientific.paper@v1` | active | Canonical scientific publication identity |
| 2 | [PaperClassification](/docs/contracts/scientific/paper-classification) | `victus.scientific.paper_classification@v1` | draft | Paper-level evidence routing classification |
| 3 | [StructuredBlock](/docs/contracts/scientific/structured-block) | `victus.scientific.structured_block@v1` | active | Preserved source context unit |
| 4 | [ExperimentMap](/docs/contracts/scientific/experiment-map) | `victus.scientific.experiment_map@v1` | draft | Result-centered block grouping artifact |
| 5 | [CanonicalEvidence](/docs/contracts/scientific/canonical-evidence) | `victus.scientific.canonical_evidence@v1` | draft | Canonical reusable scientific result |
| 6 | [ArtifactManifest](/docs/contracts/scientific/artifact-manifest) | `victus.storage.artifact_manifest@v1` | draft | Physical artifact manifest and lineage record |
| 7 | [PipelineRun](/docs/contracts/scientific/pipeline-run) | `victus.orchestration.pipeline_run@v1` | draft | Canonical pipeline execution record |
| 8 | [PipelineEvent](/docs/contracts/scientific/pipeline-event) | `victus.orchestration.pipeline_event@v1` | draft | Append-only pipeline event record |

## Compatibility Decisions

- `StructuredBlock` replaces legacy `Section Block` terminology.
- `CanonicalEvidence` replaces the previous `Claim` contract concept.
- Victus does not define or use `Claim` as a system contract.
- `PaperContent` is omitted for now.
- `paper.md`, `paper.processed.json`, and `paper.final.json` are operational
  pipeline artifacts, not canonical scientific contracts.
- `paper.final.json` may be a repository-local implementation of
  `StructuredBlock[]`.
- IDs are deterministic for `Paper`, `StructuredBlock`, `ExperimentMap`,
  experiment scopes, and `CanonicalEvidence`.
- Regenerated extraction outputs must coexist with prior versions unless an
  explicit promotion or migration decision supersedes them.
- Pipeline, parser, model, and prompt versions belong in a separate provenance
  contract such as `ProcessingProvenance` or `ExtractionRun`.
- Victus-RAG consumes `CanonicalEvidence`, not `Claim`.

## Planned Subscription Shape

`victus-processing` is expected to produce:

- `victus.scientific.paper@v1`
- `victus.scientific.structured_block@v1`
- `victus.scientific.paper_classification@v1`
- `victus.scientific.experiment_map@v1`
- `victus.scientific.canonical_evidence@v1`
- `victus.storage.artifact_manifest@v1`
- `victus.orchestration.pipeline_run@v1`
- `victus.orchestration.pipeline_event@v1`

`victus-rag` is expected to consume:

- `victus.scientific.canonical_evidence@v1`

These relationships should be declared first in repo-local
`victus.contracts.yml` files, then reflected in the global inverted
subscription registry.
