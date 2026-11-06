# BMW X1 India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-x1-variant-structure.csv`: two current India powertrain/trim configurations.
- `data/bmw-x1-price-observations.csv`: model-level starting price and grade-specific diesel price, kept separate.

## Current variants and specifications

BMW India's current X1 product page lists two combustion powertrains:
- **sDrive18i M Sport** — 1,499 cc 3-cylinder petrol, 100 kW / 134 hp, 230 Nm, 7-speed Steptronic dual-clutch, 0–100 km/h in 9.2 s.
- **sDrive18d M Sport** — 1,995 cc 4-cylinder diesel, 110 kW / 148 hp, 360 Nm, 7-speed Steptronic dual-clutch, 0–100 km/h in 8.9 s.

The official December 2023 India specification sheet provides the detailed technical values. Drive layout is not repeated in the captured spec table, so it is left blank.

## Price observations

- Current X1 product page: ₹50,90,000 starting ex-showroom; the page does not map this starting amount to a named grade.
- Current BMW all-models listing: sDrive18d M Sport from ₹52,90,000.

No petrol grade-specific price is assigned from the model-level starting amount without explicit OEM mapping.

## Status

Partial. Both current powertrain/trim configurations are normalized and the diesel grade price is explicit, but the ₹50.90L starting price is not explicitly assigned to the sDrive18i grade.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India current X1 product page: https://www.bmw.in/en/all-models/x-series/X1/bmw-X1.html
- BMW India current all-models SUV listing: https://www.bmw.in/en/all-models.html?category=suv
- BMW India December 2023 X1 specification sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-x-series/X1/bmw-specsheet-x1-combined-a4-dec-2023.pdf.asset.1702893287559.pdf
