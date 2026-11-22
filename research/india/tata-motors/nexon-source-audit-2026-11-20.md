# Tata Nexon ICE — source audit (2026-11-20)

## Status

**Desk audit started; not publishable.** This audit covers the India-market ICE Nexon (petrol/diesel/CNG), not Nexon.ev. The current Tata product page links a 2026 ICE brochure and a separate iCNG brochure; the main brochure PDF fetch timed out during this pass, so the official product page and its explicit footnotes are the strongest captured evidence here.

## Official evidence captured

- Current product page: https://tatamotors-prod.adobecqms.net/nexon/ice.html
- Official price page: https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/nexon/ice/price.html
- Current brochure link from the page resolves to: https://tatamotors-prod.adobecqms.net/content/dam/tml/pv/products/nexon/year-2026/ice/promoting-vc/brochures/may/nexon-brochure-may.pdf
- Separate iCNG brochure link from the page resolves to: https://tatamotors-prod.adobecqms.net/content/dam/tml/pv/products/nexon/year-2025/cng/promoting-vc/brochures/october/nexon-i-cng-brochure.pdf
- Official page says starting price ₹7.39 lakh ex-showroom; prices are indicative, subject to change, and dealer confirmation is required. This is not a Trichy on-road price.
- Official page identifies 1.2L turbocharged Revotron petrol (120 PS) and 1.5L turbocharged Revotorq diesel (115 PS). Transmission options include manual and automatic families; current page references 7-speed DCA and AMT/DCT paddle-shifter configurations. Exact variant/powertrain combinations require the live variant selector and dealer order sheet.
- Safety/technology claims include six airbags, three-point ELR belts for all occupants, ESP, TPMS, 360-degree surround-view camera, blind-view monitor, reverse camera, E-call/B-call and ADAS features. ADAS list shown includes front collision warning, autonomous emergency braking, high-beam assist, lane-centering, lane-departure warning, lane-keep assist and traffic-sign recognition.
- The current official page specifically states ADAS is only available on Fearless+ PS DCA; ADAS is not available on CNG or diesel. JBL-branded audio and subwoofer are also limited to Fearless+ PS DCA. Rear sunshade is limited to Fearless+ PS DCA and all Red #Dark editions. Do not generalize these features across Nexon variants.
- The same page lists 10.25-inch Harman infotainment and digital cluster, wireless Android Auto/Apple CarPlay, wireless charger, iRA connected services, ventilated leatherette seats, air purifier, cooled glovebox, rear AC vents and automatic climate control. Exact variant applicability must be tied to current official price/variant list.
- Official page notes iRA first-year subscription is free and renewal charges apply. It also states several features are not available on CNG, including multi-drive modes, cruise control, iRA connected-car features, E-call/B-call and subwoofer. Confirm current terms and package availability.
- The site describes TPMS but does not establish individual live tyre-pressure readout for every trim. Do not label it highline/individual without evidence.

## Rights

Tata platform terms restrict TML-owned content to personal, non-commercial use unless otherwise agreed in writing, prohibit redistribution without express prior written consent, and prohibit commercial use, derivative use and data-mining/extraction tools. All Nexon sources are marked rights **pending / not approved**. No scraping or copying brochure tables/images into Motivo.

## Open verification work

- [ ] Retrieve and manually review the current 2026 Nexon ICE brochure; current PDF fetch timed out.
- [ ] Review current iCNG brochure and confirm whether its model-year remains current.
- [ ] Capture the complete live trim list across petrol, diesel and CNG; preserve exact engine/transmission and edition suffixes.
- [ ] Verify feature applicability from the live variant selector and a dated authorised-dealer order sheet.
- [ ] Confirm TPMS readout type, exact JBL speaker/subwoofer count and audio brand by trim.
- [ ] Confirm iRA remote functions, subscription duration/renewal fees and any remote engine/climate functions.
- [ ] Capture complete current official variant-wise ex-showroom prices, effective date and any city/state applicability; do not collect on-road quotes.
- [ ] Confirm current safety-test protocol/rating scope and model-year applicability before publishing a rating.
- [ ] Obtain written redistribution permission or use a separately licensed dataset.
- [ ] Independent review before normalization.

## Decision

No Nexon ICE variant is eligible for production import. Research remains private pending brochure retrieval, model-year/variant mapping, field-level review and rights approval.


## Official ex-showroom price check (2026-11-22)

Status: **official price range and one named variant price captured; full variant-wise prices not exposed in retrieved page content**.

Checked Tata Motors' current official Nexon ICE price page:
https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/nexon/ice/price.html

The official page states:
- Starting ex-showroom price: ₹7.39 lakh for Smart 1.2 petrol.
- Overall displayed range: ₹7.39 lakh–₹15.50 lakh across the listed 60+ Petrol, Diesel and iCNG combinations.
- Fearless+ PS: ₹12.41 lakh ex-showroom, as stated in the page FAQ. The FAQ does not fully disambiguate every engine/transmission suffix for this named trim, so do not create a specific variant record from that label alone.

The live variant cards display a “Price” label but the retrieved page content does not expose the individual numeric values for every variant. Therefore the range and FAQ value are not a substitute for a complete price matrix.

Decision:
- Capture the starting price and published range as internal source evidence only.
- Do not infer individual variant prices from the range or from dealer quotations.
- Full variant-wise ex-showroom prices remain **unavailable / pending verification** until the official selector returns numeric values or a dated official price list is captured.
- Do not collect on-road, RTO, insurance, accessories, warranty, handling, offers or finance scheme values.
- Source rights remain pending; no production import or redistribution approval is implied.
- Last checked: 2026-11-22.


## Current 2026 feature applicability — explicit OEM footnotes (2026-11-22)

Rechecked the current Tata Nexon ICE product page and its variant-specific footnotes:
https://tatamotors-prod.adobecqms.net/nexon/ice.html

| Feature | Officially stated applicability | Normalization rule |
|---|---|---|
| Six airbags | Standard | Model-level standard-fit claim on current page |
| ESP | Standard | Model-level standard-fit claim on current page |
| ADAS package | Fearless+ PS DCA only | Do not assign to diesel or CNG; official page explicitly excludes both |
| JBL-branded speaker system | Fearless+ PS DCA only | Keep separate from generic Harman infotainment branding |
| Subwoofer | Fearless+ PS DCA only | Same exact restriction as JBL system |
| Rear sunshade | Fearless+ PS DCA and all Red #Dark editions | Do not infer on all Fearless trims or every #Dark-labelled package without matching exact edition |
| iRA connected-car features | Petrol and diesel only | Current page explicitly excludes CNG; first-year subscription free, renewal charges apply |
| E-call / B-call | Petrol and diesel only | Current page explicitly excludes CNG |
| Multi-drive modes / cruise control | Petrol and diesel only | Current page explicitly excludes CNG |
| 10.25-inch Harman infotainment and digital cluster | Promoted on current product page; exact variant applicability not exposed in retrieved page text | Keep as model-level marketing claim until matrix/order sheet confirms trim |
| Wireless Android Auto / Apple CarPlay | Promoted on current product page; exact variant applicability not exposed in retrieved page text | Do not assign to every trim without exact matrix |
| TPMS / 360 camera / BVM | Promoted on current product page; exact trim and readout type not exposed | TPMS individual-pressure readout remains unverified |

The current page's footnote is the strongest captured exact-trim evidence for the top ADAS/audio/rear-sunshade package. Other technology claims remain model-level until the current 2026 brochure or official selector provides exact trim applicability.

The 2026 ICE brochure link is visible on the official page, but retrieval failed because the PDF exceeded the available fetch size limit. The separate 2026 iCNG brochure also timed out. Do not substitute the 2025 Nexon brochure's variant matrix for the current 2026 lineup.

No production feature records are approved: model-year/variant crosswalk, complete matrix, exact city pricing, independent review and redistribution rights remain open.


## Current official specifications-page recheck (2026-11-22)

Source: https://tatamotors-prod.adobecqms.net/nexon/ice/specifications.html

The current official Tata specifications page now exposes the 2026 ICE and iCNG brochure links and a live/indexed selector with **70+ named trim, powertrain and edition combinations**. The selector contains standard, Camo, Dark and Red #Dark-labelled variants, so names must be preserved exactly and edition suffixes must not be collapsed into a base trim. A normalized exact count is still pending because the indexed list contains overlapping naming patterns (including “New” labels and suffix variants) that require deduplication against the selector's current orderable configuration.

Current official FAQ evidence on the same page:
- Petrol: 1.2L turbo Revotron, 120 PS / 170 Nm.
- Diesel: 1.5L turbo Revotorq, 113 PS / 260 Nm.
- iCNG: 1.2L turbo Revotron, 98 PS / 170 Nm.
- Transmission summary: petrol includes 5MT, 6MT, 6AMT and 7-speed DCA; diesel includes 6MT and 6AMT; iCNG is described as 6MT only.
- Dimensions: 3,995 × 1,804 × 1,620 mm; wheelbase 2,498 mm; boot 321L CNG / 382L petrol-diesel.
- Safety and infotainment summaries are model-level, not a substitute for trim applicability. The explicit footnotes on the current product page remain controlling for restrictions already captured: JBL 9-speaker system, subwoofer and ADAS only on Fearless+ PS DCA; ADAS excluded on CNG and diesel; rear sunshade only Fearless+ PS DCA and Red #Dark editions; iRA/E-call/B-call/multi-drive/cruise restrictions on CNG remain as previously noted.

Important discrepancy:
- The specifications-page FAQ describes iCNG as 6MT only, consistent with the current product-page FAQ snapshot.
- The indexed selector includes several CNG trim/edition labels; do not infer a CNG AMT merely from a trim label. Each exact selector item must be parsed for transmission before crosswalk creation.
- The product-page price snapshot and the current specifications page do not provide a complete numeric variant-wise price table in retrieved text.

Decision:
- Nexon 2026 selector availability is now materially better evidenced than the earlier product-page-only audit.
- Exact normalized variant count and fuel × engine × transmission crosswalk remain **in progress**, not marked complete.
- Current brochure content must still be manually reviewed; earlier PDF retrieval failure is not considered resolved merely because brochure links are visible.
- Exact feature applicability, price rows, model-year/effective date, source-specific factual-use review and independent review remain pending.


## Re-opened current official specifications page — live FAQ and brochure-link validation (2026-11-22)

Page: https://tatamotors-prod.adobecqms.net/nexon/ice/specifications.html

The rendered official page confirms the following text:
- The brochure area labels links as “Nexon Brochure 2026” and “Nexon iCNG Brochure 2026”.
- The main 2026 ICE PDF link resolves, but the web retrieval service rejects it because the PDF exceeds its 10 MiB content limit. This is a retrieval limitation, not evidence that the file is missing.
- The link labelled “Nexon iCNG Brochure 2026” resolves to a URL path containing `year-2025/cng/.../october/Nexon iCNG Brochure.pdf`. This is a **label/path year mismatch**. Do not assume it is a 2026-edition document until Tata provides a revision date or current order-sheet confirmation.
- FAQ engine values: petrol 120 PS / 170 Nm; diesel 113 PS / 260 Nm; iCNG 98 PS / 170 Nm.
- FAQ transmission values: petrol 5MT, 6MT, 6AMT and 7-speed DCT; diesel 6MT and 6AMT; iCNG exclusively 6MT.
- FAQ dimensions: 3,995 × 1,804 × 1,620 mm; wheelbase 2,498 mm; boot 321L CNG / 382L petrol and diesel.
- FAQ markets a 5-star BNCAP rating and lists 6 airbags, ADAS, ABS/EBD, ESP, hill assist, TPMS, 360 camera/BVM, ISOFIX, rain-sensing wipers and auto headlamps. The same page explicitly warns that not all features/specifications are available in all variants/personas. Rating protocol, tested variant, model-year and feature applicability must be verified before any variant-level publication.
- FAQ lists 10.25-inch touchscreen, wireless AA/CarPlay, iRA 70+ features, JBL 9-speaker audio, OTA and navigation with live traffic. The exact-trim footnote on the same page remains controlling: JBL 9-speaker, subwoofer and ADAS only Fearless+ PS DCA; ADAS not available on CNG or diesel. Rear sunshade only Fearless+ PS DCA and all Red #Dark editions; Red #Dark only Fearless+ PS. Do not treat the general FAQ feature list as standard fitment.
- Footnote repeats that multi-drive modes, cruise control, iRA connected-car features, E-call/B-call and subwoofer are not available on CNG; these features are available only on petrol/diesel as specified by the page.

Reconciliation:
- Earlier audit's diesel 115 PS figure came from the current product page summary; the specifications-page FAQ states 113 PS. Record this as an official-page discrepancy (115 vs 113 PS), not as a resolved value. The FAQ's 113 PS / 260 Nm is the current specifications-page value, while the product-page summary needs rechecking against the technical sheet.
- The iCNG 6MT-only transmission is directly stated in the current FAQ. Do not infer any iCNG AMT/DCT combination from the selector's CNG labels.
- The page's visible selector controls are rendered dynamically and the text extraction does not expose a stable full variant list in this capture. Existing “70+ indexed labels” is a search/index observation only, not a verified unique orderable-variant count. Do not count it as a crosswalk.
- The 2026-labelled iCNG brochure URL path points to a 2025 folder; exact brochure revision remains unresolved.

Next verification:
- Obtain a current dealer order sheet or accessible OEM configurator export to enumerate unique current orderable combinations.
- Obtain a dated technical specification to resolve diesel power output and iCNG brochure revision.
- Review each exact selector item for fuel/engine/transmission and edition suffix; no guessed combinations.


## Rechecked indexed OEM selector and independent variant-count cross-check (2026-11-22)

Sources:
- Tata official specifications page: https://tatamotors-prod.adobecqms.net/nexon/ice/specifications.html
- Tata official price/variant page: https://tatamotors-prod.adobecqms.net/content/tml/pv/in/en/nexon/ice/price.html
- Independent cross-check: Autocar India variant page, last updated 16 Nov 2026: https://www.autocarindia.com/cars/tata/nexon/variants/

New evidence:
- The indexed extraction for Tata's official specifications page exposes a long Search Variant list. It includes exact labels across Smart, Smart+, Smart+ S, Pure+, Pure+ S, Pure+ PS, Creative, Creative+ S, Creative+ PS and Fearless+ PS families, with petrol/diesel/iCNG and Camo, Dark and Red #Dark edition labels.
- Autocar's 16 Nov 2026 variant page independently describes the current Nexon range as **80 variants**. This is a useful secondary count cross-check, not an OEM orderability guarantee.
- Tata's official price page also exposes variant cards and feature groupings in indexed content. Its feature descriptions include Smart, Smart+ CNG, Smart+ S CNG, Pure+ CNG, Pure+ S CNG, Pure+ PS CNG, Creative CNG, Creative+ PS and Fearless+ PS CNG labels, among others. Do not infer transmission from trim-family names alone.

Count and crosswalk decision:
- Record **80 as a secondary-source reported range count only** (Autocar, updated 16 Nov 2026).
- The OEM indexed selector list is now visible in search extraction, but its labels require normalization: remove no suffixes until edition/powertrain identity is parsed; distinguish 5MT/6MT/6AMT/7DCT; and deduplicate “New”/Camo/Dark/Red #Dark aliases only when evidence proves they refer to the same orderable SKU.
- Do not mark 80 as 80 confirmed OEM unique combinations yet. The official page's rendered selector still does not provide a stable, fully structured export in the opened page text. Current OEM FAQ remains controlling for transmission family: petrol 5MT/6MT/6AMT/7DCT, diesel 6MT/6AMT, iCNG 6MT only.
- A dated Tata dealer order sheet or structured configurator export is still required to finalize the unique current orderable SKU count and the fuel × engine × transmission crosswalk.

Feature and pricing caution:
- Tata's official page says feature availability varies by variant/persona; its explicit footnote continues to restrict JBL/subwoofer/ADAS to Fearless+ PS DCA, excludes ADAS from CNG and diesel, and restricts rear sunshade to Fearless+ PS DCA and Red #Dark editions.
- The secondary Autocar matrix is useful for locating possible combinations but must not override OEM evidence or be copied into Motivo production data without source review.
- Official variant-wise numeric prices remain incomplete in retrieved OEM content. Do not substitute secondary price tables for the official ex-showroom-only pricing requirement.

Status after this pass:
- [x] Current OEM indexed selector labels surfaced and edition families recorded.
- [x] Independent 80-variant count cross-check recorded with source/date.
- [ ] Normalize exact selector labels into a deduplicated SKU crosswalk.
- [ ] Confirm orderability and count with a dated OEM/dealer order sheet or structured configurator export.
- [ ] Map exact feature applicability and official ex-showroom prices to each confirmed SKU.
- [ ] Complete factual-use rights review and independent review.

No Nexon production records are approved by this update.
