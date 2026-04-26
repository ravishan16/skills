# Tenant lifecycle reference

Use this reference when the user asks how tenants are provisioned, suspended, offboarded, or deleted.

## Provisioning

- create tenant identifiers and storage layout
- register hostname mappings
- store brand settings and access rules
- provision the initial report or dataset permissions

## Suspension

- disable report access quickly at the trusted routing layer
- preserve auditability of who was suspended and why
- avoid deleting data as the first response to a temporary suspension

## Offboarding and deletion

- remove domain mappings
- revoke or disable tenant access
- delete or archive tenant-specific data according to policy
- record the deletion workflow so cleanup is auditable

## Why this matters

White-labeled SaaS platforms need lifecycle behavior, not just request routing.

## What to return

- onboarding steps
- suspension behavior
- offboarding or deletion path
- control-plane records that must exist
