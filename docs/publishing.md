# Publishing checklist

Use this checklist before publishing a skill to skills.sh or any equivalent marketplace.

## How skills.sh publishing works

skills.sh indexes public GitHub-hosted skills rather than using a dedicated "publish" API. In practice, publishing means:

1. the repository is public
2. the skill structure is valid
3. skill metadata is complete
4. the default branch stays installable and releasable

Install command for this repository:

```bash
npx skills add ravishan16/skills
```

## Required

- `SKILL.md` has complete frontmatter
- trigger description is specific and actionable
- scope and non-goals are clear
- examples exist
- evals exist
- repo validation passes
- README mentions the skill

## Recommended

- defaults and failure modes are documented
- install/runtime assumptions are documented
- output artifacts are described
- benchmark notes exist for performance-sensitive skills
- GitHub Actions publish workflow succeeds
- packaged skill artifacts are generated cleanly

## Repository metadata

- Author metadata must be `Ravishankar Sivasubramaniam`
- include `license`, `compatibility`, and `metadata` in every published skill frontmatter
- prefer explicit version metadata for release builds

## For this repository

The first release should prioritize a strong, clearly scoped `data-analysis` skill over a broad catalog of partially defined skills.
