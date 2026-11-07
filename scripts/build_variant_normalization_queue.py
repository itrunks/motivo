#!/usr/bin/env python3
"""Build a source-linked, non-importable work queue for manual variant normalization."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

FIELDS = [
    "work_item_id", "brand_id", "model_name", "source_id", "source_url",
    "source_checked_at", "audit_status", "raw_variant_names_observed",
    "raw_price_observation", "raw_audit_notes", "source_review_status",
    "commercial_reuse_allowed", "redistribution_allowed", "terms_or_license_url",
    "license_name", "normalization_status", "normalized_variant_names",
    "normalized_engine", "fuel", "transmission", "body_style", "model_year",
    "normalized_price_rows", "reviewer_notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variants", type=Path, default=Path("data/variant-source-audit.csv"))
    parser.add_argument("--crosswalk", type=Path, default=Path("data/audit-source-crosswalk.csv"))
    parser.add_argument("--registry", type=Path, default=Path("data/source-registry.csv"))
    parser.add_argument("--out", type=Path, default=Path("data/variant-normalization-workqueue.csv"))
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    try:
        variants = read_csv(args.variants)
        crosswalk_rows = read_csv(args.crosswalk)
        registry_rows = read_csv(args.registry)
    except OSError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2

    crosswalk: dict[tuple[str, str, str], str] = {}
    errors: list[str] = []
    for line, row in enumerate(crosswalk_rows, 2):
        if row.get("audit_type") != "variant":
            continue
        key = (row.get("brand_id", "").strip(), row.get("model_name", "").strip(),
               row.get("source_url", "").strip())
        if key in crosswalk:
            errors.append(f"crosswalk line {line}: duplicate variant mapping for {key}")
        crosswalk[key] = row.get("source_id", "").strip()

    registry: dict[str, dict[str, str]] = {}
    registry_urls: dict[str, str] = {}
    for line, row in enumerate(registry_rows, 2):
        source_id = row.get("source_id", "").strip()
        source_url = row.get("source_url", "").strip()
        if not source_id or not source_url:
            errors.append(f"registry line {line}: source_id and source_url are required")
            continue
        if source_id in registry:
            errors.append(f"registry line {line}: duplicate source_id {source_id!r}")
            continue
        if source_url in registry_urls:
            errors.append(f"registry line {line}: duplicate source_url {source_url!r}")
            continue
        registry[source_id] = row
        registry_urls[source_url] = source_id

    output_rows: list[dict[str, str]] = []
    seen_work_ids: set[str] = set()
    for line, row in enumerate(variants, 2):
        brand = row.get("brand_id", "").strip()
        model = row.get("model_name", "").strip()
        url = row.get("official_variant_source_url", "").strip()
        key = (brand, model, url)
        source_id = crosswalk.get(key)
        if not source_id:
            errors.append(f"variant audit line {line}: exact source crosswalk mapping missing for {key}")
            continue
        source = registry.get(source_id)
        if not source:
            errors.append(f"variant audit line {line}: source_id {source_id!r} missing from registry")
            continue
        if source.get("source_url", "").strip() != url:
            errors.append(f"variant audit line {line}: registry URL mismatch for source_id {source_id!r}")
            continue

        work_id = f"variant-review-{line - 1:04d}"
        if work_id in seen_work_ids:
            errors.append(f"variant audit line {line}: duplicate work item {work_id}")
            continue
        seen_work_ids.add(work_id)
        output_rows.append({
            "work_item_id": work_id,
            "brand_id": brand,
            "model_name": model,
            "source_id": source_id,
            "source_url": url,
            "source_checked_at": row.get("source_checked_at", "").strip(),
            "audit_status": row.get("audit_status", "").strip(),
            "raw_variant_names_observed": row.get("variant_names_observed", ""),
            "raw_price_observation": row.get("price_observation", ""),
            "raw_audit_notes": row.get("notes", ""),
            "source_review_status": source.get("review_status", "").strip(),
            "commercial_reuse_allowed": source.get("commercial_reuse_allowed", "").strip(),
            "redistribution_allowed": source.get("redistribution_allowed", "").strip(),
            "terms_or_license_url": source.get("terms_or_license_url", "").strip(),
            "license_name": source.get("license_name", "").strip(),
            "normalization_status": "needs_manual_review",
            "normalized_variant_names": "",
            "normalized_engine": "",
            "fuel": "",
            "transmission": "",
            "body_style": "",
            "model_year": "",
            "normalized_price_rows": "",
            "reviewer_notes": "",
        })

    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    rights = Counter(row["source_review_status"] for row in output_rows)
    report = {
        "ok": True,
        "work_items": len(output_rows),
        "source_mappings_verified": len(output_rows),
        "normalization_status": "needs_manual_review",
        "source_review_status_counts": dict(rights),
        "import_ready_records": 0,
        "firestore_write_performed": False,
        "publication_performed": False,
        "output": str(args.out),
    }
    report_path = args.report or args.out.with_suffix(".report.json")
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
