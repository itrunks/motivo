# Hyundai EXTER variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/hyundai-exter-variant-price-normalization.csv`: 15 exact price rows from Hyundai's 2026 launch announcement.
- `data/hyundai-exter-variant-structure.csv`: 19 trim/powertrain/transmission combinations from the current Hyundai India features matrix.

## Current OEM feature matrix

The current features page lists HX 2, HX 3, HX 4, HX 4+, HX 6, HX 6 Knight, HX 8, HX 10 and HX 10 Knight.

Petrol 1.2 l Kappa applicability:
- HX 2: MT
- HX 3: MT / AMT
- HX 4: MT
- HX 4+: AMT
- HX 6: MT / AMT
- HX 6 Knight: MT / AMT
- HX 8: MT / AMT
- HX 10: AMT
- HX 10 Knight: AMT

Bi-fuel 1.2 l Kappa petrol+CNG applicability:
- HX 2, HX 3, HX 4, HX 6, HX 6 Knight and HX 8: MT

## Price evidence

Hyundai's 2026 launch announcement publishes 15 ex-showroom INR rows:
- Petrol MT: HX 2, HX 3, HX 4, HX 6, HX 8
- Petrol AMT: HX 3, HX 4+, HX 6, HX 8, HX 10
- Petrol+CNG MT: HX 2, HX 3, HX 4, HX 6, HX 8

Displayed price range: ₹5,79,900–₹9,41,900.

The current official catalogue currently displays a rounded model range of ₹5.80–9.41 lakh. The detailed price table is in a dated launch announcement; the exact price effective date is not explicitly captured in the announcement excerpt. Therefore these values are recorded as OEM launch-price observations, not guaranteed current city-specific dealer prices.

## Reconciliation and gaps

The current feature matrix includes HX 6 Knight and HX 10 Knight, while the launch price table does not include separate Knight Edition price rows. No Knight price is inferred. The 19-row structure matrix and 15-row price matrix intentionally remain separate; they are not merged into invented price rows.

Body style is recorded as SUV based on Hyundai's official model listing. Model year is blank because the OEM pages do not provide an explicit model-year field in the captured evidence.

## Rights and import gate

The source registry remains `review_required`; commercial reuse and redistribution are `unknown`. Public OEM pages are not proof of commercial reuse permission. These CSVs are research/normalization outputs, not approved import manifests. No Firestore write or publication has been performed.
