# Plans

## Root documentation entrypoint restructure

### Goal

Make the repository root easier to understand for first-time human readers and AI agents.

### Scope

- Improve `README.md` as the human-facing entrypoint.
- Improve `AGENTS.md` as the agent-facing entrypoint.
- Improve `docs/index.md` as the canonical documentation map.
- Keep existing documentation paths stable.

### Assumptions

- `victus-docs` remains the canonical documentation control plane.
- `repos/**` remains read-only synchronized context.
- Implementation details stay in owning repositories.

### Steps

1. Rewrite the root README around purpose, start paths, repository map, and ownership.
2. Tighten `AGENTS.md` into a clear execution contract for agents.
3. Turn `docs/index.md` into a stronger navigation hub for humans and agents.
4. Validate markdown links and repository status.

### Validation

- Inspect changed markdown files.
- Run link-oriented checks with available shell tools.
- Confirm no synchronized repo files under `repos/**` were edited.

### Risks

- Over-documenting the root could duplicate deeper architecture docs.
- Renaming files would create broken links, so this plan avoids renames.
