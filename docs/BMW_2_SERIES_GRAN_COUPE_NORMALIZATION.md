# BMW 2 Series Gran Coupé India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-2-series-gran-coupe-variant-structure.csv`: one current India retail configuration.
- `data/bmw-2-series-gran-coupe-price-observations.csv`: official list-price and limited-offer observations kept separate.

## Current India configuration

BMW India's current product page shows one India retail label: **218 M Sport**. The official 2025 India brochure identifies the technical configuration as:
- BMW TwinPower Turbo 3-cylinder petrol.
- 1,499 cc.
- 115 kW / 156 hp.
- 230 Nm.
- 7-speed Steptronic dual-clutch automatic.
- 230 km/h top speed.

The India brochure does not state the drive layout in its technical data table, so that field is left blank rather than inferred.

## Price basis

- Current BMW product page: ₹45,80,000 starting price.
- BMW India special-offers page: ₹45,30,000 GST-benefit promotional price, with limited-state/limited-unit and dealer terms.

The promotional price is not treated as a standard national list price. Both are retained as separate official observations.

## Status

Complete for the currently listed India 218 M Sport configuration and the official price/offer evidence. Equipment, colour and upholstery selections are personalization choices, not separate powertrain variants.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India 2 Series Gran Coupé product page: https://www.bmw.in/en/all-models/2-series/2-series-gran-coupe/bmw-2-series-gran-coupe.html
- BMW India 2025 2 Series Gran Coupé brochure: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/all-models/i-series/Brochures/The_New_2_Series_Gran_Coupe_Brochure_2025.pdf.asset.1752847862923.pdf
- BMW India special offers: https://www.bmw.in/en/topics/special-offers.html
