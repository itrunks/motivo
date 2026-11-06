# Toyota Legender powertrain normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-legender-powertrain-families.csv`: 3 official engine/transmission families.
- `data/toyota-legender-price-observations.csv`: one model-level starting price and two dated historical launch prices.
- No complete current grade-to-powertrain matrix is declared complete because the captured official sources do not provide exact current grade/drive pairings.

## Powertrain evidence

Toyota's official brochure exposes three specification columns: 2.8 l diesel 6AT, 2.8 l diesel 6MT with iMT, and 2.8 l diesel NeoDrive 48V 6AT. It identifies a 7-seat SUV and 2WD/4WD drive availability depending on configuration. Toyota's June 2, 2025 announcement confirms the NeoDrive 48V grade; the March 5, 2025 announcement confirms a 4x4 MT grade. The current showroom overview mainly describes the diesel AT model and does not establish a complete grade-to-drive mapping.

The three rows are powertrain families, not confirmed orderable retail variants. Do not cross-join all drive types and transmissions or invent trim names.

## Price evidence

Toyota's official range listing shows Legender from ₹42,92,000. This is a model-level starting price only. The 4x4 MT ₹46,36,000 and NeoDrive 48V ₹50,09,000 values are dated March/June 2025 launch observations and are not represented as current 2026 dealer prices.

## Status / next evidence needed

Capture current Toyota configurator or dealer grade-wise price list to confirm which current grades are orderable, the exact 2WD/4WD pairing, and current prices. Until then, retain powertrain-family observations only.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- Official Legender brochure: https://www.toyotabharat.com/documents/brochures/fortuner-mmc/legender-brochure-mobile.pdf
- Current Legender showroom: https://www.toyotabharat.com/showroom/fortuner/index-legender.html
- 4x4 MT launch: https://www.toyotabharat.com/news/2025/tkm-introduces-legender-4x4-in-all-new-manual-transmission-mt-grade.html
- NeoDrive 48V launch: https://www.toyotabharat.com/news/2025/tkm-launches-fortuner-and-legender-neo-drive-48v-variants.html
- Toyota official model range price: https://www.toyotabharat.com/showroom/prius/
