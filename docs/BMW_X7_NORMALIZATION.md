# BMW X7 India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-x7-variant-structure.csv`: three current India X7 configurations with engine output and 48V system output distinguished.
- `data/bmw-x7-price-observations.csv`: three current official price observations.

## Current India variants and prices

| India model label | Fuel | Current official ex-showroom price |
|---|---|---:|
| X7 xDrive40i | Petrol | ₹1,34,90,000 |
| X7 xDrive40d DPE 7 Seater | Diesel | ₹1,32,20,000 |
| X7 xDrive40d M Sport / M Model | Diesel | ₹1,38,60,000 |

BMW India's current X7 product page lists xDrive40i and a starting price of ₹1,34,90,000. Its current all-models listing separately identifies the DPE 7 Seater diesel and the xDrive40d M Model with their respective prices. Prices are official ex-showroom observations and remain subject to invoicing/dealer confirmation.

## Technical normalization

### X7 xDrive40i petrol

The current India overview identifies the xDrive40i. BMW's current X7 technical-data page gives a 2,998 cc inline-six petrol engine with 280 kW / 381 hp and 520 Nm combustion-engine torque. The 48V mild-hybrid system produces a combined system figure of 540 Nm; 8-speed automatic, all-wheel drive and 0–100 km/h in 5.8 seconds are shown.

### X7 xDrive40d diesel

The official India December 2023 specification sheet lists both:
- X7 xDrive40d DPE 7 Seater
- X7 xDrive40d M Sport

Both use a 2,993 cc inline-six diesel, 250 kW / 340 hp and 700 Nm combustion-engine output, 8-speed Steptronic Sport transmission, xDrive all-wheel drive and 0–100 km/h in 5.9 seconds.

BMW's current X7 technical-data page separately reports 48V combined system output of 259 kW / 352 hp and 720 Nm for the xDrive40d powertrain. The CSV keeps combustion-engine and total-system figures in separate columns to avoid mixing the two measurement bases.

## Status

Complete for the three currently listed India X7 configurations and official price observations. The DPE 7 Seater label is explicit; the M Model page labels the variant X7 xDrive40d, while the India specification sheet names the trim X7 xDrive40d M Sport. This naming relationship is documented rather than hidden.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India X7 current overview: https://www.bmw.in/en/all-models/x-series/x7/bmw-x7-overview.html
- BMW India current all-models listing: https://www.bmw.in/en/all-models.html
- BMW India current X7 technical data: https://www.bmw.in/en/all-models/x-series/x7/x7-2025-g07-ice-technical-data.html
- BMW India December 2023 X7 diesel specification sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-x-series/X7/bmw-specsheet-x7-msports-and-dpe-signature-a4-dec-2023.pdf.asset.1703661265086.pdf
