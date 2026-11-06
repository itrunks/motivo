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
