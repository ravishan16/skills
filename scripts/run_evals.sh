#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

for skill_dir in skills/*; do
  [[ -d "$skill_dir" ]] || continue
  [[ "$(basename "$skill_dir")" == "_template" ]] && continue

  eval_json="$skill_dir/evals/evals.json"
  if [[ ! -f "$eval_json" ]]; then
    echo "Missing structured eval file: $eval_json" >&2
    exit 1
  fi

  python3 - "$eval_json" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
data = json.loads(path.read_text())

if not isinstance(data, dict):
    raise SystemExit(f"{path}: eval file must contain a JSON object")

if not data.get("skill_name"):
    raise SystemExit(f"{path}: missing skill_name")

evals = data.get("evals")
if not isinstance(evals, list) or not evals:
    raise SystemExit(f"{path}: evals must be a non-empty list")

required = {"id", "prompt", "expected_output"}
for idx, item in enumerate(evals, start=1):
    if not isinstance(item, dict):
        raise SystemExit(f"{path}: eval #{idx} must be an object")
    missing = sorted(required - item.keys())
    if missing:
        raise SystemExit(f"{path}: eval #{idx} missing fields: {', '.join(missing)}")
    assertions = item.get("assertions")
    if assertions is not None and (not isinstance(assertions, list) or not assertions):
        raise SystemExit(f"{path}: eval #{idx} assertions must be a non-empty list when present")
PY
done

echo "Eval layout checks passed."
