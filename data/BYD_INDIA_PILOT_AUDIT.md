# BYD India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Official model and variant price observations captured; city-wise on-road price capture and source reuse review pending  
**Primary source:** BYD Auto India official price page

## Executive result

The current India retail passenger-car range contains four model families, all battery-electric:
1. ATTO 3 — electric SUV
2. eMAX 7 — electric MPV
3. SEAL — electric sedan
4. SEALION 7 — electric SUV

The official BYD India price page provides a model/variant table with starting ex-showroom prices, claimed range, battery capacity and seating. This is materially stronger evidence than third-party aggregator price bands and can be retained as OEM source observations, subject to verifying the live page's footnotes and effective-date terms before production ingestion.

## Official India model and variant observations

The official BYD India electric-car price page displays the following variant-level rows. Prices are INR ex-showroom as labelled by the OEM.

| Model | Variant | Price (INR) | Battery | Claimed range / test basis | Seating |
|---|---|---:|---:|---|---:|
| ATTO 3 | Dynamic | 24,99,000 | 49.92 kWh | 468 km ARAI / 410 km NEDC | 5 |
| ATTO 3 | Premium | 30,35,000 | 60.48 kWh | 521 km ARAI / 480 km NEDC | 5 |
| ATTO 3 | Superior | 34,49,000 | 60.48 kWh | 521 km ARAI / 480 km NEDC | 5 |
| eMAX 7 | Comfort 6-seater | 27,90,000 | 71.8 kWh | 485 km MIDC | 6 |
| eMAX 7 | Comfort 7-seater | 28,30,000 | 71.8 kWh | 485 km MIDC | 7 |
| eMAX 7 | Superior 6-seater | 29,30,000 | 71.8 kWh | 530 km NEDC | 6 |
| eMAX 7 | Superior 7-seater | 29,90,000 | 71.8 kWh | 530 km NEDC | 7 |
| SEAL | Dynamic | 41,50,000 | 61.44 kWh | 510 km (page-stated) | 5 |
| SEAL | Premium | 46,20,000 | 82.56 kWh | 650 km (page-stated) | 5 |
| SEAL | Performance | 53,65,000 | 82.56 kWh | 580 km (page-stated) | 5 |
| SEALION 7 | Dynamic | 41,90,000 | 71.8 kWh | 520 km NEDC | 5 |
| SEALION 7 | Premium | 49,90,000 | 82.56 kWh | 567 km NEDC | 5 |
| SEALION 7 | Performance | 55,90,000 | 82.56 kWh | 542 km NEDC | 5 |

**Observation metadata**
- Source: BYD India official electric-car price page.
- Observation date: 2026-11-06.
- Effective date: the price page does not expose a clear per-row effective date in the captured content.
- Price type: ex-showroom, as explicitly labelled in the OEM table.
- City: national/general listing; no city-specific RTO or on-road price is stated.
- Currency: INR.
- The page does not make it clear in the captured table whether every row is affected by a temporary offer. Recheck live OEM terms at ingestion time.

## Recent OEM pricing and product updates

### July 1, 2026 price revision

BYD India announced a portfolio price revision effective 2026-07-01. The increase was 1–2% depending on model and variant, driven by foreign-exchange movement. Customers booking in May/June under the announced conditions retained prior prices if delivery occurred by 2026-07-31. Do not apply a blanket uplift to old rows; use the current official variant table as a fresh observation and preserve the announcement as price-history evidence.

### eMAX 7 Comfort variants

A July 1, 2026 industry report says BYD introduced eMAX 7 Comfort variants with a 71.8 kWh battery, starting at ₹27.90 lakh ex-showroom. The official price page now lists Comfort 6-seat and 7-seat separately. Keep seating configuration in the variant identity; do not collapse these into one variant.

### SEALION 7 Dynamic and limited festive edition

The official BYD India news page records:
- SEALION 7 Dynamic introduced 2026-08-20 at an introductory price of ₹41.90 lakh.
- A limited-edition SEALION 7 for festive season introduced 2026-10-12.

The standard Dynamic variant and limited festive edition must be represented distinctly if the official product/booking material exposes a separate edition SKU. Do not create a new model family for the limited edition. The current standard price table lists Dynamic, Premium and Performance; the limited-edition page should be inspected before adding any edition-level price or equipment row.

## Upcoming / excluded candidates

| Candidate | Current evidence | Motivo disposition |
|---|---|---|
| ATTO 2 | Third-party listing shows estimated 2026 launch; no official India product/price page captured | Upcoming watchlist only |
| SEAL U | Third-party listing shows estimated late-2026 launch and plug-in hybrid positioning; no official India retail confirmation captured | Upcoming watchlist only |
| DENZA models | Separate BYD premium marque; not part of BYD India current passenger-car catalogue in the captured source | Separate brand-entry research, not BYD model |
| Global BYD PHEV/ICE models | No current India retail evidence | Exclude from India sellable catalogue |

## Data modelling and validation notes

- All four current model families are BEV. Do not add petrol/diesel variants.
- Keep battery capacity and claimed range test cycle as separate fields; do not compare ARAI, MIDC and NEDC numbers as equivalent.
- Keep eMAX 7 6-seat and 7-seat configurations as separate variants.
- Keep SEALION 7 Dynamic, Premium and Performance separate.
- Preserve the official OEM spelling/casing: ATTO 3, eMAX 7, SEAL, SEALION 7.
- Do not infer drivetrain (FWD/RWD/AWD), motor output, charging speed or model year from price-page data alone.
- The July 2026 price revision is historical context; do not apply a flat 1–2% uplift to the official current table.
- No city-wise on-road values were captured. The OEM dealer locator supports state/city selection, but a dealer locator is not an on-road quote.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| BYD India electric-car price page | https://bydautoindia.com/car-dealer/electric-car-price | Official model/variant price table, battery, range and seating | High for displayed OEM values; effective date not stated |
| BYD India car-price page | https://bydautoindia.com/car-dealer/byd-car-price | Official current model cards and starting-price cross-check | High for displayed OEM values |
| BYD India news | https://bydautoindia.com/news | Official dated product/price announcements | High |
| BYD India July 2026 price revision | https://bydautoindia.com/news/BYD-India-announces-price-revisions-across-vehicle-portfolio-effective-July-1%2C-2026 | Effective date and 1–2% model/variant-specific increase | High |
| Autocar India BYD listing (updated 2026-11-03) | https://www.autocarindia.com/cars/byd | Secondary cross-check for current four-model lineup and upcoming candidates | Medium; not primary price authority |
| ETAuto price revision report (2026-07-01) | https://auto.economictimes.indiatimes.com/news/passenger-vehicle/byd-india-introduces-prices-hike-in-select-electric-car-variants-by-up-to-1-lakh/132118139 | Cross-check for selected price changes and eMAX 7 Comfort introduction | Medium-high |
| Economic Times SEALION 7 Dynamic launch report | https://m.economictimes.com/industry/auto/auto-news/byds-india-unit-launches-sealion-7-dynamic-at-rs-41-90-lakh/articleshow/133370597.cms | Secondary dated launch confirmation | Medium-high |

## Staging decision

**BYD is ready for structured OEM price observations, but not yet for automatic production import.**

Safe to stage in a review queue:
1. Four current model families.
2. Thirteen OEM-displayed variant/seating price rows.
3. Ex-showroom price type, INR, observation date, battery capacity, range/test basis and seating.
4. July 2026 price-revision history and August/October SEALION 7 updates.

Still required before Firestore import:
1. Review the official page's full footnotes and price disclaimer.
2. Confirm the price page is not a temporary promotional or location-dependent view.
3. Capture drivetrain, motor output, charging and model-year from current OEM brochures.
4. Confirm current orderability and exact edition SKU for the limited SEALION 7.
5. Collect city-wise on-road prices from approved reusable sources.
6. Complete source licensing/reuse review.

No Firestore import, provider API credit usage, or publication was performed.
