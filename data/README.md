# Motivo catalogue data workflow

## Approved scope

- Market: India (`IN`) passenger cars.
- Model coverage: current models and currently offered variants only. A model-year label may be the current or immediately upcoming model year where the manufacturer is actively selling it.
- Prices: collect all supported price types and locations. Keep ex-showroom and on-road as separate records. On-road prices must be tied to a city/state (and RTO where available), effective date, and an explicit classification.
- No historical/discontinued catalogue import in this phase.

## Source acceptance

A public webpage or downloadable file is not automatically reusable. Before importing or publishing, record the publisher, exact source URL, terms/licence URL, commercial-use permission, redistribution permission, attribution requirements, retrieval date, and the fields covered.

Preferred evidence order:
1. Manufacturer/OEM product pages, brochures, price lists and official dealer circulars for model, variant, specification and ex-showroom price facts.
2. Government/open-government sources for government-published vehicle and location facts where relevant. These generally do not provide a complete retail variant catalogue or city on-road prices.
3. Official crash-test agencies for safety results, preserving the tested configuration and protocol.
4. Independent publishers only after reviewing their terms and confirming commercial reuse and redistribution rights for the exact data/compilation.

Do not scrape behind login, bypass access controls, or republish third-party photographs, brochures, descriptions or compilations without permission. Store facts and source links; do not copy expressive text. Treat uncertain permissions as `hold`.

## Initial source audit (2026-11-06)

| Source | Candidate coverage | Audit decision | Reason / next action |
|---|---|---|---|
| OEM official websites and brochures (audit separately per manufacturer) | Current model/variant names, specifications, ex-showroom prices | `review_required` | Primary evidence, but terms, automated access and reuse must be checked per OEM. Do not assume public display grants bulk redistribution rights. |
| TCO India dataset, Hugging Face: https://huggingface.co/datasets/bhavabhuthi/tco-india | Brands, models, variants/specs, dated variant × city on-road prices; claims CarDekho/CarWale coverage | `hold` | Dataset README states CC-BY-4.0 for its compilation and names CarDekho/CarWale as upstream sources. That statement alone does not establish rights to redistribute upstream-derived content commercially. Obtain upstream permission/terms analysis and inspect row-level provenance before import. |
| SIAM statistical publications: https://www.siam.in/statistical-services/statistical-profile | Industry production/sales and model-wise statistics | `exclude_for_catalogue_seed` | Relevant reports are subscription-priced; not a free, reusable full retail variant/price source. |
| Open Government Data Platform: https://data.gov.in/ | Government vehicle/transport statistics and selected datasets | `limited_use` | Useful for contextual/official statistics, not a comprehensive live retail model/variant or city on-road price catalogue. Check each dataset's own licence/API terms. |
| Parivahan VAHAN public reports: https://analytics.parivahan.gov.in/analytics/vahanpublicreport | Registration aggregates | `limited_use` | Not a retail specification/price feed; use only for appropriately attributed aggregate context if terms permit. |

The audit above is an initial source triage, not a blanket legal opinion. Each specific source URL and dataset revision needs its own approval before import.

## Import workflow

1. Copy `catalogue-import-template.csv` and add only source-verified records.
2. Keep one row per entity fact. A variant row describes a current variant; a price row describes one variant × price type × location × effective date.
3. Run `python3 scripts/validate_catalogue.py path/to/file.csv --out-dir data/staging`.
4. Review the generated JSONL and validation report. The tool emits only draft records; it never publishes to Firestore.
5. Resolve every error and review every warning. Confirm source permission separately; schema-valid does not mean licence-approved.
6. Import to Firestore only through a future authenticated admin-only import job after human review. Never put service-account credentials in this repository or browser bundle.

## Price semantics

- `ex_showroom`: exact amount for the exact variant and effective date. City may be omitted only when the publisher explicitly treats it as nationally uniform.
- `on_road`: must include city and state. Preserve component breakdown when available. Do not calculate missing insurance, tax or registration as if it were a published quote.
- `official`: directly published by OEM/authorised source; `estimated`: calculated/indicative; `user_reported`: user-provided. Never present estimates as dealer quotes.
- Keep every price observation; do not overwrite a previous effective price. Current-price APIs should select the newest valid observation and show its date/source.

## Current-model rule

A row must be for a model currently listed for sale by the OEM or supported by a current official price list/brochure. The validator checks model-year plausibility but cannot determine whether a model is still on sale. That is a reviewer decision backed by source evidence.
