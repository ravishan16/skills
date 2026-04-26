#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a Markdown data-analysis report from a JSON payload.",
        epilog=(
            "Examples:\n"
            "  python3 scripts/render_report.py --input-json report.json\n"
            "  python3 scripts/render_report.py --input-json report.json --output report.md"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--input-json", required=True, help="Path to JSON input payload")
    parser.add_argument("--output", help="Optional path to write Markdown output")
    return parser


def list_block(items: list[str]) -> list[str]:
    if not items:
        return ["- None provided"]
    return [f"- {item}" for item in items]


def render(payload: dict[str, object]) -> str:
    overview = payload.get("dataset_overview", {})
    schema = payload.get("schema_and_quality_notes", {})
    meaning = payload.get("dataset_meaning", {})
    answerable = payload.get("questions_this_data_can_answer", [])
    unanswered = payload.get("questions_this_data_cannot_answer_yet", [])
    findings = payload.get("findings", [])
    artifacts = payload.get("artifacts", {})
    recommendations = payload.get("recommendations", [])
    ambiguities = payload.get("ambiguities_and_assumptions", {})

    lines = [
        "# Data analysis report",
        "",
        "## Dataset overview",
        "",
        f"- Source: {overview.get('source', '')}",
        f"- Format: {overview.get('format', '')}",
        f"- Rows: {overview.get('rows', '')}",
        f"- Columns: {overview.get('columns', '')}",
        f"- Selected strategy: {overview.get('selected_strategy', '')}",
        f"- Why this strategy was chosen: {overview.get('strategy_reason', '')}",
        "",
        "## Schema and quality notes",
        "",
        f"- Key column types: {schema.get('key_column_types', '')}",
        f"- Null or missing data observations: {schema.get('null_observations', '')}",
        f"- Header or schema issues: {schema.get('schema_issues', '')}",
        "",
        "## What this data appears to represent",
        "",
        f"- Likely dataset type or grain: {meaning.get('dataset_type_or_grain', '')}",
        f"- Likely key identifiers: {meaning.get('key_identifiers', '')}",
        f"- Likely measures: {meaning.get('measures', '')}",
        f"- Likely dimensions or status fields: {meaning.get('dimensions_or_statuses', '')}",
        f"- Confidence level: {meaning.get('confidence', '')}",
        "",
        "## Questions this data can likely answer",
        "",
        *list_block(answerable if isinstance(answerable, list) else []),
        "",
        "## Questions this data cannot answer yet",
        "",
        *list_block(unanswered if isinstance(unanswered, list) else []),
        "",
        "## Ambiguities and assumptions",
        "",
        f"- Semantic ambiguities: {ambiguities.get('semantic_ambiguities', '')}",
        f"- Domain context needed: {ambiguities.get('domain_context_needed', '')}",
        "",
        "## Findings",
        "",
        *list_block(findings if isinstance(findings, list) else []),
        "",
        "## Artifacts",
        "",
        f"- Written outputs: {artifacts.get('written_outputs', '')}",
        f"- Transformation record: {artifacts.get('transformation_record', '')}",
        "",
        "## Recommendations",
        "",
        *list_block(recommendations if isinstance(recommendations, list) else []),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    input_path = Path(args.input_json)

    if not input_path.exists():
        print(f"Error: input JSON not found: {input_path}", file=sys.stderr)
        return 3

    payload = json.loads(input_path.read_text())
    markdown = render(payload)

    if args.output:
        Path(args.output).write_text(markdown)
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

