# Tata Harrier current powertrain families — normalization checkpoint

Checked: 2026-11-06

## Deliverables

- `data/tata-harrier-powertrain-families.csv`: 4 confirmed engine/transmission families.
- `data/tata-harrier-price-observations.csv`: model-level ex-showroom price range from V3Cars.
- Full trim-level matrix remains incomplete: Autocar currently lists 49 variants and the current grade/edition mapping has not yet been reconciled row by row.

## Current powertrain families

The current 2026 Harrier lineup uses two 170 hp engines: 1.5 l Turbo-GDI petrol (1498 cc, 280 Nm) and 2.0 l Kryotec diesel (1956 cc, 350 Nm). Both are offered with 6-speed manual and 6-speed torque-converter automatic transmissions. The vehicle is a 5-seat SUV.

## Price scope

V3Cars lists ex-showroom prices from ₹12,99,990 to ₹26,10,990, updated July 2, 2026. This is model-level range only; no individual trim prices are copied into the catalogue until the 49-variant list is reconciled against the current Tata configurator. Autocar's Delhi on-road price range is a separate city-specific basis and is not mixed with ex-showroom prices.

## Next evidence needed

Reconcile the full 49-row current trim list (Smart, Pure X, Adventure X, Fearless X, Ultra, Dark/Red Dark/Stealth editions) against the Tata official configurator and capture exact engine/gearbox fitment for every row. Keep editions distinct where the OEM does.

## Rights

Source status `review_required`; commercial reuse and redistribution `unknown`. No Firestore write or publication performed.

## Sources

- Tata official Harrier model page: https://cars.tatamotors.com/suv/harrier.html
- Autocar India current 49-variant list: https://www.autocarindia.com/cars/tata/harrier
- V3Cars ex-showroom price list: https://www.v3cars.com/tata-cars/harrier
