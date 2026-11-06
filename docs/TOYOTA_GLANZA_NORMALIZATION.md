# Toyota Glanza 2026 powertrain normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-glanza-powertrain-families.csv`: 4 model-level powertrain families; exact retail trim mapping is not published in the captured 2026 official sources.
- `data/toyota-glanza-price-observations.csv`: one model-level starting-price observation.

## Current 2026 powertrain evidence

Toyota's October 14, 2026 launch announcement confirms the new-generation 1.2-litre, 3-cylinder Z12E petrol engine, 61 kW and 112.4 Nm. It also confirms a Petrol+CNG powertrain with 51.3 kW and 101.8 Nm, and explicitly announces AMT in CNG variants. The release gives 23.80 km/l for MT and 24.77 km/l for AMT petrol variants. It identifies Glanza as a hatchback. The current launch release does not disclose the full grade-by-transmission matrix, so E/S/G/V trim mappings from the 2025 brochure are not carried forward to the 2026 model.

The older 2025 brochure and showroom page describe a 1.2-litre 4-cylinder K-series engine, 1197 cc and earlier E/S/G/V mappings. These are historical and conflict with the 2026 launch's new 3-cylinder Z12E engine. They are not used to infer 2026 trim/powertrain applicability.

## Price

Toyota's October 14, 2026 launch announcement states a starting ex-showroom price of ₹6,99,000. No trim-wise or transmission-wise price table is published in the captured official release. The value is recorded as a model-level starting price only.

## Status / next evidence needed

This is a partial model-level normalization, not a completed retail-variant matrix. Obtain the current 2026 Toyota configurator or official brochure with exact grade names and petrol/CNG MT/AMT mapping before creating retail variant rows or marking this model complete.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- 2026 launch announcement: https://www.toyotabharat.com/news/2026/tkm-introduces-the-new-toyota-glanza.html
- Current homepage/model listing: https://www.toyotabharat.com/
- Historical 2025 brochure, retained only for comparison: https://www.toyotabharat.com/documents/brochures/e-brochure-glanza.pdf
