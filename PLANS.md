# Wiki.js Export Pipeline Plan

## Goal

Build a stable, reversible Wiki.js export pipeline that publishes documentation
to `wiki-production` without mutating the source branch or renaming source
documents.

## Scope

- Add a local export command:
  `ops/scripts/build-wikijs-export.sh . /tmp/wiki-export`
- Generate a clean temporary export tree for Wiki.js.
- Preserve source filenames and directory names in the export.
- Move only root numbered MoC files into `moc/` so Wiki.js does not have to
  resolve them from the import root.
- Generate `.wikijs-path-map.json`.
- Rewrite Markdown links against the manifest.
- Validate broken links, export path collisions, and problematic Wiki.js paths
  before publishing.
- Replace the GitHub Actions workflow with an orphan-branch publish/import flow.

## Assumptions

- `victus-docs` remains the canonical source of documentation.
- Wiki.js imports from the `wiki-production` branch only.
- `repos/**` is synchronized context and is exported as read-only rendered
  documentation when referenced, but is not edited as canonical source.
- Root MoC filenames are preserved and relocated:
  `/moc/000-SYSTEM-CONTEXT`, `/moc/100-ARCHITECTURE`,
  `/moc/200-OPERATIONS`, `/moc/300-CONTRACTS`.
- `README.md`, CamelCase names, `_registry`, and existing directory names are
  preserved in the export.

## Steps

1. Add a Python export builder for copy, MoC relocation, manifest generation,
   Markdown link rewriting, and validation.
2. Add a small Bash wrapper that is convenient locally and in CI.
3. Replace the workflow with a clean orphan branch publish.
4. Trigger the Wiki.js GraphQL import only after the export build and push
   succeed.
5. Validate locally with `/tmp/wiki-export`.

## Validation

- Run `ops/scripts/build-wikijs-export.sh . /tmp/wiki-export`.
- Inspect `.wikijs-path-map.json`.
- Confirm exported MoC paths include:
  `/moc/000-SYSTEM-CONTEXT`, `/moc/100-ARCHITECTURE`,
  `/moc/200-OPERATIONS`, `/moc/300-CONTRACTS`.
- Confirm root `AGENTS.md` and `PLANS.md` remain `/AGENTS` and `/PLANS`.
- Confirm no `.github`, `ops`, or `.git` content is exported.

## Risks

- Mirrored `repos/**` pages may increase Wiki.js page count, but exporting them
  keeps existing cross-repository navigation from producing broken links.
- Any future source pair that maps to the same export path will block export
  until resolved.
