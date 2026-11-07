# Mahindra Bolero normalization

Checked: 2026-11-06

## Deliverable

- `data/mahindra-bolero-variant-observations.csv`: four current OEM selector grade observations with shared powertrain/configuration facts and prior official prices retained for comparison.

## Current OEM selector grades

| Grade | Current selector ex-showroom | Prior official capture |
|---|---:|---:|
| B4 DIESEL | ₹8,56,999 | ₹8,49,000 |
| B6 DIESEL | ₹9,37,000 | ₹9,29,000 |
| B6 OPT DIESEL | ₹9,69,000 | ₹9,69,000 |
| B8 DIESEL | ₹9,99,000 | ₹9,99,000 |

The official brochure covers B4, B6, B6(O) and B8. The current selector label is B6 OPT; retain that live label and record the brochure's B6(O) spelling as a naming crosswalk, not a separate grade.

## Shared configuration

Official Mahindra model pages and brochure identify a 1.493L mHAWK75 diesel engine, 55.9 kW at 3600 rpm, 210 Nm at 1600–2200 rpm, 2WD and 7-seat (5+2) layout. The product detail pages show manual transmission. Exact gear-count is not copied because the retrieved current official specification excerpt does not expose it.

## Price freshness and conflict

The current selector capture differs from the earlier official capture for B4 and B6. B6 OPT and B8 match. No effective-date or page-version explanation is visible. Both values are retained for the conflicting grades; neither is selected for import.

## Rights and import gate

All observations remain `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Current Mahindra selector: https://auto.mahindra.com/own-online/variant-selection?mgc=BOL
- Official Bolero brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw3264ff05/Bolero/3Oct_BoleroClassic_Brochure.pdf
- Mahindra current B4 product page: https://auto.mahindra.com/suv/bolero-b4-diesel/BOLM081917943925.html
- Mahindra current B8 product page: https://auto.mahindra.com/suv/bolero-b8-diesel/BOLM082217943903.html
- Mahindra October 6, 2025 updated Bolero range release: https://auto.mahindra.com/hi-in/press-release/mahindra-introduces-new-bolero-range.html


## Current OEM price recheck — 2026-11-07

The live selector was rechecked and current model detail pages were opened for all four grades:

| Grade | Current selector | Current detail page | Prior official capture | Assessment |
|---|---:|---:|---:|---|
| B4 DIESEL | ₹8,56,999 | ₹8,57,000 | ₹8,49,000 | ₹1 selector/detail delta; preserve both current source values |
| B6 DIESEL | ₹9,37,000 | ₹9,37,000 | ₹9,29,000 | Current sources aligned |
| B6 OPT DIESEL | ₹9,69,000 | ₹9,69,000 | ₹9,69,000 | Current sources aligned |
| B8 DIESEL | ₹9,99,000 | ₹9,99,000 | ₹9,99,000 | Current sources aligned |

The older B4/B6 amounts are superseded official captures; the current B6 detail page now confirms ₹9,37,000. Three of four current selector/detail pairs agree exactly. B4 retains a one-rupee difference between the selector and detail page. No amount is rounded or silently substituted; both current source values are recorded separately.

All four grades are 7-seat, diesel, manual, 2WD with the mHAWK75 1493 cc engine (55.9 kW, 210 Nm). The current product pages confirm manual transmission and 7-seat configuration. The current selector's B6 OPT spelling is retained; the brochure's B6(O) spelling is a naming alias, not a separate grade.

No effective date is exposed. The selector says delivery-time prices prevail and listed prices are indicative. Source rights remain review_required/unknown. The B4 one-rupee discrepancy remains explicitly quarantined from automated import pending confirmation.

Rechecked current OEM pages:
- Selector: https://auto.mahindra.com/own-online/variant-selection?mgc=BOL
- B4: https://auto.mahindra.com/suv/bolero-b4-diesel/BOLM081917943925.html
- B6: https://auto.mahindra.com/suv/bolero-b6-diesel/BOLM082017943918.html
- B6 OPT: https://auto.mahindra.com/suv/bolero-b6-opt-diesel/BOLM082117943910.html
- B8: https://auto.mahindra.com/suv/bolero-b8-diesel/BOLM082217943903.html
