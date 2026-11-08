# Hyundai i20 N Line variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-i20-n-line-variant-structure.csv`: 3 current OEM trim/powertrain/transmission combinations.
- No variant-level price rows are created because the captured official catalogue exposes only a model-level range.

## Current OEM engine and trim plan

Hyundai's current features matrix lists N6 and N8 with the 1.0 Turbo GDi Petrol engine:
- N6: manual transmission only.
- N8: manual transmission and dual-clutch transmission (DCT).

Hyundai's current homepage identifies the manual as 6-speed and DCT as 7-speed. This yields 3 combinations. The current highlights page classifies the model as a Hatchback and lists configurations N6 and N8.

An older brochure describes iMT and DCT applicability differently. It is not used to override the current features matrix. The current matrix is the source of truth for this snapshot.

## Price evidence

The current official catalogue shows a broad ex-showroom range of ₹9.27–11.73 lakh. No complete variant-level price table was captured, so these amounts are not assigned to N6/N8 combinations. Current city-specific prices require the official selector/dealer confirmation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Current features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/i20-n-line/features
- Current highlights / body style and trims: https://www.hyundai.com/in/en/find-a-car/i20-n-line/highlights.html
- Hyundai India model catalogue / price and transmission summary: https://www.hyundai.com/in/en/find-a-car
- Hyundai India homepage: https://www.hyundai.com/in/en
- Older brochure retained only as historical comparison: https://www.hyundai.com/content/dam/hyundai/in/en/data/brochure/i20-n-line-brochure.pdf
