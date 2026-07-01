# Wiki.js Export Pipeline Plan

## Goal

Build a stable, reversible Wiki.js export pipeline that publishes normalized
documentation to `wiki-production` without mutating the source branch.

## Scope

- Add a local export command:
  `ops/scripts/build-wikijs-export.sh . /tmp/wiki-export`
- Generate a clean temporary export tree for Wiki.js.
- Normalize exported paths to lowercase kebab-case.
- Generate `.wikijs-path-map.json`.
- Rewrite Markdown links against the manifest.
- Validate broken links, normalized path collisions, and problematic Wiki.js
  paths before publishing.
- Replace the GitHub Actions workflow with an orphan-branch publish/import flow.

## Assumptions

- `victus-docs` remains the canonical source of documentation.
- Wiki.js imports from the `wiki-production` branch only.
- `repos/**` is synchronized context and is exported as read-only rendered
  documentation when referenced, but is not edited as canonical source.
- Root MoC filenames have stable public Wiki.js paths:
  `/system-context`, `/architecture`, `/operations`, `/contracts`.
- `README.md` is exported as `readme.md`; Wiki.js links omit `.md`, so a
  README at `docs/contracts/README.md` is addressed as `/docs/contracts/readme`.
- `_registry` is exported as `registry` to avoid path segments that are awkward
  in Wiki.js.

## Steps

1. Add a Python export builder for copy, normalization, manifest generation,
   Markdown link rewriting, and validation.
2. Add a small Bash wrapper that is convenient locally and in CI.
3. Replace the workflow with a clean orphan branch publish.
4. Trigger the Wiki.js GraphQL import only after the export build and push
   succeed.
5. Validate locally with `/tmp/wiki-export`.

## Validation

- Run `ops/scripts/build-wikijs-export.sh . /tmp/wiki-export`.
- Inspect `.wikijs-path-map.json`.
- Confirm exported root paths include:
  `/system-context`, `/architecture`, `/operations`, `/contracts`,
  `/agents`, `/plans`.
- Confirm no `.github`, `ops`, `repos`, or `.git` content is exported.

## Risks

- Mirrored `repos/**` pages may increase Wiki.js page count, but exporting them
  keeps existing cross-repository navigation from producing broken links.
- Any future filename pair that normalizes to the same path, such as `Paper.md`
  and `paper.md`, will block export until resolved.
