import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "approve_catalogue_sources.py"

class SourceApprovalGateTests(unittest.TestCase):
    def run_gate(self, review_status, commercial, redistribution, source_url="https://oem.example/variant"):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        draft = root / "draft.jsonl"
        audit = root / "sources.csv"
        output = root / "approved.jsonl"
        record = {
            "id": "test-variant-123456789abc",
            "entityType": "variant",
            "publicationStatus": "draft",
            "source": {"sourceId": "oem_test", "url": source_url, "retrievedAt": "2026-11-06T00:00:00Z"}
        }
        draft.write_text(json.dumps(record) + "\n", encoding="utf-8")
        fields = ["source_id", "publisher", "source_url", "terms_or_license_url", "license_name",
                  "commercial_reuse_allowed", "redistribution_allowed", "attribution_required", "review_status"]
        with audit.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerow({
                "source_id": "oem_test", "publisher": "Example OEM", "source_url": "https://oem.example/variant",
                "terms_or_license_url": "https://oem.example/terms", "license_name": "OEM written permission",
                "commercial_reuse_allowed": commercial, "redistribution_allowed": redistribution,
                "attribution_required": "yes", "review_status": review_status
            })
        result = subprocess.run([sys.executable, str(SCRIPT), str(draft), "--source-audit", str(audit), "--out", str(output)],
                                capture_output=True, text=True)
        return result, output

    def test_explicit_approval_passes_and_embeds_evidence(self):
        result, output = self.run_gate("approved", "yes", "yes")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        approved = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(approved["sourceApproval"]["reviewStatus"], "approved")
        self.assertEqual(approved["sourceApproval"]["redistributionAllowed"], "yes")

    def test_unknown_or_unapproved_rights_fail_closed(self):
        result, output = self.run_gate("review_required", "unknown", "unknown")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())

    def test_source_url_must_match_exactly(self):
        result, output = self.run_gate("approved", "yes", "yes", source_url="https://oem.example/other")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())

if __name__ == "__main__":
    unittest.main()
