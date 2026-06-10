---
id: VICTUS-CONTRACT-EXAMPLE
contract_id: victus.example
title: Example
status: draft
version: v1
owner: owning-repository-or-team
domain: domain-name
contract_type: domain
stability: experimental
updated_at: YYYY-MM-DD
---

# Example Contract Documentation

## 1. Purpose

Describe the canonical object, boundary, or guarantee this contract defines.

Explain why this contract exists and what stable identity or behavior it
provides across Victus.

State whether this contract is a root object, derived object, interface,
artifact, event, or supporting boundary.

## 2. Identity

### Identity Rules

- Canonical identifier: `example_id`
- `example_id` is globally unique inside Victus.
- `example_id` is immutable after creation.
- Downstream artifacts must reference this contract through `example_id`.
- External identifiers are metadata identifiers, not Victus identity.

### Ownership

State which repository, layer, or team owns the canonical identity and which
workflows may update non-identity fields.

## 3. Schema

### JSON Schema

```json
{
  "example_id": "string",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## 4. Field Definitions

| Field | Type | Description |
|---|---|---|
| `example_id` | String | Canonical Victus identifier for the object. |
| `created_at` | Timestamp | Object creation timestamp inside Victus. |
| `updated_at` | Timestamp | Last object update timestamp. |

## 5. Responsibilities

### Required Responsibilities

`Example` must:

- define the stable guarantees this contract owns
- preserve required identity and traceability fields
- remain independent from implementation-specific storage or pipeline details

### Forbidden Responsibilities

`Example` must not store:

- responsibilities owned by downstream contracts
- pipeline state unless this contract explicitly governs pipeline state
- storage paths as identity
- generated conclusions unless this contract explicitly governs generated output

State any domain-specific exclusions that protect contract boundaries.

## 6. Validation Rules

- Required fields must be present.
- Canonical identifiers must be unique and immutable.
- Required strings must not be empty.
- Nullable fields must use `null`.
- Empty strings must be normalized to `null`.
- Unknown values must not be invented.
- `created_at` must be set once.
- `updated_at` must change when the object is modified.

## 7. Lifecycle

### Created

State when this object or boundary is created.

Typical sources:

- source one
- source two

### Updated

State which changes may update this contract instance.

### Deleted

State whether deletion is allowed and under which conditions.

### Deprecated

State when this contract instance or version may be deprecated.

## 8. Relationships

### Upstream Contracts

- `UpstreamContract`

Use `None` when this is a root contract.

### Downstream Contracts

- `DownstreamContract`

### References

- `DownstreamContract.example_id` -> `Example.example_id`

## 9. Operational Notes

Document operationally relevant contract expectations without adding commands or
implementation walkthroughs.

Examples:

- storage suitability
- load frequency expectations
- regeneration expectations
- identity constraints for storage paths

## 10. Versioning

### Patch

Documentation clarification or validation wording refinement.

### Minor

Backward-compatible additions such as nullable fields, optional identifiers, or
non-breaking validation guidance.

### Major

Breaking schema changes, identity changes, field removals, or semantic meaning
changes.
