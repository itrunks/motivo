# Motivo vehicle catalogue architecture

## Decision

Motivo will use an owned, source-attributed vehicle catalogue in Firestore as its source of truth. The initial scope is India-market passenger cars, current models, and currently offered exact variants. Pricing coverage includes every supported ex-showroom and city-wise on-road observation with its effective date and source. Motivo will use a hybrid experience: Firestore remains the source of truth for all vehicle facts, while an Ollama-hosted open-weight model provides natural-language search, query interpretation, comparison summaries, and explanations grounded only in retrieved catalogue records. AI is an interface and reasoning layer, never the source of vehicle facts.

## Important scope boundary

"All variants" is the target coverage, not a claim that a complete, current, legally reusable dataset already exists. Coverage will expand through source-audited imports and manual review. A vehicle or field is not published unless its source, applicable market/year, and verification status are recorded. Missing values remain null/unknown; do not fill gaps with estimates presented as facts.

## Architecture

1. Expo / React Native Web client reads published catalogue data through Motivo HTTPS endpoints.
2. Firebase Cloud Functions validate query parameters and return normalized, published records.
3. Cloud Firestore stores canonical brands, models, variants, specifications, prices, ratings, and source provenance.
4. Trusted ingestion scripts / admin-only server jobs import source files and normalize records. No public client writes.
5. A review/publish step promotes validated records. Draft and rejected records are never returned by public endpoints.
6. An AI orchestration endpoint receives a user question, retrieves matching published records from Firestore, and passes only that grounded context to Ollama. The model may request approved read-only catalogue tools; the server executes them and returns results to the model.

The target data scope is all India-market passenger-car brands, models, model years/generations, and exact variants, including discontinued variants where reliable sources exist. "All" is a coverage goal, not a claim that a complete, current, legally reusable dataset is already available. Coverage will expand through source-audited imports and manual review.

The existing Let's Pick My Car integration is not the catalogue source of truth. Keep it optional and isolated until authentication, licence, field coverage, and credit economics are reviewed. Do not spend its metered credits during the initial catalogue build.

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

### Phase 6 — Hybrid AI layer
Run Ollama on a private server or managed compute host; do not expose a developer laptop's localhost endpoint to the public website. The browser calls a Firebase HTTPS endpoint, never Ollama directly. The server authenticates/rate-limits requests, retrieves relevant Firestore records, and supplies those records as context to Ollama's chat API. Use tool calling or structured JSON output for query intent and comparison requests. The server, not the model, performs Firestore reads and validates every requested ID/filter. Responses must cite record/source IDs and show "not available" for missing facts. AI must not generate missing specs, prices, ratings, or source references. If Ollama is unavailable, ordinary database search and comparison continue to work. See the official Ollama API docs for chat, tool calling, and structured outputs: https://github.com/ollama/ollama/blob/main/docs/api.md.

## Hybrid AI request flow

1. User asks a natural-language question in Motivo.
2. Firebase HTTPS endpoint validates the request and applies quotas.
3. A small intent parser / Ollama model extracts entities and filters (brand, model, variant, budget, fuel, transmission, location).
4. Backend queries Firestore using validated filters; it never lets the model execute arbitrary database queries.
5. Backend sends the retrieved facts and source metadata to Ollama for explanation/comparison.
6. Response validator checks every cited variant/source ID against retrieved records. Unsupported claims are removed or rewritten as unknown.
7. Client renders the answer with links to the exact variant and source references.

## AI hosting and privacy

- Ollama's local API is suitable for development on a trusted machine. Production needs an always-on private server or managed compute with appropriate memory/GPU capacity and access controls.
- Do not expose port 11434 publicly without a secure gateway, authentication, TLS, and request limits.
- Do not send user personal data or unrelated conversation history to the model. Send only the current question and the minimum catalogue context needed.
- Pin a model name and version after evaluation; test tool-call reliability, Tamil/English queries, latency, and hallucination rate before production.
- AI is optional. Database search, filters, and comparison must remain functional if the model is offline.
- Ollama supports chat tool calls and JSON-schema-constrained structured outputs; model capability varies, so test the selected model before depending on tool calling.

## Immediate next actions

1. Agree on the source/licence acceptance policy.
2. Create the catalogue TypeScript types and validation schemas.
3. Create the source audit spreadsheet and identify a pilot brand/model set.
4. Implement a private import pipeline and Firestore indexes/rules.
5. Publish a small verified pilot before expanding coverage.


## Implemented source audit and staging pipeline

- `data/README.md` records the current scope, source triage, licensing gate, price semantics and review workflow.
- `data/source-audit-template.csv` is the source-level audit register. Each publisher/dataset needs its own terms and permission decision.
- `data/catalogue-import-template.csv` is the row-level input template for variant and price observations.
- `scripts/validate_catalogue.py` validates CSV rows, enforces India/current-model intake conventions, checks city/state on-road price requirements, detects duplicate keys, generates deterministic IDs, and writes draft JSONL plus a validation report under `data/staging/`.
- The script is offline and dependency-free. It does not access the network, write to Firestore, or publish records. All accepted records remain `draft`; a human must approve source rights and factual accuracy before any admin import.
- Run: `python3 scripts/validate_catalogue.py data/catalogue-import-template.csv --out-dir data/staging`.
- Model-year plausibility defaults to current year ±1; current-sale status remains a reviewer decision backed by current OEM evidence.
