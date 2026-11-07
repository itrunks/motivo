# Tata Safari current powertrain families — normalization checkpoint

Checked: 2026-11-06

## Deliverables

- `data/tata-safari-powertrain-families.csv`: 4 confirmed engine/transmission families.
- `data/tata-safari-price-observations.csv`: model-level ex-showroom price range from V3Cars.
- Full trim-level matrix remains incomplete: Autocar lists 64 current variants across 6/7-seat, engine, gearbox and edition combinations.

## Current powertrain families

The 2026 Safari uses two 170 hp engines: 1.5 l Turbo-GDI petrol (1498 cc, 280 Nm) and 2.0 l Kryotec diesel (1956 cc, 350 Nm). Both are offered with 6-speed manual and 6-speed torque-converter automatic transmissions. Safari is a 6/7-seat SUV; exact seat count is trim-specific and is not inferred in the family file.

## Price scope

V3Cars lists ex-showroom prices from ₹13,39,000 to ₹26,90,000, updated July 2, 2026. This is model-level range only. Autocar's October 2026 listing shows 64 variants and a different Delhi on-road price range; the two bases are not mixed.

## Next evidence needed

Reconcile all 64 trim/engine/gearbox/seating combinations against the current Tata configurator and capture current ex-showroom prices. Special editions (Dark, Red Dark, Stealth) remain distinct where the OEM names them.

## Rights

Source status `review_required`; commercial reuse and redistribution `unknown`. No Firestore write or publication performed.

## Sources

- Tata official Safari model page: https://cars.tatamotors.com/suv/safari.html
- Autocar India 64-variant list: https://www.autocarindia.com/cars/tata/safari/variants
- V3Cars ex-showroom price list: https://www.v3cars.com/tata-cars/safari
