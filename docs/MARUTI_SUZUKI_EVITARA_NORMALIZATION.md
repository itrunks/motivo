# Maruti Suzuki e VITARA normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-evitara-variant-structure.csv`: three India-market battery/grade configurations.
- `data/maruti-suzuki-evitara-price-observations.csv`: three dated ex-showroom observations plus one separate official BaaS starting-price observation.

## Current India variants

The India-specific NEXA brochure and product page list three grades:
- Delta: 48.8 kWh LFP pack, 105.8 kW motor, 193 Nm, 440 km ARAI range.
- Zeta: 61.1 kWh LFP pack, 128 kW motor, 193 Nm, 543 km ARAI range.
- Alpha: same 61.1 kWh powertrain as Zeta, with higher equipment.

All are single-motor, 2WD, single-speed electric SUVs with five seats. The official India brochure is used for battery, motor and range values; no international-market variants or specifications are imported into this dataset.

## Price evidence and BaaS separation

The current NEXA page links to a configurator and price flow, but the numeric current variant-price cells were not extractable in this review. The price file therefore records dated August 2026 secondary-source ex-showroom observations:
- Delta 49 kWh ₹16,19,000
- Zeta 61 kWh ₹17,94,000 (increased ₹15,000 in August)
- Alpha 61 kWh ₹19,99,000 (unchanged in August)

The official February 2026 launch release separately advertises a BaaS entry price of ₹10,99,000 plus ₹3.99/km battery subscription. This is a vehicle upfront price with a battery rental model, not a full-ownership ex-showroom price. It is stored as a model-level BaaS observation and is not assigned to a particular grade.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official e VITARA model page: https://www.nexaexperience.com/e-vitara
- NEXA official e VITARA price/configurator page: https://www.nexaexperience.com/e-vitara/price
- Maruti Suzuki India-specific e VITARA 2026 brochure: https://marutisuzuki.scene7.com/is/content/maruti/NEXA-eVITARA-Brochure-2026pdf
- Maruti Suzuki official February 2026 launch and BaaS announcement: https://www.marutisuzuki.com/content/dam/arena-eds/corporate/press-release/assets/documents/2026/february/Press_Release_India_Goes_Electric_with_Maruti_Suzuki_e_VITARA.pdf
- Autocar India e VITARA current three-variant summary: https://www.autocarindia.com/cars/maruti-suzuki/e-vitara
- Cars24 August 2026 e VITARA price revision: https://www.cars24.com/news/auto/maruti-suzuki-evitara-price-revised-in-august-2026-check-variant-wise-hike/
