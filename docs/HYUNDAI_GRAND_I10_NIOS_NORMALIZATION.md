# Hyundai GRAND i10 NIOS variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-grand-i10-nios-variant-structure.csv`: 15 exact trim/powertrain combinations from the current Hyundai India engine and trim matrix.
- No variant-level price CSV is created. The captured official price page provides a starting price and narrative trim information, but does not expose a complete variant-by-variant price table.

## Current OEM engine and trim plan

The official features matrix lists these trim labels: Era, Magna, Corporate, Sportz, Sportz VIBE, Sportz(O), Sportz(O) VIBE and Asta.

- 1.2 l Kappa Petrol manual: Era, Magna, Corporate, Sportz, Sportz VIBE, Sportz(O), Asta (7 combinations).
- 1.2 l Kappa Petrol Smart Auto AMT: Corporate, Sportz, Sportz VIBE, Sportz(O), Sportz(O) VIBE, Asta (6 combinations).
- 1.2 l Bi-fuel Kappa Petrol with Hy-CNG Duo MT: Magna, Sportz (2 combinations).

Total: 15 structure combinations. The current highlights page classifies the model as a Hatchback. Hyundai's current catalogue gives a broad ex-showroom range of ₹5.59–8.04 lakh; the price page starts at ₹5,59,700. These model-level prices are not assigned to individual variants.

## Model-year note

Hyundai's owner-manual selector distinguishes Grand i10 NIOS from Jan 2026 to present and earlier periods, but the variant matrix does not map each trim to a formal model-year field. Therefore model_year remains blank in the normalized CSV.

## Price and evidence limitations

The official price page does not expose a complete current variant-price table in the captured response. A separate official 2026 VIBE Edition announcement PDF contains selected VIBE/Asta price observations, but not a complete matrix for all 15 combinations. Those partial observations are not mixed into a full price catalogue. City-specific current prices require the official selector/dealer confirmation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/grand-i10-nios/features
- Price page: https://www.hyundai.com/in/en/find-a-car/grand-i10-nios/price
- Highlights / body style: https://www.hyundai.com/in/en/find-a-car/grand-i10-nios/highlights.html
- Official model catalogue: https://www.hyundai.com/in/en/find-a-car
- Hyundai 2026 VIBE Edition announcement: https://org3.hyundai.com/content/dam/hyundai/in/en/images/hyundai-story/news/2026/vibe-nios.pdf
- Owner-manual model-year selector: https://org2.hyundai.com/in/en/connect-to-service/hyundai-service/owners-manual
