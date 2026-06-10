# Macrolytics Documentation Triage Plan

## Goal

Separate the legacy `Macrolytics/` notes into reusable Victus documentation, archived historical context, and discardable working notes without changing repository ownership boundaries.

## Scope

- Inventory documents under `Macrolytics/`.
- Classify each document by disposition.
- Identify target locations in the current Victus documentation model.
- Keep `repos/**` read-only.
- Avoid rewriting or moving source-of-truth implementation docs from mirrored repositories.

## Assumptions

- `Macrolytics/` is legacy project context for the current Victus ecosystem.
- Current canonical documentation lives in the root Maps of Content, `docs/contracts/`, `docs/adr/`, and repository-local docs mirrored under `repos/**`.
- Notes marked as drafts, logs, old tests, prompts, or Obsidian folder indexes are low-trust unless confirmed by current contracts or repository-local docs.

## Steps

1. Inventory every Markdown file under `Macrolytics/`.
2. Classify each file as `promote`, `rewrite`, `archive`, or `discard-candidate`.
3. Map reusable content to canonical Victus locations.
4. Promote only stable cross-repository contracts or decisions into `victus-docs`.
5. Leave implementation-specific details to the owning repositories.
6. After promotion, either keep `Macrolytics/` as `legacy` with a warning or remove it in a separate explicit cleanup.

## Validation

- Run `rg --files` to confirm affected documentation paths.
- Run Markdown/link checks if available.
- Manually verify that any promoted docs are linked from the relevant MoC.

## Risks

- Some legacy notes may describe ideas never implemented.
- Some names still use `Macrolytics` or old `victus-*-M` folder conventions.
- Moving content too aggressively could make speculative notes look canonical.
- `repos/**` mirrors may be stale, so canonical changes must not be inferred only from mirrors.
