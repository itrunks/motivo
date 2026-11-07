# BMW M340i India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-m340i-technical-observations.csv`: two official technical observations from different model-year spec sheets.
- `data/bmw-m340i-price-observations.csv`: current all-models price and legacy product-page price kept separate.

## Current listing

BMW India's current all-models page lists **M340i xDrive** from ₹77,80,000 ex-showroom. The older dedicated product page shows ₹75,40,000 and is treated as a legacy page observation, not the current canonical price.

## Technical evidence and conflict

Two official India specification sheets report:
- November 2023 M340i xDrive Shadow: 2,998 cc inline-six petrol, 275 kW / 374 hp, 500 Nm, 8-speed Steptronic Sport, xDrive AWD, 4.4 s.
- September 2021 M340i xDrive: 2,998 cc inline-six petrol, 285 kW / 387 hp, 500 Nm, 8-speed Steptronic Sport, xDrive AWD, 4.4 s.

The 2023 Shadow tune and 2021 earlier tune are not merged into one current spec. A current 2026 technical sheet is not exposed in the captured pages.

## Status

Partial. Current model label and ₹77.80L listing price are captured, but the current technical tune is not confirmed against a current India spec sheet; the older ₹75.40L page and older power output remain historical observations.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India current all-models listing: https://www.bmw.in/en/all-models.html?series=3
- BMW India older M340i product page: https://www.bmw.in/en/all-models/3-series/sedan/2022/bmw-3-series-sedan-overview.html
- BMW India November 2023 M340i xDrive Shadow spec sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-m-series/m340i_xdrive/BMW_Specsheet_M340i%20xDrive_A4_Nov_2023.pdf.asset.1700736393566.pdf
- BMW India September 2021 M340i xDrive spec sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/05_PR70138_INR-CWW-BMW_NSC_Specsheet_AllVariants_Sept21_M340i_xDrive_A4.pdf.asset.1633604795350.pdf
