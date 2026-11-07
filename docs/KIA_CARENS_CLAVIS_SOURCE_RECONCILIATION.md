# Kia Carens Clavis normalization — partial, unknown column quarantined

Checked: 2026-11-06

## Deliverables

- `data/kia-carens-clavis-variant-structure.csv`: 28 exact powertrain/seating configurations for the 11 named grades whose columns are identifiable in the current Kia comparison matrix.
- `data/kia-carens-clavis-price-observations.csv`: 11 named trim-level MSRP observations. The unnamed comparison column has no numeric price and is not assigned.

## Named showroom grades and configuration mapping

The current Kia showroom page lists these 11 named grade families: HTE, HTE(O), HTE(EX), HTK+, HTK+(O), HTX, HTX(O), HTX+, GTX, GTX+ and X-Line. It also presents HTE CNG and HTE(O) CNG as separate showroom cards; the comparison matrix maps CNG 6MT availability under HTE and HTE(O), so those are captured as powertrain configurations, not fabricated new trim names.

The current compare matrix's 11 named columns map to the following combinations. The structure CSV contains 28 rows, including the 6-seat DCT derivative under HTX+:

- HTE: Smartstream G1.5 petrol 6MT; Smartstream G1.5 CNG 6MT.
- HTE(O): Smartstream G1.5 petrol 6MT; Smartstream G1.5 CNG 6MT; Smartstream G1.5 T-GDi petrol 7DCT and 6MT; 1.5L CRDi VGT diesel 6AT and 6MT.
- HTE(EX): Smartstream G1.5 petrol 6MT; Smartstream G1.5 T-GDi petrol 7DCT and 6MT; 1.5L CRDi VGT diesel 6MT.
- HTK+: Smartstream G1.5 T-GDi petrol 7DCT; 1.5L CRDi VGT diesel 6AT and 6MT.
- HTK+(O): Smartstream G1.5 T-GDi petrol 7DCT and 6MT; 1.5L CRDi VGT diesel 6MT.
- HTX: Smartstream G1.5 T-GDi petrol 7DCT; 1.5L CRDi VGT diesel 6MT.
- HTX(O): Smartstream G1.5 T-GDi petrol 7DCT.
- GTX: Smartstream G1.5 T-GDi petrol 7DCT.
- HTX+: Smartstream G1.5 T-GDi petrol 7DCT (6- and 7-seat), 6iMT and 6MT.
- GTX+: Smartstream G1.5 T-GDi petrol 7DCT.
- X-Line: Smartstream G1.5 T-GDi petrol 7DCT.

Kia's current showroom identifies the 6-seat captain-seat option under HTX+; the comparison matrix marks 6-seater as included for DCT only in that column. The 7-seat configuration remains listed separately.

## Unnamed comparison column — still unresolved

The comparison page contains a twelfth column after HTE(EX) whose header is blank in the captured page text and whose price renders only as the currency symbol. The matrix indicates 7DCT for that column but no other listed powertrain. It is not mapped to any of the named showroom grades and is excluded from the normalized structure and price CSVs. The model remains partial until Kia exposes the missing grade label and numeric price.

## Price observations

The current comparison page shows these trim-level starting MSRP values:

| Grade | Starting MSRP |
|---|---:|
| HTE | ₹11,38,900 |
| HTE(O) | ₹12,34,900 |
| HTE(EX) | ₹12,85,900 |
| HTK+ | ₹16,43,900 |
| HTK+(O) | ₹16,41,900 |
| HTX | ₹19,00,900 |
| HTX(O) | ₹19,61,900 |
| GTX | ₹19,99,900 |
| HTX+ | ₹19,03,900 |
| GTX+ | ₹21,78,900 |
| X-Line | ₹21,78,900 |

The unnamed twelfth column has no numeric value. Prices are retained at trim level and are not copied onto each powertrain/seating row. The comparison page labels the values starting MSRP; no effective date is inferred.

## Powertrain and seating notes

The current Kia showroom identifies the Carens Clavis as a 7-seater family MPV, and explicitly notes a 6-seat captain-seat option for HTX+. The comparison page lists the engine/transmission families used above. The structure CSV preserves OEM naming and does not infer engine outputs where not transcribed in this pass.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. The unknown column remains quarantined. No Firestore write or public catalogue publication has been performed.

## Sources

- Kia Carens Clavis current trim comparison and powertrain/seating matrix: https://www.kia.com/in/our-vehicles/carens-clavis/specs/compare-trims.html
- Kia Carens Clavis current showroom with 13 displayed cards and HTX+ seating options: https://www.kia.com/in/our-vehicles/carens-clavis/showroom.html
- Kia Carens Clavis 2026 official brochure: https://www.kia.com/content/dam/kia2/in/en/buy/Kia-Carens-Clavis-Brochure_2026_Desktop.pdf


## Current live-source recheck — 2026-11-07

The live comparison page was reopened today and still exposes 11 named grade columns with the same starting MSRP values recorded above. Immediately after HTE(EX), it still renders a twelfth comparison column whose header is blank and whose price field contains only the ₹ symbol. The feature matrix marks Smartstream G1.5 T-GDi 7DCT as included in that column, but no numeric price or grade label is rendered. The column remains excluded from the 28 normalized rows and 11 named price observations.

The current showroom page also exposes a GT-Line / X-Line styling selector. It does not explicitly map the unnamed comparison column to GT-Line, X-Line or any named grade. This is a possible lead only; no label is inferred. The showroom continues to show the 6-seat captain-seat option as trim-specific, and the compare matrix marks 6-seat as included(DCT) only under HTX+.

The current live page therefore confirms that the unknown-column issue persists; no new price or grade identity is available. Source checked dates in the 28-row structure and 11-row price observation files are refreshed to 2026-11-07. No price effective date is inferred.

Rechecked current pages:
- Compare matrix: https://www.kia.com/in/our-vehicles/carens-clavis/specs/compare-trims.html
- Showroom and GT-Line/X-Line selector: https://www.kia.com/in/our-vehicles/carens-clavis/showroom.html
