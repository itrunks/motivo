#!/usr/bin/env python3
"""Check exact URL/source_id linkage across model and variant audit rows."""
import argparse
import csv
import sys
from pathlib import Path

def read(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=Path("data/source-registry.csv"))
    parser.add_argument("--crosswalk", type=Path, default=Path("data/audit-source-crosswalk.csv"))
    parser.add_argument("--models", type=Path, default=Path("data/current-model-audit.csv"))
    parser.add_argument("--variants", type=Path, default=Path("data/variant-source-audit.csv"))
    args = parser.parse_args()

    registry = read(args.registry)
    crosswalk = read(args.crosswalk)
    models = read(args.models)
    variants = read(args.variants)
    errors = []
    by_url = {}
    by_id = {}
    for line, row in enumerate(registry, 2):
        url, sid = row.get("source_url", "").strip(), row.get("source_id", "").strip()
        if not url or not sid:
            errors.append(f"registry line {line}: source_url and source_id are required")
            continue
        if url in by_url:
            errors.append(f"registry line {line}: duplicate source_url {url}")
        if sid in by_id and by_id[sid] != url:
            errors.append(f"registry line {line}: source_id collision {sid}")
        by_url[url], by_id[sid] = sid, url

    expected = {("model", r.get("brand_id"), r.get("model_name"), r.get("official_source_url")) for r in models}
    expected |= {("variant", r.get("brand_id"), r.get("model_name"), r.get("official_variant_source_url")) for r in variants}
    actual = set()
    for line, row in enumerate(crosswalk, 2):
        key = (row.get("audit_type"), row.get("brand_id"), row.get("model_name"), row.get("source_url"))
        sid = row.get("source_id", "").strip()
        if key in actual:
            errors.append(f"crosswalk line {line}: duplicate audit mapping {key}")
        actual.add(key)
        if not sid or by_url.get(key[3]) != sid:
            errors.append(f"crosswalk line {line}: source_id does not match registry URL")
    missing, extra = expected - actual, actual - expected
    if missing:
        errors.append(f"{len(missing)} audit rows missing from crosswalk")
    if extra:
        errors.append(f"{len(extra)} unexpected crosswalk rows")
    result = {
        "registrySources": len(registry),
        "modelAuditRows": len(models),
        "variantAuditRows": len(variants),
        "crosswalkRows": len(crosswalk),
        "missingOrInvalidMappings": len(errors),
        "errors": errors,
        "rightsApprovedSources": sum(1 for r in registry if r.get("review_status") == "approved" and r.get("commercial_reuse_allowed") == "yes" and r.get("redistribution_allowed") == "yes"),
        "productionImportApproved": False,
    }
    print(result)
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
