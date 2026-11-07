# Toyota Glanza 2026 powertrain and price normalization

Checked: 2026-11-07

## Deliverables

- `data/toyota-glanza-powertrain-families.csv`: 13 grade/fuel/transmission observations. Eleven are explicitly mapped by the technical Variant Type table; two V(O) petrol MT/AMT rows are retained as feature-matrix candidates because the technical summary omits V(O).
- `data/toyota-glanza-price-observations.csv`: one current model-level starting-price observation, not assigned to a trim.

## Current official 2026 powertrain matrix

The current Toyota Glanza showroom page was rechecked on 2026-11-07. It now contains the 2026 Z12E three-cylinder specifications and explicit grade/powertrain applicability:

| Grade | Petrol MT | Petrol AMT | CNG MT | CNG AMT |
|---|---:|---:|---:|---:|
| E | Yes | No | No | No |
| S | Yes | Yes | Yes | Yes |
| G | Yes | Yes | Yes | Yes |
| V | Yes | Yes | No | No |
| V(O) | Feature matrix only | Feature matrix only | No | No |

The technical Variant Type summary explicitly lists E (MT), S (MT & AMT), G (MT & AMT), V (MT & AMT) and CNG S/G (MT & AMT). The feature comparison table separately displays V(O) (MT/AMT), but the technical summary omits V(O). V(O) is therefore preserved as an OEM feature-matrix candidate, not treated as a fully reconciled variant until Toyota confirms the omission.

This produces 11 explicitly mapped combinations plus 2 V(O) candidate combinations. All are 5-seat hatchback configurations.

## Current technical specifications

- Engine: 1.2 L Z12E, 3-cylinder, 1197 cc (BS6 Phase 2)
- Petrol output: 61 kW at 5700 rpm; 112.4 Nm at 4500 rpm
- CNG mode: 51.3 kW at 5700 rpm; 101.8 Nm at 2900 rpm
- Petrol fuel efficiency: 23.80 km/l MT; 24.77 km/l AMT
- CNG fuel efficiency: 33.61 km/kg MT; 34.47 km/kg AMT
- Seating: 5

This current page supersedes the historical 2025 brochure's four-cylinder K-series engine and earlier CNG-only manual applicability. The 2025 brochure is retained only as historical evidence.

## Price

Toyota's 2026 launch announcement gives a model-level starting ex-showroom price of ₹6,99,000. It does not map that amount to a specific grade or transmission. The current Toyota price-list portal requires the customer to select a dealer and states that prices can change without prior notice; no public nationwide grade-wise price matrix was available in the captured page. Do not assign the ₹6.99L starting price to E or any other individual trim.

The model-level price observation is therefore retained without creating variant-level prices. Exact dealer/grade price requires a selected Toyota dealer.

## Status

Powertrain mapping is substantially improved: 11 exact combinations are supported by the technical Variant Type table, while V(O) MT/AMT remains a source-internal discrepancy. Variant-level prices are not publicly exposed in the captured official price list. Keep the model partial until V(O) and grade-wise pricing are confirmed.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Current Toyota Glanza showroom and feature matrix: https://www.toyotabharat.com/showroom/glanza/index.html
- Toyota dealer-specific price list: https://www.toyotabharat.com/pricelist/
- 2026 launch announcement: https://www.toyotabharat.com/news/2026/tkm-introduces-the-new-toyota-glanza.html
- Historical 2025 brochure: https://www.toyotabharat.com/documents/brochures/e-brochure-glanza.pdf
