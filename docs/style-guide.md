# Style guide

## Skill frontmatter

Every `SKILL.md` should define:

- `name`
- `description`
- `argument-hint` when arguments are expected
- `allowed-tools`

## Trigger descriptions

- Describe what user intent should activate the skill.
- Include a few realistic phrases or request shapes.
- Avoid vague trigger text like "use for data things."

## Step structure

Skills should favor short, ordered sections:

1. resolve input and assumptions
2. inspect metadata or prerequisites
3. execute the main workflow
4. handle errors and report outputs

## Quality bar

- Be deterministic where possible.
- State defaults explicitly.
- Explain meaningful tradeoffs.
- Prefer sharp scope over broad promise.

