# Motivo Beta Launch Checklist

Last reviewed: 2026-11-22
Repository: https://github.com/itrunks/motivo
Production preview: https://itrunks.github.io/motivo
Baseline branch: main
Latest baseline before catalogue validation work: 739555fa84c12c0bce479f6eed578a43de287e50

## Beta decision

**Status: NOT READY — foundation exists, catalogue/API and release gates remain.**

The first closed beta should validate the product workflow with a deliberately small, source-reviewed India passenger-car pilot. Do not wait for all Indian brands/models to be audited. Do not publish unverified research notes as catalogue records.

## Verified baseline findings

- [x] Expo SDK 54 + React Native Web + Expo Router + TypeScript application exists.
- [x] Home UI supports budget, fuel, transmission, body style and multi-priority filters.
- [x] `src/data/vehicles.ts` exports an empty array; no fabricated vehicle records are being displayed.
- [x] Canonical catalogue types exist in `src/types/catalogue.ts` (brands, models, variants, sourced values, prices, safety ratings).
- [x] Firestore rules deny all client reads/writes by default.
- [x] Firebase Functions project is configured for Node 22, region asia-south1.
- [x] Functions currently expose only `apiHealth` and `providerBalance`; no public catalogue read endpoints exist yet.
- [x] GitHub Actions TypeScript workflow passed for baseline commit.
- [x] GitHub Pages deployment workflow passed for baseline commit.
- [ ] Firebase Functions deployment and secret configuration verified in the live Firebase project.
- [ ] Firestore rules deployment verified in the live Firebase project.
- [ ] Production catalogue import/validation pipeline present and passing.
- [ ] Any research audit report converted into normalized, licensed, reviewed catalogue records. Research markdown alone is not production data.

## Beta scope (proposed)

Closed beta: 10–20 invited testers, web-first, India passenger cars, initial pilot of a small set of brands/models/variants with fully reviewed source provenance. Expand coverage after workflow quality is validated.

Beta must include:
- User preference capture: budget, city/state, family/usage profile, body style, fuel, transmission, priorities (no arbitrary 3-priority cap).
- Search/filter and exact-variant comparison.
- Clear distinction between official, estimated, owner-reported and unavailable values.
- Source links, model year/generation, last-verified date and ex-showroom price effective/observed date.
- No invented values. Unknown stays unknown.
- Feedback/issue reporting and a visible beta disclaimer.

Out of first beta unless separately approved: public user accounts, paid features, AI-generated vehicle facts, broad all-brand coverage, native iOS/Android distribution, unreviewed provider data imports.

## Work tracker

### Phase 0 — readiness audit
- [x] Inspect repository structure, app entry, current home UI and data source.
- [x] Inspect Firebase config, Firestore rules and Functions endpoints.
- [x] Inspect GitHub Actions workflows and latest baseline runs.
- [x] Record baseline and launch gates in this checklist.
- [x] Resolve README documentation contradictions.
- [ ] Run local web export and typecheck from a clean install; record logs.
- [ ] Inspect Firebase live project plan/billing, deployed functions, rules and secret state.

### Official ex-showroom price verification — pilot status (checked 2026-11-22)

| Pilot model | Official source result | Status |
|---|---|---|
| Maruti FRONX | Trichy petrol/CNG ranges and base/top figures captured; full variant price table not exposed; separate API result has unverified market code | Partial |
| Maruti Baleno | Current NEXA Trichy route returned stale placeholder page; 2026 launch starting price is not a complete variant list | Blocked |
| Hyundai VENUE | Official starting price ₹7,99,900; selector returned no variant price rows | Partial |
| Hyundai CRETA | 22 petrol + 16 diesel ex-showroom price rows captured; Turbo GDi coverage and Trichy-specific applicability remain open | Partial |
| Tata PUNCH ICE | Official starting figure ₹5,74,990; full variant-wise price list not retrieved | Partial |
| Tata NEXON ICE | Official price page conflicts: banner ₹7.39L; FAQ ₹7.36L start, ₹7.36–15.50L range, 60+ variants, Fearless+ PS ₹12.26L; numeric variant cards blank in text capture | Partial — conflicting OEM summaries

No dealer on-road quotations or derived on-road estimates are being collected. Do not import any of these price findings into production until exact variant mapping, freshness and source-specific factual-use review pass.


### Variant identity & powertrain crosswalk — first pass (2026-11-22)

| Pilot model | Official matrix / variant page | First-pass combinations | Status |
|---|---|---:|---|
| Maruti FRONX | NEXA live variant groups + current brochure technical table | 13 | Crosswalk captured |
| Maruti Baleno | NEXA live variant groups | 13 | Crosswalk captured; CNG AGS local orderability pending |
| Hyundai VENUE | HMIL live trim × engine × transmission matrix | 23 | Crosswalk captured |
| Hyundai CRETA | HMIL live trim × engine × transmission matrix (now includes Lounge Edition) | 29 | Crosswalk captured; price-row reconciliation pending |
| Tata PUNCH ICE | Current official specifications selector | 24 | 24-combination selector captured; persona matrix + official FAQ reconciled; airbag conflict and per-variant fitment pending |
| Tata NEXON ICE | Current official indexed selector labels + FAQ; Autocar cross-check (16 Nov 2026) | 80 reported by secondary source; OEM unique count pending | OEM selector labels now surfaced; normalize editions/SKUs and confirm orderability with dated OEM/dealer export |

First-pass mapping total: **102 confirmed combinations** across FRONX (13), Baleno (13), Venue (23), Creta (29) and Punch (24). Nexon remains excluded from this confirmed total: Autocar reports 80 variants (16 Nov 2026) and Tata's indexed selector labels are now visible, but the OEM unique orderable-SKU count still needs normalization and dated orderability confirmation. Do not add the secondary 80 count to the confirmed total. These are first-pass selector/crosswalk combinations, not fully reviewed production variants. Tata 2025 matrices must not be silently substituted for the current 2026 lineup. Punch's 24-combination selector is captured, but its trim-level feature matrix remains incomplete. Full feature matrices and independent review are still pending. All six models still require independent review, feature-by-feature applicability, model-year/effective-date confirmation and source-specific factual-use review.

### Phase 1 — catalogue and data quality
- [x] Define a six-model closed-beta pilot scope across Maruti Suzuki, Hyundai and Tata; vehicle/source audits remain pending.
- [x] Define source-use policy separating independently authored factual records, expressive-content reuse and automated-access restrictions (see docs/SOURCE_USE_AND_PUBLICATION_POLICY.md).
- [x] Add standard-library catalogue validation for record shape, references, dates, source provenance and source-specific factual-publication approval.
- [x] Add a separate source registry CSV and automated provenance/factual-use validator (crosswalk validation remains pending).
- [ ] Verify current model/generation and complete variant lists for the six pilot candidates (first-pass official variant crosswalks captured for FRONX, Baleno, Venue and Creta; Punch 2026 first-pass selector crosswalk captured (24 combinations); Nexon dynamic selector text is not exposed in the current capture; dated order sheet/configurator export required; model-year confirmation and source-specific factual-use review remain pending).
- [ ] Review each source for factual-reference publication eligibility (all 23 currently registered sources have factual_use_review=pending; none is approved).
- [ ] Normalize reviewed pilot research into brands/models/variants/specs/official ex-showroom prices/safety collections.
- [ ] Add review and publish workflow; only approved records become public.
- [ ] Add stale-price and stale-verification handling for official ex-showroom prices only.
- [ ] Produce a reproducible catalogue validation report and backup/export.

### Phase 2 — backend and security
- [x] Implement first read-only, paginated, bounded published-variants endpoint in Cloud Functions (source code only; not yet built/deployed).
- [x] Validate supported query parameters and add response schema versioning to the first endpoint (automated build/runtime verification pending).
- [ ] Keep all Firestore client writes denied; server/Admin SDK only for ingestion.
- [ ] Add abuse controls (App Check and/or rate limits) before broad public access.
- [ ] Configure secrets only in Firebase Secret Manager; never in client bundle or Git.
- [ ] Verify CORS allowlist, error handling, timeouts and cache headers.
- [ ] Deploy rules/functions to the intended Firebase project and smoke-test externally.
- [ ] Document Firebase plan/billing constraints and cost limits.

### Phase 3 — product integration and QA
- [ ] Connect UI to published catalogue API; retain a clear empty/error/loading state.
- [ ] Confirm all user preference fields and multi-select priorities work on mobile and desktop.
- [ ] Add exact variant detail and comparison with source evidence.
- [x] Pricing scope fixed to official variant-wise ex-showroom only; dealer on-road quotations, insurance, RTO, extended warranty, accessories and offers are excluded (see docs/PRICING_POLICY.md).
- [ ] Add feedback capture without collecting unnecessary personal data.
- [ ] Test empty results, partial data, stale data, network failure and API failure.
- [ ] Accessibility, responsive layout and browser smoke tests.
- [ ] Typecheck + web export + automated checks pass on release candidate.

### Phase 4 — internal alpha
- [ ] Deploy alpha build to a private/staging URL.
- [ ] Test with project owner only; record defects.
- [ ] Fix all blocker/critical defects and rerun smoke tests.

### Phase 5 — closed beta
- [ ] Invite 10–20 testers; provide scope, limitations and feedback channel.
- [ ] Track task completion, search success, comparison usefulness, data corrections and crashes.
- [ ] Review feedback at least twice during the beta window.
- [ ] Fix blockers and high-severity defects; document accepted limitations.
- [ ] Confirm no unsupported vehicle claim or source/licensing issue.

### Phase 6 — public beta / production
- [ ] Publish public beta notes, privacy notice, data methodology and contact/feedback path.
- [ ] Confirm monitoring, alerting, backup/restore and rollback procedure.
- [ ] Recheck source freshness and catalogue validation at release.
- [ ] Production go/no-go review; owner approval.
- [ ] Tag release and deploy; verify production URL and Firebase endpoints.
- [ ] Monitor first 72 hours and publish known issues.

## Release gates

A phase cannot be marked complete based on code existing alone. Require test evidence or a live deployment check.

**Closed beta gate:** no fabricated data; pilot records have acceptable reuse rights and provenance; core filters/comparison work; API and Firestore access are secure; no blocker/critical bugs; feedback route works.

**Public beta gate:** closed-beta blockers fixed; privacy/data methodology published; monitoring, backups and rollback tested; validation and smoke tests pass.

**Production gate:** explicit owner go/no-go; support/incident process; cost limits; security and licensing review; release rollback verified.

## Pilot scope reference

- [x] Initial six-model pilot scope documented in research/india/PILOT_SCOPE_CLOSED_BETA.md.
- [ ] No model/variant in this pilot scope is yet marked publishable.
- [x] Baleno 2026 desk audit note created; September 2026 update, official powertrain/feature claims and variant families captured; exact model-year, trim applicability, CNG AGS discrepancy and rights remain open.
- [x] FRONX desk audit note created; official variant groups captured, but current model-year and exact specification checks remain open.
- [x] FRONX official Trichy ex-showroom price check started; official page confirms petrol/CNG price ranges and base/top figures, but full variant-wise prices are not exposed in retrieved page content; exact variant prices and source rights remain pending.
- [x] Hyundai Venue desk audit note created; current trim labels and engine/transmission families captured; model-year, dealer lineup and rights checks remain open.
- [x] Venue official ex-showroom price page checked; starting price ₹7,99,900 captured, but variant selector returned no price rows; exact variant-wise prices and source rights remain pending.
- [x] Hyundai Creta desk audit note created; trim families and engine/transmission options captured; exact current model-year combinations and rights checks remain open.
- [x] Creta official price page variant-wise ex-showroom petrol/diesel prices captured (2026-11-22); Turbo GDi DCT coverage incomplete, city applicability and source rights pending.
- [x] Maruti Suzuki Baleno desk audit note created; 2026 update and current official variant families captured; exact MY, feature mapping and rights checks remain open.
- [x] Tata Punch desk audit note created; current 2026 official specifications selector exposes 24 combinations and persona-level feature matrix extracted; exact per-variant fitment, dual-vs-six-airbag conflict, NCAP test applicability, model-year, prices and factual-use review remain open.
- [x] Punch official ex-showroom price source checked; starting figure ₹5,74,990 captured, but complete current variant-wise price table unavailable; exact prices and source rights pending.
- [x] Tata Nexon ICE desk audit note created; current specifications FAQ and brochure links rechecked; unique orderable-variant count remains unverified, diesel output conflict (113 vs 115 PS) and iCNG brochure year mismatch recorded.
- [x] Nexon ICE official price/variant page re-opened; variant cards and feature personas captured, but numeric card prices are blank in retrieved text. Official page itself conflicts (banner ₹7.39L; FAQ ₹7.36L start, ₹7.36–15.50L range, 60+ variants, Fearless+ PS ₹12.26L; earlier snapshot had ₹12.41L). Do not publish a price until a dated official price output resolves this.

## Current blockers (confirmed from repository inspection)

1. No production vehicle records are connected to the UI (the app correctly shows an empty catalogue); the new normalized catalogue is intentionally empty.
2. A published-only variants read endpoint now exists in source code; build verification, live deployment, Firestore data setup and external smoke tests remain pending.
3. A separate source registry and validator now exist; the registry now contains 23 official source candidates (all factual-use reviews pending); no source is yet approved for factual publication. Expressive-content reuse permissions remain separately pending. Normalized catalogue bootstrap and CI validation now exist; factual-use-approved sources and actual import/review/publish workflow are still missing.
4. Firestore rules are intentionally deny-all; a safe server-mediated read path must be implemented before publishing data.
5. README data-policy wording has been corrected; it still needs a fresh build verification.
6. Live Firebase deployment, billing plan, secret configuration and runtime state have not been verified.

## Working rules

- Never claim a workflow, deployment, rule, secret, backup or endpoint is live unless a live check confirms it.
- Do not import research notes into production automatically.
- Preserve exact variant/year/generation and field-level source provenance.
- No source with pending factual-use review is eligible to support published facts. Factual-use approval does not permit copying images, prose, brochure tables, PDFs or datasets; those require separate permission.
- Do not use paid/metered provider credits without explicit approval.
- Update this file after each meaningful implementation or verification step.


## Latest verification — 2026-11-22 (current policy and Tata selector updates)

- [x] TypeScript workflow run 45016076245 completed successfully.
- [x] GitHub Pages deployment run 45016076410 completed successfully.
- Both runs correspond to the same commit above; this confirms the repository build/typecheck and Pages deployment for that commit only. It does not verify Firebase deployment, Firestore rules/data, or production catalogue readiness.
- [x] Re-opened current Tata Punch ICE product page; its performance section still contains both 193 mm and 187 mm ground-clearance claims. Keep the value unresolved.
- [x] Rechecked current Tata Punch official specifications page; 24 trim/powertrain/transmission combinations captured in a first-pass crosswalk.
- [x] Extracted the 2026 Punch brochure's eight-persona feature progression and rechecked current official FAQ (5MT/5AMT petrol+iCNG, 6MT turbo; 193 mm GC); dual-vs-six-airbag conflict and exact applicability remain open.
- [x] Rechecked current Tata Nexon official specifications page; confirmed petrol/diesel/iCNG powertrain and transmission FAQ, 2026-labelled iCNG brochure link points to a 2025 URL path, and diesel output differs between official page summaries (113 vs 115 PS). Dynamic selector does not expose a stable list in the text capture.
- [x] Added source-use policy and separate factual-reference approval fields; all 23 registered sources remain pending review.
- [ ] Re-run TypeScript, catalogue validation and Pages workflows on the latest commit; CI status not yet confirmed.


### Nexon selector follow-up — 2026-11-22

- [x] Tata official indexed specifications selector now exposes named trim/powertrain/edition labels, including Camo, Dark and Red #Dark variants.
- [x] Autocar India independently reports 80 Nexon variants (page updated 16 Nov 2026); recorded as a secondary count cross-check only.
- [ ] Normalize OEM labels and deduplicate exact orderable SKUs; preserve edition suffixes and distinguish petrol 5MT/6MT/6AMT/7DCT, diesel 6MT/6AMT and iCNG 6MT.
- [ ] Confirm the unique orderable count against a dated Tata order sheet or structured OEM configurator export.
- [ ] Map exact feature applicability and official variant-wise ex-showroom prices.
- [ ] No change to confirmed first-pass total (102); Nexon remains excluded pending OEM crosswalk validation.


### Latest CI and Nexon audit continuation — 2026-11-22

- [x] TypeScript workflow run 45019483442 completed successfully on commit 98a47ad736feba429613bdeacccc133057cb788b.
- [x] GitHub Pages build and deployment run 45019483456 completed successfully on the same commit; both build and deploy jobs passed.
- [ ] Catalogue validation was not triggered by that markdown-only commit because its workflow path filter does not include research markdown/checklist changes. Do not count it as passed.
- [x] Re-opened the full current Tata Nexon official price/variant page and recorded the card-level trim/persona labels and explicit feature groups in the Nexon audit.
- [x] Recorded official-page price-summary conflicts: page banner ₹7.39L; FAQ ₹7.36L start; FAQ range ₹7.36–₹15.50L and 60+ variants; Fearless+ PS FAQ ₹12.26L; earlier official capture ₹12.41L. Exact variant-wise numeric card prices are not exposed in the retrieved text.
- [x] Applied the official page's explicit footnote over its broad FAQ wording: ADAS/JBL/subwoofer only Fearless+ PS DCA; rear sunshade Fearless+ PS DCA and Red #Dark, with Red #Dark limited to Fearless+ PS. CNG exclusions retained.
- [ ] Normalize official card labels into unique exact SKUs and verify orderability using a dated OEM/dealer export.
- [ ] Obtain exact variant-wise official ex-showroom prices and effective dates.
- [ ] Complete source factual-use review and independent review; no Nexon production records approved.


### Tata Punch feature-matrix progress — 2026-11-22

- [x] Re-opened the current official January 2026 Tata Punch brochure and extracted its 24-combination drivetrain matrix.
- [x] Reconciled all 24 selector combinations: Petrol MT 8, Petrol AMT 5, iCNG MT 6, iCNG AMT 3, turbo petrol 6MT 2.
- [x] Mapped the eight OEM personas (Smart through Accomplished+ S) to the brochure's explicit equipment progression.
- [x] Preserved powertrain-specific footnotes: cruise control applies to NA petrol MT/AMT and iCNG MT; paddle shifter applies to NA petrol AMT and iCNG AMT.
- [x] Kept the OEM conflict (six airbags in brochure vs dual airbags in specifications FAQ) unresolved; no definitive variant-level airbag count is approved.
- [ ] Dealer orderability/effective-date confirmation, official variant-wise ex-showroom prices, exact iTPMS readout, BNCAP tested-variant applicability, factual-use rights and independent review remain pending.
- [ ] Do not import Punch production records.

Evidence: official Tata brochure https://tatamotors-prod.adobecqms.net/content/dam/tml/pv/products/punch/year-2026/ice/promoting-vc/brochures/new-punch-brochure-jan%20.pdf ; current Tata specifications page https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/punch/ice/specifications.html .

Next action: continue Nexon ICE selector normalization from the current official selector labels; preserve exact CAMO/DK/RDK/ADAS suffixes and do not assert a unique SKU count without dated OEM/dealer orderability evidence.


## Automation checkpoint — 2026-11-22 17:39 IST

### CI verification
- [x] TypeScript workflow run 45019909883 completed successfully.
- [x] GitHub Pages deployment run 45019909890 completed successfully.
- Both runs completed on commit 72b2b80d3006b8c3109088fd4a181ab5476932e1.
- Links: https://github.com/itrunks/motivo/actions/runs/45019909883 and https://github.com/itrunks/motivo/actions/runs/45019909890
- Catalogue validation was not assumed to have run because the latest markdown/checklist changes do not trigger that workflow path filter.

### Nexon ICE progress
- [x] Re-validated the current official price-page card naming patterns and exact-suffix preservation rule.
- [x] Created a provisional normalization grammar without inventing SKUs: fuel = petrol/diesel/iCNG; engine family = 1.2 turbo petrol or 1.5 turbo diesel as stated by the OEM FAQ; transmission = only when explicitly present in the card/FAQ (petrol 5MT/6MT/6AMT/7DCT; diesel 6MT/6AMT; iCNG 6MT); trim/persona = Smart, Smart+, Pure+, Creative, Creative+, Fearless+; edition = CAMO, DK/Dark, Red #Dark, ADAS/DCA and all other exact suffixes retained verbatim.
- [x] Preserved official card examples: Smart 1.2 = petrol 5MT; Smart+ AMT 1.2 = petrol AMT; Pure+ 1.2 = petrol 6MT; Creative DCA 1.2 = petrol DCA; Smart CNG/Pure+ CNG = iCNG 6MT where explicitly shown.
- [ ] Exact unique OEM SKU count remains unresolved. Official FAQ says 60+; Autocar reports 80 on 2026-11-16; neither is treated as confirmed OEM orderability.
- [ ] Dated OEM/dealer order sheet or structured configurator export is still missing; no guessed combination or price was added.
- [ ] Variant-wise official ex-showroom price output and effective dates remain unavailable in the retrieved page text.

### Durable next action
1. Obtain a dated Tata order sheet/configurator export or an accessible structured selector output.
2. Parse each exact label into fuel × engine × transmission × trim × edition rows, preserving original labels and provenance.
3. Resolve diesel 113 vs 115 PS official-page discrepancy and the 2026-labelled iCNG brochure URL pointing to a 2025 path.
4. Only after Nexon orderability is evidenced, continue Punch exact trim-level applicability and keep airbag/ground-clearance conflicts unresolved.

Checkpoint commit target: this audit update plus checklist update. No production records approved; source factual-use review remains pending.
