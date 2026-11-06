# Mahindra XUV 7XO selector price observations

Checked: 2026-11-06

## Deliverable

- `data/mahindra-xuv-7xo-variant-price-observations.csv`: 12 current OEM selector card observations (7 diesel, 5 petrol).

## Current selector observations

The current online selector exposes these grade/fuel cards and ex-showroom amounts:

| Fuel | Selector label | Ex-showroom INR |
|---|---|---:|
| Diesel | AX3 DIESEL | ₹18,37,999 |
| Diesel | AX5 DIESEL | ₹19,88,999 |
| Diesel | AX7 DIESEL | ₹21,15,500 |
| Diesel | AX7T DIESEL | ₹23,24,999 |
| Diesel | AX7T DIESEL AWD | ₹23,99,000 |
| Diesel | AX7L DIESEL | ₹24,95,999 |
| Diesel | AX7L DIESEL AWD | ₹25,94,000 |
| Petrol | AX3 PETROL | ₹17,79,000 |
| Petrol | AX5 PETROL | ₹19,29,000 |
| Petrol | AX7 PETROL | ₹20,58,000 |
| Petrol | AX7T PETROL | ₹22,62,000 |
| Petrol | AX7L PETROL | ₹24,29,000 |

The diesel selector explicitly identifies AWD on AX7T and AX7L cards. The selector output captured in this audit does not expose the exact transmission or seating capacity for each card. Those fields are deliberately left blank rather than copied from a launch-era matrix whose introductory prices were limited to the first 40,000 deliveries.

## Evidence limitations

- Mahindra's January 5, 2026 launch announcement contains an introductory price and applicability matrix, including manual/automatic, 6-/7-seat and AWD notes. Those prices were explicitly introductory for the first 40,000 deliveries and are not substituted for the current selector amounts.
- The current selector cards do not provide enough visible information in the captured response to normalize exact gearbox and seating derivatives.
- The 12 rows are selector grade/fuel price observations, not a complete exact variant × transmission × seating matrix.
- No engine output, displacement, torque or model-year fields are added where not directly shown in the current selector evidence.

## Rights and import gate

All observations remain `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra current diesel selector: https://auto.mahindra.com/own-online/variant-selection?pid=X7XO
- Mahindra current petrol selector: https://auto.mahindra.com/own-online/variant-selection?pid=X7XOM094718025565
- Mahindra January 5, 2026 launch matrix (introductory prices only): https://www.mahindra.com/news-room/press-release/en/mahindra-premieres-xuv-7xo-with-5-pioneering-tech-disruptions
