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


## Current Legender showroom recheck — 2026-11-07

The current Toyota Legender showroom page now provides a clear configuration table with three current diesel configurations:

| Current configuration | Engine | Transmission | Drive | Seats |
|---|---|---|---|---:|
| Legender 4x4 MT | 2.8 L 1GD-FTV diesel, 150 kW/204 PS, 420 Nm | 6MT with iMT | 4WD | 7 |
| Legender 4x2 AT | 2.8 L 1GD-FTV diesel, 150 kW/204 PS, 500 Nm | 6AT | 2WD | 7 |
| Legender 4x4 AT | 2.8 L 1GD-FTV diesel, 150 kW/204 PS, 500 Nm | 6AT | 4WD | 7 |

This supersedes the previous generic brochure interpretation that allowed 2WD/4WD for all three powertrain families. The current showroom explicitly maps 4x4 MT, 4x2 AT and 4x4 AT. It does not expose retail grade names beyond those configuration labels.

The current showroom page's EMI calculator states that price is unavailable and asks customers to check with the nearest dealer. The old ₹42,92,000 model-starting-price record was linked to a Prius showroom URL, not a Legender-specific source; it is now quarantined as a source-scope mismatch. The March 2025 4x4 MT and June 2025 NeoDrive 48V prices remain historical launch observations, not current prices.

The current Legender showroom page no longer lists the NeoDrive 48V powertrain. Keep the 2025 NeoDrive 48V launch as a separate historical family; do not merge it into current orderable configurations. Current price and grade mapping remain incomplete pending a dealer-specific Toyota price list.

Current source:
- https://www.toyotabharat.com/showroom/fortuner/index-legender.html
