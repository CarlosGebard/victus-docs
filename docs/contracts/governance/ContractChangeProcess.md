# Contract Change Process

Contract changes are classified as patch, minor, or major.

## Patch Changes

Patch changes clarify wording, fix documentation errors, or add non-normative
examples without changing producer or consumer obligations.

Patch changes require:

- updating the canonical contract document
- updating registry metadata when status, owner, stability, path, or version
  metadata changes

Patch changes do not normally require consumer updates or an ADR.

## Minor Changes

Minor changes add backward-compatible expectations, optional fields, optional
behaviors, or additional guidance that does not break existing producers or
consumers.

Minor changes require:

- updating the canonical contract document
- updating registry metadata when needed
- checking known producers and consumers for compatibility
- updating repo-local subscriptions if a repository begins producing or
  consuming the new capability

An ADR is required when the minor change affects architecture, ownership,
cross-repository responsibilities, or long-term compatibility policy.

## Major Changes

Major changes alter required behavior, remove or rename contract elements,
change compatibility expectations, or require coordinated producer and consumer
implementation changes.

Major changes require:

- an ADR before the canonical contract is finalized
- checking all known consumers in `_registry/contract-subscriptions.yml`
- coordinating required producer and consumer updates in the owning repositories
- updating repo-local `victus.contracts.yml` files when subscriptions change
- updating `_registry/contracts.registry.yml` and
  `_registry/contract-subscriptions.yml`

## Repository-Local Implementation Changes

Repository-local implementation changes do not automatically change canonical
contracts. If implementation behavior remains compatible with the referenced
`contract_id@version`, update only the owning repository documentation,
implementation, tests, or `victus.contracts.yml` as needed.

If an implementation change changes the stable expectations that other
repositories rely on, treat it as a canonical contract change and follow this
process before depending on the new behavior.
