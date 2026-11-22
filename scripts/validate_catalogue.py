#!/usr/bin/env python3
"""Fail-closed validation for Motivo's normalized India catalogue."""
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
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def valid_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


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
        data = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid catalogue JSON: {exc}")
        return 2
    if not isinstance(data, dict) or data.get("schemaVersion") != 1 or data.get("market") != "IN":
        print("ERROR: root must contain schemaVersion=1 and market='IN'")
        return 2

    errors: list[str] = []
    sources: dict[str, dict[str, str]] = {}
    registry = Path(args.registry)
    if not registry.exists():
        errors.append(f"source registry not found: {registry}")
    else:
        with registry.open(newline="", encoding="utf-8-sig") as handle:
            for line, row in enumerate(csv.DictReader(handle), 2):
                sid = (row.get("source_id") or "").strip()
                if not sid:
                    continue
                if sid in sources:
                    errors.append(f"source registry line {line}: duplicate source_id {sid}")
                sources[sid] = {k: (v or "").strip() for k, v in row.items()}

    # Publishing independently authored factual records is reviewed separately
    # from reusing the source's expressive content (images, prose, tables, PDFs).
    # A reviewer must explicitly approve this source for factual-reference use.
    # Commercial/redistribution permissions remain recorded for copied assets,
    # source extracts, and other licensed-content workflows; they are not silently
    # inferred from factual-use approval.
    factual_sources = {
        sid for sid, row in sources.items()
        if row.get("factual_use_review", "").lower() == "approved"
        and row.get("factual_use_basis", "").lower() == "independently_authored_facts"
        and row.get("terms_or_license_url", "").startswith("https://")
    }

    ids: dict[str, set[str]] = {}
    records: dict[str, list[dict[str, Any]]] = {}
    published_count = 0
    total = 0
    for collection in COLLECTIONS:
        items = data.get(collection, [])
        if not isinstance(items, list):
            errors.append(f"{collection}: must be an array")
            items = []
        records[collection] = [x for x in items if isinstance(x, dict)]
        ids[collection] = set()
        for index, item in enumerate(items):
            total += 1
            label = f"{collection}[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{label}: record must be an object")
                continue
            key = "variantId" if collection == "specifications" else "id"
            rid = item.get(key)
            if not isinstance(rid, str) or not rid.strip():
                errors.append(f"{label}: {key} is required")
            elif rid in ids[collection]:
                errors.append(f"{label}: duplicate {key} {rid}")
            else:
                ids[collection].add(rid)

    def refs_ok(refs: Any, label: str, required: bool) -> None:
        if not isinstance(refs, list):
            errors.append(f"{label}: sourceRefs must be an array")
            return
        if required and not refs:
            errors.append(f"{label}: published data requires sourceRefs")
        for n, ref in enumerate(refs):
            if not isinstance(ref, dict):
                errors.append(f"{label}: sourceRefs[{n}] must be an object")
                continue
            sid = ref.get("sourceId")
            if sid not in sources:
                errors.append(f"{label}: unknown sourceId {sid!r}")
                continue
            if ref.get("url") != sources[sid].get("source_url"):
                errors.append(f"{label}: source URL mismatch for {sid}")
            if required and sid not in factual_sources:
                errors.append(f"{label}: source {sid} is not approved for independently authored factual publication")
            if not valid_date(ref.get("retrievedAt")):
                errors.append(f"{label}: sourceRefs[{n}].retrievedAt must be YYYY-MM-DD")

    def sourced_value(value: Any, label: str, required: bool) -> None:
        if not isinstance(value, dict) or "value" not in value:
            errors.append(f"{label}: expected SourcedValue object")
            return
        refs_ok(value.get("sourceRefs"), label, required and value.get("value") is not None)
        if not valid_date(value.get("lastVerifiedAt")):
            errors.append(f"{label}: lastVerifiedAt must be YYYY-MM-DD")

    brand_by_id = {x.get("id"): x for x in records["brands"]}
    model_by_id = {x.get("id"): x for x in records["models"]}
    variant_by_id = {x.get("id"): x for x in records["variants"]}

    for i, x in enumerate(records["brands"]):
        label = f"brands[{i}]"
        if not x.get("name") or x.get("market") != "IN":
            errors.append(f"{label}: name and market='IN' are required")
        if x.get("status") not in STATUSES:
            errors.append(f"{label}: invalid status")
        pub = x.get("status") == "published"
        published_count += int(pub)
        refs_ok(x.get("sourceRefs"), label, pub)
        if not valid_date(x.get("lastVerifiedAt")):
            errors.append(f"{label}: invalid lastVerifiedAt")

    for i, x in enumerate(records["models"]):
        label = f"models[{i}]"
        if x.get("brandId") not in brand_by_id:
            errors.append(f"{label}: brandId must reference an existing brand")
        if x.get("bodyStyle") not in BODY_STYLES:
            errors.append(f"{label}: invalid bodyStyle")
        if x.get("status") not in STATUSES:
            errors.append(f"{label}: invalid status")
        pub = x.get("status") == "published"
        published_count += int(pub)
        refs_ok(x.get("sourceRefs"), label, pub)
        if not valid_date(x.get("lastVerifiedAt")):
            errors.append(f"{label}: invalid lastVerifiedAt")

    for i, x in enumerate(records["variants"]):
        label = f"variants[{i}]"
        if x.get("modelId") not in model_by_id:
            errors.append(f"{label}: modelId must reference an existing model")
        if x.get("fuel") not in FUELS or x.get("transmission") not in TRANSMISSIONS:
            errors.append(f"{label}: invalid fuel or transmission")
        year = x.get("modelYear")
        if not isinstance(year, int) or isinstance(year, bool) or not 1990 <= year <= 2100:
            errors.append(f"{label}: modelYear must be an integer from 1990 to 2100")
        if x.get("status") not in STATUSES:
            errors.append(f"{label}: invalid status")
        pub = x.get("status") == "published"
        published_count += int(pub)
        refs_ok(x.get("sourceRefs"), label, pub)
        if not valid_date(x.get("lastVerifiedAt")):
            errors.append(f"{label}: invalid lastVerifiedAt")

    for i, x in enumerate(records["specifications"]):
        label = f"specifications[{i}]"
        variant = variant_by_id.get(x.get("variantId"))
        if not variant:
            errors.append(f"{label}: variantId must reference an existing variant")
        parent_published = bool(variant and variant.get("status") == "published")
        for group in ("dimensionsMm", "performance", "equipment", "warranty"):
            fields = x.get(group, {})
            if not isinstance(fields, dict):
                errors.append(f"{label}: {group} must be an object")
                continue
            for key, value in fields.items():
                sourced_value(value, f"{label}.{group}.{key}", parent_published)

    for i, x in enumerate(records["prices"]):
        label = f"prices[{i}]"
        variant = variant_by_id.get(x.get("variantId"))
        if not variant:
            errors.append(f"{label}: variantId must reference an existing variant")
        pub = bool(variant and variant.get("status") == "published")
        if x.get("market") != "IN" or x.get("priceType") not in {"ex_showroom", "on_road"}:
            errors.append(f"{label}: invalid market or priceType")
        amount = x.get("amountInr")
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            errors.append(f"{label}: amountInr must be a positive number")
        if x.get("classification") not in {"official", "estimated", "user_reported"}:
            errors.append(f"{label}: invalid classification")
        if not valid_date(x.get("effectiveDate")) or not valid_date(x.get("observedAt")) or not valid_date(x.get("lastVerifiedAt")):
            errors.append(f"{label}: invalid price date")
        refs_ok(x.get("sourceRefs"), label, pub)

    for i, x in enumerate(records["safetyRatings"]):
        label = f"safetyRatings[{i}]"
        model = model_by_id.get(x.get("modelId"))
        if not model:
            errors.append(f"{label}: modelId must reference an existing model")
        if not x.get("agency") or not x.get("protocol") or not x.get("applicabilityNotes"):
            errors.append(f"{label}: agency, protocol and applicabilityNotes are required")
        refs_ok(x.get("sourceRefs"), label, bool(model and model.get("status") == "published"))
        if not valid_date(x.get("lastVerifiedAt")) or not valid_date(x.get("testDate")):
            errors.append(f"{label}: invalid testDate or lastVerifiedAt")

    if args.require_published and published_count == 0:
        errors.append("no published brands/models/variants found")
    print(f"Catalogue: {total} records checked; {published_count} published brand/model/variant records; {len(factual_sources)} factual-publication-approved sources")
    if errors:
        for error in errors:
            print("ERROR: " + error)
        return 1
    print("Catalogue structure and provenance checks passed.")
    if published_count == 0:
        print("INFO: empty catalogue is valid for bootstrap; no vehicle data is publishable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
