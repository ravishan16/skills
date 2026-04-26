# Evaluation workflow

Use `evals/evals.json` as the source of truth for structured test cases.

## Recommended loop

1. Run each eval once **with the skill**
2. Run the same eval once **without the skill** or against the previous skill version
3. Save outputs in an iteration workspace
4. Grade assertions with concrete evidence
5. Review the outputs as a human and capture feedback
6. Revise the skill and rerun the eval set in a new iteration directory

## Suggested workspace layout

```text
data-analysis-workspace/
└── iteration-1/
    ├── eval-small-csv-summary/
    │   ├── with_skill/
    │   └── without_skill/
    └── benchmark.json
```

The current repository only validates the presence and shape of `evals/evals.json`; it does not yet automate full eval execution.

