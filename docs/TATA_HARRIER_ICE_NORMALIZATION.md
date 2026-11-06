# Tata Harrier ICE 50-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/tata-harrier-ice-variant-price-observations.csv`: 50 unique variant rows with engine, fuel, transmission, displacement, power, torque, drivetrain, seating, body style and Delhi on-road price observations.

## Current variant coverage

Autocar India's current variant page was last updated 23 October 2026 and reports 50 variants. The listed grade/edition families include Smart, Pure X, Pure X Dark, Adventure X, Adventure X Dark, Adventure X+, Adventure X+ Dark, Fearless X, Fearless X Dark, Fearless X+, Fearless X+ Dark, Fearless Ultra, Fearless Ultra Stealth and Fearless Ultra Red Dark.

The 50 listed combinations are normalized as follows:

- 1.5-litre TGDi turbo-petrol: 1498 cc, 170 PS, 280 Nm; 6-speed manual or 6-speed torque-converter automatic.
- 2.0-litre Kryotec turbo-diesel: 1956 cc, 170 PS, 350 Nm; 6-speed manual or 6-speed torque-converter automatic.

The listing identifies each exact variant's fuel and transmission. All current Harrier variants are recorded as front-wheel drive, five-seat SUVs, consistent with the model specification page. Dark, Red Dark and Stealth labels remain separate OEM/publisher variant labels and are not merged into standard grades.

## Price basis

All 50 prices are **on-road Delhi INR** observations from the Autocar India variant page. The page reports a Delhi range of ₹15.09 lakh to ₹31.08 lakh and was last updated 23 October 2026. These are not ex-showroom prices and must not be used as prices for other cities. On-road amounts may vary by insurance, registration, dealer charges and offers.

## Evidence limitations

Autocar India is a secondary source. Tata's official product detail page was blocked in the earlier source audit, so this pass uses the current third-party variant listing for the exact 50-row trim/price matrix and official Tata brochure/specification material where available. The 2026 petrol engine figures are supported by the contemporary engine specification reporting; the 2.0-litre diesel figures are supported by Tata's official brochure. Confirm exact orderability and final invoice price with a Tata dealer before customer-facing use.

## Rights and import gate

All rows remain `review_required`; commercial reuse and redistribution remain `unknown`. Publicly accessible web content does not establish commercial reuse rights. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Autocar India, Tata Harrier 50-variant listing, last updated 23 October 2026: https://www.autocarindia.com/cars/tata/harrier/variants/
- Autocar India, Harrier 2026 specifications: https://www.autocarindia.com/cars/tata/harrier/specifications
- 2026 Harrier petrol engine figures and launch details: https://www.autocarindia.com/car-news/new-tata-harrier-petrol-price-starts-at-rs-1289-lakh-438590
- 2026 Harrier engine/transmission matrix and outputs: https://www.v3cars.com/news/2026-tata-harrier-variant-wise-engine-transmission-options
- Tata Harrier official 2.0-litre diesel brochure: https://tatamotors-prod.adobecqms.net/content/dam/tml/pv/products/harrier/year-2025/ice/promoting-vc/brochure/january/harrier-dark-brochure-jan.pdf
