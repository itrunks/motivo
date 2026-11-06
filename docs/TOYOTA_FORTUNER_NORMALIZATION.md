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
