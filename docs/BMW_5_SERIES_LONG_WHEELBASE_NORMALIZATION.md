# BMW 5 Series Long Wheelbase India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-5-series-long-wheelbase-variant-structure.csv`: one current India 530Li M Sport LWB configuration.
- `data/bmw-5-series-long-wheelbase-price-observations.csv`: three official price observations with source/basis differences preserved.

## Current India configuration

BMW India's current 5 Series Long Wheelbase product page and all-models listing identify the **530Li M Sport LWB**. The official 2024 India brochure specifies:
- 1,998 cc BMW TwinPower Turbo inline-four petrol.
- 190 kW / 258 hp.
- 400 Nm.
- 8-speed Steptronic automatic.
- Rear-wheel drive.
- 0–100 km/h in 6.5 seconds.

## Official price observations

| Source | Price |
|---|---:|
| Dedicated current product page | ₹76,60,000 |
| Special-offers page | ₹77,00,000 |
| BMW Finance illustration | ₹76,50,000 |

These are separate official observations and are not silently reconciled. The dedicated product page is treated as the current list-price reference; the special-offers and finance-page values are retained as distinct promotional/finance contexts pending dealer confirmation.

## Status

Partial. One current configuration is verified, but three official pages display different price amounts/bases. Confirm the applicable invoice price with BMW India before staging a single canonical price.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India 5 Series LWB product page: https://www.bmw.in/en/all-models/5-series/sedan/bmw-5-series-sedan-g68.html
- BMW India all-models listing: https://www.bmw.in/en/all-models.html?series=5
- BMW India finance illustration: https://www.bmw.in/en/bmw-financial-services/bmw-loan.html
- BMW India special offers: https://www.bmw.in/en/topics/special-offers.html
- BMW India 2024 5 Series LWB brochure: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/Brochures/2024/The-BMW-5Series-LWB_Brochure.pdf.asset.1728900429634.pdf
