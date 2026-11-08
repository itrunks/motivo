# Tata Punch ICE 26-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-punch-ice-variant-price-observations.csv`: 26 unique current variant rows with exact displayed grade/powertrain labels, fuel, transmission, displacement, power, torque, drivetrain, seating, Delhi on-road price and source metadata.

## Current variant coverage

Autocar India's current variant page was last updated 30 October 2026 and lists 26 variants across Smart, Pure, Pure+, Pure+ S, Adventure, Adventure S, Accomplished and Accomplished+ S. All 26 rows are captured individually; the turbo-petrol is present only in Adventure and Accomplished+ S. CNG AMT appears on selected grades only. No absent combination has been fabricated.

## Powertrain families

- 1.2-litre naturally aspirated Revotron petrol: 1199 cc, 87.8 PS, 115 Nm; 5-speed manual or 5-speed AMT.
- 1.2-litre Revotron iCNG bi-fuel: 1199 cc, 73.4 PS and 103 Nm in CNG mode; 5-speed manual or 5-speed AMT.
- 1.2-litre turbocharged Revotron petrol: 1199 cc, 120 PS and 170 Nm; 6-speed manual only.

All variants are recorded as front-wheel-drive, 5-seat SUVs. The engine and transmission matrix is cross-checked against Tata's 2026 brochure and current variant/powertrain reporting.

## Price basis

All 26 values are **on-road Delhi INR** observations from Autocar India's variant page. The displayed range is ₹6.24 lakh to ₹12.52 lakh. These are not ex-showroom prices and must not be reused as national or Tamil Nadu prices. On-road values vary with registration, insurance, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source for the exact 26-row variant/price matrix. Tata's official product page was inaccessible in the earlier source audit, but the 2026 official brochure and independent variant matrix support the engine, transmission and variant families. Confirm current orderability and final invoice with a Tata dealer before production/customer use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible pages do not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Punch 26-variant listing, last updated 30 October 2026: https://www.autocarindia.com/cars/tata/punch/variants/
- Tata official 2026 Punch brochure: https://tatamotors-prod.adobecqms.net/content/dam/tml/pv/products/punch/year-2026/ice/promoting-vc/brochures/new-punch-brochure-jan%20.pdf
- 2026 Punch variant-wise powertrain mapping: https://www.v3cars.com/news/2026-tata-punch-facelift-variant-wise-engine-transmission-options
- Tata Punch 2026 launch/price matrix: https://www.autocarindia.com/auto-features/which-variant-of-the-2026-tata-punch-should-you-buy-440088
