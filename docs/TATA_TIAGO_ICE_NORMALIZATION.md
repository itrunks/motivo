# Tata Tiago ICE 20-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-tiago-ice-variant-price-observations.csv`: 20 unique current variant rows with trim, fuel, transmission, engine, displacement, power, torque, drivetrain, seating, Delhi on-road price and source metadata.

## Current variant coverage

Autocar India's variant page was last updated 14 October 2026 and lists 20 variants across Smart, Pure, Pure+, Pure+ A, Creative and Creative+. The current listing contains 12 petrol variants and 8 CNG variants. Petrol and CNG are both offered with 5-speed manual and 5-speed AMT on selected trims. Creative+ is petrol-only in the captured matrix.

## Powertrain families

- 1.2-litre naturally aspirated Revotron petrol: 1199 cc, 86 PS, 113 Nm; 5-speed manual or 5-speed AMT.
- 1.2-litre Revotron iCNG bi-fuel: 1199 cc, 75.5 PS and 96.5 Nm in CNG mode; 5-speed manual or 5-speed AMT.

All variants are recorded as front-wheel-drive, 5-seat hatchbacks. The twin-cylinder CNG system remains a bi-fuel petrol/CNG powertrain, not a separate engine displacement.

## Price basis

All 20 values are **on-road Delhi INR** observations from Autocar India's variant page. The displayed range is ₹5.18 lakh to ₹9.89 lakh. These are not ex-showroom prices and must not be reused as national or Tamil Nadu prices. Local on-road values vary with registration, insurance, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source for the current 20-row trim and on-road price matrix. Tata's 2026 launch/variant materials support the trim families, powertrain and gearbox choices. The official Tata price page exposes the current grades but does not provide all numeric price cells in the extracted content. Confirm live configurator availability and dealer invoice before production/customer use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible pages do not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Tiago 20-variant listing, last updated 14 October 2026: https://www.autocarindia.com/cars/tata/tiago/variants/
- Tata official 2026 Tiago price/configurator page: https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/tiago/ice/price.html
- 2026 Tiago launch and variant-wise prices: https://www.autocarindia.com/car-news/2026-tata-tiago-facelift-launched-at-rs-469-lakh
- 2026 Tiago engine and transmission specifications: https://www.v3cars.com/news/2026-tata-tiago-variant-wise-engine-transmission-options-petrol-cng
