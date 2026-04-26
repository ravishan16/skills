#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Prepare a structured eval workspace from evals/evals.json.",
        epilog=(
            "Examples:\n"
            "  python3 scripts/prepare_eval_workspace.py --skill-dir skills/adaptive-data-analysis\n"
            "  python3 scripts/prepare_eval_workspace.py --skill-dir skills/adaptive-data-analysis "
            "--workspace-root adaptive-data-analysis-workspace --iteration iteration-2"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    p.add_argument("--skill-dir", required=True, help="Path to the skill directory")
    p.add_argument(
        "--workspace-root",
        help="Workspace root. Defaults to <skill-name>-workspace in the repository root.",
    )
    p.add_argument(
        "--iteration",
        default="iteration-1",
        help="Iteration name to create (default: iteration-1)",
    )
    p.add_argument(
        "--baseline-name",
        default="without_skill",
        help="Baseline directory name (default: without_skill)",
    )
    return p


def slug(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "-" for ch in value).strip("-")


def main() -> int:
    args = parser().parse_args()
    skill_dir = Path(args.skill_dir)
    eval_file = skill_dir / "evals" / "evals.json"
    if not eval_file.exists():
      raise SystemExit(f"Missing eval file: {eval_file}")

    data = json.loads(eval_file.read_text())
    skill_name = data["skill_name"]
    workspace_root = Path(args.workspace_root or f"{skill_name}-workspace")
    iteration_dir = workspace_root / args.iteration
    iteration_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "skill_name": skill_name,
        "iteration": args.iteration,
        "baseline_name": args.baseline_name,
        "evals": [],
    }

    for item in data["evals"]:
        eval_slug = slug(str(item["id"]))
        eval_dir = iteration_dir / f"eval-{eval_slug}"
        with_skill = eval_dir / "with_skill" / "outputs"
        baseline = eval_dir / args.baseline_name / "outputs"
        with_skill.mkdir(parents=True, exist_ok=True)
        baseline.mkdir(parents=True, exist_ok=True)

        files = item.get("files", [])
        copied_files: list[str] = []
        for file_name in files:
            source = skill_dir / file_name
            if source.exists():
                target = eval_dir / "inputs" / Path(file_name).name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                copied_files.append(str(target))

        prompt_file = eval_dir / "task.json"
        prompt_file.write_text(json.dumps(item, indent=2))

        manifest["evals"].append(
            {
                "id": item["id"],
                "directory": str(eval_dir),
                "task_file": str(prompt_file),
                "copied_files": copied_files,
            }
        )

    (iteration_dir / "benchmark.json").write_text(
        json.dumps(
            {
                "run_summary": {
                    "with_skill": {"pass_rate": None, "time_seconds": None, "tokens": None},
                    args.baseline_name: {"pass_rate": None, "time_seconds": None, "tokens": None},
                    "delta": {},
                }
            },
            indent=2,
        )
    )
    (iteration_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps({"workspace": str(iteration_dir), "eval_count": len(manifest["evals"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
