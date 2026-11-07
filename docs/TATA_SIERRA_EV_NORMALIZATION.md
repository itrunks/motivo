# Tata Sierra.ev variant normalization

Checked: 2026-11-06

## Deliverables

- `data/tata-sierra-ev-variant-structure.csv`: 8 exact grade/battery/drive configurations.
- `data/tata-sierra-ev-price-observations.csv`: 8 ex-showroom price observations from a secondary publication of the June 30, 2026 launch price table.

## Current variant structure

Tata.ev's official Sierra.ev page lists Pure, Pure S, Adventure, Empowered and Empowered A grades. The battery/drive matrix is:
- Pure: 63 kWh RWD.
- Pure S: 63 kWh RWD.
- Adventure: 63 kWh RWD / 75 kWh RWD.
- Empowered: 63 kWh RWD / 75 kWh RWD.
- Empowered A: 75 kWh RWD / 75 kWh QWD (dual-motor AWD).

This yields 8 configurations. Tata's official page specifies RWD power at 238 PS and QWD dual-motor cumulative power at 306 PS, cumulative torque 504 Nm, and 0–100 km/h in 5.8 seconds. The 75 kWh pack is stated to deliver up to 665 km MIDC range; the 63 kWh pack is 535 km; 75 kWh AWD is 624 km. Body style is SUV, 5 seats. Battery chemistry and RWD torque are not populated in the structure file where the official page does not state them.

## Price evidence

The official Tata.ev product page does not expose numeric prices in the captured content. The 8 grade/battery prices are taken from CarDekho's published June 30, 2026 launch table: Pure 63 ₹18,79,000; Pure S 63 ₹19,99,000; Adventure 63 ₹20,99,000; Adventure 75 ₹22,19,000; Empowered 63 ₹22,79,000; Empowered 75 ₹23,79,000; Empowered A 75 ₹24,79,000; Empowered A 75 AWD ₹25,99,000. The article states prices are ex-showroom and exclude the optional 7.2 kW AC home charger (₹49,000 extra). Because the price source is secondary, these observations remain `review_required` and should be cross-checked with a Tata.ev dealer before production/customer use.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Official Tata.ev product and variant page: https://ev.tata.cars/sierra/ev.html
- June 30, 2026 launch price table (secondary publication): https://www.cardekho.com/india-car-news/tata-sierra-ev-launched-at-rs-1879-lakh-find-full-prices-variants-design-features-and-specifications-here-36229.htm
- Independent price/spec cross-check: https://www.autocarindia.com/car-news/tata-sierra-ev-launched-at-rs-2499-lakh-440084
