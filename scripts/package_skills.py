#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import tarfile
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Package each published skill directory into a tar.gz archive.",
        epilog=(
            "Examples:\n"
            "  python3 scripts/package_skills.py --output-dir dist\n"
            "  python3 scripts/package_skills.py --output-dir dist --repo ravishan16/skills"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    p.add_argument("--output-dir", required=True, help="Directory for packaged skill archives")
    p.add_argument("--repo", default="ravishan16/skills", help="GitHub repo install target")
    return p


def main() -> int:
    args = parser().parse_args()
    root = Path(__file__).resolve().parent.parent
    skills_dir = root / "skills"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    packaged: list[dict[str, str]] = []
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir() and p.name != "_template"):
        archive_path = output_dir / f"{skill_dir.name}.tar.gz"
        with tarfile.open(archive_path, "w:gz") as archive:
            archive.add(skill_dir, arcname=skill_dir.name)
        packaged.append({"skill": skill_dir.name, "archive": str(archive_path)})

    manifest = {
        "repo": args.repo,
        "install_command": f"npx skills add {args.repo}",
        "packaged": packaged,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    (output_dir / "INSTALL.txt").write_text(f"npx skills add {args.repo}\n")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

