# Kia Syros variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/kia-syros-variant-structure.csv`: 17 trim/powertrain combinations from Kia India's current comparison matrix.
- `data/kia-syros-price-observations.csv`: 7 trim-level MSRP observations.

## Powertrain mapping

- Smartstream G1.0 T-GDi Petrol 6MT: HTE, HTE(O), HTK(EX), HTK+, HTK+(O) — 5 rows.
- Smartstream G1.0 T-GDi Petrol 7DCT: HTK+, HTK+(O), HTX, HTX(O) — 4 rows.
- 1.5 l CRDi VGT Diesel 6MT: HTE(O), HTK(EX), HTK+, HTK+(O) — 4 rows.
- 1.5 l CRDi VGT Diesel 6AT: HTK+, HTK+(O), HTX, HTX(O) — 4 rows.

Total 17. Kia's 2026 brochure confirms these engine and transmission families. Syros is a 5-seater compact SUV. No model-year is inferred.

## Price observations

HTE ₹8,41,900; HTE(O) ₹9,21,900; HTK(EX) ₹9,81,900; HTK+ ₹10,75,900; HTK+(O) ₹12,01,900; HTX ₹14,01,900; HTX(O) ₹14,99,900. These are trim-level MSRP observations, not engine/gearbox-specific prices, so they remain separate from structure rows. Effective date is not stated.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- https://www.kia.com/in/our-vehicles/syros/specs/compare-trims.html
- https://www.kia.com/in/our-vehicles/syros/specs.html
- https://www.kia.com/in/our-vehicles/syros/showroom.html
- https://www.kia.com/content/dam/kia2/in/en/our-vehicles/syros/KiaSyrosBrochure2026-M.pdf
