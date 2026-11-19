#!/usr/bin/env python3
"""Fail-closed validation for Motivo's source registry.

A source is publish-eligible only when commercial reuse and redistribution are
explicitly allowed and the source has been reviewed. Unknown rights are not approval.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_COLUMNS = {
    "source_id", "publisher", "source_url", "terms_or_license_url",
    "license_name", "commercial_reuse_allowed", "redistribution_allowed",
    "attribution_required", "coverage_type", "geography", "last_checked_at",
    "ingestion_method", "review_status",
}
TRUE = {"yes", "true"}
FALSE = {"no", "false"}
ALLOWED_RIGHTS = TRUE | FALSE | {"unknown", "pending", "not_applicable"}
PLACEHOLDER = re.compile(r"example\\.com|to be reviewed|placeholder|sample", re.I)


def https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="data/source-registry.csv")
    parser.add_argument("--require-approved", action="store_true",
                        help="fail unless at least one source is approved for redistribution")
    args = parser.parse_args()
    path = Path(args.registry)
    if not path.exists():
        print(f"ERROR: registry not found: {path}")
        return 2

    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    eligible = 0
    checked = 0

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - headers)
        if missing:
            print("ERROR: missing columns: " + ", ".join(missing))
            return 2

        for line, raw in enumerate(reader, start=2):
            row = {key: (value or "").strip() for key, value in raw.items() if key}
            if not any(row.values()):
                continue
            checked += 1
            source_id = row.get("source_id", "")
            if not source_id:
                errors.append(f"line {line}: source_id is required")
                continue
            if source_id in seen_ids:
                errors.append(f"line {line}: duplicate source_id '{source_id}'")
            seen_ids.add(source_id)

            # The audit template's illustrative example is never treated as a source.
            if source_id.startswith("example_") or PLACEHOLDER.search(" ".join(row.values())):
                errors.append(f"line {line}: placeholder/example row must not be in source-registry.csv")
                continue

            for field in ("publisher", "license_name", "coverage_type", "geography", "ingestion_method"):
                if not row.get(field):
                    errors.append(f"line {line}: {field} is required")

            for field in ("source_url", "terms_or_license_url"):
                value = row.get(field, "")
                if not https_url(value):
                    errors.append(f"line {line}: {field} must be a valid HTTPS URL")

            url = row.get("source_url", "")
            if url and url in seen_urls:
                errors.append(f"line {line}: duplicate source_url '{url}'")
            if url:
                seen_urls.add(url)

            for field in ("commercial_reuse_allowed", "redistribution_allowed", "attribution_required"):
                value = row.get(field, "").lower()
                if value not in ALLOWED_RIGHTS:
                    errors.append(f"line {line}: {field} must be yes/no/unknown/pending/not_applicable")

            checked_date = row.get("last_checked_at", "")
            try:
                date.fromisoformat(checked_date)
            except ValueError:
                errors.append(f"line {line}: last_checked_at must use YYYY-MM-DD")

            rights_ok = (
                row.get("commercial_reuse_allowed", "").lower() in TRUE
                and row.get("redistribution_allowed", "").lower() in TRUE
                and row.get("review_status", "").lower() == "approved"
                and bool(row.get("license_name"))
                and https_url(row.get("terms_or_license_url", ""))
            )
            if rights_ok:
                eligible += 1

    if args.require_approved and eligible == 0:
        errors.append("no source is approved for both commercial reuse and redistribution")

    print(f"Source registry: {checked} rows checked; {eligible} redistribution-eligible source(s)")
    if errors:
        for error in errors:
            print("ERROR: " + error)
        return 1
    if eligible == 0:
        print("WARNING: no approved source yet; no source data may be imported or published")
    print("Source registry structure and row checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
