# Tata Nexon current powertrain families — normalization checkpoint

Checked: 2026-11-06

## Deliverables

- `data/tata-nexon-powertrain-families.csv`: 7 engine/transmission families.
- `data/tata-nexon-price-observations.csv`: model-level ex-showroom range only.
- Full 63-variant trim/edition matrix remains incomplete.

## Powertrain families

Autocar's current 2026 variant matrix lists 63 variants across Smart, Smart+, Smart+ S, Pure+, Pure+ S, Pure+ PS, Creative, Creative+ S, Creative+ PS and Fearless+ PS families, plus Dark, Red Dark and Camo editions.

The powertrain combinations are:
- 1.2 l turbo-petrol: 5MT, 6MT, 6AMT and 7DCT.
- 1.2 l CNG: 6MT only.
- 1.5 l diesel: 6MT and 6AMT.

The model is a 5-seat compact SUV. The official Tata page and Autocar specify 120 PS petrol, 100 PS CNG and 115 PS diesel; exact grade-to-combination mapping is not fully captured in the current official configurator, so this file preserves families only.

## Price scope

V3Cars lists ex-showroom range ₹7,40,000–₹14,52,000, updated July 2, 2026. These are model-level range observations only, not grade prices. Autocar's October 30, 2026 page lists 63 variants and confirms the 2026 matrix. Do not infer variant prices from the model range.

## Next evidence needed

Capture the full 63-row grade/engine/gearbox/edition mapping from Tata's configurator or a complete official price list, then reconcile it against the Autocar variant list. Preserve Dark, Red Dark and Camo editions as distinct OEM labels.

## Rights

Source status `review_required`; commercial reuse and redistribution `unknown`. No Firestore write or publication performed.

## Sources

- Tata official Nexon model page: https://tatamotors-prod.adobecqms.net/nexon/ice.html
- Autocar India 63-variant list and powertrain matrix: https://www.autocarindia.com/cars/tata/nexon/variants
- V3Cars ex-showroom price range: https://www.v3cars.com/tata-cars/nexon
