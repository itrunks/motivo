# BMW X3 India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-x3-variant-structure.csv`: two current India X3 powertrain/trim configurations.
- `data/bmw-x3-price-observations.csv`: two current all-models grade prices plus one conflicting dedicated-page legacy observation.

## Current India variants

BMW India's current all-models listing identifies:
- **X3 xDrive20 M Sport** — petrol.
- **X3 xDrive20d M Sport Pro** — diesel.

The January 2026 official India X3 brochure provides the corresponding powertrain data:
- X3 20 xDrive: 140 kW / 190 hp, 310 Nm, 8-speed automatic, xDrive AWD, 0–100 km/h in 7.8 s.
- X3 20d xDrive: 145 kW / 197 hp, 400 Nm, 8-speed automatic, xDrive AWD, 0–100 km/h in 7.7 s.

## Price observations and discrepancy

- X3 xDrive20 M Sport: ₹76,90,000 from the current BMW all-models listing.
- X3 xDrive20d M Sport Pro: ₹78,20,000 from the current BMW all-models listing.
- Dedicated X3 product page still shows ₹75,70,000 as a model-level starting price, which conflicts with the current all-models grade prices.

The two grade prices are retained as the current listing evidence; the older dedicated-page value is kept as a separate legacy observation. Confirm the applicable invoice price with BMW dealer before canonical price staging.

## Status

Partial. Two current powertrain/trim configurations and grade prices are captured, but the dedicated product page's stale/contradictory starting price remains unresolved.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India current all-models listing: https://www.bmw.in/en/all-models.html?series=4
- BMW India dedicated X3 product page: https://www.bmw.in/en/all-models/x-series/x3/bmw-x3.html
- BMW India January 2026 X3 brochure: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure_pdf_2026/X3_Brochure_Jan_26.pdf.asset.1773130692467.pdf
