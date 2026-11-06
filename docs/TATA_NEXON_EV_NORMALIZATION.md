# Tata Nexon.ev variant normalization

Checked: 2026-11-06

## Deliverables

- `data/tata-nexon-ev-variant-structure.csv`: 7 current grade/battery configurations.
- `data/tata-nexon-ev-price-observations.csv`: 7 current ex-showroom price observations from V3Cars.

## Current variant structure

Tata.ev's official price page lists Creative+ MR, Creative 45, Fearless MR and other 45 kWh personas. Current 2026 price reporting confirms seven configurations:
- 30 kWh MR: Creative Plus MR, Fearless MR.
- 45 kWh: Creative 45, Fearless 45, Empowered 45, Empowered Plus A 45, Empowered Plus A 45 Red Dark.

All are front-wheel-drive electric SUVs with automatic single-speed transmission and 5 seats. Tata's official page states 45 kWh output 106 kW / 215 Nm and 489 km MIDC range. The 30 kWh MR variants are listed at 325 km range; the captured official page does not expose their exact motor output, so those fields remain blank.

## Price observations

Current V3Cars price table: Creative Plus MR ₹12,49,000; Fearless MR ₹13,29,000; Creative 45 ₹14,34,000; Fearless 45 ₹15,34,000; Empowered 45 ₹16,34,000; Empowered Plus A 45 ₹17,69,000; Empowered Plus A 45 Red Dark ₹17,89,000. These are secondary-source ex-showroom observations. Tata's official product page confirms the model starts at ₹12.49 lakh and states prices are ex-showroom and subject to change. Confirm current dealer quote before production/customer use.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Official Tata.ev price/variant page: https://ev.tata.cars/nexon/ev/price.html
- Official Tata.ev product/specification page: https://ev.tata.cars/nexon/ev.html
- Official 45 kWh specifications: https://ev.tata.cars/nexon/ev/specifications.html
- Current secondary price table: https://www.v3cars.com/tata-cars/nexon-ev
