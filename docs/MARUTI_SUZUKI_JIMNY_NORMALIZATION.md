# Maruti Suzuki Jimny normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-jimny-variant-structure.csv`: four current grade/transmission configurations.
- `data/maruti-suzuki-jimny-price-observations.csv`: four official NEXA Delhi ex-showroom price observations.

## Current variant matrix

NEXA's official Jimny page lists Zeta and Alpha with 5-speed manual or 4-speed automatic:
- Zeta Pro MT
- Alpha Pro MT
- Zeta Pro AT
- Alpha Pro AT

All four use the 1462 cc K15B naturally aspirated petrol engine, producing 77.1 kW / 104.8 PS and 134.2 Nm. ALLGRIP PRO 4WD, low-range transfer case and 4WD capability are standard across the range. Jimny is a 4-seat, 5-door off-road SUV.

Dual-tone paint is an appearance option, not a separate engine/transmission configuration, so it is not represented as an extra mechanical variant. The official FAQ identifies Alpha Pro AT Dual Tone as the top price point.

## Price basis

Current NEXA Delhi ex-showroom observations:
- Zeta Pro MT ₹12,59,000
- Alpha Pro MT ₹13,45,700
- Zeta Pro AT ₹13,65,000
- Alpha Pro AT ₹14,51,700

The NEXA FAQ also displays ₹14,52,100 for the Alpha Pro AT Dual Tone top model. This is treated as a paint/appearance price distinction, not a fifth powertrain row. Final dealer invoice and colour option charges should be confirmed before customer use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official Jimny model page and variant list: https://www.nexaexperience.com/jimny
- NEXA official Delhi price page: https://www.nexaexperience.com/jimny/price-in-delhi
- NEXA official price FAQ: https://www.nexaexperience.com/jimny/price
- NEXA official Jimny brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/jimny/documents/NEXA-Jimny-Brochure.pdf
- Autocar India current specification summary: https://www.autocarindia.com/cars/maruti-suzuki/jimny
