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


## Current OEM matrix reconciliation — 2026-11-07

The current official Mahindra 2026 brochure supplies the exact variant applicability matrix that was missing from the earlier selector capture. It resolves **27 exact combinations**:

- AX: 7-seat petrol MT and diesel MT (2)
- AX3: 7-seat petrol/diesel MT and AT (4)
- AX5: 7-seat petrol/diesel MT and AT (4)
- AX7: 7-seat petrol/diesel MT and AT (4)
- AX7 TECH (current selector alias AX7T): 6-seat petrol AT, diesel MT/AT; 7-seat petrol AT, diesel MT/AT/AWD AT (7)
- AX7 LUXURY (current selector alias AX7L): 6-seat petrol AT and diesel AT; 7-seat petrol AT, diesel MT/AT/AWD AT (6)

The brochure technical table confirms:
- Petrol: 2.0 L TGDi, 149.2 kW, 380 Nm, 6MT/6AT.
- Diesel: 2.2 L CRDe, 136 kW, 420 Nm with MT and 450 Nm with AT, 6MT/6AT.
- AWD is limited to AX7 TECH and AX7 LUXURY; the applicability table specifies diesel AT AWD for 7-seat derivatives only.

A new file, `data/mahindra-xuv-7xo-variant-structure.csv`, records all 27 exact combinations. Unknown year and effective-date fields remain blank. The file does not infer variant prices.

## Current selector price refresh — 2026-11-07

The live OEM selector was rechecked. It exposes 7 diesel grade/fuel cards and 5 petrol grade/fuel cards. The petrol card amounts have changed from the previous capture:

| Petrol selector card | Current ex-showroom INR |
|---|---:|
| AX3 | 17,88,000 |
| AX5 | 19,38,499 |
| AX7 | 20,68,499 |
| AX7T | 22,75,999 |
| AX7L | 24,28,999 |

Diesel card amounts remain AX3 ₹18,37,999; AX5 ₹19,88,999; AX7 ₹21,15,500; AX7T ₹23,24,999; AX7T AWD ₹23,99,000; AX7L ₹24,95,999; AX7L AWD ₹25,94,000.

The selector still does not expose per-transmission/per-seating prices. These 12 amounts remain separate grade/fuel selector observations and must not be copied to all 27 derivative rows. Mahindra's selector says delivery-time prices prevail and that displayed amounts are indicative. No launch-era introductory prices are reused.

## Remaining caveats

- Variant structure and current grade/fuel selector observations are now captured; exact per-derivative current prices are not.
- The source permission fields remain `review_required` / `unknown`.
- No Firestore import or publication is approved.
- The January 2026 launch price table was explicitly introductory for the first 40,000 deliveries and is used only as historical context, not as current pricing.

Sources:
- Current official diesel selector: https://auto.mahindra.com/own-online/variant-selection?pid=X7XO
- Current official petrol selector: https://auto.mahindra.com/own-online/variant-selection?pid=X7XOM094718025565
- Official 2026 XUV 7XO brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw73989e8a/brochures/X7XO/X7XO_brochure.pdf
- Official launch release (introductory prices only): https://www.mahindra.com/news-room/press-release/en/mahindra-premieres-xuv-7xo-with-5-pioneering-tech-disruptions
