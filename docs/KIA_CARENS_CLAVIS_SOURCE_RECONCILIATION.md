# Kia Carens Clavis — source reconciliation checkpoint

Checked: 2026-11-06

## Status: blocked pending source reconciliation

No normalized variant CSV is committed for this model yet. The current Kia comparison page exposes a 12-column trim matrix, but one column header is missing in the extracted page content and its price is rendered only as a currency symbol. The same page shows several trim labels and prices that differ from the existing 2026 brochure/workqueue snapshot.

## Evidence captured

- Current compare page lists HTE, HTE(O), HTE(EX), then one unnamed column, HTK+, HTK+(O), HTX, HTX(O), GTX, HTX+, GTX+, X-Line.
- Powertrain matrix includes Smartstream G1.5 T-GDi 7DCT, Smartstream G1.5 T-GDi 6iMT, Smartstream G1.5 T-GDi 6MT, Smartstream G1.5 CNG 6MT, Smartstream G1.5 6MT, 1.5 l CRDi VGT 6AT and 6MT.
- Seating matrix shows 7-seater for most trims and 6-seater only for a DCT configuration in the HTX+ column as extracted.
- The current price page has missing/misaligned values, including an unnamed trim column with no numeric price.
- The 2026 brochure snapshot contains a narrower trim list and does not fully reconcile to the current online comparison page.

## Required before normalization

1. Confirm the missing trim header and its actual retail label from Kia's live configurator or a current official brochure.
2. Confirm the current powertrain/trim mapping for the 6iMT, CNG, and diesel AT rows against the same trim labels.
3. Confirm current price basis and effective date; do not use a misaligned amount from the extracted comparison page.
4. Then generate the structure and price observation CSVs separately.

## Rights / publication

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or publication has been performed.

## Sources

- https://www.kia.com/in/our-vehicles/carens-clavis/specs/compare-trims.html
- https://www.kia.com/in/our-vehicles/carens-clavis/specs.html
- https://www.kia.com/in/our-vehicles/carens-clavis/showroom.html
- https://www.kia.com/content/dam/kia2/in/en/buy/Kia-Carens-Clavis-Brochure_2026_Desktop.pdf
