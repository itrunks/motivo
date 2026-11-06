import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_variant_normalization_queue.py"


class VariantNormalizationQueueTests(unittest.TestCase):
    def write_csv(self, path, fields, rows):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_builds_source_linked_queue_without_guessing_normalized_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            variants, crosswalk, registry, output = [root / name for name in
                ("variants.csv", "crosswalk.csv", "registry.csv", "queue.csv")]
            self.write_csv(variants,
                ["brand_id", "model_name", "official_variant_source_url", "source_checked_at",
                 "variant_names_observed", "price_observation", "audit_status", "notes"],
                [{"brand_id": "hyundai", "model_name": "Creta",
                  "official_variant_source_url": "https://oem.example/creta",
                  "source_checked_at": "2026-11-06",
                  "variant_names_observed": "Trim A; Trim B",
                  "price_observation": "Price table captured; exact city scope pending",
                  "audit_status": "partial", "notes": "Keep raw evidence"}])
            self.write_csv(crosswalk,
                ["audit_type", "brand_id", "model_name", "source_url", "source_id"],
                [{"audit_type": "variant", "brand_id": "hyundai", "model_name": "Creta",
                  "source_url": "https://oem.example/creta", "source_id": "src_creta"}])
            self.write_csv(registry,
                ["source_id", "source_url", "review_status", "commercial_reuse_allowed",
                 "redistribution_allowed", "terms_or_license_url", "license_name"],
                [{"source_id": "src_creta", "source_url": "https://oem.example/creta",
                  "review_status": "review_required", "commercial_reuse_allowed": "unknown",
                  "redistribution_allowed": "unknown", "terms_or_license_url": "",
                  "license_name": ""}])
            result = subprocess.run([sys.executable, str(SCRIPT), "--variants", str(variants),
                "--crosswalk", str(crosswalk), "--registry", str(registry), "--out", str(output)],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with output.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["raw_variant_names_observed"], "Trim A; Trim B")
            self.assertEqual(rows[0]["source_id"], "src_creta")
            self.assertEqual(rows[0]["source_review_status"], "review_required")
            self.assertEqual(rows[0]["normalization_status"], "needs_manual_review")
            self.assertEqual(rows[0]["fuel"], "")
            self.assertEqual(rows[0]["transmission"], "")
            self.assertEqual(rows[0]["normalized_price_rows"], "")

    def test_missing_exact_crosswalk_mapping_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            variants, crosswalk, registry, output = [root / name for name in
                ("variants.csv", "crosswalk.csv", "registry.csv", "queue.csv")]
            self.write_csv(variants,
                ["brand_id", "model_name", "official_variant_source_url"],
                [{"brand_id": "hyundai", "model_name": "Creta",
                  "official_variant_source_url": "https://oem.example/creta"}])
            self.write_csv(crosswalk,
                ["audit_type", "brand_id", "model_name", "source_url", "source_id"], [])
            self.write_csv(registry,
                ["source_id", "source_url", "review_status"], [])
            result = subprocess.run([sys.executable, str(SCRIPT), "--variants", str(variants),
                "--crosswalk", str(crosswalk), "--registry", str(registry), "--out", str(output)],
                capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
