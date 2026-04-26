# skills

Open-source, contributor-friendly **agent skills** focused on structured data workflows.

The first skill in this repo is **`data-analysis`**: a metadata-first, Parquet-first skill for **CSV**, **Parquet**, and **Excel (`.xlsx`)** that prefers **PyArrow + Polars + DuckDB** over Pandas-heavy workflows.

**Author:** Ravishankar Sivasubramaniam

## Principles

1. **Structured-data first**: start with CSV, Parquet, and Excel before expanding into document extraction.
2. **Metadata before reads**: inspect schema, size, and workbook structure before choosing a strategy.
3. **Parquet-first normalization**: convert row-oriented inputs to optimized Parquet early when it improves performance.
4. **Explicit decision-making**: choose in-memory, lazy, chunked, or out-of-core execution deliberately.
5. **Contributor-friendly by default**: every skill should be easy to review, validate, extend, and publish.
6. **Refined from real runs**: improve skills with execution traces, corrections, and recurring gotchas.

## Repository layout

```text
.
├── .github/
├── docs/
├── scripts/
└── skills/
    ├── _template/
    └── data-analysis/
```

## Current skills

| Skill | Status | Focus |
| --- | --- | --- |
| `data-analysis` | Drafting | High-performance analysis for CSV, Parquet, and Excel |

The `_template` directory is a local scaffold and is **not** intended to be installed as a skill.

## Development

Run the repo checks locally:

```bash
./scripts/validate_skill.sh
./scripts/lint_docs.sh
./scripts/run_evals.sh
```

Prepare an eval workspace or aggregate benchmark results:

```bash
python3 scripts/prepare_eval_workspace.py --skill-dir skills/data-analysis
python3 scripts/aggregate_eval_results.py --iteration-dir data-analysis-workspace/iteration-1
```

Package skills for release or marketplace smoke testing:

```bash
python3 scripts/package_skills.py --output-dir dist
```

## Contribution flow

1. Start from `skills/_template/`.
2. Keep scope tight and trigger text specific.
3. Add examples and evals with each skill.
4. Run the repo checks before opening a pull request.

See **`CONTRIBUTING.md`** for the authoring guide and **`docs/publishing.md`** for publish-readiness expectations.

## Install from skills.sh-compatible GitHub source

skills.sh does not require a separate publish API. Public GitHub repositories that follow the skill format can be installed directly:

```bash
npx skills add ravishan16/skills
```

## Roadmap

- Finish the first release of `data-analysis`
- Add evals and benchmark baselines
- Add publish-ready metadata and workflow checks
- Refine skills with real-task feedback and richer gotchas/reference material
- Explore follow-on structured-data skills before expanding into PDF extraction
