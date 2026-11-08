# Maruti Suzuki Celerio normalization

Checked: 2026-11-08

## Deliverable

- `data/maruti-suzuki-celerio-variant-normalization.csv`: 8 current petrol/S-CNG variant structures.
- `data/maruti-suzuki-celerio-price-observations.csv`: 24 city-scoped and legacy price observations (8 Delhi, 8 Perambra, 8 legacy unscoped).

## Current variant matrix

Maruti Suzuki's official Celerio price page lists eight variants:
- Petrol manual: LXi MT, VXi MT, ZXi MT and ZXi+ MT.
- Petrol AGS: VXi AGS, ZXi AGS and ZXi+ AGS.
- S-CNG manual: VXi CNG.

All use the 998 cc K10C three-cylinder engine family. Petrol output is 50.4 kW / 68.5 PS and 91.1 Nm. CNG mode output is 41.7 kW / 56.6 PS and 82.1 Nm. Petrol uses 5-speed manual or AGS; CNG is 5-speed manual only. All configurations are front-wheel-drive, 5-seat hatchbacks.

## Price basis

The official price page displays eight variants with Book Now actions and a stated waiting period of 2+ months. However, the displayed prices differ by city:

| Variant | Delhi page | Perambra city page |
|---|---:|---:|
| LXi MT | ₹4,69,900 | ₹4,69,900 |
| VXi MT | ₹5,15,900 | ₹5,18,400 |
| VXi AGS | ₹5,60,900 | ₹5,63,400 |
| ZXi MT | ₹5,70,900 | ₹5,73,400 |
| VXi CNG | ₹5,97,900 | ₹5,97,900 |
| ZXi AGS | ₹6,15,900 | ₹6,18,400 |
| ZXi+ MT | ₹6,27,900 | ₹6,30,400 |
| ZXi+ AGS | ₹6,72,900 | ₹6,75,400 |

These are official displayed ex-showroom starting amounts, not on-road prices. The page states that invoice-date prices and schemes prevail and does not expose an effective date. The previous normalized amounts match the Perambra snapshot for affected petrol grades, but their city scope was not retained. They are preserved as legacy observations and removed from the city-agnostic normalized rows. Do not publish one national amount from these values.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Celerio model page: https://www.marutisuzuki.com/arena/celerio
- Maruti Suzuki official Delhi-default variant price page: https://www.marutisuzuki.com/arena/celerio/price
- Maruti Suzuki official Perambra city price page: https://www.marutisuzuki.com/arena/celerio/price?city=perembra
- Maruti Suzuki Celerio official brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/celerio/documents/Arena-Celerio-Brochure.pdf
- Autocar India Celerio specifications, last updated 15 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/celerio/specifications
