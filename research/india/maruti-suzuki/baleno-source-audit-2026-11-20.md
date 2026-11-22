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
