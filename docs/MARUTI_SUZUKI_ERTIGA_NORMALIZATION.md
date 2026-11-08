# Maruti Suzuki Ertiga normalization

Checked: 2026-11-08

## Deliverable

- `data/maruti-suzuki-ertiga-variant-normalization.csv`: nine current Smart Hybrid petrol and S-CNG configurations.
- `data/maruti-suzuki-ertiga-price-observations.csv`: 18 Delhi, Punalur and legacy price observations.

## Current variant matrix

Maruti Suzuki's official price page lists nine variants:
- Petrol manual: LXi, VXi, ZXi and ZXi+.
- Petrol automatic: VXi AT, ZXi AT and ZXi+ AT.
- S-CNG manual: VXi CNG and ZXi CNG.

All use the 1462 cc K15C engine family. Smart Hybrid petrol output is 75.8 kW / 103.06 PS and 139 Nm. CNG mode output is 64.6 kW / 87.8 PS and 121.5 Nm; petrol mode on the CNG vehicle is 74.0 kW / 100.6 PS and 137.1 Nm. Petrol variants use 5-speed manual or 6-speed automatic; CNG variants use 5-speed manual only. All are front-wheel-drive, 7-seat MPVs.

## Price basis

The official Delhi-default price page exposes nine named variants with Book Now actions and a 2+ months waiting indication. Delhi displayed ex-showroom starting amounts:

| Variant | Delhi page |
|---|---:|
| LXi MT | ₹8,90,000 |
| VXi MT | ₹9,95,300 |
| VXi CNG | ₹10,93,800 |
| ZXi MT | ₹11,01,500 |
| VXi AT | ₹11,30,300 |
| ZXi+ MT | ₹11,69,100 |
| ZXi CNG | ₹12,00,000 |
| ZXi AT | ₹12,36,500 |
| ZXi+ AT | ₹13,04,100 |

The Punalur city page separately shows seven grades; the ZXi+ MT and ZXi+ AT amounts are ₹11,79,100 and ₹13,14,100, respectively, each ₹10,000 above the Delhi page. Punalur prices for VXi CNG and ZXi MT were not captured in this pass. The prior normalized values for the two ZXi+ grades match Punalur, but their original city scope was not retained. They are preserved as legacy observations and all prices are removed from the city-agnostic normalized rows. The page states invoice-date prices and schemes prevail and does not publish an effective date. Do not assign a national price.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Ertiga model page: https://www.marutisuzuki.com/arena/ertiga
- Maruti Suzuki official Delhi-default Ertiga price page: https://www.marutisuzuki.com/arena/ertiga/price
- Maruti Suzuki official Punalur city price page: https://www.marutisuzuki.com/arena/ertiga/price?city=punalur
- Maruti Suzuki official Ertiga brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/ertiga/document/Arena-Ertiga-Brochure.pdf
- October 2026 price revision cross-check: https://www.cars24.com/news/auto/maruti-suzuki-ertiga-price-hike-in-october-2026-up-to-rs-10000-costlier/
