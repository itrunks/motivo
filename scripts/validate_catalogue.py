#!/usr/bin/env python3
"""Validate Motivo's normalized India catalogue before import/publish.

Uses only Python's standard library. Publication is fail-closed: every published
record and every non-null sourced field must point to a registry source whose
commercial reuse and redistribution rights are explicitly approved.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

COLLECTIONS = ("brands", "models", "variants", "specifications", "prices", "safetyRatings")
STATUSES = {"draft", "review", "published", "rejected"}
FUELS = {"petrol", "diesel", "cng", "lpg", "mild_hybrid", "strong_hybrid", "plug_in_hybrid", "electric"}
TRANSMISSIONS = {"manual", "amt", "cvt", "dct", "torque_converter", "single_speed", "other"}
BODY_STYLES = {"hatchback", "sedan", "compact_suv", "mid_size_suv", "full_size_suv", "mpv", "muv", "crossover", "coupe", "convertible", "pickup", "other"}
DATE_RE = re.compile(r"^\\d{4}-\\d{2}-\\d{2}$")


def valid_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def load_sources(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    sources: dict[str, dict[str, str]] = {}
    if not path.exists():
        return {}, [f"source registry not found: {path}"]
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for line, row in enumerate(reader, 2):
            sid = (row.get("source_id") or "").strip()
            if not sid:
                continue
            if sid in sources:
                errors.append(f"source registry line {line}: duplicate source_id {sid}")
            sources[sid] = {k: (v or "").strip() for k, v in row.items()}
    return sources, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalogue", default="data/catalogue.json")
    parser.add_argument("--registry", default="data/source-registry.csv")
    parser.add_argument("--require-published", action="store_true")
    args = parser.parse_args()

    path = Path(args.catalogue)
    if not path.exists():
        print(f"ERROR: catalogue not found: {path}")
        return 2
    try:
        catalogue = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid catalogue JSON: {exc}")
        return 2
    if not isinstance(catalogue, dict) or catalogue.get("schemaVersion") != 1:
        print("ERROR: catalogue root must be an object with schemaVersion=1")
        return 2

    sources, errors = load_sources(Path(args.registry))
    approved = {
        sid for sid, source in sources.items()
        if source.get("commercial_reuse_allowed", "").lower() in {"yes", "true"}
        and source.get("redistribution_allowed", "").lower() in {"yes", "true"}
        and source.get("review_status", "").lower() == "approved"
        and source.get("terms_or_license_url", "").startswith("https://")
    }

    ids: dict[str, set[str]] = {}
    total = 0
    published = 0

    def check_refs(refs: Any, label: str, required: bool) -> None:
        if not isinstance(refs, list):
            errors.append(f"{label}: sourceRefs must be an array")
            return
        if required and not refs:
            errors.append(f"{label}: published record/value requires sourceRefs")
        for index, ref in enumerate(refs):
            if not isinstance(ref, dict):
                errors.append(f"{label}: sourceRefs[{index}] must be an object")
                continue
            sid = ref.get("sourceId")
            if sid not in sources:
                errors.append(f"{label}: unknown sourceId {sid!r}")
                continue
            if ref.get("url") != sources[sid].get("source_url"):
                errors.append(f"{label}: URL does not match registry for source {sid}")
            if required and sid not in approved:
                errors.append(f"{label}: source {sid} is not approved for redistribution")
            if not valid_date(ref.get("retrievedAt")):
                errors.append(f"{label}: sourceRefs[{index}].retrievedAt must be YYYY-MM-DD")

    def check_sourced(value: Any, label: str, required: bool) -> None:
        if not isinstance(value, dict) or "value" not in value:
            errors.append(f"{label}: sourced value must contain value and sourceRefs")
            return
        refs = value.get("sourceRefs", [])
        check_refs(refs, label, required and value.get("value") is not None)
        if not valid_date(value.get("lastVerifiedAt")):
            errors.append(f"{label}: lastVerifiedAt must be YYYY-MM-DD")

    for collection in COLLECTIONS:
        records = catalogue.get(collection, [])
        if not isinstance(records, list):
            errors.append(f"{collection}: must be an array")
            continue
        ids[collection] = set()
        for index, record in enumerate(records):
            total += 1
            label = f"{collection}[{index}]"
            if not isinstance(record, dict):
                errors.append(f"{label}: record must be an object")
                continue
            rid = record.get("id") if collection != "specifications" else record.get("variantId")
            if not isinstance(rid, str) or not rid.strip():
                errors.append(f"{label}: id/variantId is required")
            elif rid in ids[collection]:
                errors.append(f"{label}: duplicate id {rid}")
            else:
                ids[collection].add(rid)

            status = record.get("status", "draft")
            if collection != "specifications" and status not in STATUSES:
                errors.append(f"{label}: invalid status {status!r}")
            is_published = status == "published"
            if is_published:
                published += 1
            check_refs(record.get("sourceRefs"), label, is_published)
            if not valid_date(record.get("lastVerifiedAt")):
                errors.append(f"{label}: lastVerifiedAt must be YYYY-MM-DD")

            if collection == "brands":
                for field in ("name", "market"):
                    if not record.get(field):
                        errors.append(f"{label}: {field} is required")
                if record.get("market") != "IN":
                    errors.append(f"{label}: market must be IN")
            elif collection == "models":
                if record.get("brandId") not in ids.get("brands", set()):
                    errors.append(f"{label}: brandId must reference an existing brand")
                if record.get("bodyStyle") not in BODY_STYLES:
                    errors.append(f"{label}: invalid bodyStyle")
            elif collection == "variants":
                if record.get("modelId") not in ids.get("models", set()):
                    errors.append(f"{label}: modelId must reference an existing model")
                if record.get("fuel") not in FUELS:
                    errors.append(f"{label}: invalid fuel")
                if record.get("transmission") not in TRANSMISSIONS:
                    errors.append(f"{label}: invalid transmission")
                if not isinstance(record.get("modelYear"), int) or not 1990 <= record.get("modelYear", 0) <= 2100:
                    errors.append(f"{label}: modelYear must be an integer from 1990 to 2100")
            elif collection == "specifications":
                if record.get("variantId") not in ids.get("variants", set()):
                    errors.append(f"{label}: variantId must reference an existing variant")
                for group in ("dimensionsMm", "performance", "equipment", "warranty"):
                    fields = record.get(group, {})
                    if not isinstance(fields, dict):
                        errors.append(f"{label}: {group} must be an object")
                        continue
                    for key, sourced in fields.items():
                        check_sourced(sourced, f"{label}.{group}.{key}", is_published)
            elif collection == "prices":
                if record.get("variantId") not in ids.get("variants", set()):
                    errors.append(f"{label}: variantId must reference an existing variant")
                if record.get("market") != "IN" or record.get("priceType") not in {"ex_showroom", "on_road"}:
                    errors.append(f"{label}: invalid market or priceType")
                if not isinstance(record.get("amountInr"), (int, float)) or record.get("amountInr", 0) <= 0:
                    errors.append(f"{label}: amountInr must be a positive number")
                if record.get("classification") not in {"official", "estimated", "user_reported"}:
                    errors.append(f"{label}: invalid price classification")
                if not valid_date(record.get("effectiveDate")) or not valid_date(record.get("observedAt")):
                    errors.append(f"{label}: effectiveDate and observedAt must be YYYY-MM-DD")
            elif collection == "safetyRatings":
                if record.get("modelId") not in ids.get("models", set()):
                    errors.append(f"{label}: modelId must reference an existing model")
                if not record.get("agency") or not record.get("protocol") or not record.get("applicabilityNotes"):
                    errors.append(f"{label}: agency, protocol and applicabilityNotes are required")

    if args.require_published and published == 0:
        errors.append("no published records found")

    print(f"Catalogue: {total} records checked; {published} published; {len(approved)} approved sources")
    if errors:
        for error in errors:
            print("ERROR: " + error)
        return 1
    print("Catalogue structural and provenance checks passed.")
    if published == 0:
        print("INFO: empty catalogue is valid for bootstrap; nothing is publishable yet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
