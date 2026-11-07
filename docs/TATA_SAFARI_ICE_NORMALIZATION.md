# Tata Safari ICE 64-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-safari-ice-variant-price-observations.csv`: 64 unique current variant rows with exact displayed variant labels, engine, fuel, gearbox, displacement, output, torque, drivetrain, seat count, Delhi on-road price and source metadata.

## Current variant coverage

Autocar India's variant page was last updated 23 October 2026 and lists 64 variants. The catalogue includes Smart, Pure X, Pure X Dark, Adventure X+, Adventure X+ Dark, Accomplished X, Accomplished X Dark, Accomplished X+, Accomplished X+ Dark, Accomplished Ultra, Accomplished Ultra Stealth and Accomplished Ultra Red Dark.

The 64 combinations include 46 seven-seat and 18 six-seat entries. Six-seat configurations are retained only where the listing explicitly names them; no seat count has been inferred from trim grade alone.

## Powertrain families

- 1.5-litre TGDi turbo-petrol: 1498 cc, 170 PS, 280 Nm; 6-speed manual or 6-speed torque-converter automatic.
- 2.0-litre Kryotec turbo-diesel: 1956 cc, 170 PS, 350 Nm; 6-speed manual or 6-speed torque-converter automatic.

Both engine families are listed with front-wheel drive. The variant page explicitly distinguishes fuel, gearbox and seating count for each row.

## Price basis

All 64 values are **on-road Delhi INR** observations from Autocar India's current variant page. The displayed range is ₹15.55 lakh to ₹32.03 lakh. These are not ex-showroom prices and must not be used as national or Tamil Nadu prices. On-road values may vary by insurance, registration, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source. Tata's official Safari price page exposes current grade/feature families and a Configure action, but the extracted price cells are blank. The 64-row exact trim/engine/seat/price matrix therefore remains secondary-source evidence and should be reconciled with the live Tata configurator or dealer quotation before production/customer use. The engine outputs are supported by the 2026 engine specification matrix; current official model pages should be preferred for future refreshes.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Public access does not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Safari 64-variant listing, last updated 23 October 2026: https://www.autocarindia.com/cars/tata/safari/variants/
- Official Tata Safari price/configurator page: https://tatamotors-prod.adobecqms.net/safari/ice/price.html
- 2026 Safari powertrain and variant mapping: https://www.v3cars.com/news/2026-tata-safari-variant-wise-engine-transmission-options
- 2026 Safari engine output cross-check: https://www.v3cars.com/news/2026-tata-safari-petrol-vs-diesel-price-features-comparison
