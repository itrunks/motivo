# Tata Altroz ICE 27-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-altroz-ice-variant-price-observations.csv`: 27 unique current variant rows with exact displayed trim/powertrain labels, fuel, gearbox, engine, displacement, power, torque, drivetrain, seating, Balod on-road price and source metadata.

## Current variant coverage

Autocar India's current variant page was last updated 3 November 2026 and lists 27 variants across Smart, Pure, Pure S, Creative, Creative S, Accomplished S and Accomplished+ S.

The rows preserve the exact petrol, petrol-CNG and diesel combinations shown by the listing. Petrol is available with manual, AMT and DCA; CNG is available with manual and AMT; diesel is manual-only in this current listing. The DCA is not merged with the AMT.

## Powertrain families

- 1.2-litre naturally aspirated Revotron petrol: 1199 cc, 88 PS, 115 Nm; 5-speed manual, 5-speed AMT or 6-speed DCA.
- 1.2-litre Revotron iCNG bi-fuel: 1199 cc, 73.5 PS and 103 Nm in CNG mode; 5-speed manual or 5-speed AMT.
- 1.5-litre turbocharged Revotorq diesel: 1497 cc, 90 PS, 200 Nm; 5-speed manual.

All variants are recorded as front-wheel-drive, 5-seat premium hatchbacks.

## Price basis

All 27 prices are **on-road Balod INR** observations from Autocar India's variant page. The displayed range is ₹6.52 lakh to ₹12.48 lakh. These are not ex-showroom prices and are not Delhi, Chennai or Tamil Nadu prices. Local on-road amounts vary with RTO, insurance, registration, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source for the current 27-row trim and on-road price matrix. Tata's official May 2025 launch release and product note support the three powertrain families and transmission options. The current OEM configurator should be used to confirm orderability and a local dealer quote before production/customer use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible pages do not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Altroz 27-variant listing, last updated 3 November 2026: https://www.autocarindia.com/cars/tata/altroz/variants
- Tata Motors, May 22, 2025 all-new Altroz launch and powertrain options: https://static-assets.tatamotors.com/Production/www-tatamotors-com-NEW/wp-content/uploads/2025/05/PR_TML-launches-All-New-Altroz.pdf
- Tata Motors, all-new Altroz product note and technical specifications: https://static-assets.tatamotors.com/Production/www-tatamotors-com-NEW/wp-content/uploads/2025/05/All-New-Altroz-Product-Note.pdf
