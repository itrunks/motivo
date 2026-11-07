# Hyundai i20 variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-i20-variant-structure.csv`: 12 exact trim/transmission combinations from Hyundai India's current engine and trim matrix.
- No complete variant-level price CSV is created. The available February 2026 price announcement covers selected variants and is not a complete current price matrix.

## Current OEM engine and trim plan

The features page lists these trim labels: Era, Magna Executive, Magna, Sportz, Sportz(O), Sportz(O) Knight, Asta, Asta(O), Asta(O) Knight.

Engine: 1.2 l Kappa Petrol.

- Manual: Era, Magna Executive, Magna, Sportz, Sportz(O), Sportz(O) Knight, Asta, Asta(O) — 8 combinations.
- Intelligent Variable Transmission (IVT): Sportz, Sportz(O), Asta(O), Asta(O) Knight — 4 combinations.

Total: 12 combinations. The highlights page identifies body style as Hatchback. Model year remains blank because the cited current trim matrix does not specify an individual model-year field.

## Price evidence

The official current model catalogue displays a broad ex-showroom range of ₹5.99–10.63 lakh. Hyundai's 5 February 2026 press release announces refreshed pricing for selected variants and a new starting price of ₹5,99,000. Neither source, as captured, provides a complete variant-by-variant price matrix covering all 12 combinations. Therefore no model-level range or selected launch price is assigned to individual structure rows. Current city-specific prices require the official selector/dealer confirmation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/i20/features
- Highlights / body style: https://www.hyundai.com/in/en/find-a-car/i20/highlights.html
- Current model catalogue: https://www.hyundai.com/in/en/find-a-car
- 5 February 2026 selected-variant price announcement: https://www.hyundai.com/content/dam/hyundai/in/en/images/hyundai-story/news/2025/i20-new-price-value.pdf
