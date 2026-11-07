# BMW M4 Competition India normalization

Checked: 2026-11-07

## Audit outcome

**Status: complete — one current India-market M4 Competition configuration and a current official displayed price captured.**

The current BMW India product page identifies the model as **M4 Competition Coupé** and displays a starting price of ₹1,62,90,000. The India-specific 2 May 2024 launch release identifies the sold configuration as **M4 Competition M xDrive**, with a 3.0-litre S58 inline-six petrol engine, 530 hp, 650 Nm, M xDrive all-wheel drive and 0–100 km/h in 3.5 seconds. The current BMW India technical page confirms 390 kW/530 hp, 2,993 cc, 650 Nm, 8-speed automatic and AWD.

## Normalized configuration

| Field | India-market value |
|---|---|
| Variant | BMW M4 Competition M xDrive Coupé |
| Fuel | Petrol |
| Engine | 3.0-litre S58 M TwinPower Turbo inline-six |
| Displacement | 2,993 cc |
| Power | 390 kW / 530 hp |
| Torque | 650 Nm |
| Transmission | 8-speed automatic M Steptronic with Drivelogic |
| Drivetrain | M xDrive all-wheel drive |
| 0–100 km/h | 3.5 seconds |
| Top speed | 250 km/h |
| Seating | Not stated in captured India OEM sources; left blank |

The BMW India technical page also exposes a separate rear-wheel-drive 510 hp specification block. This is not treated as a second India-market configuration because the India-specific launch release and current product page identify the local M4 Competition as the 530 hp M xDrive car. The M4 CS is separately labelled on BMW's page and is outside this M4 Competition model audit.

## Price observations

- **Current BMW India product-page display:** ₹1,62,90,000, checked 2026-11-07.
- **Historical India launch price:** ₹1,53,00,000 ex-showroom, announced 2024-05-02.
- The current product-page disclaimer says prices are exclusive of applicable taxes/statutory levies; the BMW India all-models catalogue explains its ex-showroom price as GST-inclusive but excluding road tax, TCS, RTO, statutory/local levies and insurance. The invoicing price prevails. Confirm exact dealer quotation before purchase.

## Deliverables

- `data/bmw-m4-competition-variant-structure.csv` — one India-market M xDrive configuration.
- `data/bmw-m4-competition-price-observations.csv` — current displayed price and dated historical launch price.
- `docs/BMW_M4_COMPETITION_NORMALIZATION.md` — evidence and decisions.

## Sources

1. BMW India current product page: https://www.bmw.in/en/all-models/m-series/bmw-4-series-m-models/bmw-m4-coupe.html
2. BMW India current technical data: https://www.bmw.in/en/all-models/m-series/bmw-4-series-m-models/bmw-m4-coupe-technical-data.html
3. BMW India launch release, 2 May 2024: https://www.press.bmwgroup.com/india/article/detail/T0441579EN/the-new-bmw-m4-competition-m-xdrive-arrives-in-india?showMedia=photo
4. BMW India current all-models catalogue: https://www.bmw.in/content/bmw/marketIN/bmw_in/en/all-models.html

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. Staging only. No production Firestore write or publication performed.
