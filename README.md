# Victus Docs

`victus-docs` is the documentation control plane for the Victus ecosystem.

It exists to give humans and AI agents one stable place to understand system context, shared contracts, architecture decisions, and repository boundaries.

## Start Here

| Reader | First file | Purpose |
|---|---|---|
| Human | [docs/index.md](docs/index.md) | Canonical documentation map |
| AI agent | [AGENTS.md](AGENTS.md) | Repository rules and required reading order |
| Architecture reviewer | [docs/architecture/context.md](docs/architecture/context.md) | System context and architecture principles |
| Contract reviewer | [docs/contracts/index.md](docs/contracts/index.md) | Stable cross-repository expectations |

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

| Path | Role |
|---|---|
| [docs/index.md](docs/index.md) | Main documentation index |
| [docs/agents/entrypoint.md](docs/agents/entrypoint.md) | AI-agent navigation entrypoint |
| [docs/architecture/context.md](docs/architecture/context.md) | Victus system context |
| [docs/contracts/index.md](docs/contracts/index.md) | Contract index |
| [docs/adr/index.md](docs/adr/index.md) | Architecture decisions |
| [repos/](repos/) | Read-only synchronized repository documentation |

## Ecosystem Repositories

| Repository | Responsibility |
|---|---|
| `victus-docs` | Global documentation, contracts, ADRs, and agent-readable navigation |
| `victus-infra` | Infrastructure, networking, storage, secrets, observability, and deployment foundation |
| `victus-processing` | Paper ingestion, extraction, chunking, claims, and embeddings |
| `victus-rag` | Retrieval, vector database integration, API orchestration, prompts, and answers |

## Validation

This repository is primarily Markdown documentation. Useful sanity checks are:

```bash
git status --short
find docs -type f -name '*.md' -print
```

Before publishing documentation changes, confirm changed files are intentional and links still point to existing files.
