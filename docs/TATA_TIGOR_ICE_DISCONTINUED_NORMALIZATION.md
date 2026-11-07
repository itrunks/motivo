# Tata Tigor ICE discontinued-model normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-tigor-ice-discontinued-variant-observations.csv`: 14 unique final retail variant observations with fuel, transmission, engine, displacement, output, torque, drivetrain, seating and last-recorded ex-showroom price.

## Model lifecycle status

Tata Tigor is **discontinued**, not a current orderable passenger-car model. Autocar India's model page records discontinuation in September 2026; the current Tata Cars navigation captured during the workqueue audit no longer lists Tigor. This record is retained for historical catalogue/search coverage only. Do not show it as currently available or imply a dealer can order a new unit.

## Last listed variant coverage

The discontinued model had 14 variants across five trims: XM, XT, XZ, XZ+ and XZ+ Lux.

- Petrol: XM MT; XT MT/AMT; XZ MT/AMT; XZ+ MT/AMT; XZ+ Lux MT.
- CNG: XT MT; XZ MT/AMT; XZ+ MT/AMT; XZ+ Lux MT.

## Powertrain

- 1.2-litre naturally aspirated Revotron petrol: 1199 cc, 86 PS, 113 Nm; 5-speed manual or 5-speed AMT.
- 1.2-litre Revotron iCNG bi-fuel: 1199 cc, 73 PS, 95 Nm in CNG mode; 5-speed manual or 5-speed AMT.

All configurations are front-wheel-drive, 5-seat compact sedans.

## Price basis

The CSV stores Autocar India's last-recorded ex-showroom prices: ₹5.60 lakh to ₹9.00 lakh. These are historical discontinued-model values, not current quotes. Other sources captured a slightly different final August/September 2026 price revision, so the exact final dealer invoice may differ. The price data must remain marked historical.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. This is historical staging data only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Tigor (2025–2026), discontinued September 2026: https://www.autocarindia.com/cars/tata/tigor-2025
- Autocar India, 14-variant last-recorded price matrix, last updated 28 October 2026: https://www.autocarindia.com/cars/tata/tigor-2025/variants
- Autocar India, Tigor engine specifications: https://www.autocarindia.com/cars/tata/tigor-2025/specifications
- V3Cars, final 2026 price list before discontinuation: https://www.v3cars.com/tata-cars/tigor
