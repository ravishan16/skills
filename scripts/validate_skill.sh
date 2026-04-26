#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

required_root_files=(
  "README.md"
  "CONTRIBUTING.md"
  "CODE_OF_CONDUCT.md"
  "LICENSE"
)

for file in "${required_root_files[@]}"; do
  [[ -f "$file" ]] || { echo "Missing required file: $file" >&2; exit 1; }
done

[[ -d skills ]] || { echo "Missing skills directory" >&2; exit 1; }

found_skill=0
while IFS= read -r -d '' skill_dir; do
  found_skill=1
  skill_name="$(basename "$skill_dir")"
  skill_file="$skill_dir/SKILL.md"

  [[ -f "$skill_file" ]] || { echo "Missing SKILL.md in $skill_dir" >&2; exit 1; }
  grep -q '^---$' "$skill_file" || { echo "Missing frontmatter markers in $skill_file" >&2; exit 1; }
  grep -q '^name:' "$skill_file" || { echo "Missing name in $skill_file" >&2; exit 1; }
  grep -q '^description:' "$skill_file" || { echo "Missing description in $skill_file" >&2; exit 1; }
  grep -q '^allowed-tools:' "$skill_file" || { echo "Missing allowed-tools in $skill_file" >&2; exit 1; }

  declared_name="$(sed -n 's/^name:[[:space:]]*//p' "$skill_file" | head -1)"
  [[ "$declared_name" == "$skill_name" ]] || {
    echo "Skill name mismatch: folder '$skill_name' vs frontmatter '$declared_name'" >&2
    exit 1
  }

  for subdir in examples evals assets references snippets scripts; do
    [[ -d "$skill_dir/$subdir" ]] || { echo "Missing $subdir directory in $skill_dir" >&2; exit 1; }
  done

  grep -q '^license:' "$skill_file" || { echo "Missing license in $skill_file" >&2; exit 1; }
  grep -q '^compatibility:' "$skill_file" || { echo "Missing compatibility in $skill_file" >&2; exit 1; }
  grep -q '^metadata:' "$skill_file" || { echo "Missing metadata block in $skill_file" >&2; exit 1; }
  grep -q '^[[:space:]]*author:[[:space:]]*Ravishankar Sivasubramaniam' "$skill_file" || {
    echo "Missing required author metadata in $skill_file" >&2
    exit 1
  }
done < <(find skills -mindepth 1 -maxdepth 1 -type d -exec test -f '{}/SKILL.md' ';' -print0 | sort -z)

[[ "$found_skill" -eq 1 ]] || { echo "No skills found" >&2; exit 1; }

[[ -f skills/_template/TEMPLATE.md ]] || { echo "Missing template scaffold file: skills/_template/TEMPLATE.md" >&2; exit 1; }
[[ -f skills/_template/README.md ]] || { echo "Missing template README: skills/_template/README.md" >&2; exit 1; }

echo "Skill structure is valid."
