# Tata Harrier.ev variant normalization

Checked: 2026-11-06

## Deliverables

- `data/tata-harrier-ev-variant-structure.csv`: 12 official grade/battery/drive/charger-package configurations.
- `data/tata-harrier-ev-price-observations.csv`: 6 price observations from a secondary source; all remain review-required.

## Current variant matrix

Tata's official Harrier.ev price/variant page lists Adventure 65, Adventure 65 ACFC, Adventure S 65, Adventure S 65 ACFC, Fearless+ 65, Fearless+ 65 ACFC, Fearless+ 75, Fearless+ 75 ACFC, Fearless+ 75 AWD, Fearless+ 75 AWD ACFC, Empowered 75 and Empowered 75 ACFC.

The 65 kWh and 75 kWh packs are LFP. RWD uses the rear motor rated 238 PS. The dual-motor QWD/AWD configuration is listed for Fearless+ 75 AWD and is rated 396 PS / 504 Nm. ACFC suffix denotes the 7.2 kW AC fast-charger package. All configurations are 5-seat SUVs with automatic electric drive. The structure file leaves RWD torque blank because the captured official page does not expose a single unambiguous RWD torque figure.

## Price evidence

The official Tata page exposes variant names but no numeric prices in the captured content. Six matching price observations are taken from V3Cars: Adventure 65 ₹21,79,000; Adventure S 65 ₹22,29,000; Fearless+ 65 ₹24,29,000; Fearless+ 75 ₹25,29,000; Fearless+ 75 AWD ₹26,79,000; Empowered 75 ₹27,79,000. These are secondary-source ex-showroom observations, with no effective date shown in the captured table. They require Tata dealer confirmation. ACFC price additions are not inferred.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Official Tata Harrier.ev variant matrix: https://ev.tata.cars/harrier/ev/price.html
- Official product overview/specifications: https://ev.tata.cars/harrier/ev.html
- Secondary current price table: https://www.v3cars.com/tata-cars/harrier-ev
