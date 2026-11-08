# Maruti Suzuki Wagon R normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-wagon-r-variant-structure.csv`: 12 current petrol, S-CNG and flex-fuel configurations.
- `data/maruti-suzuki-wagon-r-price-observations.csv`: 12 official Maruti Suzuki ex-showroom price observations.

## Current variant coverage

The current official Maruti Suzuki price page exposes 12 configurations:
- 1.0-litre petrol: LXi MT, VXi MT and VXi AGS.
- 1.0-litre S-CNG: LXi CNG MT and VXi CNG MT.
- 1.2-litre petrol: ZXi MT, ZXi AGS, ZXi+ MT, ZXi+ AGS, ZXi+ Dual Tone MT and ZXi+ Dual Tone AGS.
- 1.2-litre flex-fuel: ZXi+ MT FFV.

The flex-fuel selector is treated as a separate official variant, but the exact approved ethanol blend range is not populated because the captured official price/configurator page does not specify it.

## Powertrain families

- 1.0-litre K10C petrol: 998 cc, 50.4 kW / 68.5 PS, 91.1 Nm; 5-speed manual or 5-speed AGS.
- 1.0-litre K10C S-CNG: 998 cc, 41.7 kW / 56.6 PS and 82.1 Nm in CNG mode; 5-speed manual.
- 1.2-litre K12N petrol: 1197 cc, 66.9 kW / 90.9 PS, 113.7 Nm; 5-speed manual or 5-speed AGS.
- 1.2-litre K12N flex-fuel: official price page lists the ZXi+ MT FFV separately; the current selector does not expose a distinct engine-output table, so the standard K12N output is recorded as a family-level reference and fuel blend detail remains unpopulated.

All variants are front-wheel-drive, 5-seat tall-boy hatchbacks.

## Price basis

Official Maruti Suzuki price page observations, ex-showroom:
- LXi MT ₹4,98,900
- VXi MT ₹5,54,400
- LXi CNG MT ₹5,93,900
- ZXi MT ₹5,98,400
- VXi AGS ₹5,99,400
- ZXi+ MT ₹6,41,400
- ZXi AGS ₹6,43,400
- VXi CNG MT ₹6,49,400
- ZXi+ Dual Tone MT ₹6,52,400
- ZXi+ AGS ₹6,86,400
- ZXi+ Dual Tone AGS ₹6,97,400
- ZXi+ MT FFV ₹7,23,900

Maruti states invoice-date prices and schemes prevail. These are ex-showroom observations, not on-road prices.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Wagon R model page: https://www.marutisuzuki.com/arena/wagon-r
- Maruti Suzuki official Wagon R price page: https://www.marutisuzuki.com/arena/wagon-r/price
- Maruti Suzuki official Wagon R brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/wagonr/documents/Arena-Wagon-r-Brochure.pdf
- Autocar India current 10-variant summary, last updated 30 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/wagon-r/variants/
- V3Cars November 2026 variant-wise price table: https://www.v3cars.com/maruti-arena-cars/wagon-r
