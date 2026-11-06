# Maruti Suzuki Invicto normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-invicto-variant-structure.csv`: three current strong-hybrid seating/grade configurations.
- `data/maruti-suzuki-invicto-price-observations.csv`: three official NEXA ex-showroom price observations.

## Current variant coverage

NEXA's official Invicto page lists three variants:
- Zeta+ e-CVT 7-seater.
- Zeta+ e-CVT 8-seater.
- Alpha+ e-CVT 7-seater.

All use the same 2.0-litre M20A Atkinson-cycle strong-hybrid powertrain and e-CVT automatic. The 7-seat versions have second-row captain chairs; the 8-seat Zeta+ uses a second-row bench. Invicto is front-wheel-drive and is available only as a strong hybrid; no petrol-only or CNG configuration is included.

## Powertrain

- 1987 cc M20A Atkinson-cycle petrol engine: 112.8 kW / 152.9 PS and 188 Nm.
- Electric motor: 83.73 kW and 206 Nm.
- Total hybrid system output: 188.9 PS.
- 168-cell NiMH battery, 201.6 V.
- e-CVT, front-wheel drive.

The engine output, electric motor output and total system output are separate fields and are not added together.

## Price basis

Current official NEXA ex-showroom observations:
- Zeta+ e-CVT 7-seater ₹25,02,400 (October 29, 2026 revision).
- Zeta+ e-CVT 8-seater ₹25,37,300.
- Alpha+ e-CVT 7-seater ₹28,70,500.

The October 29, 2026 revision increased only the 7-seat Zeta+ by ₹5,000; the other two prices remained unchanged from the August revision. Autocar's Delhi on-road values are higher and are not mixed with the official ex-showroom amounts.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official Invicto model page and seating variants: https://www.nexaexperience.com/invicto
- NEXA official Invicto price page: https://www.nexaexperience.com/invicto/price
- NEXA official Invicto brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/invicto/documents/NEXA-Invicto-Brochure.pdf
- Autocar India, current three-variant listing, last updated 13 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/invicto/variants
- Cars24, October 29 2026 Invicto price revision: https://www.cars24.com/news/auto/maruti-suzuki-invicto-becomes-costlier-in-october-2026/
