# Contributing

Thanks for helping build a high-quality skills repository.

## What belongs here

This repository is for **skills**, not generic scripts. Each contribution should package a focused capability in a way that an agent can discover, load, and execute consistently.

Good contributions usually have:

- a tight problem statement
- a clear trigger description
- explicit constraints and failure modes
- examples that show realistic usage
- evals that prove the skill behaves as intended

The best skills usually come from **real execution**, not generic brainstorming alone. When refining a skill, capture:

- steps that worked repeatedly
- corrections you had to give the agent
- edge cases that caused mistakes
- expected inputs, outputs, and artifacts

## Repository conventions

### Skill layout

Every skill should live under `skills/<skill-name>/` and include:

```text
skills/<skill-name>/
├── SKILL.md
├── examples/
├── evals/
├── assets/
├── references/
├── snippets/
└── scripts/
```

Use `skills/_template/` as the starting point.

### Naming

- Use lowercase letters, numbers, and hyphens for skill names.
- Keep the folder name and `name:` frontmatter aligned.
- Prefer descriptive names over broad labels.

### Skill-writing style

- Lead with when to use the skill.
- Keep trigger phrases concrete.
- Prefer deterministic steps over vague advice.
- State tool/runtime assumptions explicitly.
- Surface failure modes rather than hiding them.
- If a skill makes tradeoffs, explain the decision policy.
- Keep `SKILL.md` focused on core instructions and move detailed material into `references/` or `assets/`.
- Add a **gotchas** section when the agent would likely make a wrong assumption without it.
- Prefer reusable procedures and templates over one-off answers.
- Put reusable code or command fragments in `snippets/` when the skill would otherwise keep reinventing them.
- Put executable helper logic in `scripts/` when it needs a stable interface, `--help`, or machine-readable output.

### Evals

- Prefer structured eval definitions in `evals/evals.json`.
- Each eval should include a realistic `prompt`, an `expected_output`, and assertions once the first run has shown what success looks like.
- When useful, keep supporting notes or human-readable summaries alongside `evals/evals.json`, not instead of it.

### Data-analysis repo expectations

For structured-data skills, contributors should:

- inspect metadata before expensive reads
- prefer Arrow-compatible workflows
- normalize row-oriented data to Parquet when appropriate
- explain when Polars or DuckDB should be preferred
- document output artifacts and cleanup behavior

## Pull requests

Before opening a PR:

1. Run `./scripts/validate_skill.sh`
2. Run `./scripts/lint_docs.sh`
3. Run `./scripts/run_evals.sh`
4. Make sure examples and evals match the skill's current behavior
5. If you learned something from a real run, update the skill or references so the correction is preserved

Use focused PRs. Avoid mixing unrelated repo cleanup with skill work.

## Issues and proposals

If you want to add a new skill, open an issue first when the scope is unclear or overlaps with an existing skill.

## Licensing

By contributing, you agree that your contributions will be licensed under this repository's license.
