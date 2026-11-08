# Hyundai AURA variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/hyundai-aura-variant-structure.csv`: 7 exact engine/trim/transmission/fuel combinations from Hyundai India's official engine and trim plan.
- No variant-level price rows are created because the captured official price page renders an empty variant-price table and requires model/state/city/fuel/transmission selection.

## Official structure evidence

Hyundai's current features page shows the engine and trim plan:

- 1.2 l Kappa petrol manual: E, S, SX, SX(O)
- 1.2 l Kappa petrol AMT: SX+ is explicitly annotated in the SX column; the precise current retail label should be confirmed with dealer/configurator before import.
- 1.2 l Kappa bi-fuel petrol with Hy-CNG manual: S, SX

This yields 7 evidence-backed combinations. The OEM home page independently confirms the 1.2 l Kappa petrol and 1.2 l bi-fuel petrol+CNG engine families and 5-speed manual / Smart Auto AMT transmission families.

Hyundai's AURA highlights page identifies body style as Sedan and lists configurations E, S, Corporate, SX and SX(O). The features matrix's SX+ AMT annotation and highlights configuration list are not perfectly aligned; preserve the exact annotation as observed and flag the trim-label discrepancy rather than silently reconciling it.

## Price evidence and limitations

The official AURA price page currently displays a starting price of ₹5,99,990, but its variant-price table is blank in the captured page and it requires model, state, city, fuel type and transmission selection. The current model catalogue displays a broad ₹5.99–8.59 lakh range. These broad model-level figures are not assigned to individual variants. All variant price fields remain blank.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / engine and trim plan: https://www.hyundai.com/in/en/find-a-car/aura/features
- Current price selector: https://www.hyundai.com/in/en/find-a-car/aura/price
- Highlights / body style and configurations: https://www.hyundai.com/in/en/find-a-car/aura/highlights.html
- Hyundai India current model catalogue: https://www.hyundai.com/in/en/find-a-car
- Hyundai India homepage engine/transmission summary: https://www.hyundai.com/in/en


## Current official-source reconciliation — 2026-11-07

A fresh check of Hyundai India's live Aura pages confirms a trim-label discrepancy that must remain unresolved in the normalized variant table:

- The feature matrix still maps 1.2 l Kappa petrol manual to E, S, SX and SX(O); it annotates the AMT as SX+ under the SX column; and it maps Hy-CNG manual to S and SX.
- The current highlights page lists configurations E, S, Corporate, SX and SX(O).
- The current price page prose lists petrol-manual trims E, S, Corporate, SX and SX(O), says selected trims are available with AMT, and confirms multiple factory-fitted CNG variants. It does not expose the exact AMT/CNG trim mapping in the captured page. Its dynamic variant-price table remains blank.
- Hyundai's current Find-a-Car catalogue gives a model-level ex-showroom range of ₹5.99–8.59 lakh. This is not a variant price matrix and is not assigned to any row in `hyundai-aura-variant-structure.csv`.

Therefore, Corporate is now recorded as an OEM-listed configuration label, but no Corporate engine/fuel/transmission combination is added. The seven previously normalized combinations remain the only exact combinations directly supported by the feature matrix. SX+ remains an explicit OEM annotation requiring current configurator/dealer confirmation. All Aura variant price fields remain blank.

A third-party Autocar India page updated 28 October 2026 reports eight variants and additional trim/powertrain details, including Corporate as CNG-only. This is retained as a discrepancy lead only; it is not used to fill OEM gaps or approve variant facts.

Sources checked:
- https://www.hyundai.com/in/en/find-a-car/aura/features
- https://www.hyundai.com/in/en/find-a-car/aura/price
- https://www.hyundai.com/in/en/find-a-car/aura/highlights.html
- https://www.hyundai.com/in/en/find-a-car
- https://www.autocarindia.com/cars/hyundai/aura/variants/
