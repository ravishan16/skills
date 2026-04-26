#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

grep -q '^# skills$' README.md || { echo "README must start with '# skills'" >&2; exit 1; }
grep -q 'skills/_template/' CONTRIBUTING.md || { echo "CONTRIBUTING.md should reference skills/_template/" >&2; exit 1; }

for doc in docs/style-guide.md docs/security.md docs/publishing.md; do
  [[ -f "$doc" ]] || { echo "Missing documentation file: $doc" >&2; exit 1; }
done

for skill in skills/*/SKILL.md; do
  grep -q '^## ' "$skill" || { echo "Expected section headings in $skill" >&2; exit 1; }
done

echo "Documentation checks passed."

