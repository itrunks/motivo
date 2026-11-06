# Motivo Catalogue Completion Roadmap

**Project target:** 100% evidence-backed catalogue normalization and validation.  
**Working branch:** `feature/catalogue-source-audit-ingestion`  
**Current PR:** #1 — https://github.com/itrunks/motivo/pull/1  
**Last checkpoint:** 2026-11-06 — Kia EV6 committed and verified; Carens Clavis remains blocked

## Progress rules

- Mark a task complete only after source evidence is captured, normalized files and notes are committed, and the committed files are fetched back and checked.
- Keep unknown values blank. Never infer trim, engine, fuel, transmission, body style, model year, price, or price effective dates.
- Keep OEM observations separate from confirmed current city-specific prices.
- Source rights remain `review_required` and commercial reuse/redistribution remain `unknown` until explicitly verified. Do not publish/import rights-unapproved data.
- Validate only changed/new files and affected logic; do not repeat the full baseline audit without a concrete reason.
- Update this roadmap and the checkpoint after each completed model/brand so work can resume in a new conversation.

## Master completion checklist

- [x] Initial source and catalogue audit baseline (224 URLs, 251 model records, 251 variant records, 502 crosswalk mappings, 35 brands)
- [x] Variant normalization work queue generated (251 model rows)
- [x] Staging/import safety documentation and validation tooling added
- [x] Hyundai — Creta normalization and evidence notes
- [x] Hyundai — Venue structure normalization and evidence notes
- [x] Hyundai — Exter structure + launch-price observations + evidence notes
- [x] Hyundai — Verna normalization and evidence notes
- [x] Hyundai — Aura structure normalization and evidence notes
- [x] Hyundai — Grand i10 NIOS structure normalization and evidence notes
- [x] Hyundai — i20 structure normalization and evidence notes
- [x] Hyundai — i20 N Line structure normalization and evidence notes
- [x] Hyundai — i20 N Line structure normalization and evidence notes
- [x] Hyundai — Alcazar structure normalization and evidence notes
- [x] Hyundai — Creta Electric structure normalization and evidence notes
- [x] Hyundai — IONIQ 5 current powertrain normalization and evidence notes
- [x] Hyundai — Venue N Line structure normalization and evidence notes
- [x] Hyundai — Creta N Line structure normalization and evidence notes
- [x] Hyundai — BAYON structure normalization and evidence notes
- [x] All 14 Hyundai work-queue models have a normalization evidence record
- [x] Hyundai — BAYON structure normalization and evidence notes
- [x] Hyundai — all 14 work-queue models normalized (staging only)
- [ ] Remaining brands/models in the work queue (process one evidence-backed model at a time)
- [ ] Reconcile normalized model/variant rows against the 251-row work queue and 502-row crosswalk
- [ ] Resolve source permission / commercial reuse / redistribution status for every source intended for production
- [ ] Confirm price scope, currency, tax basis, geography, and effective date wherever prices are to be production-ready
- [ ] Run final changed-file validation, complete test suite, typecheck, Functions build, emulator dry-run, and CI checks
- [ ] Produce final import-readiness report with explicit blocked / approved / unknown counts
- [ ] Production import approval gate (requires verified rights and explicit authorization)
- [ ] Firestore production import and publication (only after all gates pass and authorization is present)

## Brand/model work ledger

| Brand | Model | Structure | Price evidence | Evidence notes | Commit verification | Status |
|---|---|---|---|---|---|---|
| Hyundai | Creta | [x] | [x] OEM observations; current city price still needs confirmation | [x] | [x] | Complete — staging only |
| Hyundai | Venue | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Exter | [x] | [x] launch observations; effective date/current city quote not confirmed | [x] | [x] | Complete — staging only |
| Hyundai | Verna | [x] | [x] dated launch observations; current city quote needs confirmation | [x] | [x] | Complete — staging only |
| Hyundai | Aura | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Grand i10 NIOS | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | i20 | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | i20 N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Alcazar | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Creta Electric | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | IONIQ 5 | [x] | [ ] | [x] | [x] | Complete — powertrain only |
| Hyundai | Venue N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Creta N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | BAYON | [x] | [ ] | [x] | [x] | Complete — structure only |
| Kia | Sonet | [x] | [x] 8 trim prices; HTK missing | [x] | [x] | Complete — 24 combinations |
| Kia | Seltos | [x] | [x] 12 trim prices | [x] | [x] | Staged — T-GDi 6iMT trim mapping unresolved |
| Kia | Carens Clavis EV | [x] | [x] 9 trim prices | [x] | [x] | Complete — 17 battery/seating combinations |
| Kia | Syros | [x] | [x] 7 trim prices | [x] | [x] | Complete — 17 combinations |
| Kia | Carens Clavis | [ ] | [ ] | [x] | [x] | Blocked — unnamed trim column and price/powertrain reconciliation |
| Kia | Carnival | [x] | [x] 1 price | [x] | [x] | Complete — one India retail trim |
| Kia | EV6 | [x] | [ ] | [x] | [x] | Complete — current GT-Line AWD only; price unavailable |
| Kia | EV9 | [x] | [x] 1 price observation | [x] | [x] | Complete — one India retail trim |

## Resume/checkpoint protocol

1. Read this file first on every continuation.
2. Confirm the current branch and PR head; do not assume the previous session's last write succeeded.
3. Fetch the latest work-queue and relevant evidence files. Continue from the first unchecked model.
4. Research official/manufacturer sources first; capture exact source URLs and checked date.
5. Keep structure and price evidence separate when their source scope/date differs.
6. Commit each completed model's data and evidence notes to the working branch.
7. Fetch the committed files back and verify row/column counts and key fields.
8. Update this ledger and the master checklist in the same branch.
9. Report only verified completion. If a session/window ends, the next session resumes from this file and the branch state.

## Safety / publication gates

- [x] No automatic production writes during normalization
- [x] No automatic publication of source material
- [ ] Source rights verified for every production-bound source
- [ ] Data quality and crosswalk reconciliation passed
- [ ] Final validation and CI passed on the final PR head
- [ ] Explicit production-import authorization received
