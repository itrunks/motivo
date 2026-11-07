# Maruti Suzuki S-Presso normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-s-presso-variant-normalization.csv`: 8 current petrol/S-CNG variants with official ex-showroom prices.

## Current variant matrix

Maruti Suzuki's official price page lists eight variants:
- Petrol manual: Std (O) MT, LXi (O) MT, VXi (O) MT and VXi+ (O) MT.
- Petrol AGS: VXi (O) AGS and VXi+ (O) AGS.
- S-CNG manual: LXi (O) CNG and VXi (O) CNG.

All use the 998 cc K10C engine family. Petrol output is 50.4 kW / 68.524 PS and 91.1 Nm. CNG mode output is 41.7 kW / 56.696 PS and 82.1 Nm. Petrol offers 5-speed manual or AGS; CNG is 5-speed manual only. Petrol variants are 5-seat; CNG variants are 4-seat. All are front-wheel-drive micro-SUVs.

## Price basis

Official Maruti Suzuki price page values, ex-showroom:
- Std (O) MT ₹3,49,900
- LXi (O) MT ₹3,82,400
- VXi (O) MT ₹4,32,400
- LXi (O) CNG ₹4,64,400
- VXi (O) AGS ₹4,77,400
- VXi+ (O) MT ₹4,82,400
- VXi (O) CNG ₹5,14,400
- VXi+ (O) AGS ₹5,27,400

The VXi+ (O) AGS price is confirmed from the official configurator at ₹5,27,400; it was not visible in the initial extracted price-card block. Maruti states invoice-date prices and schemes prevail.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official S-Presso model page: https://www.marutisuzuki.com/arena/s-presso
- Maruti Suzuki official S-Presso price page: https://www.marutisuzuki.com/arena/s-presso/price
- Maruti Suzuki official S-Presso brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/s-presso/documents/Arena-S-Presso-Brochure.pdf
- Maruti Suzuki official configurator for VXi+ (O) AGS: https://www.marutisuzuki.com/arena/configurator/s-presso
