# Hyundai CRETA N Line variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-creta-n-line-variant-structure.csv`: 3 exact engine/trim/transmission combinations.
- No variant-level price rows are created because the official price selector's variant-price table is empty in the captured page.

## Current OEM engine and trim plan

The current features matrix lists N8 and N10 with the 1.5 l Turbo GDi Petrol engine:
- N8: 7-speed DCT only.
- N10: 6-speed manual (MT) and 7-speed DCT.

This produces 3 exact combinations. The highlights page identifies the body style as Compact SUV (N Line), while the current price page confirms the 6-speed MT and 7-speed DCT transmission types.

## Price evidence

The official price page states a starting ex-showroom price of ₹19,03,300. The current model catalogue shows a broad range of ₹19.03–20.09 lakh. These are model-level figures; the variant selector table is empty in the captured response. No price is assigned to the individual N8/N10 combinations. Current city-specific prices require official selector/dealer confirmation.

## Source discrepancy

The current features matrix indicates N8 DCT only and N10 MT/DCT. The highlights summary's configurations field mentions N10 only, while the price page describes N8 and N10. The detailed current features matrix and price page are retained as the evidence for the three powertrain combinations; the configuration-summary mismatch is documented rather than silently ignored.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/creta-n-line/features
- Price / trim and transmission details: https://www.hyundai.com/in/en/find-a-car/creta-n-line/price
- Highlights / body style: https://www.hyundai.com/in/en/find-a-car/creta-n-line/highlights
- Current model catalogue: https://www.hyundai.com/in/en/find-a-car
