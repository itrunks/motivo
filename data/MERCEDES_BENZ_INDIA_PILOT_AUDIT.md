# Mercedes-Benz India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Discovery and source reconciliation; not approved for Firestore import  
**Primary sources:** Mercedes-Benz India official model overview and live configurator

## Scope and ingestion rules

- Treat the official India model overview and configurator as primary evidence for India-market product presence and displayed starting prices.
- A model-card starting price is a **model-level ex-showroom observation**, not a complete variant price or a city on-road quote.
- Keep separate powertrain/body-style entries where the OEM presents distinct products under the same model family (for example, GLC petrol/diesel versus GLC electric; EQS sedan versus EQS SUV).
- Do not infer variant names, equipment grades, fuel/engine mapping, or full price ranges from a starting price.
- Record source URL, observation timestamp, effective date (only when stated), price type, market, currency, and source wording.
- The official site warns that accessories, colours and fitments shown may not be standard; detailed India specifications and prices should be confirmed against the product brochure or a Mercedes-Benz franchise partner.
- No Firestore writes or publication were performed.

## Official model overview snapshot

The official India model overview reports 26 model entries. The following names and starting-price observations were visible in the overview crawl:

| OEM catalogue label | Fuel / powertrain shown | Starting price shown (INR) | Notes |
|---|---|---:|---|
| CLA | Electric | 56,50,000 | Model-level only |
| C-Class | Petrol, diesel | 61,20,000 | ICE entry |
| C-Class | Plug-in hybrid, petrol | 94,05,000 | Separate powertrain entry |
| EQS | Electric | 1,30,00,000 | Sedan entry |
| E-Class Sedan Long | Petrol, diesel | 81,50,000 | Long-wheelbase entry |
| S-Class | Plug-in hybrid | 2,20,00,000 | Verify current grade and powertrain naming |
| Mercedes-Maybach S-Class | Petrol | 2,87,50,000 | Overview label; configurator differs |
| E-Class Sedan | Plug-in hybrid | 1,45,00,000 | Separate entry from E-Class Sedan Long |
| EQS | Electric | 1,33,50,000 | SUV section; treat as EQS SUV family only after canonical-name reconciliation |
| Mercedes-Maybach EQS SUV | Electric | 2,40,00,000 | Distinct Maybach SUV |
| GLA | Petrol, diesel | 51,80,000 | Model-level only |
| GLC | Petrol, diesel | 77,00,000 | ICE entry |
| GLE | Petrol, diesel | 1,00,00,000 | Model-level only |
| GLS | Petrol, diesel | 1,37,50,000 | Model-level only |
| Mercedes-Maybach GLS | Petrol | 2,75,00,000 | Separate Maybach family |
| G-Class | Electric | 3,10,00,000 | Electric G-Class |
| G-Class | Diesel | 2,90,00,000 | Diesel G-Class |
| G-Class | Petrol | 3,74,00,000 | Petrol G-Class |
| GLC Coupé | Petrol | 99,85,000 | Distinct body style |
| GLE Coupé | Petrol | 1,52,00,000 | Distinct body style |
| CLE Cabriolet | Petrol | 1,15,00,000 | Cabriolet |
| Mercedes-Maybach SL Monogram Series | Petrol | 4,30,00,000 | Limited/series product naming |
| V-Class | Petrol, diesel | 1,40,00,000 | MPV |
| A-Class Hatchback | Petrol | 87,00,000 | Verify orderability/current inventory |
| CLE Coupé | Petrol | 1,32,50,000 | Distinct body style |
| Mercedes-AMG GT Coupé | Petrol | 3,00,00,000 | AMG product |

**Important:** The table is a transcription of the official overview snapshot, not a validated list of 26 unique canonical model families. The overview uses repeated labels (for example EQS and C-Class) across body-style/powertrain sections. Resolve canonical product IDs from individual OEM product pages before creating production catalogue entities.

## Live configurator cross-check

The live configurator also reports 26 entries, but several displayed prices differ from the overview snapshot:

| Product entry | Overview snapshot (INR) | Configurator snapshot (INR) | Disposition |
|---|---:|---:|---|
| E-Class Sedan Long | 81,50,000 | 82,00,000 | Keep both source observations; effective-date conflict unresolved |
| Mercedes-Maybach S-Class | 2,87,50,000 | 3,20,00,000 | Significant discrepancy; hold price as unresolved |
| EQS SUV entry | 1,33,50,000 | 1,35,00,000 | Confirm canonical product and retain both observations |
| GLC Electric | Not separately priced in overview snapshot | 78,50,000 | New Electric configurator entry |
| G-Class Electric | 3,10,00,000 | 3,15,00,000 | Retain source-specific observations |
| G-Class Petrol | 3,74,00,000 | 3,80,00,000 | Retain source-specific observations |
| CLE Cabriolet | 1,15,00,000 | 1,16,00,000 | Retain source-specific observations |
| CLE Coupé | 1,32,50,000 | 1,34,00,000 | Retain source-specific observations |
| Mercedes-AMG GT Coupé | 3,00,00,000 | 3,05,00,000 | Retain source-specific observations |
| Mercedes-Maybach SL Monogram Series | 4,30,00,000 | 4,40,00,000 | Retain source-specific observations |

The configurator snapshot is the better current discovery source for configurator-present products, but do not automatically overwrite overview observations. The source pages do not expose a clear effective date for every displayed starting price. Observation date for this audit is 2026-11-06; effective date remains unknown unless an OEM price announcement or dated price sheet establishes it.

## Current-market and lifecycle cautions

- The official homepage promotes the all-new electric CLA and the all-new GLC electric. The configurator includes both; GLC electric appears as a separate "New Electric" entry.
- The homepage also advertises an all-new GLA world premiere scheduled for 2026-07-29. Do not treat a launch teaser or future reveal as proof that a specific India variant is orderable unless the India configurator/product page confirms it.
- The homepage's November 2026 "Opportunity Knocks" stock cards include C 200 and GLE 300d 4MATIC LWB AMG Line. These are available-car/offer observations, not evidence of a full retail variant matrix.
- Do not import historical AMG, EQ, or discontinued models solely because third-party portals still list them.
- Third-party price aggregators may help discover candidates but cannot override official India product availability or official price evidence.

## Price evidence captured

All values below are **starting-price observations** displayed by the OEM, not exact variant-level price rows. The official pages do not provide a uniform dated price-list export in the captured evidence. No city-wise on-road prices were captured.

Official model overview:
- https://www.mercedes-benz.co.in/passengercars/models.html

Live configurator:
- https://www.mercedes-benz.co.in/passengercars/configurator.html?view=BODYTYPE

Official India homepage:
- https://www.mercedes-benz.co.in/

## Staging decision

**Do not stage variant-level prices from this audit yet.** The evidence supports:
1. Candidate model/product-family discovery.
2. Model-level starting-price observations with source-specific provenance.
3. A discrepancy queue for the overview/configurator price conflicts.
4. A requirement to inspect each individual model's configurator and brochure before variant ingestion.

Not supported yet:
- Complete current variant lists for all models.
- Exact variant-to-price mapping.
- Price effective dates for each displayed amount.
- City-wise on-road prices.
- Availability/orderability for every product/grade.
- Definitive canonical model IDs for all repeated OEM labels.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Mercedes-Benz India model overview | https://www.mercedes-benz.co.in/passengercars/models.html | Product discovery and overview starting prices | High for page display; effective date unresolved |
| Mercedes-Benz India configurator | https://www.mercedes-benz.co.in/passengercars/configurator.html?view=BODYTYPE | Current configurator presence and starting-price cross-check | High for page display; effective date unresolved |
| Mercedes-Benz India homepage | https://www.mercedes-benz.co.in/ | Current campaigns, available-car cards, launch communications | High for announcements; not a full price list |

## Next audit actions

1. Resolve canonical product identity for repeated model labels and body-style variants.
2. Open each India product page and capture exact selectable variants, engine, fuel, transmission, body style, and variant-level price where exposed.
3. Check the linked official eBrochure for grade/technical specification evidence.
4. Preserve all overview/configurator conflicts as separate observations until the OEM clarifies effective dates.
5. Begin city-wise on-road price collection only after source terms and reuse rights have been reviewed.
