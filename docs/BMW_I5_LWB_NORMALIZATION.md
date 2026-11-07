# BMW i5 Long Wheelbase India normalization

Checked: 2026-11-06

## Audit outcome

**Status: complete — one currently listed India configuration with official OEM technical and displayed price evidence.**

BMW India currently lists the i5 Long Wheelbase separately from the standard-wheelbase i5 M60. The current product page identifies the model as **i5 Long Wheelbase**, displays a starting price of **₹79,60,000**, and presents the **i5 eDrive35L M Sport** as the product configuration.

## Current India configuration

| Variant | Fuel | Motor output | Torque | Battery | Range | 0–100 km/h | Drive |
|---|---|---:|---:|---:|---:|---:|---|
| BMW i5 eDrive35L M Sport | Electric | 268 hp | 410 Nm | 81.6 kWh gross | 669 km MIDC | 6.7 s | Rear-wheel drive |

BMW India's 7 September 2026 launch release specifies an integrated rear-axle electric drive unit with single-speed transmission, 195 km/h top speed, maximum 160 kW DC charging and 11 kW AC charging. The official product page states up to 669 km range and describes rear-axle air suspension. Do not conflate this locally assembled lower-output LWB with the imported standard-wheelbase i5 M60 xDrive.

## Price and First Edition treatment

BMW India's current i5 LWB product page displays a starting price of ₹79,60,000. The 7 September 2026 launch release calls ₹79,60,000 the introductory ex-showroom price for both the standard eDrive35L M Sport and the limited First Edition. BMW states invoice-time pricing applies and the displayed ex-showroom amount excludes road tax, TCS, RTO/statutory charges, local levies and insurance.

The same launch release says all 99 First Edition units sold out before launch. Therefore the First Edition is retained as a historical launch/edition note only and is not represented as a current orderable variant or separate current price row. The single current configuration is eDrive35L M Sport.

## Deliverables

- `data/bmw-i5-lwb-variant-structure.csv` — one India-market configuration.
- `data/bmw-i5-lwb-price-observations.csv` — one current product-page price observation, with launch-price context.

## Sources

1. BMW India i5 LWB current product page: https://www.bmw.in/en/all-models/bmw-i-series/i5/bmw-i5-overview.html
2. BMW Group India launch release (7 September 2026): https://www.press.bmwgroup.com/india/article/detail/T0460524EN/the-calm-to-your-storm%3A-the-first-ever-bmw-i5-long-wheelbase-launched-in-india
3. BMW India current all-models catalogue: https://www.bmw.in/en/all-models.html

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. This work is staging-only. No Firestore write or publication was performed.
