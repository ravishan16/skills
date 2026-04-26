#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Aggregate grading.json and timing.json files into benchmark.json.",
        epilog=(
            "Examples:\n"
            "  python3 scripts/aggregate_eval_results.py --iteration-dir data-analysis-workspace/iteration-1\n"
            "  python3 scripts/aggregate_eval_results.py --iteration-dir data-analysis-workspace/iteration-2 "
            "--baseline-name old_skill"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    p.add_argument("--iteration-dir", required=True, help="Iteration directory to aggregate")
    p.add_argument("--baseline-name", default="without_skill", help="Baseline directory name")
    return p


def stats(values: list[float]) -> dict[str, float] | None:
    if not values:
        return None
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return {"mean": mean, "stddev": math.sqrt(variance)}


def load_json(path: Path) -> dict | None:
    return json.loads(path.read_text()) if path.exists() else None


def main() -> int:
    args = parser().parse_args()
    iteration_dir = Path(args.iteration_dir)
    configs = ["with_skill", args.baseline_name]
    aggregate: dict[str, dict[str, list[float]]] = {
        config: {"pass_rate": [], "time_seconds": [], "tokens": []} for config in configs
    }

    for eval_dir in sorted(iteration_dir.glob("eval-*")):
        for config in configs:
            config_dir = eval_dir / config
            grading = load_json(config_dir / "grading.json")
            timing = load_json(config_dir / "timing.json")

            if grading:
                summary = grading.get("summary", {})
                pass_rate = summary.get("pass_rate")
                if pass_rate is not None:
                    aggregate[config]["pass_rate"].append(float(pass_rate))
            if timing:
                duration_ms = timing.get("duration_ms")
                tokens = timing.get("total_tokens")
                if duration_ms is not None:
                    aggregate[config]["time_seconds"].append(float(duration_ms) / 1000.0)
                if tokens is not None:
                    aggregate[config]["tokens"].append(float(tokens))

    run_summary: dict[str, dict | float] = {}
    for config in configs:
        run_summary[config] = {
            "pass_rate": stats(aggregate[config]["pass_rate"]),
            "time_seconds": stats(aggregate[config]["time_seconds"]),
            "tokens": stats(aggregate[config]["tokens"]),
        }

    with_skill = run_summary.get("with_skill", {})
    baseline = run_summary.get(args.baseline_name, {})
    delta: dict[str, float] = {}
    for metric in ("pass_rate", "time_seconds", "tokens"):
        with_stats = with_skill.get(metric) if isinstance(with_skill, dict) else None
        base_stats = baseline.get(metric) if isinstance(baseline, dict) else None
        if with_stats and base_stats:
            delta[metric] = with_stats["mean"] - base_stats["mean"]

    benchmark = {"run_summary": {**run_summary, "delta": delta}}
    output_path = iteration_dir / "benchmark.json"
    output_path.write_text(json.dumps(benchmark, indent=2))
    print(json.dumps({"benchmark": str(output_path), "delta": delta}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

