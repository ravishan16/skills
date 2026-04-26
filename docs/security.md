# Security guidance

## General rules

- Do not hardcode credentials or secrets.
- Avoid unnecessary network access.
- Prefer local file processing for v1 skills unless remote access is explicitly part of the skill.
- Make destructive actions opt-in and explicit.

## Structured-data skills

- Do not overwrite raw source data unless explicitly asked.
- Report schema ambiguity, parse failures, and unsupported workbook features explicitly.
- Keep temporary artifacts predictable and clean them up when they are not part of the deliverable.

## Review guidance

Reviewers should check for:

- unexpected network reads or writes
- hidden dependency on external state
- silent error masking
- unsafe shell usage

