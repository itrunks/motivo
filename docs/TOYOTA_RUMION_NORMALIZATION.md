# Toyota Rumion variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-rumion-variant-structure.csv`: 8 grade/powertrain combinations from the current showroom and official grade announcements.
- `data/toyota-rumion-price-observations.csv`: 4 current showroom price observations and one dated historical G-AT launch price.

## Current variant structure

The current showroom and official launch announcements support:
- Petrol NeoDrive: E MT, S MT, S AT, G MT, G AT, V MT, V AT.
- E-CNG: S MT.

All configurations use the 1.5 l K-Series petrol engine family; CNG is bi-fuel Petrol+CNG. Petrol NeoDrive offers 5-speed manual and 6-speed automatic. The MPV has 7 seats. The official 2024 G-AT announcement confirms the automatic grade and reopening of E-CNG bookings. The current showroom's E MT grade is retained as a current variant, although the original 2023 launch brochure did not include it.

## Price observations

The current showroom page displays E MT ₹9,79,000; S MT ₹10,77,000; S MT CNG ₹11,69,000; G MT ₹11,93,000. It does not state an effective date or tax basis in the extracted price list. G AT ₹13,00,000 is from the dated April 29, 2024 launch announcement and is historical only. Prices for S AT, V MT and V AT were not captured from a current official numeric price table; no prices are inferred.

Toyota's current model range page lists Rumion from ₹9,79,000. This agrees with the current showroom E MT value, but the model-level range is not used to fill missing grade prices.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- Current showroom / grade and displayed price list: https://www.toyotabharat.com/showroom/rumion/index.html
- Official 2024 G-AT grade launch: https://www.toyotabharat.com/news/2024/tkm-introduces-new-grade-of-the-toyota-rumion.html
- Original launch and powertrain options: https://www.toyotabharat.com/news/2023/tkm-launches-the-all-new-toyota-rumion-the-prestigious-family-car-with-an-mpv-lineage.html
- Official brochure: https://www.toyotabharat.com/documents/brochures/e-brochure-rumion.pdf
