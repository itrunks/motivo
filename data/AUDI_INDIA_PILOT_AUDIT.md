# Audi India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** OEM model discovery captured; variant-price ingestion held pending price reckoner data extraction and dated price sheet

## Executive result

Audi India's official model page exposes six primary model families: **Q3, Q5, Q7, Q8, A4 and A6**. Its official navigation additionally lists **Q3 Sportback, SQ8 and RS Q8 Performance** as individual product entries. The Q8 family therefore has three distinct official entries (Q8, SQ8, RS Q8 Performance); Q3 and Q3 Sportback must remain distinct body-style/product entries.

The official India site links an Audi Price Reckoner and explicitly states that ex-showroom prices do **not** include TCS. The price-reckoner page's underlying price data is loaded through an external interactive link and was not fully extractable in this audit. Do not invent OEM price rows from third-party listings.

## Official India catalogue snapshot

| Canonical product | Family | Body style / positioning | OEM source evidence | Disposition |
|---|---|---|---|---|
| Q3 | Q | SUV | Official model overview and navigation | Current official catalogue entry |
| Q3 Sportback | Q | Sportback SUV | Official navigation product link | Distinct body-style/product entry |
| Q5 | Q | SUV | Official model overview and navigation | Current official catalogue entry |
| Q7 | Q | SUV | Official model overview and navigation | Current official catalogue entry |
| Q8 | Q | SUV | Official model overview and navigation | Current official catalogue entry |
| SQ8 | Q / S performance | Performance SUV | Official navigation product link | Separate performance product |
| RS Q8 Performance | Q / RS performance | High-performance SUV | Official navigation product link | Separate performance product |
| A4 | A | Sedan | Official model overview and navigation | Current official catalogue entry |
| A6 | A | Sedan | Official model overview and navigation | Current official catalogue entry |

**Model count note:** The official overview groups products under six model families; the navigation lists nine product entries. Preserve both concepts in the data model (model family vs product) rather than forcing one count.

## Official pricing evidence

The Audi India Price Reckoner page links to the live price reckoner and states:

> The Ex-Showroom prices do not include TCS.

The interactive reckoner content was not available as static text in the captured source. Therefore:
- No exact OEM variant-level prices are staged by this audit.
- Do not derive exact Audi prices from third-party aggregators.
- Treat any future reckoner extraction as source-specific price observations with an observation timestamp.
- Record TCS as excluded from the ex-showroom figure; do not add it into the OEM amount.
- Confirm whether the live reckoner includes any additional caveats, effective date, variant selection or city selection before ingestion.

## Third-party market snapshot — discovery only

Third-party price portals crawled on 2026-11-06 list the following India-market candidates and indicative ex-showroom price ranges. These values are **not OEM-verified** and are not approved for production ingestion.

| Product | Third-party indicative range | Source status |
|---|---:|---|
| Q3 | ₹51.99–55.99 lakh | Secondary only |
| Q3 Sportback | ₹54.25 lakh | Secondary only |
| Q5 | ₹65.55–70.73 lakh | Secondary only |
| Q7 | ₹87.17–96.15 lakh | Secondary only |
| Q8 | ₹1.13 crore | Secondary only |
| SQ8 | ₹1.78–1.81 crore | Secondary disagreement |
| RS Q8 Performance | ₹2.34 crore | Secondary only |
| A4 | ₹46.88–55.83 lakh | Secondary only |
| A6 | ₹63.74–71.66 lakh | Secondary disagreement |

Third-party portal discrepancies are material: for example A6 and Q5 price ranges vary across portals, and SQ8 values differ slightly. Keep them in a research queue, not as canonical OEM price observations.

## Lifecycle and availability controls

- Audi's official India catalogue page and navigation are the authority for current India catalogue presence in this audit.
- Do not include A5, Q6 e-tron, A6 e-tron, e-tron GT facelift, Q9 or other future products as current retail products based only on third-party expected launch dates.
- The current official model overview does not list the older e-tron, Q8 e-tron or e-tron GT family in its primary six-family catalogue. Do not carry forward older EV catalogue rows as current.
- Third-party portals mark older Q3 2022–2026 and previous-generation e-tron products discontinued; use this only as a lifecycle cross-check, not as the primary proof.
- Distinguish Q8, SQ8 and RS Q8 Performance. Do not flatten S/RS derivatives into a generic Q8 variant unless the OEM product structure explicitly supports that relationship.
- Distinguish Q3 Sportback from Q3 SUV, as the OEM navigation exposes separate product links.
- Do not assume all variants are available in all cities or currently orderable merely because the model page exists.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Audi India all models | https://www.audi.in/en/models/ | Primary family list and official navigation product entries | High |
| Audi India homepage | https://www.audi.in/en/ | Current India product promotions and navigation | High |
| Audi India Price Reckoner | https://www.audi.in/en/customer-area/price-reckoner/ | Official ex-showroom pricing entry point and TCS exclusion note | High for terms; price data not statically extracted |
| Autocar India Audi listing | https://www.autocarindia.com/cars/audi | Secondary price and lifecycle discovery | Medium; not OEM price authority |
| ZigWheels Audi listing | https://www.zigwheels.com/audi-cars/ | Secondary current/discontinued model cross-check | Medium; not OEM price authority |
| CarDekho Audi listing | https://www.cardekho.com/cars/Audi | Secondary model/price cross-check | Medium; not OEM price authority |
| Audi India press / official site | https://www.audi.in/en/ | Official announcements; model-specific dated price announcements must be collected individually | High when announcement is OEM-authored |

## Staging decision

**Do not import variant-level Audi prices yet.**

Safe workpaper evidence:
1. Six official model families and nine official product entries.
2. Official ex-showroom pricing caveat: TCS excluded.
3. Third-party price ranges as discovery-only leads, clearly labelled non-OEM.
4. Lifecycle hold queue for older EVs and upcoming products.

Required before variant ingestion:
1. Extract the live Audi Price Reckoner content from its official linked application.
2. Capture exact product/variant labels, engine, fuel, transmission, drivetrain and ex-showroom amount.
3. Capture reckoner effective date, observation date, TCS and other price exclusions.
4. Confirm model-year and orderability per India product page or authorised dealer.
5. Collect city-specific on-road prices only from sources with approved reuse rights.

No Firestore import, provider API credit usage, or publication was performed.
