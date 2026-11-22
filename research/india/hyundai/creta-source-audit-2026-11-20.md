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


## Official ex-showroom price check (2026-11-22)

Status: **official variant-wise prices captured for listed petrol/diesel combinations; Turbo GDi coverage incomplete; Trichy-specific applicability and rights pending**.

Source: Hyundai Motor India's official CRETA price page:
https://www.hyundai.com/in/en/find-a-car/creta/price

The page explicitly labels these as ex-showroom prices. Values below are transcribed from the official page as observed on 2026-11-22; they are not on-road prices.

### Petrol

| Variant / powertrain | Ex-showroom price |
|---|---:|
| 1.5 MPi Petrol MT E | ₹10,90,700 |
| 1.5 MPi Petrol MT EX | ₹12,06,700 |
| 1.5 MPi Petrol MT EX(O) | ₹13,14,200 |
| 1.5 MPi Petrol MT S(O) | ₹14,20,700 |
| 1.5 MPi Petrol MT S(O) Knight Edition | ₹14,39,200 |
| 1.5 MPi Petrol IVT EX(O) | ₹14,49,700 |
| 1.5 MPi Petrol MT SX | ₹14,99,900 |
| 1.5 MPi Petrol MT SX DT | ₹15,19,400 |
| 1.5 MPi Petrol IVT S(O) | ₹15,65,700 |
| 1.5 MPi Petrol MT SX Premium | ₹16,34,200 |
| 1.5 MPi Petrol MT SX Premium DT | ₹16,49,200 |
| 1.5 MPi Petrol MT King | ₹17,27,800 |
| 1.5 MPi Petrol MT King DT | ₹17,42,800 |
| 1.5 MPi Petrol IVT SX Premium | ₹17,78,700 |
| 1.5 MPi Petrol IVT SX Premium DT | ₹17,93,700 |
| 1.5 MPi Petrol IVT King | ₹18,68,800 |
| 1.5 MPi Petrol IVT King Knight Edition | ₹18,83,300 |
| 1.5 MPi Petrol IVT King DT | ₹18,83,800 |
| 1.5 MPi Petrol IVT King Lounge | ₹19,21,700 |
| 1.5 MPi Petrol IVT King Lounge DT | ₹19,36,700 |
| 1.5 Turbo Petrol DCT King | ₹19,91,300 |
| 1.5 Turbo Petrol DCT King DT | ₹20,06,300 |

### Diesel

| Variant / powertrain | Ex-showroom price |
|---|---:|
| 1.5 CRDi Diesel MT DSL E | ₹12,61,000 |
| 1.5 CRDi Diesel MT DSL EX | ₹13,73,000 |
| 1.5 CRDi Diesel MT DSL EX(O) | ₹14,80,200 |
| 1.5 CRDi Diesel MT DSL S(O) | ₹15,91,700 |
| 1.5 CRDi Diesel MT DSL S(O) Knight Edition | ₹16,10,200 |
| 1.5 CRDi Diesel AT DSL EX(O) | ₹16,15,200 |
| 1.5 CRDi Diesel AT DSL S(O) | ₹17,36,700 |
| 1.5 CRDi Diesel MT DSL SX Premium | ₹17,99,700 |
| 1.5 CRDi Diesel MT DSL SX Premium DT | ₹18,14,700 |
| 1.5 CRDi Diesel MT DSL King | ₹18,92,800 |
| 1.5 CRDi Diesel MT DSL King DT | ₹19,07,800 |
| 1.5 CRDi Diesel AT DSL King | ₹19,80,800 |
| 1.5 CRDi Diesel AT DSL King DT | ₹19,95,800 |
| 1.5 CRDi Diesel AT DSL King Knight Edition | ₹20,14,300 |
| 1.5 CRDi Diesel AT DSL King Lounge | ₹20,30,700 |
| 1.5 CRDi Diesel AT DSL King Lounge DT | ₹20,45,700 |

The page's retrieved price table does not show the complete Turbo GDi DCT variant family; only the two King DCT entries above appear in the petrol section. Do not invent or infer omitted combinations. The listed values are the source's current India price-page values; a dedicated Chennai/Tiruchirappalli page should be checked before any city-specific display.

Decision:
- Variant-wise ex-showroom values above are captured as internal research evidence only.
- Keep exact variant identity aligned to the live feature/variant matrix; DT and special-edition suffixes must not be discarded.
- Turbo GDi DCT price coverage remains incomplete.
- Do not convert these figures to on-road prices or add taxes/insurance.
- Source rights remain pending; no production import or redistribution approval is implied.
- Last checked: 2026-11-22.


## Variant identity & powertrain crosswalk — official matrix pass (2026-11-22)

**Status: official trim × engine × transmission matrix transcribed; current dealer orderability, independent review and rights approval remain open.**

The live HMIL CRETA features matrix lists the following exact combinations:

| Motivo powertrain identity | Engine / fuel | Explicit trim + transmission combinations | Count |
|---|---|---|---:|
| CRETA_15_MPI_PETROL | 1.5L MPi petrol | E MT; EX MT; EX(O) MT; S(O) MT; S(O) Knight MT; SX MT; SX Premium MT; King MT; EX(O) IVT; S(O) IVT; SX Premium IVT; King IVT; King Knight IVT | 13 |
| CRETA_15_CRDI_DIESEL | 1.5L U2 CRDi diesel | E MT; EX MT; EX(O) MT; S(O) MT; S(O) Knight MT; SX MT; King MT; King Knight MT; EX(O) AT; S(O) AT; King AT; King Knight AT | 12 |
| CRETA_15_TGDI_PETROL | 1.5L Turbo GDi petrol | King DCT | 1 |
| **Total listed combinations** |  |  | **26** |

Correction to avoid ambiguity: the matrix has 9 trim columns (E, EX, EX(O), S(O), S(O) Knight, SX, SX Premium, King, King Knight). The E trim is explicitly shown with MT for both 1.5L MPi petrol and 1.5L CRDi diesel. Preserve these base manual variants.

Transmission normalization:
- MT = manual.
- IVT, AT and DCT = automatic.
- Preserve trim suffixes such as Knight Edition; do not merge those with standard trim records.
- Preserve petrol MPi, diesel CRDi and turbo GDi as separate powertrain identities even when the trim label is the same.

The official price page captured 22 petrol and 16 diesel price rows in the earlier price pass, while this engine matrix crosswalk yields 13 MPi petrol + 12 diesel + 1 Turbo GDi = 26 trim/powertrain/transmission combinations. This discrepancy means the price rows and matrix rows must not be joined by trim label alone; exact engine/transmission identity and price-page suffixes need a reconciliation pass before any price record is normalized. The price audit's count and this matrix count describe different captured page content and are not interchangeable.

Evidence:
- HMIL official CRETA features matrix: https://www.hyundai.com/in/en/find-a-car/creta/features
- HMIL official CRETA price page: https://www.hyundai.com/in/en/find-a-car/creta/price

This completes the first-pass official trim/powertrain crosswalk. Reconcile the official price-page rows, confirm current model-year and local orderability, audit all feature rows by exact variant, and obtain rights clearance before normalization. No production import is approved.
