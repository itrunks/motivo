# Audi A4 India normalization

Checked: 2026-11-06

## Deliverable

- `data/audi-a4-variant-structure.csv`: three current India trim labels with shared official powertrain specifications.

## Current official trim matrix

Audi India's current A4 Sedan page lists three trims:
- Premium
- Premium Plus
- Technology

The current page confirms a 2.0L TFSI petrol engine, 150 kW / 204 hp, 7-speed S tronic transmission and 0–100 km/h in 7.1 seconds. The official 2024 brochure provides the shared 320 Nm torque, front-wheel drive and 1,984 cc displacement; the current page does not restate displacement, so the CSV leaves it blank rather than silently carrying forward the older number.

The current configurator link is live, but the captured page does not render grade-level price or equipment differences. Audi's Price Reckoner likewise does not expose embedded values in the captured text.

## Status

Partial. Three current trims and shared powertrain are normalized; exact grade-specific equipment and current India ex-showroom prices remain unavailable in the captured official sources.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Audi India A4 Sedan current product page: https://www.audi.in/en/models/a4/a4-sedan/
- Audi India A4 configurator: https://www.audi.in/en/models/a4/a4-sedan/configurator/
- Audi A4 2024 official brochure (historical technical cross-check): https://www.audi.in/dam/nemo/in/Downloads/A4/050_Audi%20A4%20Digital%20Brochure%20_2024%20Small.pdf
