# Hyundai ALCAZAR variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-alcazar-variant-structure.csv`: 14 exact engine/trim/seating/transmission combinations from Hyundai India's current engine and trim plan.
- No variant-level price CSV is created because the captured official price page provides narrative ranges and configuration descriptions, not a complete exact price matrix.

## Current OEM engine and trim plan

The current Hyundai features matrix lists Executive, Prestige, Corporate, Platinum, Signature and Signature Knight.

**1.5 l Turbo GDi Petrol**
- 6-seater: Signature — DCT.
- 7-seater: Executive — MT; Prestige — MT / DCT; Platinum — MT; Signature — DCT; Signature Knight — DCT.

**1.5 l U2 CRDi Diesel**
- 6-seater: Signature — AT.
- 7-seater: Executive — MT; Corporate — MT / AT; Platinum — MT; Signature — AT; Signature Knight — AT.

Total: 14 exact combinations. Seating capacity is retained in normalized_variant_name so 6S and 7S variants are not collapsed into one record. The current model highlights classify Alcazar as an SUV. Official homepage identifies 6-speed MT, 7-speed DCT and 6-speed AT.

## Price evidence

The current official price page displays a starting ex-showroom price of ₹14,50,700 and describes powertrain and seating combinations. The model catalogue gives a broad range of ₹14.50–21.24 lakh. These are model-level observations, not variant-specific prices, and are not assigned to individual rows. Current city-specific variant prices require the official selector/dealer confirmation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Current features / engine, trim and seating matrix: https://www.hyundai.com/in/en/find-a-car/alcazar/features
- Highlights / SUV body style and seating: https://www.hyundai.com/in/en/find-a-car/alcazar/highlights
- Current price page: https://www.hyundai.com/in/en/find-a-car/alcazar/price
- Current model catalogue: https://www.hyundai.com/in/en/find-a-car
- Hyundai India homepage / transmission details: https://www.hyundai.com/in/en
