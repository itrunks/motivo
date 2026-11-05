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


## Dzire variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/dzire/price

The official price page exposes nine exact variant cards. The page FAQ states that the displayed base price is ex-showroom and that on-road price varies by city, insurance and registration. The following are captured as OEM ex-showroom starting-price observations.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) |
|---|---|---|---:|
| Dzire LXi MT | Petrol | Manual | 630600 |
| Dzire VXi MT | Petrol | Manual | 727100 |
| Dzire VXi AMT | Petrol | Automatic | 772100 |
| Dzire VXi CNG | S-CNG | Manual | 818100 |
| Dzire ZXi MT | Petrol | Manual | 827700 |
| Dzire ZXi AMT | Petrol | Automatic | 872700 |
| Dzire ZXi+ MT | Petrol | Manual | 896300 |
| Dzire ZXi CNG | S-CNG | Manual | 918700 |
| Dzire ZXi+ AMT | Petrol | Automatic | 941300 |

**Source inconsistency to resolve:** the same page's FAQ says the top ZXi+ AMT ex-showroom price is ₹9,31,300, while the visible variant card says ₹9,41,300. Retain the card observation with an explicit conflict flag; do not silently reconcile or publish this record until rechecked against a dated official price list/dealer confirmation.

Audit status:
- Nine exact variant cards and displayed amounts captured
- One internal OEM page price conflict flagged
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

## Brezza variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/brezza/price

The official page exposes a selector with 13 variant labels, but only three price cards and exact amounts were available in the captured page content. Do not infer the other ten amounts.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) |
|---|---|---|---:|
| Brezza VXi AT | Petrol | Automatic | 1060900 |
| Brezza ZXi AT | Petrol | Automatic | 1200500 |
| Brezza ZXi+ AT | Petrol | Automatic | 1370500 |

The official page explicitly labels these as Delhi ex-showroom prices effective 24 July 2026. Preserve that geography and effective date in each observation; do not convert them to national prices or on-road prices. The selector also lists LXI/VXI/ZXI manual, CNG manual and Turbo-labelled variants, but the captured content does not expose corresponding exact amounts. The page's selected-card engine summary appears inconsistent with the broader Brezza product configuration; verify variant-to-engine mapping from the matching official brochure before variant import.

Audit status:
- 13 variant labels visible in selector
- 3 exact Delhi ex-showroom card amounts captured
- Remaining displayed amounts not captured; no inference
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

## Ertiga variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/ertiga/price

The official page exposes nine exact variant cards and starting prices. The captured OEM card summaries identify 1,462 cc, manual/6AT, Smart Hybrid petrol or S-CNG.

| Official variant label | Fuel / powertrain | Transmission | Displayed starting price (INR) |
|---|---|---|---:|
| Ertiga LXi MT | Smart Hybrid petrol | Manual (5MT) | 890000 |
| Ertiga VXi MT | Smart Hybrid petrol | Manual (5MT) | 995300 |
| Ertiga VXi CNG | S-CNG | Manual (5MT) | 1093800 |
| Ertiga ZXi MT | Smart Hybrid petrol | Manual (5MT) | 1101500 |
| Ertiga VXi AT | Smart Hybrid petrol | Automatic (6AT) | 1130300 |
| Ertiga ZXi+ MT | Smart Hybrid petrol | Manual (5MT) | 1169100 |
| Ertiga ZXi CNG | S-CNG | Manual (5MT) | 1200000 |
| Ertiga ZXi AT | Smart Hybrid petrol | Automatic (6AT) | 1236500 |
| Ertiga ZXi+ AT | Smart Hybrid petrol | Automatic (6AT) | 1304100 |

The page's FAQ contains an apparent unrelated Eeco CNG price sentence under an Ertiga question. Ignore that FAQ text for Ertiga price facts; use the Ertiga variant cards only. The page states invoice-date pricing applies. Seating capacity is shown as seven.

Audit status:
- Nine exact OEM variant cards and displayed amounts captured
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

## Victoris variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/victoris/price

The official page exposes 21 variant price cards. Exact displayed starting prices are captured below without filling any missing values. Petrol and S-CNG card summaries show 1,462 cc; strong-hybrid cards show 1,490 cc. Some AWD/ADAS naming differs between the image/card title and the visible card text; retain the exact OEM label and verify the final variant code against the brochure before import.

| Official variant label | Fuel / powertrain | Transmission / drive | Displayed starting price (INR) |
|---|---|---|---:|
| Victoris LXI MT 2W | Petrol | Manual, 2WD | 1049900 |
| Victoris LXI CNG MT | S-CNG | Manual | 1154900 |
| Victoris VXI MT 2W | Petrol | Manual, 2WD | 1184900 |
| Victoris VXI CNG MT 2W | S-CNG | Manual, 2WD | 1289900 |
| Victoris VXI AT 2W | Petrol | Automatic, 2WD | 1340900 |
| Victoris ZXI MT | Petrol | Manual | 1377300 |
| Victoris ZXI (O) MT | Petrol | Manual | 1384400 |
| Victoris ZXI CNG MT | S-CNG | Manual | 1482300 |
| Victoris ZXI AT | Petrol | Automatic | 1533300 |
| Victoris ZXI (O) AT | Petrol | Automatic | 1540400 |
| Victoris ZXI+ MT | Petrol | Manual | 1544300 |
| Victoris ZXI+ (O) MT | Petrol | Manual | 1563400 |
| Victoris VXI THS 2W | Strong Hybrid | Automatic, 2WD | 1642900 |
| Victoris ZXI+ AT 2W (ADAS) | Petrol | Automatic, 2WD | 1739300 |
| Victoris ZXI+ (O) AT 2W (ADAS) | Petrol | Automatic, 2WD | 1758400 |
| Victoris ZXI Strong Hybrid | Strong Hybrid | Automatic | 1800300 |
| Victoris ZXI (O) Strong Hybrid | Strong Hybrid | Automatic | 1859300 |
| Victoris ZXI+ AT 4W (AllGrip) | Petrol | Automatic, 4WD | 1884300 |
| Victoris ZXI+ (O) AT 4W (AllGrip) | Petrol | Automatic, 4WD | 1942300 |
| Victoris ZXI+ Strong Hybrid | Strong Hybrid | Automatic | 1967300 |
| Victoris ZXI+ (O) Strong Hybrid | Strong Hybrid | Automatic | 1998900 |

The source page displays a waiting-time indicator on these cards; this is a dated page snapshot, not a delivery guarantee. No city-wise on-road prices were captured.

Audit status:
- 21 exact OEM card amounts captured
- Variant naming / 2WD-4WD / ADAS labels need brochure-code cross-check before import
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

## Eeco variant price audit

Checked: 2026-11-06
Primary source: https://www.marutisuzuki.com/arena/eeco/price

The official Eeco page exposes five exact price cards. Four are passenger configurations; the ambulance shell is a special-purpose configuration and should not be mixed into the retail passenger-car variant catalogue without a separately approved scope decision.

| Official variant label | Fuel | Transmission | Displayed starting price (INR) | Catalogue treatment |
|---|---|---|---:|---|
| Eeco 5 Seater Standard | Petrol | Manual (5MT) | 528400 | Passenger |
| Eeco 6 Seater Standard | Petrol | Manual (5MT) | 554900 | Passenger |
| Eeco 5 Seater AC | Petrol | Manual (5MT) | 561300 | Passenger |
| Eeco Ambulance Shell | Petrol | Manual (5MT) | 644600 | Hold: special-purpose |
| Eeco 5 Seater AC CNG | S-CNG | Manual (5MT) | 645800 | Passenger |

The variant selector also lists Eeco Ambulance, but no exact price card for that label was exposed in the captured content. Do not infer its price. The page FAQ contains a different base cargo-variant amount and a CNG cargo-variant amount; those do not match the passenger variant cards above and must not be substituted for them. Keep the passenger card observations separate from cargo/ambulance configurations. The page displays a waiting-time indicator and states invoice-date prices/schemes apply.

Audit status:
- Five exact OEM card amounts captured
- Four passenger configurations separated from ambulance special-purpose variant
- Eeco Ambulance exact amount not captured
- City-wise on-road prices not captured
- Source reuse / redistribution permission review required
- Firestore import not performed

## Arena audit progress after this batch

- Dzire: 9 exact price cards; one conflicting top-variant amount in the OEM FAQ flagged for reconciliation.
- Brezza: 3 exact Delhi ex-showroom price cards; 10 other selector variants remain without captured amounts.
- Ertiga: 9 exact price cards.
- Victoris: 21 exact price cards; exact variant codes and drivetrain labels need brochure cross-check.
- Eeco: 5 exact price cards; ambulance shell held outside the retail passenger variant set.

All captured amounts remain source-audit observations only. No Firestore write or public catalogue publication has been performed. OEM terms/reuse permission still require review.


## NEXA current model and source audit

Checked: 2026-11-06
Primary sources:
- https://www.nexaexperience.com/
- https://www.nexaexperience.com/compare-cars

The official NEXA homepage and comparison page currently expose seven India-market models: Baleno, FRONX, Grand Vitara, Jimny, XL6, Invicto and e VITARA. This verifies current official catalogue presence, but does not by itself establish every variant's orderability, stock availability or exact model-year mapping.

| Model | Official price/detail page | Audit finding |
|---|---|---|
| Baleno | https://www.nexaexperience.com/baleno/price | Price page exists; captured page content is dynamic and does not expose a reliable complete variant-price table |
| FRONX | https://www.nexaexperience.com/fronx/price | Price page exists; FAQ explicitly says displayed site price is ex-showroom and on-road varies by city/state |
| Grand Vitara | https://www.nexaexperience.com/grand-vitara/price | Search-indexed official variant table exposes 18 named variants and exact amounts; source page's price effective-date context requires confirmation before importing |
| Jimny | https://www.nexaexperience.com/jimny/price | Official price page and top-model ex-showroom amount are exposed; complete card table not captured in this pass |
| XL6 | https://www.nexaexperience.com/xl6/price | Official model page confirms seven variants: Zeta, Zeta AT, Alpha, Alpha AT, Alpha+, Alpha+ AT and Zeta CNG; exact complete price table not captured |
| Invicto | https://www.nexaexperience.com/invicto/price | Official price page exists and states prices are indicative ex-showroom; complete variant table not captured |
| e VITARA | https://www.nexaexperience.com/e-vitara/price | Official electric model price page exists; exact price cards not exposed in captured page content |

### Grand Vitara: official variant price table captured from search index

The official NEXA Grand Vitara price page's indexed content exposes the following 18 exact variant amounts. Treat these as preliminary observations because the indexed page text says reductions/starting prices are effective from 22 September 2025 and vary by variant; re-open the live price page and confirm current applicability/effective date before import.

| Official variant label | Displayed price (INR) |
|---|---:|
| Grand Vitara Sigma | 1076500 |
| Grand Vitara Delta | 1209700 |
| Grand Vitara Delta AT | 1344700 |
| Grand Vitara Zeta | 1370000 |
| Grand Vitara Zeta (O) | 1428000 |
| Grand Vitara Zeta AT | 1505000 |
| Grand Vitara Alpha | 1519700 |
| Grand Vitara Zeta (O) AT | 1563000 |
| Grand Vitara Alpha (O) | 1577600 |
| Grand Vitara Alpha AT | 1654700 |
| Grand Vitara Strong Hybrid Delta+ | 1663300 |
| Grand Vitara Alpha (O) AT | 1712600 |
| Grand Vitara Strong Hybrid Zeta+ | 1791600 |
| Grand Vitara Alpha ALLGRIP | 1799700 |
| Grand Vitara Strong Hybrid Zeta+ (O) | 1850300 |
| Grand Vitara Alpha (O) ALLGRIP | 1857600 |
| Grand Vitara Strong Hybrid Alpha+ | 1950200 |
| Grand Vitara Strong Hybrid Alpha+ (O) | 1957000 |

### NEXA source and price-quality flags

- The official NEXA compare page lists Baleno from ₹9,09,900, while the official homepage search snapshot lists Baleno from ₹5,98,900. These are materially inconsistent; neither amount is accepted as a price observation until the live model price page is rechecked and the discrepancy explained.
- The NEXA compare page lists starting prices for Invicto, e VITARA, Jimny, XL6, Grand Vitara and FRONX, but these summary values are not a substitute for exact variant cards.
- NEXA price-page FAQs describe site prices as ex-showroom and explain that on-road prices vary with city/state taxes, registration and insurance. Do not convert these figures into city on-road prices.
- Official page presence is a model-listing signal, not proof of current dealer stock or a complete current variant matrix.
- Source terms and commercial reuse permission remain review required.
- No NEXA records have been imported into Firestore.

Sources:
- https://www.nexaexperience.com/compare-cars
- https://www.nexaexperience.com/
- https://www.nexaexperience.com/baleno/price
- https://www.nexaexperience.com/fronx/price
- https://www.nexaexperience.com/grand-vitara/price
- https://www.nexaexperience.com/jimny/price
- https://www.nexaexperience.com/xl6/price
- https://www.nexaexperience.com/invicto/price
- https://www.nexaexperience.com/e-vitara/price

