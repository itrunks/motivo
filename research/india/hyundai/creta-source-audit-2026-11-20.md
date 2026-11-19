# Hyundai CRETA — India source audit

Audit date: 2026-11-20
Research status: **official current feature/variant snapshot captured; model-year and exact active lineup confirmation pending**
Publication status: **not eligible for catalogue publication**

## Model identity

- Manufacturer: Hyundai Motor India Limited (HMIL)
- Model: CRETA (current India-market generation shown on HMIL site)
- Segment: mid-size SUV (canonical Motivo mapping: mid_size_suv)
- Official product page: https://www.hyundai.com/in/en/find-a-car/creta/highlights
- Official feature-by-variant matrix: https://www.hyundai.com/in/en/find-a-car/creta/features
- Official India price page: https://www.hyundai.com/in/en/find-a-car/creta/price
- Official website terms: https://www.hyundai.com/in/en/utility/legal-disclaimer/terms-and-conditions-of-the-website

## Current feature matrix snapshot

The official feature matrix exposes these primary trim labels:
E, EX, EX(O), S(O), S(O) Knight, SX, SX Premium, King and King Knight.

The matrix maps three engine families:
- 1.5L MPi petrol — MT and IVT, depending on trim.
- 1.5L U2 CRDi diesel — MT and AT, depending on trim.
- 1.5L Turbo GDi petrol — DCT on selected top trim(s).

Special editions (including Summer Edition) and market-specific packages may alter the visible trim naming/equipment. Do not infer that every trim exists with every engine/transmission. Create variant records only for exact combinations confirmed by the live official price selector or dated dealer order sheet.

## Feature evidence captured (trim-level applicability required)

The current official matrix advertises a range of equipment including:
- Bose 8-speaker premium audio system with front centre speaker and subwoofer on selected upper trims.
- Smartphone connectivity listed as wireless Android Auto / Apple CarPlay on some trims; a footnote states some higher trims use a wired-to-wireless adapter. Preserve that distinction rather than labelling all as native wireless.
- 10.25-inch navigation system and multi-display digital cluster on selected trims.
- Panoramic sunroof, dual-zone automatic climate control, ventilated front seats and wireless charger on selected trims.
- Bluelink connected-car features and OTA map/infotainment updates on selected trims.
- Six airbags, side/curtain airbags, ABS/EBD and ESC are shown in the published safety matrix; confirm exact standard-fit details against the current model-year matrix before ingestion.
- Safety and convenience features vary by trim and transmission. Do not generalize top-trim equipment to the full range.

The official price page also describes special editions and equipment changes; use the dated live variant selector for the final model-year list. Ex-showroom prices must never be stored as on-road prices.

## Source rights finding

HMIL's official website Terms & Conditions grant a limited, non-transferable licence to view/use retrieved information for personal purposes only. They state that website materials may not be reproduced, republished, transmitted, displayed, posted or distributed, prohibit automated or manual processes to monitor/copy webpages or content, and state that materials are owned, controlled or licensed by HMIL unless otherwise noted.

Operational decision:
- Product, feature and price pages are reference-only at this stage.
- Commercial reuse and redistribution are marked pending; no permission is assumed.
- Do not scrape the site or republish brochure text, feature tables, graphics or images.
- Seek written permission or legal review before any reuse/distribution.
- A source link/citation is not itself a redistribution licence.

## Open checks before normalization

- [ ] Confirm active model year, generation code and effective dates.
- [ ] Capture complete exact engine × transmission × trim combinations from the live official price selector and a dated dealer order sheet.
- [ ] Confirm current Summer/King/Knight edition availability and whether each is a separate variant or package.
- [ ] Verify each feature's exact trim applicability; specifically native wireless vs adapter-based smartphone connectivity.
- [ ] Capture official engine codes, power, torque, dimensions, fuel tank, boot and ground clearance.
- [ ] Confirm safety standard-fit matrix and any ADAS applicability by exact transmission/trim.
- [ ] Confirm current Chennai/Tiruchirappalli price snapshot separately; do not extrapolate from another city.
- [ ] Review source terms / obtain written permission for commercial reuse and redistribution.
- [ ] Independent review of all model/variant mappings and evidence.

## Evidence links

- Official CRETA highlights: https://www.hyundai.com/in/en/find-a-car/creta/highlights
- Official CRETA feature matrix: https://www.hyundai.com/in/en/find-a-car/creta/features
- Official CRETA price page: https://www.hyundai.com/in/en/find-a-car/creta/price
- Official HMIL website Terms & Conditions: https://www.hyundai.com/in/en/utility/legal-disclaimer/terms-and-conditions-of-the-website
