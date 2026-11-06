# Maruti Suzuki Ertiga normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-ertiga-variant-normalization.csv`: nine current Smart Hybrid petrol and S-CNG configurations with official ex-showroom prices.

## Current variant matrix

Maruti Suzuki's official price page lists nine variants:
- Petrol manual: LXi, VXi, ZXi and ZXi+.
- Petrol automatic: VXi AT, ZXi AT and ZXi+ AT.
- S-CNG manual: VXi CNG and ZXi CNG.

All use the 1462 cc K15C engine family. Smart Hybrid petrol output is 75.8 kW / 103.06 PS and 139 Nm. CNG mode output is 64.6 kW / 87.8 PS and 121.5 Nm; petrol mode on the CNG vehicle is 74.0 kW / 100.6 PS and 137.1 Nm. Petrol variants use 5-speed manual or 6-speed automatic; CNG variants use 5-speed manual only. All are front-wheel-drive, 7-seat MPVs.

## Price basis

Official Maruti Suzuki price page values, ex-showroom:
- LXi MT ₹8,90,000
- VXi MT ₹9,95,300
- VXi CNG ₹10,93,800
- ZXi MT ₹11,01,500
- VXi AT ₹11,30,300
- ZXi+ MT ₹11,79,100
- ZXi CNG ₹12,00,000
- ZXi AT ₹12,36,500
- ZXi+ AT ₹13,14,100

The official page states invoice-date prices and schemes prevail. These are ex-showroom prices, not on-road quotes.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Ertiga model page: https://www.marutisuzuki.com/arena/ertiga
- Maruti Suzuki official Ertiga variant price page: https://www.marutisuzuki.com/arena/ertiga/price
- Maruti Suzuki official Ertiga brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/ertiga/document/Arena-Ertiga-Brochure.pdf
- October 2026 price revision cross-check: https://www.cars24.com/news/auto/maruti-suzuki-ertiga-price-hike-in-october-2026-up-to-rs-10000-costlier/
