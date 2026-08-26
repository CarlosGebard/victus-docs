# Victus Docs

`victus-docs` is the documentation control plane for the Victus ecosystem.

It exists to give humans and AI agents one stable place to understand system context, shared contracts, architecture decisions, and repository boundaries.

## Start Here

| Reader | First file | Purpose |
|---|---|---|
| Human | [000-SYSTEM-CONTEXT.md](/000-SYSTEM-CONTEXT) | Canonical documentation convention and system context |
| AI agent | [AGENTS.md](/AGENTS) | Repository rules and required reading order |
| Architecture reviewer | [100-ARCHITECTURE.md](/100-ARCHITECTURE) | Architecture map and system principles |
| Operations reviewer | [200-OPERATIONS.md](/200-OPERATIONS) | Documentation operations and validation |
| Contract reviewer | [300-CONTRACTS.md](/300-CONTRACTS) | Stable cross-repository expectations |

## What This Repository Owns

- Global Victus architecture documentation
- Cross-repository contracts
- Architecture Decision Records
- Agent navigation and repository rules
- Read-only documentation mirrors for ecosystem repositories

## What This Repository Does Not Own

- Application source code
- Infrastructure source code
- Pipeline implementation details
- Repository-local operational commands
- Changes inside synchronized mirrors under `repos/**`

Source changes belong in the owning repository.

## Documentation Map

Victus documentation uses a hybrid Hub-and-Node convention. Root numbered files are Maps of Content; detailed documents remain in their owning folders.

| Path | Role |
|---|---|
| [000-SYSTEM-CONTEXT.md](/000-SYSTEM-CONTEXT) | System context and documentation convention |
| [100-ARCHITECTURE.md](/100-ARCHITECTURE) | Architecture Map of Content |
| [200-OPERATIONS.md](/200-OPERATIONS) | Operations Map of Content |
| [300-CONTRACTS.md](/300-CONTRACTS) | Contracts Map of Content |
| [decisions/](decisions/) | Root decision hub |
| [docs/contracts/artifacts.md](/docs/contracts/artifacts) | Artifact contract hub |
| [docs/contracts/repository-documentation-contract.md](/docs/contracts/repository-documentation-contract) | Repository documentation contract |
| [docs/adr/index.md](/docs/adr/index) | Architecture decisions |
| [repos/](repos/) | Read-only synchronized repository documentation |

## Ecosystem Repositories

| Repository | Responsibility |
|---|---|
| `victus-docs` | Global documentation, contracts, ADRs, and agent-readable navigation |
| `victus-infra` | Infrastructure, networking, storage, secrets, observability, and deployment foundation |
| `victus-processing` | Paper ingestion, extraction, structured blocks, canonical evidence, and embeddings |
| `victus-rag` | Retrieval, vector database integration, API orchestration, prompts, and answers |

## Validation

This repository is primarily Markdown documentation. Useful sanity checks are:

```bash
git status --short
find docs -type f -name '*.md' -print
```

Before publishing documentation changes, confirm changed files are intentional and links still point to existing files.
