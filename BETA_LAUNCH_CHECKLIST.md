# Motivo Beta Launch Checklist

Last reviewed: 2026-11-19
Repository: https://github.com/itrunks/motivo
Production preview: https://itrunks.github.io/motivo
Baseline branch: main
Baseline commit: af63deedc70be8706777bca5438b565d261992bc

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
- Source links, model year/generation, last-verified date and price location/date.
- No invented values. Unknown stays unknown.
- Feedback/issue reporting and a visible beta disclaimer.

Out of first beta unless separately approved: public user accounts, paid features, AI-generated vehicle facts, broad all-brand coverage, native iOS/Android distribution, unreviewed provider data imports.

## Work tracker

### Phase 0 — readiness audit
- [x] Inspect repository structure, app entry, current home UI and data source.
- [x] Inspect Firebase config, Firestore rules and Functions endpoints.
- [x] Inspect GitHub Actions workflows and latest baseline runs.
- [x] Record baseline and launch gates in this checklist.
- [ ] Resolve README documentation contradictions.
- [ ] Run local web export and typecheck from a clean install; record logs.
- [ ] Inspect Firebase live project plan/billing, deployed functions, rules and secret state.

### Phase 1 — catalogue and data quality
- [ ] Choose pilot brands/models/variants based on completed source audits.
- [ ] Define source rights policy: commercial reuse, redistribution and attribution must be explicit.
- [ ] Add schema validation for catalogue records and field-level provenance.
- [ ] Build source registry + crosswalk validator; fail closed on missing/duplicate mappings.
- [ ] Normalize pilot research into brands/models/variants/specs/prices/safety collections.
- [ ] Add review and publish workflow; only approved records become public.
- [ ] Add stale-price and stale-verification handling.
- [ ] Produce a reproducible catalogue validation report and backup/export.

### Phase 2 — backend and security
- [ ] Implement read-only, paginated, bounded catalogue endpoints in Cloud Functions.
- [ ] Validate all query parameters and response schema versions.
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
- [ ] Verify on-road price is city/date-specific; never present ex-showroom as on-road.
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

## Current blockers (confirmed from repository inspection)

1. No production vehicle records are connected to the UI (the app correctly shows an empty catalogue).
2. No catalogue read API exists in Cloud Functions.
3. The source audit CSV is a template only; no validator/import/publish pipeline is present in the inspected repository tree.
4. Firestore rules are intentionally deny-all; a safe server-mediated read path must be implemented before publishing data.
5. README has contradictory demo-data statements and needs correction.
6. Live Firebase deployment, billing plan, secret configuration and runtime state have not been verified.

## Working rules

- Never claim a workflow, deployment, rule, secret, backup or endpoint is live unless a live check confirms it.
- Do not import research notes into production automatically.
- Preserve exact variant/year/generation and field-level source provenance.
- No source with unknown reuse rights is eligible for redistribution.
- Do not use paid/metered provider credits without explicit approval.
- Update this file after each meaningful implementation or verification step.
