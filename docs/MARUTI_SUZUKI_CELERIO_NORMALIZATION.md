# Maruti Suzuki Celerio normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-celerio-variant-normalization.csv`: 8 current petrol/S-CNG variants with official ex-showroom prices.

## Current variant matrix

Maruti Suzuki's official Celerio price page lists eight variants:
- Petrol manual: LXi MT, VXi MT, ZXi MT and ZXi+ MT.
- Petrol AGS: VXi AGS, ZXi AGS and ZXi+ AGS.
- S-CNG manual: VXi CNG.

All use the 998 cc K10C three-cylinder engine family. Petrol output is 50.4 kW / 68.5 PS and 91.1 Nm. CNG mode output is 41.7 kW / 56.6 PS and 82.1 Nm. Petrol uses 5-speed manual or AGS; CNG is 5-speed manual only. All configurations are front-wheel-drive, 5-seat hatchbacks.

## Price basis

Official Maruti Suzuki price page values, ex-showroom:
- LXi MT ₹4,69,900
- VXi MT ₹5,18,400
- VXi AGS ₹5,63,400
- ZXi MT ₹5,73,400
- VXi CNG ₹5,97,900
- ZXi AGS ₹6,18,400
- ZXi+ MT ₹6,30,400
- ZXi+ AGS ₹6,75,400

Maruti states invoice-date prices and schemes prevail. These are ex-showroom observations, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Celerio model page: https://www.marutisuzuki.com/arena/celerio
- Maruti Suzuki official variant price page: https://www.marutisuzuki.com/arena/celerio/price
- Maruti Suzuki Celerio official brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/celerio/documents/Arena-Celerio-Brochure.pdf
- Autocar India Celerio specifications, last updated 15 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/celerio/specifications
