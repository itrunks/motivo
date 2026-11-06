# Mahindra Bolero Neo normalization

Checked: 2026-11-06

## Deliverable

- `data/mahindra-bolero-neo-variant-observations.csv`: five current OEM selector grade observations with shared engine/transmission/drive/seating attributes and both current/prior selector prices retained.

## Current OEM selector grades

The current Mahindra online selector displays five diesel grades:

| Grade | Current selector ex-showroom | Prior official capture |
|---|---:|---:|
| N4 DIESEL | ₹9,06,000 | ₹8,99,000 |
| N8 DIESEL | ₹9,69,000 | ₹9,69,000 |
| N10 (R) DIESEL | ₹9,99,898 | ₹10,09,000 |
| N10 OPT DIESEL | ₹10,85,000 | ₹10,79,000 |
| N11 DIESEL | ₹10,39,000 | ₹10,30,000 |

The current selector page exposes all five labels, including N10 (R), N10 OPT and N11. The current brochure identifies the common mHAWK100 1493 cc diesel engine, 73.5 kW, 260 Nm, 5-speed manual gearbox and 7-seat (5+2) layout. It names N10 (O), while the current selector label is N10 OPT; preserve the live selector's spelling and note the brochure naming difference.

## Price freshness and conflict

The current selector capture differs from the earlier same-day official selector values recorded in the source worklog for N4, N10 (R), N10 OPT and N11. N8 is unchanged. No effective date or page-version explanation is exposed. Both values are retained; the four mismatched grades remain `source_version_conflict` and are not approved for import.

## Rights and import gate

All observations remain `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Current Mahindra online selector: https://auto.mahindra.com/own-online/variant-selection?pid=NEO
- Mahindra official Bolero Neo brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw3a6cb6e5/brochures/NEO/NEO_brochure.pdf
- Mahindra October 6, 2025 new Bolero range announcement: https://auto.mahindra.com/hi-in/press-release/mahindra-introduces-new-bolero-range.html
