# Kia Sonet variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/kia-sonet-variant-structure.csv`: 24 exact trim/powertrain/transmission combinations from Kia India's current trim comparison.
- `data/kia-sonet-price-observations.csv`: 8 trim-level ex-showroom/MSRP observations. HTK price is not rendered and remains missing.

## Current engine and transmission mapping

The official Kia comparison page exposes nine trim columns: HTE, HTE(O), HTK, HTK(O), HTK+, HTK+(O), HTX, GTX+ and X-Line.

The powertrain matrix maps:
- Smartstream G1.2 Petrol 5MT: HTE, HTE(O), HTK, HTK(O), HTK+, HTK+(O) — 6 combinations.
- Smartstream G1.0 T-GDi Petrol 6iMT: HTK(O), HTK+(O) — 2 combinations.
- Smartstream G1.0 T-GDi Petrol 7DCT: HTK(O), HTK+(O), HTX, GTX+, X-Line — 5 combinations.
- 1.5 l CRDi VGT Diesel 6MT: HTE(O), HTK(O), HTK+, HTK+(O), HTX — 5 combinations.
- 1.5 l CRDi VGT Diesel 6AT: HTE(O), HTK(O), HTK+, HTK+(O), HTX, GTX+ — 6 combinations.

Total: 24 exact trim/powertrain combinations. The Kia showroom page confirms three engine families and multiple transmissions (5MT, 6MT, 6iMT, 7DCT, 6AT). The current Kia brochure also confirms these powertrain families. The showroom identifies the Sonet as a compact SUV.

## Price observations

The current trim comparison page displays:
- HTE ₹7,44,900
- HTE(O) ₹7,87,900
- HTK: no price rendered
- HTK(O) ₹8,88,900
- HTK+ ₹9,27,900
- HTK+(O) ₹9,75,900
- HTX ₹11,59,900
- GTX+ ₹13,74,900
- X-Line ₹13,88,900

The page labels these as starting MSRP; Kia's FAQ describes the Sonet starting price as all-India ex-showroom. Since the price heading is trim-level and does not identify a particular engine/transmission, the observations are kept in a separate file and are not copied onto each powertrain combination. HTK remains blank because no price is shown. No price effective date is inferred.

An earlier workqueue snapshot contains older prices from before the current comparison page values; the current fetched comparison page is used for this checked snapshot. The historical observations are not merged with current values.

## Model-year note

No explicit model-year value is assigned to individual trim/powertrain rows because the current comparison page does not provide a retail model-year field.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. These CSVs are research/normalization outputs, not approved import manifests. No Firestore write or publication has been performed.

## Sources

- Kia Sonet trim comparison / powertrain mapping and prices: https://www.kia.com/in/our-vehicles/sonet/specs/compare-trims.html
- Kia Sonet showroom / engine and transmission summary: https://www.kia.com/in/our-vehicles/sonet/showroom.html
- Kia Sonet specifications: https://www.kia.com/in/our-vehicles/sonet/specs.html
- Kia 2026 Sonet brochure: https://www.kia.com/content/dam/kia2/in/en/our-vehicles/showroom/sonet/brochure/Sonet_Wild_Reborn_Brochure_2026_Mobile.pdf
