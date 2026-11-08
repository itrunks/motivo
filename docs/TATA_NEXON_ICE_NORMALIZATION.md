# Tata Nexon ICE 63-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-nexon-ice-variant-price-observations.csv`: 63 unique current variant rows with fuel, exact displayed grade/edition label, transmission, engine family, displacement, power, torque, drivetrain, seating, Delhi on-road price and source metadata.

## Current variant coverage

Autocar India's current variant page was last updated 30 October 2026 and lists 63 variants across Smart, Smart+, Smart+ S, Pure+, Pure+ S, Pure+ PS, Creative, Creative+ S, Creative+ S Dark, Creative+ PS, Creative+ PS Dark, Fearless+ PS, Fearless+ PS Dark, Fearless+ PS Red Dark, Fearless+ A PS and Fearless+ A PS Red Dark.

The 63 rows preserve the exact fuel/gearbox combinations displayed on the listing. Petrol, diesel and CNG are separate fuel categories. Dark, Red Dark and Camo are not collapsed into the base trim. The two Fearless+ A PS variants are petrol DCT-only.

## Powertrain families

- 1.2-litre turbocharged Revotron petrol: 1199 cc, 120 PS, 170 Nm; 5-speed manual, 6-speed manual, 6-speed AMT or 7-speed DCT depending on variant.
- 1.2-litre turbocharged Revotron iCNG bi-fuel: 1199 cc; 98 PS, 170 Nm; 6-speed manual only.
- 1.5-litre turbocharged Revotorq diesel: 1497 cc, 115 PS, 260 Nm; 6-speed manual or 6-speed AMT.

All are recorded as front-wheel-drive, 5-seat compact SUVs. The official Tata specification page lists 5-speed MT, 6-speed MT, 6-speed AMT and 7-speed DCT for petrol, 6-speed MT for CNG, and 6-speed MT/AMT for diesel.

## Price basis

All 63 amounts are **on-road Delhi INR** observations from Autocar India's variant page. The displayed range is ₹8.26 lakh to ₹17.21 lakh. These are not ex-showroom prices and must not be used as national or Tamil Nadu prices. On-road values can change with registration, insurance, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source for the 63-row variant and price matrix. Tata's official product price page confirms the current grade families and configurator but the extracted price cells are not fully populated. Tata's official specification page supports the engine families and gearbox choices. Confirm the live configurator and dealer invoice before production/customer use. CNG power is captured from Tata's official FAQ; where variant-specific CNG torque is not independently distinguished, the engine-family value is recorded as published.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible content does not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Nexon 63-variant listing, last updated 30 October 2026: https://www.autocarindia.com/cars/tata/nexon/variants
- Tata official Nexon specifications and current variant names: https://tatamotors-prod.adobecqms.net/nexon/ice/specifications.html
- Tata official Nexon current price/configurator page: https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/nexon/ice/price.html
- Tata Nexon 2026 powertrain and gearbox options: https://www.cardekho.com/india-car-news/tata-nexon-2026-which-variant-gets-which-powertrain-options-explained-35638.htm
