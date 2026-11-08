# Kia Seltos variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/kia-seltos-variant-structure.csv`: 44 trim/powertrain combinations from Kia India's current comparison matrix.
- `data/kia-seltos-price-observations.csv`: 12 trim-level MSRP observations.

## Current comparison-matrix mapping

The comparison page lists HTE, HTE(O), HTK, HTK(O), HTX, HTX(A), GTX, X-Line, GTX(A), X-Line(A), GTX(O), X-Line(O).

- Smartstream G1.5 Petrol 6MT: HTE, HTE(O), HTK, HTK(O), HTX, HTX(A) — 6 rows.
- Smartstream G1.5 Petrol IVT: HTE(O), HTK, HTK(O), HTX, HTX(A), GTX, X-Line, GTX(A), GTX(O) — 9 rows.
- Smartstream G1.5 T-GDi Petrol 7DCT: HTK(O), HTX, HTX(A), GTX, X-Line, GTX(A), X-Line(A), GTX(O), X-Line(O) — 9 rows.
- 1.5 l CRDi VGT Diesel 6MT: HTE, HTE(O), HTK, HTK(O), HTX, HTX(A) — 6 rows.
- 1.5 l CRDi VGT Diesel 6AT: HTE(O), HTK, HTK(O), HTX, HTX(A), GTX, X-Line, GTX(A), X-Line(A), GTX(O), X-Line(O) — 11 rows.

Total: 44 exact trim/powertrain combinations. The current official comparison matrix explicitly maps Smartstream G1.5 T-GDi 6iMT to HTE(O), HTK and HTK(O). These three rows are now included; no 6iMT rows are inferred for HTX, HTX(A), GTX, X-Line, GTX(A), X-Line(A), GTX(O) or X-Line(O). The prior ambiguity is resolved by the matrix itself.

## 6iMT mapping closure

The current official comparison matrix and 2026 brochure both show 6iMT availability for HTE(O), HTK and HTK(O), and not-included for the other nine trim columns. The three exact combinations have been added to the structure CSV. The 12 trim-level price observations remain separate; no price is copied onto a specific 6iMT configuration because Kia does not provide a powertrain-specific price in the captured matrix.

## Price observations

Current comparison-page values: HTE ₹11,24,900; HTE(O) ₹12,41,900; HTK ₹13,41,900; HTK(O) ₹14,51,900; HTX ₹15,91,900; HTX(A) ₹17,01,900; GTX ₹18,71,900; X-Line ₹18,71,900; GTX(A) ₹19,81,900; X-Line(A) ₹19,81,900; GTX(O) ₹21,56,900; X-Line(O) ₹21,56,900.

The showroom FAQ separately states HTE at ₹10,99,900, while the comparison page shows ₹11,24,900. The price CSV preserves the comparison-page value; this discrepancy is documented, not silently merged. Prices are trim-level and are not copied to each powertrain row. No effective date is inferred.

Kia identifies Seltos as a 5-seater compact SUV. Model year remains blank because no per-trim model-year field is exposed.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- https://www.kia.com/in/our-vehicles/seltos/specs/compare-trims.html
- https://www.kia.com/in/our-vehicles/seltos/showroom.html
- https://www.kia.com/in/our-vehicles/seltos/specs.html
