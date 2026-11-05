# Maruti Suzuki pilot source audit

Checked: 2026-11-06
Market: India
Primary sources:
- https://www.marutisuzuki.com/
- https://www.nexaexperience.com/

## Current retail catalogue candidates

The official Maruti Suzuki India homepage currently separates its passenger-car catalogue into Arena and NEXA.

| Retail channel | Models shown on official site |
|---|---|
| Arena | Alto K10, Celerio, Eeco, Ertiga, S-Presso, Dzire, Swift, Victoris, Brezza, Wagon R |
| NEXA | e Vitara, Baleno, Grand Vitara, Fronx, Jimny, XL6, Invicto |

This is a model-listing audit only. It does not yet establish the exact currently orderable variants, variant-year applicability, complete price lists, or city-wise on-road prices for every model.

## Variant-level evidence sample: S-Presso

The official S-Presso price page exposes variant names and powertrain details, including:
- Std (O) MT — 998 cc, manual, petrol
- LXi (O) MT — 998 cc, manual, petrol
- VXi (O) MT — 998 cc, manual, petrol
- LXi (O) CNG — 998 cc, manual, S-CNG
- VXi (O) AGS — 998 cc, automatic, petrol
- VXi+ (O) MT — 998 cc, manual, petrol
- VXi (O) CNG — 998 cc, manual, S-CNG
- VXi+ (O) AGS — 998 cc, automatic, petrol

The page URL includes `city=ramban` and the displayed figures are labelled "Starting at". Do not ingest these amounts as national ex-showroom prices or Ramban on-road prices until the page's price semantics and location behaviour are confirmed. Record the exact source URL and capture the displayed amount only after that check.

## Audit decision

- Brand/model listing evidence: `verified_listing`
- Exact current variant coverage: `partial`
- Price semantics: `needs_review`
- City-wise on-road coverage: `not_audited`
- Source reuse / redistribution permission: `review_required`

## Next audit work

1. Capture the official model-specific price/variant pages for every Arena and NEXA model.
2. Record exact variant labels, engine, fuel, transmission, and displayed amount with the page's city parameter.
3. Confirm whether each amount is ex-showroom, on-road, or another displayed starting price before creating a price observation.
4. Preserve source URLs and retrieval dates; do not infer missing variants or prices.
5. Review OEM terms and permissions before bulk import or public redistribution.

This file is an audit artifact only. It is not an approved Firestore import manifest.
