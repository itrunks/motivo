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

No source above is marked redistribution-approved. Do not add published sourceRefs for these sources until legal/terms review is completed and the source registry is updated with a substantiated licence/permission decision.

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
