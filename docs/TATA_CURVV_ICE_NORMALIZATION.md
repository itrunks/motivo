# Tata Curvv ICE Series X 26-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-curvv-ice-variant-price-observations.csv`: 26 unique Series X variant rows with exact displayed grade/edition labels, engine, fuel, transmission, displacement, output, torque, drivetrain, seating, Delhi on-road price and source metadata.

## Current variant coverage

Autocar India's current variant page was last updated 27 October 2026 and lists 26 variants. The six main grade families are Smart X, Pure X, Pure X+, Creative X+, Accomplished X and Accomplished X+, with Dark editions for selected grades. The 26 exact powertrain/edition combinations are preserved individually.

The 1.2-litre Revotron turbo-petrol, 1.5-litre diesel and 1.2-litre Hyperion TGDi are kept as three separate engine families. The Hyperion TGDi is only listed on Accomplished X+ DCT variants. Diesel DCT is also restricted to Accomplished X+ grades in the captured current matrix. Earlier pre-Series-X Curvv trim names and variants are not merged into the current Series X list.

## Powertrain families

- 1.2-litre Revotron turbo-petrol: 1199 cc, 120 PS, 170 Nm; 6-speed manual or 7-speed DCT.
- 1.2-litre TGDi Hyperion direct-injection turbo-petrol: 1199 cc, 125 PS, 225 Nm; 7-speed DCT.
- 1.5-litre turbocharged Revotorq diesel: 1497 cc, 118 PS, 260 Nm; 6-speed manual or 7-speed DCT.

All variants are recorded as front-wheel-drive, 5-seat coupe SUVs.

## Price basis

All 26 amounts are **on-road Delhi INR** observations from Autocar India's variant page. The displayed range is ₹11.16 lakh to ₹22.52 lakh. These are not ex-showroom prices and must not be reused as national or Tamil Nadu prices. On-road values vary with registration, insurance, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source for the exact 26-row current variant and on-road price matrix. The September 2026 Series X price/variant release and current engine specification reporting support the updated grade and powertrain structure. Confirm current configurator orderability and final dealer invoice before production/customer use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible content does not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Curvv 26-variant listing, last updated 27 October 2026: https://www.autocarindia.com/cars/tata/curvv/variants
- September 2026 Tata Curvv Series X price and variant matrix: https://www.v3cars.com/news/tata-curvv-series-x-launched-price-variants-features
- Current Curvv engine outputs and powertrain overview: https://www.autocarindia.com/cars/tata/curvv
- September 2026 Series X buyer guide and powertrain mapping: https://www.autocarindia.com/auto-features/which-tata-curvv-trim-should-you-consider-buying-432480
