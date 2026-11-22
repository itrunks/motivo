# Maruti Suzuki FRONX — India source audit

Audit date: 2026-11-19
Research status: **desk research captured; model-year confirmation and rights review pending**
Publication status: **not eligible for catalogue publication**

## Model identity

- Manufacturer: Maruti Suzuki India Limited
- Retail channel: NEXA
- Model: FRONX
- Body classification for Motivo: crossover (confirm canonical body-style mapping during normalization)
- Current India product page: https://www.nexaexperience.com/fronx
- Current city pricing page (Trichy): https://www.nexaexperience.com/fronx/price-in-trichy
- Official brochure linked from product page: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/fronx/documents/NEXA-Fronx-Brochure.pdf

The live NEXA page currently exposes separate Petrol, Turbo and CNG variant groups. Its variant names are transcribed below as factual identifiers only; the full current model-year/price-list PDF and dealer confirmation still need to be checked before treating this as the definitive 2026 lineup.

## Variant names currently shown by NEXA

| Powertrain group | Variant / transmission combinations shown | Review status |
|---|---|---|
| 1.2L petrol | Sigma MT; Delta MT; Delta AMT; Delta+ MT; Delta+ AMT; Delta+ (O) MT | Pending exact current price-list confirmation |
| 1.0L turbo petrol | Delta+ MT; Zeta MT; Zeta AT; Alpha MT; Alpha AT | Pending exact current price-list confirmation |
| S-CNG | Sigma MT CNG; Delta MT CNG | Pending exact current price-list confirmation |

Important: do not merge a trim name across engine groups. For example, Delta+ 1.2L MT and Delta+ 1.0L Turbo MT are separate variant identities. AMT/AT are not manual transmissions.

## Factual fields captured from official material

- The official NEXA product page describes a 1.2L K-series Dual Jet Dual VVT petrol engine and lists 88 hp / 113 Nm for that engine.
- The same page describes a 1.0L turbo Boosterjet direct-injection engine, but the page extract used in this desk audit does not provide a complete power/torque specification. Leave those fields unresolved until the official specification sheet is captured.
- The product page describes S-CNG as a factory-fitted option.
- The product page identifies a 9-inch SmartPlay Pro+ infotainment system with Surround Sense powered by ARKAMYS, HUD, wireless charging and 360-degree camera as available equipment; exact trim applicability must be taken from the current feature matrix, not inferred from the highlights page.
- The official Trichy price page explicitly distinguishes ex-showroom price from final on-road price and says final on-road cost depends on RTO, insurance and local charges. Do not use ex-showroom figures as on-road prices.

## Source register candidates

| Source ID | Publisher | Source | Intended use | Rights review |
|---|---|---|---|---|
| msil_nexa_fronx_product | Maruti Suzuki / NEXA | https://www.nexaexperience.com/fronx | Model identity, powertrain groups, feature claims | Pending; public access is not a reuse licence |
| msil_nexa_fronx_brochure | Maruti Suzuki / NEXA | https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/fronx/documents/NEXA-Fronx-Brochure.pdf | Variant/feature cross-check; brochure date/version must be confirmed | Pending; do not republish brochure content |
| msil_nexa_fronx_trichy_price | Maruti Suzuki / NEXA | https://www.nexaexperience.com/fronx/price-in-trichy | City-specific price research and date capture | Pending; verify current values at ingestion time |

No source above is marked redistribution-approved. The sources are recorded in data/source-registry.csv with commercial reuse and redistribution set to pending. NEXA's Terms of Use state that copyright belongs to MSIL and that extraction/re-utilisation of website content requires express written consent. No such permission has been obtained. Treat these sources as reference-only for internal research until legal review determines whether the proposed limited use of factual fields is permitted or written permission is secured. Do not add published sourceRefs or distribute extracted source content.

## Open checks before normalization

- [ ] Confirm the exact active model year and whether a 2026 facelift/generation change applies.
- [ ] Download and record the currently linked brochure version/date; compare with live variant selector.
- [ ] Capture the complete official feature-by-variant matrix, including wireless CarPlay/Android Auto, airbags, ESC, TPMS, smart key and connected-car features.
- [ ] Capture exact engine codes/displacement, power, torque, fuel compatibility and transmission mapping from official specifications.
- [ ] Verify official warranty and service schedule data separately.
- [ ] Review NEXA/Maruti website terms and brochure copyright/licensing; no reuse approval assumed.
- [ ] Independently review variant identities and all source links.
- [ ] Only then map to catalogue records and run validation.

## Evidence links

- Official NEXA FRONX product and variant page: https://www.nexaexperience.com/fronx
- Official NEXA FRONX brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/fronx/documents/NEXA-Fronx-Brochure.pdf
- Official FRONX price page for Trichy: https://www.nexaexperience.com/fronx/price-in-trichy

## Rights review finding (2026-11-19)

NEXA Terms of Use: https://www.nexaexperience.com/terms-of-use

The terms state that copyright in site pages, information and material is owned by MSIL unless otherwise indicated, and prohibit extracting or re-utilising whole or part of website content without express written consent. Therefore the current conservative rights gate remains in force: commercial reuse and redistribution are pending, not approved. This is not a legal opinion on the status of individual factual data points; it is a fail-closed operational decision until that question is reviewed or permission is obtained.


## Official ex-showroom price check (2026-11-22)

Status: **partially verified; exact variant-wise price table not captured; not publishable**.

Official NEXA Trichy price page:
https://www.nexaexperience.com/fronx/price-in-trichy

The page identifies the figures as ex-showroom pricing and its FAQ currently states:
- Petrol variants (Sigma MT through Delta+ (O) MT): ₹6,89,853–₹8,64,453.
- S-CNG variants (Sigma MT CNG and Delta MT CNG): ₹7,93,852–₹8,73,852.
- Base Sigma MT: ₹6,89,853.
- Top Alpha AT: ₹11,88,852.

The page's live variant-price table did not render in the retrieved page content, so individual prices for every variant could not be independently captured. Do not infer intermediate variant prices from the ranges.

A separate Maruti Suzuki pricing API result was found for FRONX with `forCode=08`; it reports a different base price (₹6,81,200) and a full response containing variant codes. The returned `forCode=08` is not established as Tamil Nadu/Trichy, so these figures must not be mixed into the Trichy price record. The state/market mapping for that code must be verified before using that endpoint.

Price-policy handling:
- Record only official ex-showroom values; no on-road, RTO, insurance, accessories, warranty, handling or offers.
- For this audit, retain only the source-stated Trichy ranges and the explicitly named base/top figures as internal research evidence.
- Exact variant-wise prices remain **unavailable** until the official page exposes the full table or an authorised official price list is captured.
- Last checked: 2026-11-22. Recheck immediately before any future ingestion because prices are time-sensitive.
- Source rights remain pending; this is not approval to redistribute the extracted values.


## Variant identity & powertrain crosswalk — official-source pass (2026-11-22)

**Status: variant-family mapping captured; independent second review and rights approval remain open.**

Cross-checked the live NEXA FRONX product/variant page against the currently linked official brochure. The official page separates the lineup into Petrol, Turbo and S-CNG groups; the brochure technical table independently confirms the transmission families and core engine outputs.

| Motivo powertrain identity | Fuel / engine | Official trim + transmission combinations | Count |
|---|---|---|---:|
| FRONX_12_NA_PETROL | Petrol, 1.2L K-Series Dual Jet Dual VVT | Sigma MT; Delta MT; Delta AMT; Delta+ MT; Delta+ AMT; Delta+ (O) MT | 6 |
| FRONX_10_TURBO_PETROL | Petrol, 1.0L Turbo Boosterjet | Delta+ MT; Zeta MT; Zeta AT; Alpha MT; Alpha AT | 5 |
| FRONX_12_SCNG | Petrol + factory S-CNG, 1.2L | Sigma MT CNG; Delta MT CNG | 2 |
| **Total listed combinations** |  |  | **13** |

Technical cross-check from the official brochure:
- 1.2L petrol: 66 kW / 89.73 PS, 113 Nm; 5MT or 5AMT.
- 1.2L S-CNG: petrol mode 66 kW / 89.73 PS and 113 Nm; CNG mode 57 kW / 77.5 PS and 98.5 Nm; 5MT.
- 1.0L turbo petrol: 73.6 kW / 100.06 PS, 147.6 Nm; 5MT or 6AT.
- The official brochure identifies the 1.0L turbo system as a mild-hybrid/ISG-assisted powertrain; preserve exact official terminology in normalized technical records.

Mapping rules:
1. Treat Delta+ MT in the 1.2L naturally aspirated group and Delta+ MT in the 1.0L turbo group as different variant records.
2. Treat AMT and AT as automatic transmissions, never manual.
3. Do not create a 1.2L AMT CNG variant; the current official variant group lists only CNG MT.
4. Keep model year / effective date and city-specific pricing as separate dimensions from this variant identity map.
5. Do not inherit model-level marketing features across every trim.

Evidence:
- Current official NEXA FRONX variant page: https://www.nexaexperience.com/fronx
- Official FRONX brochure: https://www.nexaexperience.com/content/dam/msil/nexa/in/en/assets/cars/fronx/documents/NEXA-Fronx-Brochure.pdf

This completes the first-pass official variant-family crosswalk only. It does not clear the model for production import: source redistribution rights remain pending, feature-by-variant review and independent verification remain open, and exact current Trichy variant prices are not fully captured.
