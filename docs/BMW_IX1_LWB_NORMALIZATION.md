# BMW iX1 Long Wheelbase India normalization

Checked: 2026-11-06

## Audit outcome

**Status: complete — one current India-market electric configuration and a current official displayed price observation captured. Staging only.**

BMW India's current all-models catalogue lists the iX1 LWB under its full-electric range. The current model card identifies the product as **iX1 eDrive20L M Sport**. The September 2026 India brochure's technical table labels the drive-system configuration **iX1 eDrive20L**. These are treated as one configuration; the brochure's technical label is preserved and the current catalogue's marketed suffix is retained.

## Normalized India configuration

| Field | OEM evidence |
|---|---|
| Variant | BMW iX1 eDrive20L M Sport (catalogue label); eDrive20L (brochure technical label) |
| Fuel / drive system | All-electric |
| Power | 150 kW / 204 hp |
| Torque | 250 Nm |
| Drivetrain | Front-wheel drive |
| Transmission | Not stated in India brochure; left blank |
| Battery | 66.4 kWh |
| Range | Up to 546 km MIDC |
| 0–100 km/h | 8.6 s |
| Top speed | 175 km/h |
| DC charging | Up to 130 kW |
| AC charging | 11 kW |
| Seating | Not stated in the cited India iX1 technical brochure; left blank. |

The current product page states 204 hp delivered to the front axle, 66.4 kWh battery and 546 km MIDC range. The September 2026 India brochure supplies the complete current technical row including 150 kW, 250 Nm, FWD, acceleration, top speed, range and charging ratings.

## Price treatment

- **Current official page observation:** ₹54,70,000, displayed as the starting price on BMW India's current iX1 LWB product page, checked 2026-11-06.
- The product-page disclaimer states prices are exclusive of applicable taxes and statutory levies; exact invoice/tax basis and city applicability should be confirmed with an authorised BMW dealer.
- Older secondary launch coverage reported an introductory price around ₹49 lakh in January 2025. It is not recorded as an OEM price observation because the captured official sources do not establish a dated iX1 launch price.
- No city-specific on-road price is inferred.

## Deliverables

- `data/bmw-ix1-lwb-variant-structure.csv` — one current India configuration; unpublished transmission left blank.
- `data/bmw-ix1-lwb-price-observations.csv` — current official displayed price, with historical launch amount explicitly separated.
- `docs/BMW_IX1_LWB_NORMALIZATION.md` — evidence and normalization decisions.

## Sources

1. BMW India, current iX1 LWB product page: https://www.bmw.in/en/all-models/bmw-i/iX1/2025/bmw-ix1-highlights.html
2. BMW India, September 2026 iX1 LWB brochure: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure_pdf_2026/iX1_LWB_Brochure.pdf.asset.1790595797393.pdf
3. BMW India, all-models catalogue: https://www.bmw.in/en/all-models.html
4. Autocar India, 17 January 2025, secondary launch coverage (reported launch price only; not used as OEM price evidence): https://www.autocarindia.com/car-news-amp/bmw-ix1-lwb-launched-at-rs-49-lakh-auto-expo-2025

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. This work is staging-only. No Firestore write or publication was performed.
