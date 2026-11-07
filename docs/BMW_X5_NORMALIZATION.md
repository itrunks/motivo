# BMW X5 India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-x5-variant-structure.csv`: four India powertrain/trim combinations from official BMW specification sheets.
- `data/bmw-x5-price-observations.csv`: two current model-level price observations.

## Current India model and technical variants

BMW India's current X5 product page lists the petrol X5 from ₹96,90,000; the current all-models page separately lists X5 xDrive30d diesel from ₹98,90,000.

Official India spec sheets identify these four powertrain/trim combinations:
- xDrive40i xLine — 2,998 cc petrol inline-six, 280 kW / 381 hp, 520 Nm, 8-speed Steptronic Sport, xDrive AWD, 5.4 s.
- xDrive40i M Sport — same petrol powertrain and performance.
- xDrive30d SportX Plus — 2,993 cc diesel inline-six, 195 kW / 265 hp, 620 Nm, 8-speed Steptronic, xDrive AWD, 6.5 s.
- xDrive30d M Sport — same diesel powertrain and performance.

## Price limitation

The current official product/listing pages provide model-level starting prices only. They do not map the ₹96.90L petrol and ₹98.90L diesel starting amounts to each of the four trim labels. No trim-level price is fabricated.

## Status

Partial. Four technical trim/powertrain combinations are normalized and current model-level prices captured; exact current orderability and grade-specific price mapping remain unconfirmed.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India current X5 product page: https://www.bmw.in/en/all-models/x-series/x5/x5-2025-g05.html
- BMW India current all-models listing: https://www.bmw.in/en/all-models.html?series=2
- BMW India November 2023 X5 petrol spec sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-x-series/X5/bmw-specsheet-x5-petrol-a4-nov-2023.pdf.asset.1700028189229.pdf
- BMW India January 2023 X5 diesel spec sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-x-series/X5/BMW_Specsheet_X5_Diseal_A4_Jan_2023.pdf.asset.1674016439061.pdf
