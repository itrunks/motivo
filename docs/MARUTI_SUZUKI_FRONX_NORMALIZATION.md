# Maruti Suzuki Fronx normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-fronx-variant-structure.csv`: 12 current petrol, S-CNG and turbo-petrol configurations.
- `data/maruti-suzuki-fronx-price-observations.csv`: 12 official NEXA ex-showroom price observations.

## Current variant coverage

The current NEXA price page lists 12 configurations:
- 1.2-litre petrol: Sigma MT; Delta MT/AGS; Delta+ MT/AGS.
- 1.2-litre S-CNG: Sigma MT and Delta MT.
- 1.0-litre Turbo Boosterjet: Delta+ DiTC MT; Zeta DiTC MT/AT; Alpha DiTC MT/AT.

The current official price page is used as the orderability/price source. An earlier queue note mentioned a possible Delta+ (O) MT selector label, but that label is not in the current 12-row NEXA price page and is not promoted into the orderable variant matrix.

## Powertrain families

**1.2-litre naturally aspirated K-Series petrol**
- 1197 cc, 66 kW / 89.73 PS, 113 Nm.
- 5-speed manual or 5-speed AGS.

**1.2-litre K-Series S-CNG**
- 1197 cc, 57 kW / 77.5 PS and 98.5 Nm in CNG mode.
- 5-speed manual only.

**1.0-litre Turbo Boosterjet**
- 998 cc, 73.6 kW / 100.06 PS, 147.6 Nm.
- 5-speed manual or 6-speed torque-converter automatic.
- Progressive Smart Hybrid / ISG assistance is noted separately; the turbo engine is not conflated with the naturally aspirated K-Series engine.

All variants are front-wheel-drive, 5-seat compact crossover SUVs.

## Price basis

Current official NEXA ex-showroom observations:
- Sigma Petrol MT ₹6,89,900
- Sigma CNG MT ₹7,93,900
- Delta Petrol MT ₹7,74,900
- Delta CNG MT ₹8,73,900
- Delta AGS Petrol ₹8,24,900
- Delta+ Petrol MT ₹8,14,500
- Delta+ AGS Petrol ₹8,64,500
- Delta+ DiTC Petrol ₹8,96,900
- Zeta DiTC Petrol ₹9,75,900
- Zeta Automatic DiTC Petrol ₹11,03,900
- Alpha DiTC Petrol ₹10,60,900
- Alpha Automatic DiTC Petrol ₹11,88,900

The NEXA page states that prices are ex-showroom and indicative; invoice-date dealer pricing prevails. The October 2026 secondary price revision independently confirms the selected ₹5,000 revisions to Sigma and turbo variants.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official Fronx variant/price page: https://www.nexaexperience.com/fronx/price
- NEXA official Fronx model page and variant-family mapping: https://www.nexaexperience.com/fronx
- NEXA official Fronx brochure and engine specifications: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/fronx/documents/NEXA-Fronx-Brochure.pdf
- Cars24, October 2026 Fronx price revisions: https://www.cars24.com/news/auto/maruti-suzuki-fronx-new-price-oct26-which-variants-are-more-expensive-now/
- Autocar India, current 12-variant price/trim page, last updated 30 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/fronx/variants
