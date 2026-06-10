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

1. [000-SYSTEM-CONTEXT.md](000-SYSTEM-CONTEXT.md)
2. [100-ARCHITECTURE.md](100-ARCHITECTURE.md)
3. [300-CONTRACTS.md](300-CONTRACTS.md)
4. [200-OPERATIONS.md](200-OPERATIONS.md)
5. [decisions/](decisions/)

## Repository Rules

- Treat `repos/**` as read-only synchronized documentation context.
- Do not edit source code from this repository.
- Keep global architecture, contracts, ADRs, and agent navigation in `victus-docs`.
- Keep implementation details in the owning repositories.
- Prefer contracts over implementation details.
- Prefer explicit documentation over assumptions.
- Ask for missing architectural decisions instead of inventing behavior.
- Explain a short plan before multi-file or ambiguous changes.
- Validate changed documentation before claiming completion.
- Start with `300-CONTRACTS.md` when modifying contracts.
- Never edit `repos/**` as a canonical contract source.
- When a repository needs a contract, update its local `victus.contracts.yml` in
  the owning repository instead of copying contract files.
- If modifying a canonical contract, check the registry and consumer
  subscriptions first.
- Do not move existing `repos/**` files.
- Do not create real domain contracts until the domain contract is explicitly
  designed and approved.
- Do not rename existing contract documents unless necessary.

## Documentation Ownership

`victus-docs` owns:

- `000-SYSTEM-CONTEXT.md`
- `100-ARCHITECTURE.md`
- `200-OPERATIONS.md`
- `300-CONTRACTS.md`
- `decisions/`
- `docs/contracts/`
- `docs/adr/`

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
| [000-SYSTEM-CONTEXT.md](000-SYSTEM-CONTEXT.md) | System context and documentation convention |
| [100-ARCHITECTURE.md](100-ARCHITECTURE.md) | Architecture Map of Content |
| [200-OPERATIONS.md](200-OPERATIONS.md) | Operations Map of Content |
| [300-CONTRACTS.md](300-CONTRACTS.md) | Contracts Map of Content |
| [decisions/](decisions/) | Decision hub |
| [docs/contracts/](docs/contracts/) | Canonical supporting contracts |
| [docs/adr/](docs/adr/) | Architecture Decision Records |
| [repos/](repos/) | Read-only synchronized context |

## Change Policy

Prefer focused documentation diffs:

- update indexes when adding new docs
- preserve existing paths unless a rename is explicitly required
- add ADRs for architectural decisions
- add or update runbooks for operational procedures
- keep implementation details in the owning repository
