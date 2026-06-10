# Contract Subscription Model

Canonical contracts live once in `victus-docs`.

Repositories do not copy canonical contract files. A repository declares the
contracts it produces and consumes through a repo-local `victus.contracts.yml`
file. Each reference uses `contract_id@version`.

Two repositories can consume the same contract without every repository depending
on that contract. Subscription is explicit and repository-scoped.

The repo-local subscription file belongs to the owning repository because it
describes how that repository implements, produces, or consumes canonical
contracts. Implementation paths and usage notes belong there, not in the
canonical contract definition.

`victus-docs` keeps the canonical registry and repository subscription map:

- `_registry/contracts.registry.yml` lists canonical contract definitions.
- `_registry/contract-subscriptions.yml` lists repository subscriptions by
  repository and role.

The subscription registry provides global visibility. It does not replace
repo-local `victus.contracts.yml` files.

Breaking changes require checking all known consumers before the canonical
contract is changed. Producers and consumers must coordinate updates through the
owning repositories and update subscription data when the effective contract
relationship changes.
