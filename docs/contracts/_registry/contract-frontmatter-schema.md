# Contract Frontmatter Schema

Future canonical contract documents must include this frontmatter:

```yaml
id:
contract_id:
title:
status:
version:
owner:
domain:
contract_type:
stability:
updated_at:
```

## Field Semantics

`id` is the document identity. It identifies the documentation node and may be
used by navigation, publishing, or documentation tooling.

`contract_id` is the stable machine-readable contract identity. It must remain
stable across document moves and is paired with `version` when repositories refer
to a contract.

`title` is the human-readable contract title.

`status` is the lifecycle state of the contract, such as `draft`, `active`,
`deprecated`, or `retired`.

`version` is the semantic contract version. Repository subscriptions refer to
contracts as `contract_id@version`.

`owner` is the responsible team or repository for stewardship and change review.

`domain` is a classification for discovery and governance. It is not a storage
location and does not imply where the contract file must live.

`contract_type` classifies the contract purpose, such as `domain`,
`orchestration`, `storage`, `process`, or `database`.

`stability` describes compatibility expectations, such as `experimental`,
`stable`, or `deprecated`.

`updated_at` is the date of the last material contract update.

## Registry-Only Fields

The registry may also include fields that are not required in document
frontmatter:

```yaml
implemented_by:
consumed_by:
change_policy:
```

`implemented_by` lists repositories expected to implement or produce the
contract.

`consumed_by` lists repositories expected to consume the contract.

`change_policy` defines the governance requirement for changing the contract,
such as `proposal_required`.
