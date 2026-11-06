# Catalogue staging import

This workflow deliberately separates factual review, reuse permission, staging writes and publication.

## Current gate status

The current variant audit CSV is a research worklog, not an import manifest. It does not provide a normalized row per exact variant and does not prove commercial reuse or redistribution rights. Do not transform its semicolon-delimited observations into publishable records by guessing trim/powertrain mappings.

## Variant normalization work queue

Generate the source-linked manual review queue:

```bash
python3 scripts/build_variant_normalization_queue.py
```

The generated `data/variant-normalization-workqueue.csv` contains one work item per audited model. It preserves the raw variant and price observations, links each item to its exact source registry entry, and leaves normalized engine, fuel, transmission, body style, model year and price fields blank until verified. Every row is marked `needs_manual_review`; the queue is not an import manifest and does not imply that each semicolon-separated fragment is a retail variant. The script fails closed if an exact crosswalk or registry URL is missing or duplicated.

## Pipeline

1. Review each work item against the exact OEM source and capture exact retail variant labels, engine, fuel, transmission, body style and model year. Preserve distinct powertrain/trim combinations; do not infer combinations from a model-level summary.
2. Prepare exact variant and price rows in the format in `data/catalogue-import-template.csv`.
3. Run the offline validator:

   ```bash
   python3 scripts/validate_catalogue.py path/to/import.csv --out-dir data/staging
   ```

4. Review the source-specific permission record in `data/source-registry.csv`. The current 224 source URLs are linked through `data/audit-source-crosswalk.csv`; all remain `review_required` until terms and commercial redistribution rights are documented. Each imported record must use an exact source URL with an explicit terms/licence URL, licence name, `review_status=approved`, `commercial_reuse_allowed=yes`, and `redistribution_allowed=yes`. Public visibility is not permission.
5. Validate source mapping with `python scripts/validate_source_crosswalk.py`.
6. Run the reuse gate against the same canonical registry. It checks every draft row against the exact audited source URL and fails closed on duplicate registry IDs or URLs:

   ```bash
   python3 scripts/approve_catalogue_sources.py data/staging/import.draft.jsonl \
     --source-audit data/source-registry.csv \
     --out data/staging/import.approved.jsonl
   ```

   It fails closed if any source is missing, duplicated, unapproved, or has unknown/denied reuse rights.
7. Dry-run the Firestore importer:

   ```bash
   cd functions && npm install && npm run build
   node lib/admin/importCatalogue.js --input ../data/staging/import.approved.jsonl --batch-id pilot-2026-11-06
   ```

8. Start the Firestore emulator and explicitly write the draft batch:

   ```bash
   firebase emulators:start --only firestore
   # in another terminal, from functions/
   FIRESTORE_EMULATOR_HOST=127.0.0.1:8080 GCLOUD_PROJECT=motivo-staging \
     node lib/admin/importCatalogue.js --input ../data/staging/import.approved.jsonl \
     --batch-id pilot-2026-11-06 --write
   ```

## Safety properties

- The importer is emulator-only. It refuses writes unless `FIRESTORE_EMULATOR_HOST` is set; it has no production override.
- Writes go only to `catalogueStaging/{batchId}/records/{recordId}`, never the public catalogue collections.
- Every record must remain `draft` and carry explicit source approval metadata.
- IDs are deterministic from the offline validator; duplicate IDs in a batch are rejected.
- Writes are chunked below Firestore's 500-operation batch limit.
- No publication, public read permission, or production write is performed.
- Production import requires a separately reviewed admin-only deployment path, a dedicated staging/production project decision, backup/rollback plan, and human approval of the exact manifest. Do not put service-account credentials in Git or the client.

## Environment boundary

The repository currently has only the Firebase project `motivo-car-research` configured; there is no dedicated staging Firebase project. CI provisions an ephemeral Firestore Emulator and verifies a synthetic draft write there. That CI fixture is not real vehicle data and is never sent to a Firebase project. Keep manual writes in the local emulator until a dedicated staging project and credentials are configured securely.
