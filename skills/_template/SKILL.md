---
name: your-skill-name
description: >
  Describe exactly when this skill should trigger, what user requests it serves,
  and what makes it distinct from other skills in the repository.
license: MIT
compatibility: Describe runtime or environment assumptions if they matter.
metadata:
  author: Ravishankar Sivasubramaniam
  version: "0.1.0"
argument-hint: <required-arg> [optional-arg]
allowed-tools: Bash
---

## When to use this skill

- State the user intents that should trigger the skill.
- Include 2-3 concrete examples.
- Keep the scope narrow.

## Inputs

- Supported input types
- Required runtime or tools
- Important defaults or assumptions

## Workflow

1. Resolve inputs and validate assumptions.
2. Inspect the minimum metadata needed before doing expensive work.
3. Execute the main workflow with explicit defaults.
4. Report outputs, artifacts, and any meaningful tradeoffs.

## Gotchas

- Add short, high-value corrections the agent is likely to miss without the skill.
- Keep only the surprising facts here.

## Available scripts

- List bundled scripts in `scripts/` when the skill has executable helpers.
- Mention what each script does and when to run it.

## Failure modes

- What should happen when dependencies are missing
- What should happen when the input is unsupported
- What should happen when the requested operation is ambiguous

## Output contract

- Describe what the skill should return or write.
- Describe any files, summaries, or logs it should produce.
- If the skill interprets data or intent, separate:
  - what is directly observed
  - what is inferred with confidence
  - what remains ambiguous and needs confirmation

## Progressive disclosure

- Keep the main skill focused on core instructions.
- Put long reference material in `references/`.
- Put reusable templates in `assets/`.
- Put reusable code or command fragments in `snippets/`.
- Put executable helpers with stable interfaces in `scripts/`.
- Tell the agent when to load each reference or template.
