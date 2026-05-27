# AGENTS.md

This repository is the canonical documentation control plane for the Victus ecosystem.

## Mission

Agents working in this repository must improve documentation clarity without blurring repository ownership.

Use this repository to reason about:

- global architecture
- shared contracts
- architecture decisions
- agent navigation
- synchronized documentation context

Do not use this repository to edit implementation source code.

## Agent Entrypoint

Agents must start here:

1. [docs/agents/entrypoint.md](docs/agents/entrypoint.md)
2. [docs/index.md](docs/index.md)
3. [docs/architecture/context.md](docs/architecture/context.md)
4. [docs/contracts/index.md](docs/contracts/index.md)
5. [docs/adr/index.md](docs/adr/index.md)

## Repository Rules

- Treat `repos/**` as read-only synchronized documentation context.
- Do not edit source code from this repository.
- Keep global architecture, contracts, ADRs, and agent navigation in `victus-docs`.
- Keep implementation details in the owning repositories.
- Prefer contracts over implementation details.
- Prefer explicit documentation over assumptions.
- Ask for missing architectural decisions instead of inventing behavior.
- Use `PLANS.md` before multi-file or ambiguous changes.
- Validate changed documentation before claiming completion.

## Documentation Ownership

`victus-docs` owns:

- `docs/architecture/`
- `docs/contracts/`
- `docs/adr/`
- `docs/agents/`

Synchronized repository documentation lives under:

- `repos/victus-infra/`
- `repos/victus-processing/`
- `repos/victus-rag/`

These synchronized directories are context mirrors, not source-of-truth editing locations.

## Root Navigation

| File or directory | Use |
|---|---|
| [README.md](README.md) | Human-facing repository overview |
| [AGENTS.md](AGENTS.md) | Agent-facing rules and navigation |
| [PLANS.md](PLANS.md) | Plans for larger or ambiguous tasks |
| [docs/](docs/) | Canonical documentation |
| [repos/](repos/) | Read-only synchronized context |

## Change Policy

Prefer focused documentation diffs:

- update indexes when adding new docs
- preserve existing paths unless a rename is explicitly required
- add ADRs for architectural decisions
- add or update runbooks for operational procedures
- keep implementation details in the owning repository
