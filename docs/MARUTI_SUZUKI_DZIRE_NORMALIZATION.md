# Maruti Suzuki Dzire normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-dzire-variant-normalization.csv`: 11 current petrol and S-CNG variants with official ex-showroom prices.

## Current variant matrix

Maruti Suzuki's official Dzire price page lists 11 combinations across LXi, VXi, ZXi and ZXi+:
- Petrol manual: LXi, VXi, ZXi and ZXi+.
- Petrol AGS: VXi, ZXi and ZXi+.
- S-CNG manual: VXi and ZXi.
- S-CNG AGS: VXi and ZXi.

All use the 1197 cc Z12E engine family. Petrol output is 60 kW / 81.58 PS and 111.7 Nm. CNG mode output is 51.3 kW / 69.75 PS and 101.8 Nm. Petrol and CNG are front-wheel-drive 5-seat compact sedans. Both petrol and CNG have 5-speed manual or AGS variants in the current 2026 range.

## CNG automatic update

Maruti announced the Dzire CNG-AGS variants in September 2026. VXi and ZXi CNG now have AGS versions. These are recorded as distinct powertrain/gearbox combinations rather than being inferred from petrol AMT availability.

## Price basis

Official Maruti Suzuki price page values, ex-showroom:
- LXi MT ₹6,30,600
- VXi MT ₹7,27,100
- VXi AMT ₹7,72,100
- VXi CNG MT ₹8,18,100
- ZXi MT ₹8,27,700
- VXi CNG AGS ₹8,53,100
- ZXi AMT ₹8,72,700
- ZXi+ MT ₹8,96,300
- ZXi CNG MT ₹9,18,700
- ZXi+ AMT ₹9,41,300
- ZXi CNG AGS ₹9,53,700

The official site states invoice-date prices and schemes prevail. These are ex-showroom observations, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Dzire model page: https://www.marutisuzuki.com/arena/dzire
- Maruti Suzuki official Dzire price page: https://www.marutisuzuki.com/arena/dzire/price
- Maruti Suzuki official Dzire brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/dzire/documents/Arena-Dzire-Brochure.pdf
- Maruti Suzuki Dzire CNG-AGS official price matrix, 21 September 2026: https://www.v3cars.com/news/maruti-dzire-cng-amt-automatic-full-price-list-sep-2026
