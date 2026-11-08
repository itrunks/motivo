# Maruti Suzuki Swift normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-swift-variant-normalization.csv`: 17 current petrol and S-CNG grade/gearbox combinations with official ex-showroom prices.

## Current variant matrix

The official Maruti Suzuki price page lists 17 combinations across LXi, VXi, VXi (O), ZXi and ZXi+:
- Petrol manual and AMT configurations.
- S-CNG manual and newly introduced S-CNG AGS configurations.
- ZXi+ dual-tone manual and AMT editions are separate price rows.

The 2026 Swift uses a 1197 cc Z12E three-cylinder petrol engine. Petrol output is 60 kW / 81.58 PS and 111.7 Nm. The CNG version is listed at 51.3 kW / 69.78 PS and 101.8 Nm in CNG mode. Petrol and CNG variants are front-wheel-drive 5-seat hatchbacks. Manual and AGS are 5-speed.

## CNG automatic update

Maruti announced the Swift CNG-AGS range in September 2026. The VXi, VXi (O) and ZXi CNG grades now have AGS variants. These are included as separate combinations and are not confused with petrol AMT rows.

## Price basis

Official Maruti Suzuki price page values, ex-showroom:
- LXi MT ₹5,83,900
- VXi MT ₹6,67,900
- VXi (O) MT ₹6,93,900
- VXi AMT ₹7,12,900
- VXi (O) AMT ₹7,38,900
- VXi CNG MT ₹7,57,400
- ZXi MT ₹7,61,900
- VXi (O) CNG MT ₹7,83,400
- VXi CNG AGS ₹7,92,400
- ZXi AMT ₹8,06,900
- VXi (O) CNG AGS ₹8,18,400
- ZXi+ MT ₹8,28,900
- ZXi+ Dual Tone MT ₹8,43,900
- ZXi CNG MT ₹8,51,400
- ZXi+ AMT ₹8,73,900
- ZXi CNG AGS ₹8,86,400
- ZXi+ Dual Tone AMT ₹8,88,900

The official site states invoice-date prices and schemes prevail. These are ex-showroom observations, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Swift model page: https://www.marutisuzuki.com/arena/swift
- Maruti Suzuki official Swift price page: https://www.marutisuzuki.com/arena/swift/price
- Maruti Suzuki official Swift brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/swift/documents/Swift-Brochure.pdf
- Maruti Suzuki Swift CNG-AGS launch and official price matrix, 21 September 2026: https://www.v3cars.com/news/maruti-swift-cng-amt-automatic-full-price-list-sep-2026
