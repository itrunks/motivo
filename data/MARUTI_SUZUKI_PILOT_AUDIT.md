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


## Detailed S-Presso variant and ex-showroom price capture

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/s-presso/price

The official variant page exposes these exact displayed "Starting at" amounts. Its FAQ explicitly refers to the base amount as an ex-showroom price, and explains that on-road cost adds insurance, registration and road tax. These are therefore captured as official ex-showroom observations, not city-wise on-road quotes.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) | Audit status |
|---|---|---|---:|---|
| S-Presso Std (O) MT | Petrol | Manual | 349900 | price captured |
| S-Presso LXi (O) MT | Petrol | Manual | 382400 | price captured |
| S-Presso VXi (O) MT | Petrol | Manual | 432400 | price captured |
| S-Presso LXi (O) CNG | S-CNG | Manual | 464400 | price captured |
| S-Presso VXi (O) AGS | Petrol | Automatic (AGS) | 477400 | price captured |
| S-Presso VXi+ (O) MT | Petrol | Manual | 482400 | price captured |
| S-Presso VXi (O) CNG | S-CNG | Manual | 514400 | price captured |
| S-Presso VXi+ (O) AGS | Petrol | Automatic (AGS) | — | variant listed; exact price not exposed in captured page content |

The page also states that prices prevailing at invoice/bill time apply. Treat the captured values as observations retrieved on the checked date, not guaranteed future dealer quotes. The page displays a waiting-time indicator; it is not a guarantee of orderability or delivery date.

The official page currently lists eight variant labels, while only seven exact starting amounts were exposed in the captured content. Do not fill the missing VXi+ (O) AGS price from a third-party listing. Recheck the official page interactively or obtain an official dealer price list before recording that eighth amount.

## Data quality and import boundary

- These are variant-level ex-showroom observations for S-Presso only.
- No city-wise on-road prices have been captured in this pilot.
- No Firestore import is authorized by this audit.
- Source terms and commercial redistribution permission remain under review.
- The official brochure supports variant naming and equipment/specification cross-checks, but the official live price page is the source for the captured amounts.

Additional source:
- https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/s-presso/documents/S-presso-Brochure.pdf
