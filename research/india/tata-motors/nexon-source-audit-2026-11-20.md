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
