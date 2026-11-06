# Hyundai VENUE N Line variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-venue-n-line-variant-structure.csv`: 3 exact engine/trim/transmission combinations.
- No variant-level price rows are created because the official page's variant-price table is not populated in the captured result.

## Current OEM engine and trim plan

The current features matrix lists N6 and N10:
- N6: Kappa 1.0 Turbo GDi Petrol with MT / DCT.
- N10: Kappa 1.0 Turbo GDi Petrol with DCT only.

The official price page confirms the manual is 6-speed and the DCT is 7-speed. This produces 3 exact combinations. The highlights page identifies body style as Sub-compact SUV (N Line), with N6 and N10 configurations.

## Price evidence

The official price page states a starting ex-showroom price of ₹10,66,100 and describes the two trim/transmission offerings, but its detailed variant-price table is empty in the captured page. The broader model catalogue range is ₹10.66–15.66 lakh. Neither amount is assigned to an individual combination. City-specific current prices require the official selector/dealer confirmation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/venue-n-line/features
- Price / trim transmission details: https://www.hyundai.com/in/en/find-a-car/venue-n-line/price
- Highlights / body style and configurations: https://www.hyundai.com/in/en/find-a-car/venue-n-line/highlights.html
- Current model catalogue: https://www.hyundai.com/in/en/find-a-car
- Owner manual selector / current generation period: https://org2.hyundai.com/in/en/connect-to-service/hyundai-service/owners-manual
