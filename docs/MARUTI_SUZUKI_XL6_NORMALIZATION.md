# Maruti Suzuki XL6 normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-xl6-variant-structure.csv`: seven current grade/powertrain/gearbox configurations.
- `data/maruti-suzuki-xl6-price-observations.csv`: seven official NEXA ex-showroom price observations.

## Current variant matrix

NEXA's current XL6 price page lists seven configurations:
- Zeta Smart Hybrid 5MT
- Zeta CNG 5MT
- Zeta Smart Hybrid 6AT
- Alpha Smart Hybrid 5MT
- Alpha Smart Hybrid 6AT
- Alpha+ Smart Hybrid 5MT
- Alpha+ Smart Hybrid 6AT

All use the 1462 cc K15C engine family. Petrol Smart Hybrid output is 75.8 kW / 103.06 PS and 139 Nm, with 5-speed manual or 6-speed torque-converter automatic. The factory S-CNG variant produces 64.6 kW / 87.8 PS and 121.5 Nm in CNG mode, with 5-speed manual only. All are front-wheel-drive, 6-seat MPVs with second-row captain seats.

## Price basis

Current official NEXA ex-showroom observations:
- Zeta Smart Hybrid 5MT ₹11,62,300
- Zeta CNG 5MT ₹12,60,800
- Zeta Smart Hybrid 6AT ₹12,97,300
- Alpha Smart Hybrid 5MT ₹12,58,800
- Alpha Smart Hybrid 6AT ₹13,93,800
- Alpha+ Smart Hybrid 5MT ₹13,17,100
- Alpha+ Smart Hybrid 6AT ₹14,52,100

NEXA states that prices are indicative and subject to invoice date; final on-road pricing varies by city. These are ex-showroom values, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official XL6 price/variant page: https://www.nexaexperience.com/xl6/price
- NEXA official XL6 model page: https://www.nexaexperience.com/xl6
- NEXA official XL6 brochure and specifications: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/xl6/Documents/NEXA-Xl6-Brochure.pdf
- Autocar India current seven-variant listing, last updated 26 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/xl6/variants
