#!/usr/bin/env python3
"""Validate Motivo's source-attributed India current-car catalogue CSV.

This tool is intentionally offline and dependency-free. It normalizes approved
CSV-shaped input into draft JSONL; it does not write to Firestore or publish data.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED = {
    "entity_type", "source_id", "source_url", "retrieved_at", "market",
    "brand_name", "model_name", "variant_name", "model_year", "fuel",
    "transmission", "body_style", "state_code", "city", "price_type",
    "amount_inr", "price_classification", "effective_date", "publication_status",
}
ENUMS = {
    "entity_type": {"variant", "price"},
    "market": {"IN"},
    "fuel": {"petrol", "diesel", "cng", "lpg", "mild_hybrid", "strong_hybrid", "plug_in_hybrid", "electric"},
    "transmission": {"manual", "amt", "cvt", "dct", "torque_converter", "single_speed", "other"},
    "body_style": {"hatchback", "sedan", "compact_suv", "mid_size_suv", "full_size_suv", "mpv", "muv", "crossover", "coupe", "convertible", "pickup", "other"},
    "price_type": {"ex_showroom", "on_road"},
    "price_classification": {"official", "estimated", "user_reported"},
    "publication_status": {"draft"},
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def stable_id(*parts: str) -> str:
    raw = "|".join(p.strip().casefold() for p in parts)
    slug = re.sub(r"[^a-z0-9]+", "-", raw).strip("-")[:48] or "record"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return f"{slug}-{digest}"


def valid_date(value: str) -> bool:
    if not DATE_RE.match(value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("data/staging"))
    parser.add_argument("--current-year", type=int, default=date.today().year)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    output: list[dict[str, Any]] = []
    seen: set[tuple[str, ...]] = set()
    counts: Counter[str] = Counter()

    try:
        with args.csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = set(reader.fieldnames or [])
            missing = sorted(REQUIRED - headers)
            if missing:
                errors.append("Missing columns: " + ", ".join(missing))
                rows = []
            else:
                rows = list(reader)
    except OSError as exc:
        print(f"Cannot read input: {exc}", file=sys.stderr)
        return 2

    for line, raw in enumerate(rows, start=2):
        row = {key: (value or "").strip() for key, value in raw.items() if key}
        row_errors: list[str] = []
        for field in ("entity_type", "source_id", "source_url", "retrieved_at", "market", "brand_name", "model_name", "variant_name", "publication_status"):
            if not row.get(field):
                row_errors.append(f"{field} is required")
        for field, allowed in ENUMS.items():
            if row.get(field) and row[field] not in allowed:
                row_errors.append(f"{field} must be one of: {', '.join(sorted(allowed))}")

        if row.get("source_url") and not row["source_url"].startswith(("https://", "http://")):
            row_errors.append("source_url must be an http(s) URL")
        if row.get("retrieved_at"):
            try:
                datetime.fromisoformat(row["retrieved_at"].replace("Z", "+00:00"))
            except ValueError:
                row_errors.append("retrieved_at must be an ISO-8601 timestamp")

        try:
            model_year = int(row.get("model_year", ""))
            if model_year < args.current_year - 1 or model_year > args.current_year + 1:
                row_errors.append(f"model_year must be within {args.current_year - 1}..{args.current_year + 1} for current catalogue intake")
        except ValueError:
            model_year = None
            row_errors.append("model_year must be an integer")

        entity_type = row.get("entity_type")
        if entity_type == "variant":
            for field in ("fuel", "transmission", "body_style"):
                if not row.get(field):
                    row_errors.append(f"{field} is required for variant rows")
            if any(row.get(field) for field in ("price_type", "amount_inr", "state_code", "city")):
                warnings.append(f"row {line}: price columns on a variant row are ignored; add a separate price row")
        elif entity_type == "price":
            for field in ("price_type", "amount_inr", "price_classification", "effective_date"):
                if not row.get(field):
                    row_errors.append(f"{field} is required for price rows")
            if row.get("price_type") == "on_road" and (not row.get("state_code") or not row.get("city")):
                row_errors.append("on_road prices require state_code and city")
            if row.get("price_type") == "ex_showroom" and not row.get("state_code") and not row.get("city"):
                warnings.append(f"row {line}: national ex-showroom price; verify source explicitly states it is national")
            try:
                amount = float(row.get("amount_inr", ""))
                if amount <= 0:
                    row_errors.append("amount_inr must be greater than zero")
            except ValueError:
                amount = None
                row_errors.append("amount_inr must be numeric")
            if row.get("effective_date") and not valid_date(row["effective_date"]):
                row_errors.append("effective_date must be YYYY-MM-DD")

        if row.get("publication_status") != "draft":
            row_errors.append("imports must remain draft until reviewed")
        if row_errors:
            errors.extend(f"row {line}: {message}" for message in row_errors)
            continue

        key = (entity_type, row["brand_name"].casefold(), row["model_name"].casefold(),
               row["variant_name"].casefold(), str(model_year), row.get("price_type", ""),
               row.get("state_code", "").upper(), row.get("city", "").casefold(),
               row.get("effective_date", ""))
        if key in seen:
            errors.append(f"row {line}: duplicate entity key {key}")
            continue
        seen.add(key)

        record_id = stable_id(*key)
        record: dict[str, Any] = {
            "id": record_id,
            "entityType": entity_type,
            "market": "IN",
            "brandName": row["brand_name"],
            "modelName": row["model_name"],
            "variantName": row["variant_name"],
            "modelYear": model_year,
            "publicationStatus": "draft",
            "source": {
                "sourceId": row["source_id"],
                "url": row["source_url"],
                "retrievedAt": row["retrieved_at"],
            },
        }
        if entity_type == "variant":
            record.update({"fuel": row["fuel"], "transmission": row["transmission"], "bodyStyle": row["body_style"]})
        else:
            record.update({
                "priceType": row["price_type"],
                "amountInr": amount,
                "classification": row["price_classification"],
                "effectiveDate": row["effective_date"],
                "stateCode": row.get("state_code") or None,
                "city": row.get("city") or None,
            })
        output.append(record)
        counts[entity_type] += 1

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.csv_file.stem
    jsonl_path = args.out_dir / f"{stem}.draft.jsonl"
    report_path = args.out_dir / f"{stem}.validation.json"
    jsonl_path.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in output), encoding="utf-8")
    report = {
        "input": str(args.csv_file),
        "validatedAt": datetime.now(timezone.utc).isoformat(),
        "scope": {"market": "IN", "modelCoverage": "current", "currentModelYearWindow": [args.current_year - 1, args.current_year + 1]},
        "acceptedDraftRows": len(output),
        "counts": dict(counts),
        "errors": errors,
        "warnings": warnings,
        "firestoreWritePerformed": False,
        "publicationPerformed": False,
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Draft JSONL: {jsonl_path}")
    print(f"Validation report: {report_path}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
