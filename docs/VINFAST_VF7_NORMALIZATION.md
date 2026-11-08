# VinFast VF 7 India normalization

Checked: 2026-11-06

## Deliverables

- `data/vinfast-vf7-variant-structure.csv`: five current grade/powertrain configurations.
- `data/vinfast-vf7-price-observations.csv`: one official model-level starting-price observation.

## Current variants

VinFast India lists five VF 7 variants: Earth, Wind, Wind Infinity, Sky AWD and Sky Infinity AWD.

- Earth: 59.6 kWh pack, 130 kW / 177 PS, 250 Nm, FWD, 438 km ARAI range.
- Wind and Wind Infinity: 70.8 kWh gross pack (launch source) / 70 kWh usable capacity (current official product page), 150 kW / 204 PS, 310 Nm, FWD, 532 km ARAI range.
- Sky AWD and Sky Infinity AWD: 70.8 kWh gross pack / 70 kWh usable capacity, dual motors, 260 kW / 354 PS, 500 Nm, AWD, 510 km ARAI range.

All variants are 5-seat mid-size electric SUVs. Infinity editions are equipment/roof packages, not separate motor/battery configurations.

## Price basis

The official VF 7 product page displays ₹22,99,000 as the model starting price. It does not expose a current trim-wise price matrix in the captured content, so the amount is not assigned to Earth, Wind, Wind Infinity, Sky AWD or Sky Infinity AWD individually. Autocar's January 2026 report provides a historical variant-wise list, but the current official model page's starting amount differs from that historical table; the historical prices are not substituted for current OEM quotes.

## Battery capacity note

The official launch/variant source records 70.8 kWh for the larger battery pack, while the current product page labels 70 kWh as usable battery capacity. Both are retained in separate gross/usable fields rather than treated as conflicting values.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- VinFast India official VF 7 product page: https://vinfastauto.in/en/vf7
- VinFast India official reservation portal: https://shop.vinfastauto.in/reservation
- Official India launch announcement: https://vinfastauto.in/en/press-release/vinfast-makes-its-landmark-debut-with-launch-of-made-in-india-premium-electric-suvs
- Autocar India, January 12 2026 variant price revision and powertrain matrix: https://www.autocarindia.com/car-news/vinfast-vf6-vf7-prices-hiked-by-up-to-rs-1-3-lakh
