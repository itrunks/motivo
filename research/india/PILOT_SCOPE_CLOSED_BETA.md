# India closed-beta pilot scope

Last reviewed: 2026-11-20
Status: **scope selected; vehicle/source audits not yet started or approved**

## Objective

Build a deliberately small but useful India passenger-car catalogue for a 10–20 person closed beta. The pilot is a research target, not a claim that these vehicles or variants have already been verified. No record from this scope is eligible for publication until its current model-year, variant identity, field evidence and reuse rights have passed review.

## Selected brands and model candidates

| Brand | Model candidate | Segment coverage | Why included | Audit status |
|---|---|---|---|---|
| Maruti Suzuki | Baleno | Premium hatchback | High-volume hatchback; useful benchmark for feature/value comparisons | 2026 Stunning New Baleno desk audit started; exact model-year/trim mapping/rights pending |
| Maruti Suzuki | Fronx | Crossover / compact SUV | Popular crossover with multiple powertrain/trim combinations | Pending |
| Hyundai | Venue | Compact SUV | Mainstream compact-SUV comparison coverage | Official lineup snapshot captured; model-year/rights pending |
| Hyundai | Creta | Mid-size SUV | Adds a larger family-SUV segment and a distinct price band | Official feature/trim snapshot captured; model-year/rights pending |
| Tata Motors | Punch | Micro-SUV | Entry SUV/crossover coverage and a different size/price point | 2026 product page + Jan 2026 brochure reviewed; current variant/year and rights pending |
| Tata Motors | Nexon | Compact SUV | Mainstream compact-SUV and powertrain comparison coverage | 2026 ICE product page reviewed; brochure retrieval, exact variant/year and rights pending |

This six-model scope is intentionally limited to three high-reach manufacturers and multiple high-demand body/price segments. The model list is a prioritisation decision only; verify each model is on sale in India at the time of audit before creating catalogue records. If a model has been replaced, discontinued or renamed, record the effective dates and do not silently merge generations.

## Variant selection rule

For each model, audit the current India-market model year and enumerate the complete officially offered variant list first. Then select a beta comparison subset that covers, where offered:

1. Entry variant (price/accessibility baseline).
2. Mid variant (mainstream value point).
3. Top variant (feature ceiling).
4. Each materially different engine/fuel and transmission combination that changes the buyer decision.

Do not infer that a trim name, engine, transmission or feature carries over from the previous model year. Treat facelift/generation changes as separate model records when the underlying generation changes; preserve model-year and effective dates.

## Evidence and rights gates

- Prefer OEM India product pages, brochures, price lists, owner manuals, official press releases and official safety-test publications for factual vehicle fields.
- Use independent publications and owner/community reports as corroboration or clearly labelled real-world observations, not as substitutes for missing OEM facts.
- Record the exact source URL, retrieval date, publication/effective date when available, and field-level source references.
- The current source registry requires explicit commercial reuse and redistribution approval before a source can support a published record. A publicly accessible OEM brochure is **not automatically** a redistribution licence.
- If a source's terms are unclear, mark rights as pending and keep any extracted data in private review notes. Do not copy brochure prose, tables, images or other expressive content into the product.
- Do not populate data/catalogue.json with draft guesses just to make the app look populated. Keep unknown values null/absent and retain the evidence trail.

## Work sequence

- [x] Define pilot brand/model scope.
- [ ] Verify current model/generation and model-year lineup for all six candidates (Baleno, FRONX, Venue, Creta, Punch and Nexon desk research started; exact MY/rights remain open).
- [ ] Audit source terms and record eligible sources in data/source-registry.csv (Baleno, FRONX, Venue, Creta, Punch and Nexon source candidates registered; all rights pending).
- [ ] Capture complete official variant lists and exact powertrain/trim identities.
- [ ] Normalize only evidence-backed records into the canonical schema.
- [ ] Independent review of source links, model year, variant mapping and rights.
- [ ] Publish only records that pass all validation and human review gates.

## Market context references

These sources justify prioritisation only; they are not treated as licensed catalogue data sources:

- Maruti Suzuki FY 2025–26 official sales release: https://www.marutisuzuki.com/content/dam/arena-eds/corporate/press-release/assets/documents/2026/april/Press_Release_Maruti_Suzuki_sales_in_March_2026_and_FY_2025_26.pdf
- Autocar India H1 2026 bestselling models by powertrain: https://www.autocarindia.com/auto-features-amp/bestselling-cars-in-h1-2026-by-powertrain-type-440885
- Autocar India October 2026 B2 segment dispatch table: https://www.v3cars.com/b2-segment-cars-in-india
- Maruti Suzuki official NEXA model catalogue: https://www.nexaexperience.com/
