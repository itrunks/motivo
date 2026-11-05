# Motivo vehicle catalogue architecture

## Decision

Motivo will use an owned, source-attributed vehicle catalogue in Firestore as its source of truth. The initial scope is every India-market brand, model, and exact variant that can be supported by verifiable sources. The initial product does not depend on an LLM or on a paid API. AI can be evaluated later as an optional interface over this catalogue; it must never invent or author vehicle facts.

## Important scope boundary

"All variants" is the target coverage, not a claim that a complete, current, legally reusable dataset already exists. Coverage will expand through source-audited imports and manual review. A vehicle or field is not published unless its source, applicable market/year, and verification status are recorded. Missing values remain null/unknown; do not fill gaps with estimates presented as facts.

## Architecture

1. Expo / React Native Web client reads published catalogue data through Motivo HTTPS endpoints.
2. Firebase Cloud Functions validate query parameters and return normalized, published records.
3. Cloud Firestore stores canonical brands, models, variants, specifications, prices, ratings, and source provenance.
4. Trusted ingestion scripts / admin-only server jobs import source files and normalize records. No public client writes.
5. A review/publish step promotes validated records. Draft and rejected records are never returned by public endpoints.

The existing Let's Pick My Car integration is not the catalogue source of truth for this architecture. Do not spend its metered credits during the initial database build. Keep its integration isolated until its authentication issue is resolved and its licence/coverage is reviewed.

## Firestore collections

- brands/{brandId}: canonical brand name, aliases, country/market, status, source references.
- models/{modelId}: brandId, canonical name, generation, model year range, body style, launch/discontinued dates, status.
- variants/{variantId}: modelId, exact variant name, model year, fuel, transmission, drivetrain, engine/EV configuration, status, published flag.
- variantSpecs/{variantId}: structured dimensions, engine, performance, capacity, features, warranty and equipment. Store field-level source references and effective dates where values vary.
- prices/{priceId}: variantId, state/city/RTO context, ex-showroom, registration/road tax, insurance, other charges, on-road total, currency, effective date, observed date, source, and whether the value is official, estimated, or user-supplied. Never label an estimate as a dealer quote.
- ratings/{ratingId}: variant/model applicability, agency, protocol/version, score, test date, tested configuration, source and applicability notes.
- sources/{sourceId}: publisher, URL, licence/terms URL, retrieval date, attribution text, permitted uses, dataset revision and notes.
- imports/{importId}: source, file checksum, import time, row counts, validation errors, reviewer, status and published revision.

Use stable IDs generated from normalized identifiers, not display names alone. Keep source records and normalized records separate so updates are traceable.

## Data quality rules

- Preserve exact variant names and distinguish model year / generation / facelift.
- Never merge variants just because names are similar.
- Separate ARAI/claimed mileage from owner-reported or independently tested real-world mileage. Record test methodology and source.
- Separate ex-showroom price from on-road price. On-road pricing is location- and date-specific and must identify its tax/insurance assumptions.
- Safety ratings must retain agency, protocol, test date, tested variant/configuration, and applicability. Do not transfer a rating to other variants without evidence.
- Unknown values are null, not zero or guessed.
- Every published fact must have provenance and last-verified date. Expired prices should be marked stale and excluded from "current price" answers.
- Respect each source's licence, attribution and commercial-use terms before importing or republishing data. Publicly accessible does not automatically mean reusable.

## Public API (planned)

- GET /catalogue/brands
- GET /catalogue/models?brandId=...
- GET /catalogue/variants?modelId=...&fuel=...&transmission=...
- GET /catalogue/variants/{variantId}
- GET /catalogue/compare?variantIds=...
- GET /catalogue/prices?variantId=...&state=...&city=...

Only published records are returned. Add pagination, bounded query limits, cache headers, input validation, and response schema versioning. Do not expose draft data or ingestion endpoints publicly.

## Security and operations

- Keep Firestore client writes denied.
- Ingestion uses Firebase Admin credentials only in a trusted local/admin environment or a protected server job; never put service-account credentials in the web app or Git.
- Public reads go through Cloud Functions initially. Review App Check / abuse controls and per-IP or per-client quotas before enabling broad traffic.
- Do not put provider API keys in the client, logs, GitHub, or screenshots.
- Keep a versioned export/backup of each published catalogue release.

## Delivery plan

### Phase 1 — Catalogue foundation
Create the canonical TypeScript schema, Firestore collection conventions, validation rules, and source registry. Keep the existing UI empty until verified records exist.

### Phase 2 — Source audit
Build a source matrix for Indian brands and their official specifications, variant brochures, government/open datasets, and independently published safety data. Record licence, attribution, coverage, update frequency, and field coverage. Reject sources without acceptable reuse terms.

### Phase 3 — Import and review
Build a CSV/JSON import tool with schema validation, duplicate detection, stable ID generation, provenance capture, and a review report. Import a small pilot set first; do not bulk-publish unreviewed rows.

### Phase 4 — Read API and UI
Implement read-only catalogue endpoints and connect the home filters, exact variant detail, and comparison screens. Display source and last-verified date with every material fact. Add location-specific price only when sourced.

### Phase 5 — Coverage expansion
Expand brand-by-brand and model-year-by-model-year until the target coverage is met. Publish coverage metrics and clearly show unsupported/missing fields.

### Phase 6 — Optional AI
Only after the catalogue is reliable, consider Ollama or another model as a natural-language query layer. It should call the read API and answer only from retrieved records, with citations. AI must not generate missing specs or prices.

## Immediate next actions

1. Agree on the source/licence acceptance policy.
2. Create the catalogue TypeScript types and validation schemas.
3. Create the source audit spreadsheet and identify a pilot brand/model set.
4. Implement a private import pipeline and Firestore indexes/rules.
5. Publish a small verified pilot before expanding coverage.
