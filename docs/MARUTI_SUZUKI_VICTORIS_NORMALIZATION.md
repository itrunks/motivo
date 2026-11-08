# Maruti Suzuki Victoris normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-victoris-variant-structure.csv`: 21 current grade/powertrain/drive configurations.
- `data/maruti-suzuki-victoris-price-observations.csv`: 21 official Maruti Suzuki ex-showroom price observations.

## Current variant coverage

The official Maruti Suzuki Victoris price page lists 21 current configurations across petrol, S-CNG, strong hybrid and ALLGRIP SELECT AWD. The structure file preserves the actual published combinations and does not create missing cross-products.

## Powertrain families

**1.5-litre K15C Smart Hybrid petrol**
- 1462 cc, 75.8 kW / 103.06 PS, 139 Nm.
- 5-speed manual or 6-speed torque-converter automatic.
- FWD or ALLGRIP SELECT AWD depending on grade.

**1.5-litre K15C S-CNG**
- 1462 cc, 64.6 kW / 87.8 PS and 121.5 Nm in CNG mode.
- 5-speed manual only.
- FWD.

**1.5-litre Atkinson-cycle strong hybrid**
- 1490 cc petrol engine, 68 kW / 92.45 PS and 122 Nm.
- 85 kW / 115.56 PS total system output, lithium-ion battery, 177.6 V.
- e-CVT and FWD.

All variants are 5-seat compact SUVs. Strong-hybrid engine output and total system output are stored separately; they are not added together.

## Price basis

All 21 values are official Maruti Suzuki ex-showroom INR observations from the current Victoris price page. The displayed range is ₹10,49,900 to ₹19,98,900. Maruti's page states that invoice-date prices and applicable schemes prevail. These are ex-showroom values, not on-road prices.

The October 29, 2026 Cars24 report confirms the only recent price revision was to selected ZXi+ variants; strong-hybrid prices remained unchanged. The official page values captured on 6 November are used as the current price observations.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Victoris price page: https://www.marutisuzuki.com/arena/victoris/price
- Maruti Suzuki official Victoris model page: https://www.marutisuzuki.com/arena/Victoris
- Maruti Suzuki official Victoris brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/victoris/documents/Arena-Victoris-Brochure-Mobile.pdf
- Maruti Suzuki introductory full price list: https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Press_Release_Maruti_Suzuki_announces_introductory_prices_for_the_VICTORIS_starting_at_%E2%82%B9_1049900.pdf
- Cars24, October 29 2026 Victoris price update: https://www.cars24.com/news/auto/maruti-suzuki-victoris-price-list-updated-in-october-2026/
