# Maruti Suzuki Baleno — source audit (2026-11-20)

## Status

**Desk audit started; not publishable.** The current official NEXA site now presents the September 2026 “Stunning New Baleno”. Do not reuse specifications, variant names or feature applicability from the outgoing pre-facelift model without a separate historical model-year record.

## Current official evidence captured

- Maruti Suzuki's September 2026 launch release identifies the Stunning New Baleno as a new product update and states bookings opened at ₹11,000, with introductory starting price ₹6,09,900 ex-showroom. This is not an on-road price and must not be copied as a current Trichy quote.
- The launch release states the Z12E petrol engine produces 61 kW (approx. 82.9 PS) at 5,700 rpm and 112.4 Nm at 4,500 rpm, with 5-speed MT and AGS options. It gives claimed fuel efficiency of 23.80 km/l (MT), 24.77 km/l (AGS), and 33.61 km/kg (S-CNG MT).
- The same release lists standard safety equipment: six airbags, ESP, ABS/EBD, emergency stop signal, hill-hold control, reverse parking sensors, three-point seatbelts, seatbelt reminders and TPMS. It describes Level 2 ADAS with radar + camera and eight functions: advanced emergency braking, lane keep assist, lane departure prevention/warning, adaptive cruise control, high-beam assist, vehicle sway warning and forward collision warning. Confirm exact trim applicability from the official variant matrix before recording variant-level facts.
- The launch release lists ventilated front seats, leatherette upholstery, Clarion premium sound system, Qi wireless charging with active cooling, 360-view camera, HUD, 9-inch SmartPlay Pro+ with wireless Apple CarPlay/Android Auto, and Suzuki Connect with 40+ features. These are model-level launch claims, not proof of fitment on every trim.
- NEXA's current Baleno page lists petrol variants: Sigma MT; Delta MT/AMT; Zeta MT/AMT; Alpha MT/AMT; Alpha(O) MT/AMT.
- NEXA's current page lists CNG variants as Delta CNG MT, Zeta CNG MT, Delta CNG AGS and Zeta CNG AGS. This conflicts with the launch release, which only explicitly describes S-CNG MT. Keep CNG AGS applicability unresolved until the current brochure/configurator/dealer order sheet confirms it.
- Official NEXA page links the current brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/newbaleno/download-brochure/The-Stunning-New-Baleno-Brochure.pdf
- NEXA page also describes Suzuki Connect remote operations including remote door lock/cancel lock, remote immobilizer request, remote alarm, remote hazard lights, and remote headlights off. Remote engine start and cabin pre-cooling are not established by the captured source; do not claim them.

## Sources registered

1. NEXA Baleno product page — https://www.nexaexperience.com/baleno
2. NEXA current brochure — https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/newbaleno/download-brochure/The-Stunning-New-Baleno-Brochure.pdf
3. NEXA Baleno live price page — https://www.nexaexperience.com/baleno/price
4. Maruti Suzuki September 2026 launch release — https://www.marutisuzuki.com/corporate/media/press-releases/2026/september/dare-to-go-glam-with-the-stunning-new-baleno-designed-for-dynamic-achievers
5. NEXA terms — https://www.nexaexperience.com/terms-of-use

## Rights and publication gate

NEXA terms state that copyright in site pages, screens, information and material is owned by MSIL unless otherwise indicated. The terms do not grant Motivo commercial reuse or redistribution rights. Therefore all registered Baleno sources are marked **pending / not approved**. Public accessibility or an official OEM source is not a redistribution licence. Seek written permission or obtain legal review of a suitable independent data-licensing route. Until then, keep research notes private and do not republish copied tables, brochure text, images or other expressive material.

## Open verification work

- [ ] Confirm the precise model-year / effective date and whether all dealer inventory is the September 2026 update.
- [ ] Review the complete current brochure and live variant/specification matrix; capture all trim-level feature applicability.
- [ ] Resolve CNG AGS discrepancy between the product page and launch release.
- [ ] Confirm current complete variant list, colours and city-specific price validity with an authorised NEXA dealer.
- [ ] Capture engine, dimensions, weights, tyres, suspension, braking and emissions specifications from current official technical documents.
- [ ] Verify whether TPMS is only warning-level or provides individual tyre pressures; do not infer highline display.
- [ ] Confirm Clarion system speaker count and exact trim applicability.
- [ ] Confirm Suzuki Connect subscription/feature eligibility and whether any remote climate/engine operation exists for this powertrain.
- [ ] Obtain written commercial reuse and redistribution permission or keep source status pending.
- [ ] Independent reviewer to verify source links, model identity, variant mapping and rights before normalization.

## Decision

Baleno desk research is **in progress**. No variant is eligible for Motivo production import. Keep `data/catalogue.json` unchanged until rights, exact model-year, variant mapping and field-level review pass.


## Official ex-showroom price check (2026-11-22)

Status: **blocked — current variant-wise official price data not retrievable from the captured NEXA page**.

Checked the official NEXA Trichy route:
https://www.nexaexperience.com/baleno/price-in-trichy

The retrieved page is an old/stale page snapshot (crawler metadata indicates approximately 1.5 years old) and exposes placeholders such as `₹ {price}`, rather than the current September 2026 Baleno price list. It links to the variant/pricing component, but the retrieved content does not include actual variant-wise prices.

The September 2026 Maruti launch release gives an introductory starting price of ₹6,09,900 ex-showroom. This is a launch starting-price claim, not a complete current Trichy variant-wise price list; do not treat it as a current live price or infer other variant prices from it.

Decision:
- No Baleno variant price is entered into the catalogue.
- Do not substitute third-party price tables for the official-only pricing requirement.
- Revisit the official NEXA live price selector/API or obtain a dated official price list that clearly identifies variant and effective date.
- Price status remains **unavailable / pending verification**, not zero and not estimated.
- Source rights remain pending; no publication approval is implied.
- Last checked: 2026-11-22.


## Variant identity & powertrain crosswalk — official-source pass (2026-11-22)

**Status: live official variant families captured; CNG AGS needs brochure/configurator order-level confirmation; independent review and rights approval remain open.**

The current NEXA Baleno product page separates the lineup as follows:

| Motivo powertrain identity | Fuel / engine | Official trim + transmission combinations | Count | Confidence |
|---|---|---|---:|---|
| BALENO_Z12E_PETROL | Petrol, Z12E series | Sigma MT; Delta MT; Delta AMT; Zeta MT; Zeta AMT; Alpha MT; Alpha AMT; Alpha(O) MT; Alpha(O) AMT | 9 | Live official page |
| BALENO_Z12E_SCNG | Petrol + S-CNG | Delta CNG MT; Zeta CNG MT; Delta CNG AGS; Zeta CNG AGS | 4 | Live official page; confirm orderability in current configurator |
| **Total listed combinations** |  |  | **13** |  |

The live official page explicitly lists the four CNG combinations, including Delta CNG AGS and Zeta CNG AGS. This resolves the earlier page-vs-launch-release discrepancy for the **current live website listing**, but does not yet prove every combination is orderable in every city or available for immediate dealer allocation. Keep the current configurator/order sheet as a remaining confirmation gate.

Powertrain notes:
- Current launch release identifies Z12E petrol output as 61 kW (approx. 82.9 PS) at 5,700 rpm and 112.4 Nm at 4,500 rpm.
- The current official product page describes AGS as a 5-speed automated manual transmission. It is an automatic transmission for Motivo filters, not MT.
- Do not infer exact CNG-mode output, gear ratios or variant-level equipment from the model highlights page; capture these from the dated technical brochure/configurator only.

Mapping rules:
1. The same trim may have MT and AMT records; preserve transmission as part of variant identity.
2. Do not assume CNG AGS is available in every NEXA city solely because it appears on the national product page.
3. Do not transfer petrol feature fitment to CNG variants without an explicit variant matrix.
4. Preserve exact trim spelling including Alpha(O).
5. Model-year, effective price date, and local availability remain independent attributes.

Evidence:
- Current official NEXA Baleno variant page: https://www.nexaexperience.com/baleno
- Current official brochure linked from that page: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/newbaleno/download-brochure/The-Stunning-New-Baleno-Brochure.pdf
- September 2026 launch release: https://www.marutisuzuki.com/corporate/media/press-releases/2026/september/dare-to-go-glam-with-the-stunning-new-baleno-designed-for-dynamic-achievers

This completes the first-pass live-page variant-family crosswalk only. Full model-year/orderability confirmation, field-level feature matrix, technical cross-check, exact variant-wise Trichy price capture, independent review and source redistribution rights remain open. No production import is approved.


## Current 2026 brochure: variant crosswalk and priority feature matrix (2026-11-22)

The current brochure linked from the live NEXA page was retrieved and reviewed. It explicitly identifies these seven powertrain/trim groups and 13 combinations:

| Powertrain identity | Fuel | Exact trim/transmission combinations | Count |
|---|---|---|---:|
| BALENO_Z12E_PETROL | Petrol | Sigma MT; Delta MT; Delta AMT; Zeta MT; Zeta AMT; Alpha MT; Alpha AMT; Alpha(O) MT; Alpha(O) AMT | 9 |
| BALENO_Z12E_SCNG | Petrol + CNG | Delta S-CNG MT; Delta S-CNG AMT; Zeta S-CNG MT; Zeta S-CNG AMT | 4 |
| **Total** |  |  | **13** |

This current brochure confirms S-CNG with both MT and AMT for Delta and Zeta. The earlier launch-release wording that only described S-CNG MT was incomplete; the live product page and current brochure both list CNG AGS. Keep local orderability and exact city allocation as separate checks.

### High-priority feature applicability

| Feature | Sigma MT | Delta petrol/CNG MT/AMT | Zeta petrol/CNG MT/AMT | Alpha MT/AMT | Alpha(O) MT/AMT |
|---|---|---|---|---|---|
| 6 airbags | Yes | Yes | Yes | Yes | Yes |
| ESP + Hill Hold Assist | Yes | Yes | Yes | Yes | Yes |
| TPMS | No | Yes | Yes | Yes | Yes |
| Wireless Android Auto / Apple CarPlay | No | Yes | Yes | Yes | Yes |
| SmartPlay Pro+ | No | No | Yes | Yes | Yes |
| Premium Sound System by Clarion | No | No | No | Yes | Yes |
| 360 View Camera | No | No | No | Yes | Yes |
| HUD | No | No | No | Yes | Yes |
| Front ventilated seats | No | No | No | Yes | Yes |
| Wireless charger | No | No | Yes | Yes | Yes |
| Auto AC | Manual AC | Manual AC | Auto AC | Auto AC | Auto AC |
| Push start/stop | No | No | Yes | Yes | Yes |
| Suzuki Connect remote operations | No | No | Yes | Yes | Yes |
| Level 2 ADAS | No | No | No | No | Yes |

Clarifications:
- Clarion is the premium audio brand confirmed for Alpha and Alpha(O); do not label it Bose, JBL or Harman.
- The brochure shows ADAS Level 2+ only for Alpha(O), with ACC, lane-keep assist, lane-departure prevention/warning, vehicle sway warning, advanced emergency braking, forward collision warning and high-beam assist.
- Suzuki Connect remote functions listed include door lock/cancel lock, hazard lights, headlights off, alarm, immobilizer request and battery health. Remote engine start and remote cabin pre-cooling are not listed in this brochure.
- TPMS is listed from Delta onward, but the brochure does not establish individual live tyre-pressure values. Do not label it highline TPMS.
- The brochure groups petrol and CNG variants in the same Delta/Zeta feature columns. Any fuel-specific exception must be checked before applying a feature to CNG.

Source: current official NEXA brochure:
https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/newbaleno/download-brochure/The-Stunning-New-Baleno-Brochure.pdf

This completes the first-pass current brochure feature matrix for the five brochure personas. Exact local availability, any fuel-specific footnotes, effective model-year, exact current Trichy ex-showroom price per variant, independent review and source-rights approval remain pending. Do not import these findings into production.
