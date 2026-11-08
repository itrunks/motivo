# Mahindra Thar ROXX normalization

Checked: 2026-11-06

## Deliverable

- `data/mahindra-thar-roxx-variant-price-observations.csv`: 21 current variant/powertrain/drive combinations with Delhi on-road prices.

## Current variant coverage

Autocar India's current variant page was last updated 2 November 2026 and lists 21 variants across MX1, MX3, MX5, AX3L, Star Edition, AX5L and AX7L. The 21 rows include the petrol/diesel, manual/automatic and 2WD/4WD combinations actually listed.

Mahindra's online selector exposes additional Mocha interior codes for selected AX7L and MX5 combinations. Mocha is an interior option code, not a separate engine or drivetrain variant, so it is not cross-producted into the 21 mechanical rows. Star Edition is a distinct edition and remains a separate variant family.

## Powertrain families

- 2.0-litre mStallion TGDi turbo-petrol: 1997 cc, 130 kW / 177 PS, 380 Nm; 6-speed manual or 6-speed torque-converter automatic; RWD in the listed petrol configurations.
- 2.2-litre mHawk turbo-diesel, 2WD tune: 2198 cc, 111.9 kW / 152 PS, 330 Nm; 6-speed manual or automatic.
- 2.2-litre mHawk turbo-diesel, 4WD tune: 2198 cc, 128.6 kW / 175 PS, 370 Nm; 6-speed manual or automatic.

All variants are 5-seat, 5-door lifestyle SUVs. The diesel 2WD and 4WD output tunes are kept distinct. The official selector's Mocha interior options and Star Edition codes are not confused with powertrain names.

## Price basis

All 21 values are **on-road Delhi INR** observations from Autocar India, last updated 2 November 2026. The displayed range is ₹14.53 lakh to ₹28.00 lakh. These are not ex-showroom or national prices.

Mahindra's official online selector provides ex-showroom prices for individual codes, but the full current 21-row mapping was not captured in one selector response. The Autocar Delhi on-road table is therefore the complete current comparison set; it is not merged with partial OEM ex-showroom cards.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra official Thar ROXX variant selector: https://auto.mahindra.com/own-online/variant-selection?pid=TH5D
- Mahindra official Thar ROXX product page: https://auto.mahindra.com/suv/thar-roxx
- Mahindra official Thar ROXX brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw3f4e8d8a/thar-roxx/brochure/thar-roxx-brochure.pdf
- Autocar India, Thar ROXX 21-variant listing, last updated 2 November 2026: https://www.autocarindia.com/cars/mahindra/thar-roxx/variants
- V3Cars, October 2026 Thar ROXX price revision: https://www.v3cars.com/news/oct-2026-mahindra-thar-roxx-price-change
