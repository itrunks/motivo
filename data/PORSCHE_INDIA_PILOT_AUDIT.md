# Porsche India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Official configurator and model-comparison observations captured; production import pending price-term and model-year reconciliation

## Executive result

Porsche India's current India model-comparison/configurator surface groups its portfolio into five model families: **911, Taycan, Panamera, Macan and Cayenne**. The India comparison tool reports 20 available model/derivative entries. The older Porsche India dealer microsite still mentions Boxster and Cayman in generic brand copy; that text is not evidence of current India retail availability and should not be used to create current catalogue rows.

The official India-configured model pages display prices in INR and label the amounts "incl. VAT". In India context this is the OEM's displayed configured price basis; do not silently relabel it "ex-showroom" without checking the exact price disclaimer/terms on each page. The configurator also shows model year, fuel/powertrain, drivetrain and transmission for each entry.

## Official current family inventory

| Model family | Product group | Powertrain |
|---|---|---|
| 911 | Carrera, GTS, GT3, Turbo | Petrol |
| Taycan | 4S, 4S Black Edition, Turbo | Electric |
| Panamera | Panamera | Petrol |
| Macan | Macan | Petrol |
| Macan | Macan Electric, Macan 4S Electric, Macan Turbo Electric | Electric |
| Cayenne | Cayenne, Black Edition, GTS, Coupé derivatives | Petrol |
| Cayenne | Cayenne Electric, Cayenne Turbo Electric | Electric |

The official comparison tool shows 20 available entries across the five families, including additional 911, Taycan and Cayenne derivatives beyond the subset transcribed below. Use the live configurator as the source of truth for the complete selectable list at ingestion time.

## Official price and specification observations

Prices are as displayed by Porsche India's India model comparison/configurator on 2026-11-06. The page uses "From" and "incl. VAT"; no city-specific RTO/on-road quote was captured. Amounts below are INR.

| Family | Official product/derivative | Model year shown | Powertrain | Drive | Transmission | Displayed price (INR) |
|---|---|---:|---|---|---|---:|
| 911 | 911 Carrera | 2027 | Petrol | RWD | PDK automatic | 2,11,29,000 |
| 911 | 911 Carrera 4 GTS | 2027 | Petrol | AWD | PDK automatic | 2,82,14,000 |
| 911 | 911 Turbo S | 2027 | Petrol | AWD | PDK automatic | 3,82,49,000 |
| 911 | 911 GT3 | 2027 | Petrol | RWD | PDK automatic | 3,32,60,000 |
| Taycan | Taycan 4S | 2027 | Electric | AWD | Automatic | 2,00,70,000 |
| Taycan | Taycan 4S Black Edition | 2027 | Electric | AWD | Automatic | 2,09,45,000 |
| Taycan | Taycan Turbo | 2027 | Electric | AWD | Automatic | 2,74,27,000 |
| Panamera | Panamera | 2027 | Petrol | RWD | PDK automatic | 1,79,12,000 |
| Macan | Macan (electric) | 2025 | Electric | RWD | Automatic | 1,21,62,000 |
| Macan | Macan 4S Electric | 2027 | Electric | AWD | Automatic | 1,63,04,000 |
| Macan | Macan Turbo Electric | 2027 | Electric | AWD | Automatic | 1,77,74,000 |
| Macan | Macan (petrol) | 2026 | Petrol | AWD | PDK automatic | 91,09,000 |
| Cayenne | Cayenne Electric | 2026 | Electric | AWD | Automatic | 1,77,27,000 |
| Cayenne | Cayenne Turbo Electric | 2026 | Electric | AWD | Automatic | 2,27,51,000 |
| Cayenne | Cayenne | 2027 | Petrol | AWD | Automatic | 1,51,18,000 |
| Cayenne | Cayenne Black Edition | 2027 | Petrol | AWD | Automatic | 1,83,03,000 |
| Cayenne | Cayenne GTS | 2027 | Petrol | AWD | Automatic | 2,11,26,000 |
| Cayenne Coupé | Cayenne Coupé | 2027 | Petrol | AWD | Automatic | 1,57,37,000 |
| Cayenne Coupé | Cayenne Coupé Black Edition | 2027 | Petrol | AWD | Automatic | 1,89,95,000 |
| Cayenne Coupé | Cayenne GTS Coupé | 2027 | Petrol | AWD | Automatic | 2,12,61,000 |

**Data caution:** The comparison page is a dynamic configurator. Prices and selected product entries can change. The 2026-11-06 values are observations, not a permanent price list. The "incl. VAT" wording must be preserved as source terminology in the raw observation until the exact Indian tax/price basis is confirmed by Porsche India.

## Important dated launch evidence — Cayenne Electric

Porsche Newsroom's India launch announcement dated **2026-09-30** confirms:
- Cayenne Electric launched in India in two variants.
- Cayenne Electric price: ₹1,77,27,000.
- Cayenne Turbo Electric price: ₹2,27,51,000.
- Porsche stated deliveries would commence on the launch date.
- Petrol Cayenne variants will continue to be sold alongside the electric model.

This is strong OEM evidence for current India availability and launch price of both electric variants. Retain the announcement date as price-history metadata, but still preserve the live configurator observation separately.

## Family and variant modelling rules

- Keep petrol Macan and Macan Electric as distinct powertrain products under the Macan family; do not merge them.
- Keep Cayenne petrol, Cayenne Coupé and Cayenne Electric product/body-style entries distinct.
- Keep 911 Carrera, Carrera 4 GTS, Turbo S and GT3 as distinct derivatives; do not flatten all into generic 911 variants without preserving derivative identity.
- Taycan 4S Black Edition is a distinct edition/derivative, not a separate model family.
- Preserve 2025/2026/2027 model-year values exactly as displayed; do not infer a universal model year from the audit date.
- Keep powertrain, drive configuration, transmission and price as separate attributes.
- Do not infer battery size, WLTP range, motor output or optional-equipment pricing from the starting-price cards.

## Exclusions and lifecycle cautions

- The old Porsche India dealer microsite includes Boxster and Cayman in generic portfolio copy. The current India configurator/comparison snapshot lists five families and does not show Boxster or Cayman as selectable families. Do not add them to the current India sellable catalogue based only on the old microsite text.
- Do not treat global Porsche models or international MSRP as India retail products/prices.
- Special editions and limited allocations should be added only when the India configurator or a dated Porsche India launch announcement confirms the specific product and India availability.
- The India configurator's 20-entry count is the current captured discovery count; do not hardcode it as a permanent catalogue invariant.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Porsche India model comparison | https://compare.porsche.com/en-IN | India product entries, displayed prices and technical summary | High for displayed values; dynamic page and price basis needs disclaimer review |
| Porsche India model overview/configurator | https://www.porsche.com/middle-east/_india_/models/ | India configurator model families, derivative, model year, powertrain, drive and displayed price | High for displayed values |
| Porsche Newsroom — Cayenne Electric India launch (2026-09-30) | https://pnr-prd2-pub1.newsroom.porsche.com/en_PME/2026/products/porsche-india-cayenne-electric-43378.html | Dated India launch, two variants, prices and delivery timing | High; OEM announcement |
| Porsche India dealer microsite | https://dealer.porsche.com/in/india/ | Dealer network and historical/general brand context | High for dealer network; legacy model list not current catalogue evidence |
| Autocar India Porsche listing | https://www.autocarindia.com/cars/porsche | Secondary lineup and price cross-check | Medium; not primary price authority |

## Staging decision

**Porsche is ready for structured OEM configurator observations, but not automatic production import yet.**

Safe review-queue evidence:
1. Five official model families and 20 selectable model/derivative entries.
2. The 20 displayed price observations transcribed above.
3. Model year, powertrain, drive and transmission for the displayed subset.
4. Dated OEM Cayenne Electric India launch and two variant prices.

Required before Firestore import:
1. Review the exact India price disclaimer and clarify "incl. VAT" semantics before mapping to the app's price-type enum.
2. Re-capture all 20 live configurator entries with observation timestamp and exact product identifiers.
3. Capture official India brochures for battery, engine, range, output and variant equipment.
4. Confirm which entries are orderable and any limited-edition/stock constraints.
5. Collect city-wise on-road prices from sources with approved reuse rights.
6. Complete source licensing/reuse review.

No Firestore import, provider API credit usage, or publication was performed.
