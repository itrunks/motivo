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


## Detailed Alto K10 variant and ex-showroom price capture

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/alto-k10/price

The official Alto K10 variant page lists eight current variant labels with displayed "Starting at" prices. The page's city query parameter varies across search snapshots, but the amounts shown in the page content are consistent across the retrieved variants. The page also states that prices/schemes prevailing at invoice/bill time apply. Capture these as dated official ex-showroom observations only after confirming the page's displayed amount semantics; do not treat them as on-road amounts.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) |
|---|---|---|---:|
| Alto K10 Std (O) | Petrol | Manual | 369900 |
| Alto K10 LXi (O) MT | Petrol | Manual | 399900 |
| Alto K10 VXi (O) MT | Petrol | Manual | 452400 |
| Alto K10 LXi (O) CNG | S-CNG | Manual | 484400 |
| Alto K10 VXi (O) AGS | Petrol | Automatic (AGS) | 497400 |
| Alto K10 VXi+ (O) MT | Petrol | Manual | 499900 |
| Alto K10 VXi (O) CNG | S-CNG | Manual | 534400 |
| Alto K10 VXi+ (O) AGS | Petrol | Automatic (AGS) | 544900 |

The official brochure supports the variant-family names and confirms 5MT/AGS availability for petrol and 5MT for CNG. It also states CNG seating capacity as four persons, while petrol seating capacity is five. Do not store one seating value across all variants.

Sources:
- https://www.marutisuzuki.com/arena/alto-k10/price
- https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/alto-k10/documents/AltoK10-KV-Brochure.pdf

Audit status:
- Variant names and displayed amounts: captured from OEM page
- Detailed variant specifications: brochure cross-check available
- City-specific on-road prices: not captured
- Source reuse / redistribution permission: review required
- Firestore import: not performed

Note: The official page content is the evidence for the captured amount set. Third-party price aggregators are not used to fill or correct OEM values. The data remains an audit observation pending terms review and human approval.


## Celerio variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/celerio/price?city=perembra

The official Celerio page exposes a list of eight variant names in its variant selector, and four cards with exact displayed starting prices in the captured page content. Capture only the four directly displayed amounts; do not infer the other four prices from the selector or third-party sources.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) | Evidence |
|---|---|---|---:|---|
| Celerio LXi MT | Petrol | Manual (5MT) | 469900 | Price displayed |
| Celerio VXi MT | Petrol | Manual (5MT) | 518400 | Price displayed |
| Celerio VXi AGS | Petrol | Automatic (AGS) | 563400 | Price displayed |
| Celerio ZXi MT | Petrol | Manual (5MT) | 573400 | Price displayed |

The page's variant selector additionally lists Celerio VXi CNG, ZXi+ AGS, ZXi+ MT, ZXi AGS and other trim labels; no exact amount for those variants is included here because the captured page content did not expose their price cards. Note that the captured card text appears to have some transmission feature labels out of sequence; use the explicit variant name and the card's headline powertrain summary as evidence, and recheck the detailed variant specification before importing transmission values.

The official page's terms say prices prevailing at invoice/bill time apply, and its FAQ describes the displayed base price as ex-showroom. No on-road price is recorded in this audit.

Audit status:
- Exact variant labels: partial list visible
- Exact displayed prices: 4 captured
- Full variant × specification matrix: pending
- City-wise on-road prices: not captured
- Source reuse / redistribution permission: review required
- Firestore import: not performed

Source note: The official website page was opened with a city query parameter (`city=perembra`). Do not assume the displayed starting price is a local on-road quote; retain it as an OEM displayed starting/ex-showroom observation subject to final source semantics review.


## WagonR variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/wagon-r/price?city=kurukshetra

The official OEM page exposes the following variant cards and exact displayed starting prices. Amounts are retained as OEM displayed starting/ex-showroom observations; they are not on-road quotes.

| Official variant label | Engine | Fuel | Transmission | Displayed starting price (INR) |
|---|---:|---|---|---:|
| WagonR LXi MT | 998 cc | Petrol | Manual | 498900 |
| WagonR VXi MT | 998 cc | Petrol | Manual | 554400 |
| WagonR LXi CNG | 998 cc | S-CNG | Manual | 593900 |
| WagonR ZXi MT | 1197 cc | Petrol | Manual | 598400 |
| WagonR VXi AGS | 998 cc | Petrol | Automatic (AGS) | 599400 |
| WagonR ZXi AGS | 1197 cc | Petrol | Automatic (AGS) | 643400 |
| WagonR VXi CNG | 998 cc | S-CNG | Manual | 649400 |
| WagonR ZXi+ MT | 1197 cc | Petrol | Manual | 652400 |
| WagonR ZXi+ AGS | 1197 cc | Petrol | Automatic (AGS) | 697400 |
| WagonR Bioflex (ZXi+ MT FFV) | 1197 cc | Flex Fuel | Manual | 723900 |

The OEM page displays a "2+ months waiting" indicator alongside the listed cards. This is captured as page context only, not a guaranteed delivery estimate. The page states prices/schemes prevailing at invoice/bill time apply.

Audit status:
- Ten exact OEM variant labels and displayed amounts captured
- Variant powertrain summary captured from OEM cards
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

Source: Maruti Suzuki official WagonR price and variants page. The page was opened with a city query parameter, but the displayed amounts are treated as OEM starting prices, not location-specific on-road quotes.


## Swift variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/swift/price

The official Maruti Suzuki Swift price page exposes the following exact variant cards and displayed starting prices. Prices are recorded as official OEM ex-showroom starting-price observations, not on-road quotes.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) |
|---|---|---|---:|
| Swift LXi MT | Petrol | Manual | 583900 |
| Swift VXi MT | Petrol | Manual | 667900 |
| Swift VXi (O) MT | Petrol | Manual | 693900 |
| Swift VXi AMT | Petrol | Automatic (AMT) | 712900 |
| Swift VXi (O) AMT | Petrol | Automatic (AMT) | 738900 |
| Swift VXi CNG | S-CNG | Manual | 757400 |
| Swift ZXi MT | Petrol | Manual | 761900 |
| Swift VXi (O) CNG | S-CNG | Manual | 783400 |
| Swift VXi CNG AGS | S-CNG | Automatic (AGS) | 792400 |
| Swift ZXi AMT | Petrol | Automatic (AMT) | 806900 |
| Swift VXi (O) CNG AGS | S-CNG | Automatic (AGS) | 818400 |
| Swift ZXi+ MT | Petrol | Manual | 843900 |
| Swift ZXi CNG | S-CNG | Manual | 851400 |
| Swift ZXi CNG AGS | S-CNG | Automatic (AGS) | 886400 |
| Swift ZXi+ AMT | Petrol | Automatic (AMT) | 888900 |

The official page indicates 2+ months waiting on many cards and states prices/schemes prevailing at invoice/bill time apply. Treat waiting-time text as a page snapshot only, not a delivery promise. Some CNG AGS cards do not expose engine displacement in the card text; do not fill missing engine values from inference.

Audit status:
- 15 official variant cards and displayed amounts captured
- Fuel and transmission captured from OEM card labels
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

Source: Maruti Suzuki official Swift price and variants page. The official page states that displayed prices are indicative ex-showroom prices and applicability is based on invoice date.
