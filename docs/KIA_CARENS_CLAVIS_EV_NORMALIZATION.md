# Kia Carens Clavis EV variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/kia-carens-clavis-ev-variant-structure.csv`: 17 battery/trim/seating combinations.
- `data/kia-carens-clavis-ev-price-observations.csv`: 9 trim-level price observations.

## Battery, trim and seating matrix

Kia's current comparison page and 2026 brochure list nine trims:
- 42 kWh: HTK+, HTX E, HTX.
- 51.4 kWh Extended Range: HTX E ER, HTX ER, GTX ER, HTX+ ER, GTX+ ER, X-Line ER.

Seating plan: HTK+ is 7-seater only. All other listed trims offer both 6-seater and 7-seater configurations. This yields 1 + (2 x 2) + (6 x 2) = 17 rows. The 6-seater uses second-row captain seats; the 7-seater uses a second-row bench. Battery pack and seating capacity are separate dimensions in the CSV.

Kia's brochure specifies 99 kW motor output for the 42 kWh pack and 126 kW for the 51.4 kWh pack, with 255 Nm torque for both. Kia's official pages describe shift-by-wire and automatic operation. Body category is recorded as MPV based on Kia's MPV positioning and 2026 MPV award references.

## Price observations

The current official trim comparison displays nine prices: HTK+ ₹18,03,900; HTX E ₹19,99,900; HTX ₹20,53,900; HTX E ER ₹22,03,900; HTX ER ₹22,53,900; GTX ER ₹23,03,900; HTX+ ER ₹24,53,900; GTX+ ER ₹24,99,900; X-Line ER ₹24,99,900. Kia's FAQ confirms 6/7-seat versions of a trim have the same price. Values are retained as trim-level ex-showroom/MSRP observations, not duplicated onto the 17 seating rows.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- Kia Carens Clavis EV showroom: https://www.kia.com/in/our-vehicles/carens-clavis-ev/showroom.html
- Kia Carens Clavis EV specifications: https://www.kia.com/in/our-vehicles/carens-clavis-ev/specs.html
- Kia Carens Clavis EV trim comparison: https://www.kia.com/in/our-vehicles/carens-clavis-ev/specs/compare-trims.html
- Kia 2026 brochure: https://www.kia.com/content/dam/kia2/in/en/our-vehicles/kia-carens-clavis-ev/showroom/Kia_Carens_Clavis_EV_Brochure_16PP_Mobile.pdf
