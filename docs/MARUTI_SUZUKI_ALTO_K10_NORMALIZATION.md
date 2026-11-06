# Maruti Suzuki Alto K10 normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-alto-k10-variant-normalization.csv`: 8 current petrol/CNG variant and official ex-showroom price rows.

## Current variant matrix

Maruti Suzuki's official Alto K10 page and brochure list eight combinations:
- Petrol: STD (O) MT, LXi (O) MT, VXi (O) MT, VXi (O) AGS, VXi+ (O) MT and VXi+ (O) AGS.
- S-CNG: LXi (O) CNG and VXi (O) CNG, both manual.

The 998 cc K10C Dual Jet Dual VVT petrol engine produces 50.4 kW (68.5 PS) and 91.1 Nm. The S-CNG mode produces 41.7 kW (56.7 PS) and 82.1 Nm. Petrol variants offer 5-speed manual or AGS; CNG variants are 5-speed manual only. Petrol is a 5-seat configuration; CNG is 4-seat. All are front-wheel-drive hatchbacks.

## Price basis

Official Maruti Suzuki price FAQ values, ex-showroom:
- STD (O) MT ₹3,69,900
- LXi (O) MT ₹3,99,900
- VXi (O) MT ₹4,49,900
- LXi (O) CNG ₹4,81,900
- VXi (O) AGS ₹4,94,900
- VXi+ (O) MT ₹4,99,900
- VXi (O) CNG ₹5,31,900
- VXi+ (O) AGS ₹5,44,900

Maruti states invoice-date prices and schemes prevail. These are ex-showroom observations, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Alto K10 model page: https://www.marutisuzuki.com/arena/alto-k10
- Maruti Suzuki official variant price page and FAQ: https://www.marutisuzuki.com/arena/alto-k10/price
- Maruti Suzuki Alto K10 official brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/alto-k10/documents/AltoK10-KV-Brochure.pdf
- Autocar India current variant listing, last updated 14 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/alto-k10/variants
