# Mahindra Scorpio-N normalization

Checked: 2026-11-06

## Deliverables

- `data/mahindra-scorpio-n-variant-price-observations.csv`: 31 populated grade / powertrain / transmission / drive / seating combinations from Mahindra's official August 5, 2026 price matrix.

## Normalized configuration coverage

The official OEM matrix contains only the following populated combinations. Blank matrix cells are not variants and have not been filled by cross-joining trim, engine and transmission lists.

- Petrol, 2WD, 6-speed manual: Z2, Z4, Z8S, Z8T, Z8L (ADAS) — 7-seat; Z8L (ADAS) also has a 6-seat configuration.
- Petrol, 2WD, 6-speed automatic: Z4, Z8S, Z8T, Z8L (ADAS) — 7-seat; Z8L (ADAS) also has a 6-seat configuration.
- Diesel, 2WD, 6-speed manual: Z2, Z4, Z6, Z8S, Z8, Z8T, Z8L (ADAS) — 7-seat; Z8L (ADAS) also has a 6-seat configuration.
- Diesel, 2WD, 6-speed automatic: Z4, Z6, Z8S, Z8, Z8T, Z8L (ADAS) — 7-seat; Z8L (ADAS) also has a 6-seat configuration.
- Diesel, 4WD, 6-speed manual: Z4, Z8T, Z8L (ADAS) — 7-seat only.
- Diesel, 4WD, 6-speed automatic: Z8T, Z8L (ADAS) — 7-seat only.

The official price matrix yields 31 populated combinations. It identifies G20 mStallion TGDi petrol and D22 mHawk diesel engines, but this pass does not add displacement, output or torque values because those specifications were not needed to normalize the matrix and are not transcribed here.

## Price evidence

Mahindra's August 5, 2026 announcement explicitly labels the table as ex-showroom prices in lakh. Values have been converted to integer INR without changing the stated price basis. The official online selector provides a current order flow and confirms grade/code families, but selector card values can differ slightly from the press-release table and are delivery-time indicative. Keep the dated release matrix separate from any later selector/dealer quote; do not silently overwrite or blend them.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. This OEM page is an audit source, not proof of permission to commercially reproduce its content. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra official Scorpio-N feature and variant-wise price release, August 5, 2026: https://auto.mahindra.com/press-release/mahindra-elevates-the-scorpio-n-experience.html
- Mahindra official online variant selector: https://auto.mahindra.com/own-online/variant-selection?pid=SCN

