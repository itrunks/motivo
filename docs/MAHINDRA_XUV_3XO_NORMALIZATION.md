# Mahindra XUV 3XO normalization

Checked: 2026-11-06

## Deliverables

- `data/mahindra-xuv-3xo-variant-structure.csv`: 31 current variants from Autocar India's 30 October 2026 listing.
- `data/mahindra-xuv-3xo-onroad-price-observations.csv`: 31 city-specific Fatehabad on-road prices.
- `data/mahindra-xuv-3xo-oem-selector-price-observations.csv`: 18 current Mahindra selector ex-showroom price cards (8 petrol, 6 diesel, 4 CNG).

## Current variant coverage

Autocar India lists 31 variants across 11 trims, from MX1 to AX7 Luxury. The current range includes MX1, MX2, MX3, MX3 Pro, REVX M, REVX M (O), REVX Edge, REVX Edge (O), MX Edge, AX5, REVX A, AX5 Luxury, AX7 and AX7 Luxury grade families. The 31 rows preserve the exact fuel and transmission combinations displayed in the current listing.

The official Mahindra selector exposes additional grade codes and fuel filters. Its captured cards provide 18 exact ex-showroom prices, but the names do not map one-to-one to every Autocar variant row. These official price observations are stored separately; no guessed crosswalk is applied.

## Powertrain families

- 1.2-litre mStallion turbo-petrol MPFi: 1197 cc, 82 kW / 111.5 PS, 200 Nm; 6-speed manual or 6-speed torque-converter automatic.
- 1.2-litre mStallion TGDi turbo-petrol: 1197 cc, 96 kW / 130.5 PS, 230 Nm; 6-speed manual or 6-speed torque-converter automatic.
- 1.2-litre turbo-petrol bi-fuel CNG: 1197 cc, 85 kW / 115.6 PS, 230 Nm; 6-speed manual.
- 1.5-litre mHawk diesel: 1497 cc, 85.8 kW / 116.7 PS, 300 Nm; 6-speed manual or 6-speed AMT.

All captured variants are front-wheel-drive, 5-seat compact SUVs. The CNG configuration is a factory-fitted twin-cylinder bi-fuel system. The TGDi and MPFi petrol engines remain separate.

## Price evidence and basis

**Autocar secondary source:** 31 on-road Fatehabad INR observations, last updated 30 October 2026. Displayed range ₹8.69 lakh to ₹17.45 lakh. These are not ex-showroom or national prices.

**Mahindra OEM selector:** 18 ex-showroom observations:
- Petrol cards: AX7 L TGDi ₹15,03,500; MX3 ₹10,84,900; MX2 Pro ₹9,99,500; REVX A ₹12,39,500; AX5 ₹11,88,000; AX5 L TGDi ₹13,27,500; MX3 Pro ₹11,13,000; AX7 TGDi ₹13,34,000.
- Diesel cards: REVX Edge ₹10,59,000; AX7 L ₹14,07,500; AX5 ₹11,39,500; REVX Edge (O) ₹11,09,000; AX7 ₹13,03,500; MX2 ₹9,36,000.
- CNG cards: AX5 ₹11,19,000; REVX A ₹12,27,000; REVX Edge (O) ₹10,79,000; MX Edge ₹9,99,000.

The two price sets remain separate because they have different bases, variant labels and coverage. The OEM selector states that prices at delivery prevail and that its prices are indicative. Confirm current dealer invoice and exact selector-to-trim mapping before production import.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra official XUV 3XO variant selector: https://auto.mahindra.com/own-online/variant-selection?pid=X3XO
- Mahindra official REVX EDGE launch release, 18 September 2026: https://www.mahindra.com/news-room/press-release/en/mahindra-expands-xuv-3xo-revx-line-up-introduces-xuv-3xo-revx-edge-with-a-starting-price-of-rupees-9.39-lakh
- Autocar India, XUV 3XO 31-variant listing, last updated 30 October 2026: https://www.autocarindia.com/cars/mahindra/xuv-3xo/variants/
- Mahindra official XUV 3XO brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw3c3f0b8a/xuv-3xo/brochure/xuv-3xo-brochure.pdf
