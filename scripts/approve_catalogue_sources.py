#!/usr/bin/env python3
"""Gate draft catalogue JSONL on explicit, source-specific reuse approval."""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft_jsonl", type=Path)
    parser.add_argument("--source-audit", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    approvals = {}
    with args.source_audit.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            source_id = (row.get("source_id") or "").strip()
            if not source_id:
                continue
            approvals[source_id] = {
                "reviewStatus": (row.get("review_status") or "").strip(),
                "commercialReuseAllowed": (row.get("commercial_reuse_allowed") or "").strip().lower(),
                "redistributionAllowed": (row.get("redistribution_allowed") or "").strip().lower(),
                "sourceUrl": (row.get("source_url") or "").strip(),
                "termsUrl": (row.get("terms_or_license_url") or "").strip(),
                "licenseName": (row.get("license_name") or "").strip(),
                "attributionRequired": (row.get("attribution_required") or "").strip().lower(),
                "publisher": (row.get("publisher") or "").strip(),
            }

    approved_records, errors = [], []
    with args.draft_jsonl.open(encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
                continue
            source = record.get("source") or {}
            source_id = source.get("sourceId")
            approval = approvals.get(source_id)
            if not approval:
                errors.append(f"line {line_no}: source_id {source_id!r} is absent from source audit")
                continue
            if approval["reviewStatus"] != "approved":
                errors.append(f"line {line_no}: source {source_id!r} review_status is not approved")
            if approval["commercialReuseAllowed"] != "yes":
                errors.append(f"line {line_no}: source {source_id!r} lacks explicit commercial reuse approval")
            if approval["redistributionAllowed"] != "yes":
                errors.append(f"line {line_no}: source {source_id!r} lacks explicit redistribution approval")
            if approval["sourceUrl"] != source.get("url"):
                errors.append(f"line {line_no}: record URL does not exactly match audited source URL for {source_id!r}")
            if not approval["termsUrl"] or not approval["licenseName"]:
                errors.append(f"line {line_no}: source {source_id!r} is missing terms URL or licence name")
            if record.get("publicationStatus") != "draft":
                errors.append(f"line {line_no}: only draft records can enter staging")
            if approval["reviewStatus"] == "approved" and approval["commercialReuseAllowed"] == "yes" and approval["redistributionAllowed"] == "yes" and approval["sourceUrl"] == source.get("url") and approval["termsUrl"] and approval["licenseName"] and record.get("publicationStatus") == "draft":
                record["sourceApproval"] = approval
                approved_records.append(record)

    if errors:
        print(json.dumps({"approved": False, "recordsChecked": len(approved_records) + len(errors), "errors": errors}, indent=2))
        return 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in approved_records), encoding="utf-8")
    print(json.dumps({"approved": True, "recordsApproved": len(approved_records), "output": str(args.out)}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
