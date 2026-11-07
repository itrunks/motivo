# Kia Carens variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/kia-carens-variant-structure.csv`: 2 current India showroom configurations.
- No variant-level price observations are created. The current showroom does not render a numeric price; the specs page shows a model-level starting MSRP that is not assigned to the petrol or CNG configuration.

## Current India configurations

Kia's current showroom exposes:
- Premium (O) 7 — 1.5 l Smartstream G1.5 Petrol, manual transmission.
- Premium (O) CNG — 1.5 l Smartstream G1.5 bi-fuel Petrol+CNG, manual transmission.

Kia's showroom identifies Carens as a 7-seater family vehicle with 6/7-seat family configurations in the model range. The current two displayed retail cards are both labeled 7. The body style is recorded as MPV. Older Prestige/Luxury trim labels from historical brochures are intentionally excluded because the current India showroom no longer exposes them as current retail cards.

## Price limitation

The current showroom cards do not display a numeric price. The specifications page displays a starting MSRP of ₹11,11,900 at model level, but the source does not clearly map this number to the CNG configuration. No variant price is populated. Confirm the live configurator or dealer price before customer quotation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- https://www.kia.com/in/our-vehicles/carens/showroom.html
- https://www.kia.com/in/our-vehicles/carens/specs.html
- https://www.kia.com/in/our-vehicles/carens/specs/compare-trims.html
