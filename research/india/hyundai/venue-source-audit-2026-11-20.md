# Hyundai VENUE — India source audit

Audit date: 2026-11-20
Research status: **official lineup snapshot captured; model-year and dealer confirmation pending**
Publication status: **not eligible for catalogue publication**

## Model identity

- Manufacturer: Hyundai Motor India Limited (HMIL)
- Model: VENUE (all-new generation shown on current India site)
- Body style: sub-compact SUV; canonical Motivo mapping should be selected after checking the catalogue enum (likely compact_suv).
- Official product page: https://www.hyundai.com/in/en/find-a-car/venue/highlights
- Official feature-by-variant matrix: https://www.hyundai.com/in/en/find-a-car/venue/features
- Official owner's manual: https://www.hyundai.com/content/dam/hyundai/in/en/data/connect-to-service/owners-manual/2025/venue-venue-n-line-nov-2025-to-present.pdf
- Official website terms: https://www.hyundai.com/in/en/utility/legal-disclaimer/terms-and-conditions-of-the-website

The live Hyundai product page lists the all-new VENUE and displays a current trim set. The website is dynamic and Hyundai explicitly reserves the right to change specifications/equipment; this is a dated web snapshot, not a guaranteed model-year or dealer stock statement.

## Variant / powertrain identity snapshot

The official features page currently exposes these VENUE trim labels:

HX2, HX4, HX5, HX5+, HX5 Knight, HX6, HX6T, HX6T Knight, HX7, HX8, HX8 Knight, HX10, HX10 Knight.

The same official matrix maps engine/transmission combinations as follows:

| Engine family | Officially listed transmission combinations | Notes |
|---|---|---|
| Kappa 1.2L MPi petrol | MT | Offered across selected HX trims |
| Kappa 1.0L Turbo GDi petrol | MT and DCT | Availability differs by trim |
| U2 1.5L CRDi diesel | MT and AT | Availability differs by trim |

Do not create every possible engine × trim combination. Use only combinations explicitly shown in the official matrix and confirm them against a dated price list / dealer order sheet before normalization. Venue N Line is a separate product line and is not included in this six-model pilot candidate list.

## Feature evidence captured (trim applicability must be checked row-by-row)

The official highlights/features pages currently advertise, among other items:
- Bose 8-speaker premium audio system.
- Wireless Android Auto and Apple CarPlay.
- 12.3-inch ccNC navigation infotainment and 12.3-inch digital cluster on selected top trims.
- OTA vehicle updates and Bluelink connected-car functions on selected trims.
- Front ventilated seats, surround-view monitor and blind-spot view monitor on selected trims.
- TPMS Highline, six airbags, ESC and hill-start assist are included in the published safety feature list; confirm exact standard/variant applicability in the matrix and current price list.
- ADAS Level 2 equipment is trim-dependent; do not imply it is standard across the range.
- The highlights page states 33 safety features are standard across all variants, but each individual equipment field still needs a matrix-level applicability check before catalogue ingestion.

No trim-level feature has been promoted into catalogue data in this audit. The official page itself warns that equipment may vary and specifications are subject to change.

## Source rights finding

HMIL's official website Terms & Conditions grant a limited, non-transferable licence to view/use retrieved information for personal purposes only. They state that website materials may not be reproduced, republished, transmitted, displayed, posted or distributed, and prohibit automated or manual processes to monitor or copy webpages/content. They also state that site materials are owned, controlled or licensed by HMIL unless otherwise noted.

Operational decision:
- The official product page, feature matrix and owner's manual are reference-only at this stage.
- Commercial reuse and redistribution are marked pending; no permission is assumed.
- Do not scrape the site or republish brochure/manual text, tables, graphics or images.
- Seek written permission or legal review before any reuse/distribution.
- A source link/citation is not itself a redistribution licence.
- This note records limited factual research findings and does not reproduce the complete feature matrix or manual.

## Open checks before normalization

- [ ] Confirm the active model year, generation code and effective launch date from a dated official press release / price list.
- [ ] Obtain a dated official price list or dealer order sheet for the complete live variant lineup.
- [ ] Confirm exact engine/transmission combinations and any model-year-specific engine codes.
- [ ] Capture trim applicability for each equipment field from the current official matrix; verify safety standard-fit claims.
- [ ] Verify official technical specifications (power, torque, dimensions, fuel tank, boot, ground clearance) and distinguish brochure vs owner-manual values.
- [ ] Verify warranty, service schedule and service cost separately; do not infer.
- [ ] Rights review / written permission for commercial reuse and redistribution.
- [ ] Independent review of model identity, variant mapping, evidence and rights.

## Evidence links

- Official VENUE highlights: https://www.hyundai.com/in/en/find-a-car/venue/highlights
- Official VENUE feature matrix: https://www.hyundai.com/in/en/find-a-car/venue/features
- Official Venue / Venue N Line owner's manual (Nov 2025 to present): https://www.hyundai.com/content/dam/hyundai/in/en/data/connect-to-service/owners-manual/2025/venue-venue-n-line-nov-2025-to-present.pdf
- Official HMIL website Terms & Conditions: https://www.hyundai.com/in/en/utility/legal-disclaimer/terms-and-conditions-of-the-website
