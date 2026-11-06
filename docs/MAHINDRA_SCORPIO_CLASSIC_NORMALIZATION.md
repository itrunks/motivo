# Mahindra Scorpio Classic normalization

Checked: 2026-11-06

## Deliverables

- `data/mahindra-scorpio-classic-variant-structure.csv`: two current OEM grades with shared engine, fuel, transmission and drive configuration.
- `data/mahindra-scorpio-classic-price-observations.csv`: four official price observations (two official pages per grade), preserved without selecting a preferred amount.

## Current variant structure

Mahindra's current selector and model detail pages identify two retail diesel grades: CLASSIC S DIESEL and CLASSIC S11 DIESEL. Both detail pages show a 2.2L mHawk diesel, 2184 cc, 97 kW, 300 Nm, 6-speed manual, 2WD and 7SF seating.

The official brochure describes seating layouts more specifically:
- Classic S: 7-side-facing or 9-side-facing.
- Classic S11: 7-captain-chair or 7-side-facing.

The live product pages display 7SF for both grades. The brochure's multiple seating layouts are retained as notes only; no additional seat-specific variants are generated without current selector/price evidence.

## Official price conflict — quarantined

The current online selector and the current model detail pages disagree:

| Grade | Online selector | Model detail page |
|---|---:|---:|
| Classic S Diesel | ₹13,43,200 | ₹13,36,700 |
| Classic S11 Diesel | ₹17,48,400 | ₹17,39,900 |

Both pages label the amounts ex-showroom. No effective date or explanatory scope difference is exposed in the captured content. All four observations are preserved with `source_conflict`; no price is selected or approved for import.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Current selector: https://auto.mahindra.com/own-online/variant-selection?mgc=SCRC
- Classic S detail page: https://auto.mahindra.com/suv/scorpio-classic-classic-s-diesel/SCRCM088617973485.html
- Classic S11 detail page: https://auto.mahindra.com/suv/scorpio-classic-classic-s11-diesel/SCRCM088817973500.html
- Mahindra official Scorpio Classic brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw560e60c0/SCRC/Scorpio-Classic-Brochure_SV.pdf
- Current owner manual (revision August 2026): https://mvault-cloudfront.mahindra.com/Owner%27s-Manual/Scorpio%20Classic_HTML_01Sep2026/file3Dc405Busers5Bs054995Bdesktop5B-scorpioclassic-om.ditamap.html


## Live OEM price recheck — 2026-11-07

The earlier price conflict is resolved on the current live OEM pages. Both the online selector and the two model detail pages now show identical ex-showroom amounts:

| Grade | Current selector | Current detail page | Result |
|---|---:|---:|---|
| CLASSIC S DIESEL | ₹13,43,200 | ₹13,43,200 | Aligned |
| CLASSIC S11 DIESEL | ₹17,48,400 | ₹17,48,400 | Aligned |

The previous detail-page captures of ₹13,36,700 and ₹17,39,900 are retained only as superseded historical observations in this workpaper narrative; they are not current prices. The four current source observations are updated to the live values and marked `official_sources_aligned`.

The pages still provide no explicit price effective date or city scope. These are current OEM ex-showroom observations, not dated city-wise on-road quotes. Source reuse and redistribution remain unapproved.

Rechecked sources:
- Selector: https://auto.mahindra.com/own-online/variant-selection?mgc=SCRC
- CLASSIC S DIESEL: https://auto.mahindra.com/suv/scorpio-classic-classic-s-diesel/SCRCM088617973485.html
- CLASSIC S11 DIESEL: https://auto.mahindra.com/suv/scorpio-classic-classic-s11-diesel/SCRCM088817973500.html
