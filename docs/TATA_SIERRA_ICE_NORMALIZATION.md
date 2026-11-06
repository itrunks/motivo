# Tata Sierra 2026 ICE variant normalization

Checked: 2026-11-06

## Deliverables

The 59-row variant catalogue is split into three CSV files to keep the evidence batches manageable:
- `data/tata-sierra-variant-normalization-part1.csv` — 30 rows.
- `data/tata-sierra-variant-normalization-part2.csv` — 15 rows.
- `data/tata-sierra-variant-normalization-part3.csv` — 14 rows.

All three files were fetched back from the feature branch and row-count verified: 30 + 15 + 14 = 59 variants.

## Powertrain families

The current variant listing covers 59 combinations across:
- 1.5 l Revotron naturally aspirated petrol, 1498 cc, 106 hp / 145 Nm, 6-speed manual or 7-speed DCA.
- 1.5 l Hyperion turbo-petrol, 1498 cc, 160 hp / 255 Nm, 6-speed automatic.
- 1.5 l Kryojet turbo-diesel, 1497 cc, 118 hp / 280 Nm, 6-speed manual or 6-speed torque-converter automatic.

All variants are 5-seat SUVs. Trim families include Smart+, Pure, Pure+, Adventure+, Accomplished and Accomplished+, plus Legend (L), L(O) and Dark editions. Dark and Legend packages are preserved as separate OEM labels rather than collapsed into base trims.

## Price evidence and limitation

The 59 prices are **on-road Delhi** observations from Autocar India's variant page, last updated October 31, 2026. They are not ex-showroom prices and must not be compared directly with the ex-showroom figures in other model files. City scope is explicitly Delhi. The official Tata product page does not expose a complete numeric 59-variant price matrix in the captured content. Use the Autocar figures as secondary-source observations and confirm current dealer invoice values before customer use.

## Reconciliation notes

The official Tata brochure/website should remain the preferred source for exact current orderability. The 59-row third-party listing may contain editions whose availability varies by city/dealer; this is recorded without asserting nationwide stock availability. No 6-seat configuration is inferred; the Sierra ICE listing is 5-seat.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Autocar India 59-variant list and on-road Delhi prices (updated October 31, 2026): https://www.autocarindia.com/cars/tata/sierra/variants
- Tata official Sierra model page: https://cars.tatamotors.com/suv/sierra.html
- V3Cars variant/engine price cross-check: https://www.v3cars.com/tata-cars/sierra
- Tata official brochure: https://cars.tatamotors.com/content/dam/tml/pv/products/sierra/overview/brochure.pdf
