# Maruti Suzuki Grand Vitara normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-grand-vitara-variant-structure.csv`: 20 current grade/powertrain/drive configurations.
- `data/maruti-suzuki-grand-vitara-price-observations.csv`: 20 Delhi on-road price observations from the current variant listing.

## Current variant coverage

Autocar India's variant page was last updated 28 October 2026 and lists 20 variants. The current range includes naturally aspirated petrol, S-CNG, strong hybrid and ALLGRIP SELECT AWD configurations. The 20 exact combinations are preserved; the catalogue does not cross-product every grade with every engine or gearbox.

## Powertrain families

**1.5-litre K15C Smart Hybrid petrol**
- 1462 cc, 75.8 kW / 103.06 PS, 139 Nm.
- 5-speed manual or 6-speed torque-converter automatic.
- FWD, except the separate ALLGRIP configurations.

**1.5-litre K15C S-CNG**
- 1462 cc, 64.6 kW / 87.8 PS and 121.5 Nm in CNG mode.
- 5-speed manual only.
- FWD.

**1.5-litre Atkinson-cycle strong hybrid**
- 1490 cc petrol engine, 68 kW / 92.45 PS and 122 Nm.
- 85 kW / 115.56 PS total system output, lithium-ion battery, 177.6 V.
- e-CVT and FWD.

**ALLGRIP SELECT**
- Alpha and Alpha (O) use the 1.5-litre K15C Smart Hybrid petrol engine with 6-speed automatic and AWD.
- ALLGRIP is not assigned to the manual petrol or hybrid variants.

All variants are 5-seat mid-size SUVs.

## Price basis

All 20 amounts are **on-road Delhi INR** from Autocar India's 28 October 2026 variant page. The displayed range is ₹12.49 lakh to ₹22.77 lakh. These are not ex-showroom prices and must not be used as national or Tamil Nadu prices. On-road totals vary with RTO, insurance, dealer charges and offers.

NEXA's official price page states ex-showroom prices and notes that the final on-road amount varies by city. Its official FAQ gives ₹19,72,400 as the Alpha+ (O) strong-hybrid ex-showroom amount. That is a different price basis from the ₹22.77 lakh Autocar Delhi on-road observation.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible pages do not establish commercial reuse rights. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official Grand Vitara model/variant page: https://www.nexaexperience.com/grand-vitara
- NEXA official price page and FAQ: https://www.nexaexperience.com/grand-vitara/price
- NEXA official Grand Vitara brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/grand-vitara/sigma/documents/NEXA-Grand-Vitara-Brochure-old-3.pdf
- Autocar India, Grand Vitara 20-variant listing, last updated 28 October 2026: https://www.autocarindia.com/cars/maruti-suzuki/grand-vitara/variants
- Cars24 October 2026 price revision cross-check: https://www.cars24.com/news/auto/maruti-suzuki-grand-vitara-becomes-costlier-by-up-to-rs-10000-in-oct-2026/
