import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_source_crosswalk.py"

class SourceCrosswalkTests(unittest.TestCase):
    def test_exact_registry_crosswalk_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def write(name, headers, rows):
                with (root / name).open("w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=headers); w.writeheader(); w.writerows(rows)
            write("registry.csv", ["source_id","source_url","review_status","commercial_reuse_allowed","redistribution_allowed"], [
                {"source_id":"s1","source_url":"https://oem.example/x","review_status":"review_required","commercial_reuse_allowed":"unknown","redistribution_allowed":"unknown"}])
            write("crosswalk.csv", ["audit_type","brand_id","model_name","source_url","source_id"], [
                {"audit_type":"variant","brand_id":"b","model_name":"m","source_url":"https://oem.example/x","source_id":"s1"}])
            write("models.csv", ["brand_id","model_name","official_source_url"], [])
            write("variants.csv", ["brand_id","model_name","official_variant_source_url"], [
                {"brand_id":"b","model_name":"m","official_variant_source_url":"https://oem.example/x"}])
            r = subprocess.run([sys.executable, str(SCRIPT), "--registry", str(root/"registry.csv"),
                "--crosswalk", str(root/"crosswalk.csv"), "--models", str(root/"models.csv"),
                "--variants", str(root/"variants.csv")], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_missing_mapping_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def write(name, headers, rows):
                with (root / name).open("w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=headers); w.writeheader(); w.writerows(rows)
            write("registry.csv", ["source_id","source_url"], [{"source_id":"s1","source_url":"https://oem.example/x"}])
            write("crosswalk.csv", ["audit_type","brand_id","model_name","source_url","source_id"], [])
            write("models.csv", ["brand_id","model_name","official_source_url"], [])
            write("variants.csv", ["brand_id","model_name","official_variant_source_url"], [
                {"brand_id":"b","model_name":"m","official_variant_source_url":"https://oem.example/x"}])
            r = subprocess.run([sys.executable, str(SCRIPT), "--registry", str(root/"registry.csv"),
                "--crosswalk", str(root/"crosswalk.csv"), "--models", str(root/"models.csv"),
                "--variants", str(root/"variants.csv")], capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)

if __name__ == "__main__":
    unittest.main()
