# Production import readiness report

**Checked:** 2026-11-06  
**Scope:** India passenger-car candidate catalogue  
**Decision:** HOLD — no production import or publication is authorised by the current evidence.

## Executive result

The variant-source audit has 251 rows matching the 251 model candidates. This is research coverage, not an import manifest. The rows contain semicolon-delimited variant observations and narrative price notes; they are not normalized exact variant × model-year × powertrain × price records.

**Import-ready records: 0.** This is not a statement that no vehicles or prices exist. It means none of the current research rows has passed every factual, provenance, source-reuse and schema gate required for ingestion.

## Blocking conditions

1. **No source reuse approvals.** The source register currently marks OEM sources `review_required`; commercial reuse and redistribution are unknown. The TCO India compilation is `hold` because its claimed CC-BY licence does not establish rights to redistribute upstream CarDekho/CarWale-derived content.
2. **No exact source registry linkage.** The variant worklog is keyed by `brand_id + model_name`; it does not carry a per-record `source_id` or a normalized exact source URL for every observation.
3. **Unstructured variant and price observations.** `variant_names_observed` and `price_observation` are free-text fields. A row may contain several trims, multiple powertrains, partial prices, model-level prices or a discrepancy. It cannot be safely converted to one record per exact variant without further extraction and verification.
4. **Missing applicability metadata.** Model year/generation, exact fuel/transmission/drivetrain mapping, price basis, location scope and effective date are not consistently present.
5. **Unresolved evidence states.** Partial matrices, missing prices, historical observations, source conflicts, dealer-confirmation cases and current-orderability uncertainty must remain quarantined.

## Variant audit status counts

| Audit status | Rows |
|---|---:|
| official_variant_prices_observed | 41 |
| official_single_configuration_price_observed | 3 |
| partial_official_variant_prices | 31 |
| official_variant_structure_price_missing | 57 |
| official_model_listing_only | 34 |
| dealer_confirmation_required | 30 |
| incomplete_official_data | 8 |
| variant_structure_observed_price_missing | 6 |
| official_variant_structure_price_partial | 6 |
| official_single_configuration_price_basis_pending | 6 |
| india_retail_status_unconfirmed | 3 |
| official_current_range_observed_price_missing | 2 |
| historical_official_variant_structure_only | 2 |
| official_powertrain_structure_price_missing | 2 |
| official_single_configuration_price_partial | 2 |
| official_variant_prices_partial | 2 |
| official_variant_prices_observed_scope_mismatch | 1 |
| official_variant_names_powertrain_map_pending | 1 |
| official_variant_structure_partial | 1 |
| historical_official_variant_prices_only | 1 |
| source_conflict | 1 |
| current_orderability_unconfirmed | 1 |
| official_product_page_access_blocked | 7 |
| current_catalogue_presence_unconfirmed | 1 |
| official_inventory_price_basis_pending | 1 |
| price_source_conflict | 1 |
| **Total** | **251** |

The 41 rows with observed official price matrices and 3 single-configuration observations are promising extraction candidates, but they are not automatically importable. Each still needs exact row-level facts, date/basis/applicability and source reuse approval.

## Gate policy

A record may enter the approved staging manifest only when all conditions are met:

- Exact OEM/dealer source URL and retrieval timestamp are captured.
- The source register contains that exact URL, terms/licence URL and licence/permission basis.
- `review_status=approved`, `commercial_reuse_allowed=yes` and `redistribution_allowed=yes` are explicitly recorded.
- Exact variant identity, model year/generation, powertrain and transmission are source-supported.
- Every price has an explicit type, amount, classification, effective date and required location scope.
- No unresolved source conflict or dealer-orderability dependency remains.
- The offline schema validator and source-approval gate both pass.

Unknown facts remain null or pending; they are not inferred. Ex-showroom prices are never converted into on-road prices.

## Safe next steps

1. Obtain source-specific written permission or a clearly applicable licence for each source intended for commercial display and redistribution.
2. Convert only fully evidenced OEM observations into normalized import rows.
3. Run schema validation and the source-reuse approval gate.
4. Dry-run the manifest, then write it to a dedicated staging Firestore project or local Firestore Emulator.
5. Verify record counts, relationships, source attribution and rollback before any production import.
6. Publish only after a separate reviewed release step.

## Environment constraint

The repository's `.firebaserc` currently defines only `motivo-car-research`. No separate staging Firebase project is configured. The new importer intentionally refuses non-emulator writes. Production writes require a separately reviewed deployment mechanism and secure credentials; no service-account key should be committed to the repository.

**No Firestore documents were written by this readiness review. No production deployment, publication or merge was performed.**
