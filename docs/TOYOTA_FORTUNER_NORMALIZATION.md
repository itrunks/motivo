# Toyota Fortuner powertrain normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-fortuner-powertrain-families.csv`: 6 official engine/transmission/drive families.
- `data/toyota-fortuner-price-observations.csv`: one model-level starting price and two 2026 Leader Edition prices.
- No complete grade-to-powertrain matrix is declared complete; the current official configurator extraction does not expose exact grade applicability.

## Powertrain evidence

Toyota's current specification page confirms petrol 2.7 l with 5MT or 6AT in 2WD, and diesel 2.8 l turbo with 6MT or 6AT in 2WD/4WD. The Fortuner is a 7-seat SUV. The six rows are powertrain families, not six confirmed retail variants. Do not cross-join them with grade names without configurator evidence.

## Price evidence

Toyota's online booking page shows model starting price ₹34,76,000. This remains model-level only. Toyota's October 5, 2026 Leader Edition announcement lists 4x2 MT at ₹36,51,000 and 4x2 AT at ₹38,72,000. Those prices are not assigned to all standard 4x2 Fortuner configurations. Current dealer quotes remain unverified.

## Status

Obtain a current official configurator capture or grade-wise price list mapping grades to engine, transmission and drive type before completing the retail variant matrix. The 2025 Neo Drive 48V edition is retained as a separate historical powertrain and is not merged into standard grades.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- https://tweb.toyotabharat.com/fortuner.html
- https://www.toyotabharat.com/news/2026/tkm-introduces-the-2026-fortuner-leader-edition.html
- https://www.toyotabharat.com/showroom/fortuner/index-fortuner.html
- https://www.toyotabharat.com/news/2025/tkm-launches-fortuner-and-legender-neo-drive-48v-variants.html


## Current showroom and Leader Edition recheck — 2026-11-07

The current Toyota Fortuner showroom page was reopened. It confirms the model is a 7-seat SUV and exposes the following powertrain families:

- Petrol 2.7 L (2694 cc), 122 kW / 166 PS, 245 Nm, 5MT or 6AT, 2WD only.
- Diesel 2.8 L turbo (2755 cc), 150 kW / 204 PS, 420 Nm with MT and 500 Nm with AT, 6MT with iMT or 6AT, 2WD or 4WD.
- 4WD-specific off-road systems (H4/L4, DAC, electronic drive control and differential lock) are limited to diesel 4WD variants.

The current showroom page still does not expose retail grade names or a grade-to-engine/drive/transmission matrix. It has a test-drive enquiry form and an EMI calculator, but the calculator explicitly says the price is unavailable and directs customers to the nearest dealer. The older Toyota online booking endpoint returned 503 during this recheck. Therefore, the six powertrain rows remain powertrain families, not confirmed retail variants.

The October 9, 2026 Leader Edition release is current and lists two prices: 4x2 MT ₹36,51,000 and 4x2 AT ₹38,72,000. It confirms both transmissions and 4x2 drive but does not explicitly state the fuel type or exact standard grade mapping. Keep the two prices assigned only to the Leader Edition labels; do not infer diesel or cross-apply them to standard Fortuner grades. The model starting price ₹34,76,000 remains an unverified model-level observation because the booking endpoint was unavailable and the current showroom calculator does not expose a price.

The 2025 Neo Drive 48V edition remains a separate historical powertrain and is not merged into standard grades. Source reuse/redistribution remain review_required/unknown.

Rechecked sources:
- Current Fortuner showroom/specifications: https://www.toyotabharat.com/showroom/fortuner/index-fortuner.html
- 2026 Leader Edition announcement: https://www.toyotabharat.com/news/2026/tkm-introduces-the-2026-fortuner-leader-edition.html
- Toyota dealer-specific price list: https://www.toyotabharat.com/pricelist/
