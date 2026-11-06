# Current India brand inventory

This is a **candidate audit queue**, not a declaration that every listed marque currently has an orderable passenger car in India. The validator and catalogue publication must not treat these rows as verified.

## Review each candidate

1. Open the India-specific official product catalogue.
2. Confirm at least one passenger-car model is currently offered/orderable in India.
3. Capture exact model names, currently offered variants, official model page, brochure/price-list URL, and date checked.
4. Review terms and permitted reuse for every source before bulk ingestion.
5. Mark `current_sales_status` as `active_verified`, `not_current`, or `unclear`; attach `status_evidence_url`.
6. Only `active_verified` brands can move to the approved import queue.

## Scope rules

- Passenger cars sold in India, including retail SUVs/MPVs and passenger EVs.
- Exclude commercial-only vehicles, two-wheelers, three-wheelers, and discontinued models.
- A marque/group presence is not enough: confirm current passenger-car sales under that marque.
- Keep parent group and retail brand separate (e.g. Audi and Volkswagen are separate brands).
- This file is for completeness tracking. It is not a source for vehicle facts or price claims.

## Initial candidate set

Candidates were seeded from a current India car-brand directory and recent India PV maker/brand coverage, then cross-checked against official OEM/group web presence where available. Third-party lists are discovery aids only, not publication evidence. The official Škoda Auto Volkswagen India site states that its India operations cover Volkswagen, Škoda, Audi, Bentley, Lamborghini and Porsche; each brand still requires current passenger-car product verification.

Sources for discovery:
- https://autoastra.in/brands
- https://drivewithsaran.com/brand (unofficial dispatch compilation; discovery only)
- https://skoda-vw.co.in/

## Reconciled inventory snapshot (2026-11-06)

The companion `india-brand-inventory.csv` now contains **37 unique brand IDs** reconciled against the India pilot audit workpapers:

- `active_verified`: 30 brands
- `unclear`: 5 brands
- `not_current`: 2 brands

These are **brand-level India retail-presence classifications**, not a statement that every model, derivative or variant is currently orderable. Model-level orderability and exact current prices remain subject to each brand audit and dated OEM/dealer evidence. Only `active_verified` brands are eligible for the approved import queue; `unclear` and `not_current` must remain excluded.

### Canonical identity rules

- Keep the retail marque separate from its legal operating company and parent group.
- `mg` remains the stable brand ID and `MG Motor` the retail marque. `JSW MG Motor India Private Limited` is the Indian operating joint venture formed by JSW Group and SAIC Motor; MG SELECT is a sales channel, not a separate marque.
- `tata` remains the stable brand ID and `Tata Motors` the inventory display name. Keep the Tata passenger-car catalogue separate from commercial-vehicle products.
- Parent groups are recorded for grouping only. They must not be used to merge distinct retail marques such as Audi, Bentley, Lamborghini, Porsche, Škoda and Volkswagen.
- Jaguar and Genesis remain in the completeness inventory with `not_current`; they are not current sellable catalogue brands. Keep both in the watchlist/review workflow.
- Lotus remains `unclear` until India retail orderability is confirmed. Aston Martin, Bentley, Ferrari and McLaren also remain `unclear` pending local dealer/orderability confirmation.

The CSV is a completeness and review-control file. It is not an approved vehicle import manifest and does not grant permission to scrape, copy or redistribute OEM content.

## Model-level reconciliation snapshot (2026-11-06)

The companion `current-model-audit.csv` now contains **251 unique brand/model candidates across 35 brands**. Every `active_verified` brand in the brand inventory has at least one model candidate represented.

- `listed_on_official_site`: 219 rows
- `dealer_confirmation_required`: 32 rows
- Variant-level audit: pending; model listing evidence is not proof that every derivative is currently orderable.
- Jaguar and Genesis are intentionally excluded from the current-model candidate file because their brand status is `not_current`.
- Lotus, Aston Martin, Bentley, Ferrari, McLaren, Rolls-Royce, Lamborghini, Force Gurkha and selected Mahindra EV candidates are held for dealer/orderability confirmation as recorded in the CSV.
- Commercial pickups, buses, fleet vans, taxi-only products, discontinued nameplates and announced future products are excluded from the private passenger-car candidate set unless explicitly called out in the row notes.

### Model identity and derivative rules

- Keep separately marketed ICE and EV products separate where the OEM presents distinct model entries (for example Tata Nexon / Nexon.ev and MG Hector Tomahawk EV / PHEV).
- Keep trims, editions, body styles, seating configurations and powertrain derivatives attached to their canonical model family unless the OEM gives them separate model identities.
- Preserve OEM spelling and naming (including Citroën suffix-X names and official capitalization).
- Do not convert model-level starting prices into variant prices. Do not create city on-road observations from ex-showroom amounts.
- Every model candidate still requires exact current variant, price, model-year and source-reuse review before staging or publication.


## Variant-source audit worklog (2026-11-06)

The companion `variant-source-audit.csv` begins Step 5 with an official-source pilot for Hyundai. It is a **source-quality worklog**, not a verified variant or price import file.

- Creta: the official price page exposes 38 named petrol/diesel price rows, but the highest displayed row (₹20,45,700) conflicts with the official model listing maximum (₹20.11 lakh). Keep all observed values quarantined pending confirmation.
- Venue: official page describes HX trims and powertrain/gearbox combinations, but the captured variant-price table is empty.
- Exter: official page describes HX and legacy trim labels plus petrol/CNG families, but the captured variant-price table is empty.
- Verna: official page describes HX trim labels and MPi/Turbo GDi engines, but the captured variant-price table is empty.
- The audit does not infer exact trim-to-engine mappings, model year, or current orderability where the OEM page does not expose them.
- No variant prices have been approved for import. Dealer/configurator confirmation and source reuse review remain mandatory.

### Variant evidence acceptance rules

- Capture the exact OEM variant label, model year (when stated), fuel/powertrain, transmission, seating/body configuration, price amount, price basis, city/state scope, effective date, source URL and checked date.
- Preserve the OEM's exact naming. Do not manufacture trim combinations by crossing engine and transmission lists.
- Keep ex-showroom and on-road observations separate; never calculate one from the other.
- A missing or dynamically empty OEM table is not evidence that the model has no variants.
- Conflicting OEM values are quarantined and must not be resolved by selecting the more convenient value.
- Third-party variant/price pages may be used as discrepancy leads only, not as final publication evidence when an OEM/dealer source is required.


### Hyundai follow-on batch (2026-11-06)

The variant-source worklog now covers **14 Hyundai models**: Creta, Venue, Exter, Verna, Aura, Grand i10 NIOS, i20, i20 N Line, Alcazar, Creta Electric and IONIQ 5 (11 rows because the original four are retained and seven more were added).

- Aura: official feature matrix identifies E/S/SX/SX(O) and references SX+ AMT; confirm current SX+ retail naming and prices.
- Grand i10 NIOS: official price-page text names petrol MT, AMT and CNG trim families; dynamic city-price table was empty in the captured content.
- i20: official page names Era through Asta(O) Knight trim families and confirms 1.2L petrol MT/IVT; no individual price rows were exposed.
- i20 N Line: official page names N6/N8, dual-tone variants and 6MT/7DCT; no individual price rows were exposed.
- Alcazar: official page confirms petrol/diesel, MT/DCT/AT and 6-/7-seat layouts; exact trim labels were not exposed, so no combinations were generated.
- Creta Electric: official highlights page identifies five 42 kWh and four 51.4 kWh configurations; BaaS pricing must remain separate from full-battery vehicle pricing.
- IONIQ 5: the official catalogue exposes a single model-card ex-showroom amount and 72.6 kWh battery, not a verified variant price matrix.

The Hyundai batch now has 14 model records in the worklog. All remain evidence-review records; none is an approved variant-price import. The source worklog deliberately records empty/dynamic price tables as missing evidence rather than filling values from third-party aggregators.


- Venue N Line: N6 MT, N6 DCT and N10 DCT are explicitly described; the official city-price table is empty in captured content.
- Creta N Line: official page confirms 1.5L Turbo GDi petrol and 6MT/7DCT, but does not expose exact trim labels in captured content.
- BAYON: official page confirms 1.5L MPi petrol, 6MT across the range and IVT on selected trims, but does not name the individual trims or expose prices.

Hyundai model coverage in the source worklog is now **14 of 14 non-taxi models** displayed in the official India catalogue. Prime-HB and Prime-SD are taxi products and remain outside the passenger retail scope. This does not mean all 14 models have complete variant data: exact variant prices remain unapproved and several pages expose only model-level or powertrain-level information.


## Kia variant-source pilot (2026-11-06)

The companion variant worklog now includes three Kia model reviews, using Kia India pages:

- **Sonet:** official trim comparison exposes prices for seven trims, while HTK and HTX price cells are not rendered in the captured result. The official brochure is needed to map exact engine/transmission applicability; missing values remain blank.
- **Seltos:** official comparison page exposes prices for 12 named trims (HTE through X-Line(O)). Treat these as observed OEM comparison-page amounts only; verify city/ex-showroom basis, effective date and powertrain-specific applicability before importing.
- **Carens Clavis EV:** official comparison page exposes nine trim/battery combinations and their displayed prices. Keep 42 kWh Standard Range and 51.4 kWh Extended Range distinct, and preserve 6-/7-seat configuration applicability. Battery-as-a-Service is a separate pricing/financing basis and must not be merged with full vehicle price.

No Kia variant price is approved for production import yet. Source reuse terms, price basis, effective date and dealer confirmation remain outstanding. The internal dealer circular and third-party reporting are not treated as publication-grade evidence where official Kia pages can provide the same facts.


### Kia follow-on batch (2026-11-06)

The Kia source worklog now includes **seven models**: Sonet, Seltos, Carens Clavis EV, Syros, Carens Clavis, Carnival and EV6.

- **Syros:** official trim-comparison page exposes seven named trims and displayed prices, plus engine/transmission availability. Preserve the comparison matrix to resolve which powertrain/gearbox is offered with each trim; do not duplicate one trim into multiple variants without that mapping.
- **Carens Clavis:** the official 2026 brochure identifies core trim names, petrol/diesel engine families, transmission families and seating configurations. It is a brochure snapshot; the 2026 GT-Line/X-Line and HTX(O) A additions require a current official configurator/price-list check. A third-party article reports a refreshed 2026 price matrix, but this is retained as a discrepancy lead only and is not used as approved price evidence.
- **Carnival:** official specifications confirm a 2.2L diesel, 8AT and 7-seat configuration. The official page's ₹0,00,000 placeholder is invalid as a price and must not be imported; current orderability and price need dealer confirmation.
- **EV6:** official comparison page exposes GT-Line and GT-Line AWD, mapping 77.4 kWh RWD/AWD respectively. The GT-Line displayed ₹60,96,638 while AWD has no numeric amount; the displayed figure is kept as MSRP pending confirmation of India price basis and effective date.
- The prior Sonet, Seltos and Carens Clavis EV observations remain unchanged.

The Kia batch is still a research worklog. Officially displayed prices are not approved until price basis, effective date, variant-to-powertrain mapping and source-reuse checks are complete. No Firestore or catalogue writes have been made.


- **Carens:** current official showroom content renders Premium (O) Petrol MT and Premium (O) CNG MT. Legacy trim families are not carried forward. A third-party listing also shows a diesel MT configuration, but it is not corroborated by the captured official page and remains excluded pending dealer confirmation.
- **EV9:** the official India showroom page explicitly labels the vehicle an "Overseas model". It displays GT-Line AWD as a single trim but does not establish India retail availability or an India price. Keep it out of the approved India variant queue until local orderability is confirmed.

The Kia source worklog now covers **nine model candidates**, including the two unresolved cases above. Do not interpret model-catalogue presence as proof of India retail sale: EV9 remains unconfirmed, and Carnival still needs dealer confirmation.


## Toyota variant-source pilot (2026-11-06)

The companion variant worklog begins Toyota with five model reviews: Innova Crysta, Innova Hycross, Urban Cruiser Hyryder, Glanza and Urban Cruiser Taisor.

- **Innova Crysta:** Toyota's official showroom confirms diesel G/GX/VX/ZX grades, 5-speed manual and 7-/8-seat applicability. Toyota's 2026-11-05 release confirms retail grades GX, GX+, VX and ZX, and separately introduces Crysta LIMO for fleet/commercial customers. Do not mix the fleet LIMO identity or fleet-only GX-SLF with the retail passenger variants. The official release gives GX Fleet prices only; do not apply them to retail GX.
- **Innova Hycross:** Toyota's official showroom confirms petrol G-SLF/GX/GX(O) and strong-hybrid VX/VX(O)/ZX/ZX(O), with 7-/8-seat availability varying by grade. Only the model starting price is captured; individual grade prices need an official price list/configurator capture.
- **Urban Cruiser Hyryder:** Toyota's official page confirms separate E-CNG, Neodrive and Hybrid families, and explicitly names E-CNG S and G with 5MT. The full grade/engine/transmission matrix and exact prices remain incomplete.
- **Glanza:** the current Toyota catalogue confirms the model, but a complete official current grade/price matrix was not captured. A 2026 facelift price table exists in secondary reporting, but it is not accepted as final evidence without Toyota corroboration.
- **Urban Cruiser Taisor:** Toyota's official launch release documents the original grade/powertrain matrix and introductory 2024 prices. This is historical evidence only; it cannot be treated as a current 2026 variant/price list.

The Toyota batch currently contains **five model records**. Official source evidence is intentionally separated from historical launch prices, model-card starting prices and fleet-only variants. No Toyota price is approved for production import. Continue with current official price-list/configurator capture and dealer confirmation where the official public pages do not expose full matrices.


### Toyota follow-on batch (2026-11-06)

Toyota variant-source coverage now includes **eight models**: Innova Crysta, Innova Hycross, Urban Cruiser Hyryder, Glanza, Urban Cruiser Taisor, Fortuner, Hilux and Camry.

- **Fortuner:** official specifications confirm petrol 2.7L and diesel 2.8L powertrains, with 5MT/6MT/6AT and 2WD/4WD applicability depending on engine/grade. The full trim-to-powertrain matrix and prices were not captured; do not generate every possible combination.
- **Hilux:** official page identifies STD MT, High MT and High AT, all within the 2.8L diesel 4WD range. STD/High MT use 6MT with iMT; High AT uses 6AT. Only a model starting price is visible.
- **Camry:** official page confirms one India petrol-hybrid configuration with 2.5L engine, e-CVT and five seats. The exact retail grade label and variant-specific price are not exposed.

The official Toyota pages also state that website pricing and availability may change and that online orderability depends on city/dealer coverage. These constraints are retained in the audit: starting prices are model-level observations, not variant prices, and current manufacturable/orderable status must be verified at the configurator/dealer stage.

The Toyota batch has eight model records. No price rows have been approved for production import; exact current grade/variant price evidence remains incomplete for every model in this pilot.


### Toyota completion and MG Motor variant-source batch (2026-11-06)

Toyota's variant-source worklog now covers all 13 model candidates in the model audit, including Rumion, Urban Cruiser Ebella, Vellfire, Land Cruiser 300 and Legender. The companion variant-source-audit.csv now also contains the first **10 MG Motor model reviews**: Comet EV, Windsor EV, ZS EV, Hector, Astor, Hector Tomahawk EV, Hector Tomahawk PHEV, Majestor, Cyberster and M9.

- MG official product pages expose current trim names and displayed prices for Comet EV, Windsor EV, ZS EV, Hector and Astor. For EVs, Battery-as-a-Service (BaaS) upfront amounts and per-kilometre battery rental are kept separate from full-battery ex-showroom prices.
- Hector Tomahawk EV and PHEV official launch material publishes separate variant-wise price tables and seating configurations. The two powertrains remain separate model identities in the candidate audit.
- Majestor's current official page and separate official launch/price announcements do not map cleanly to one variant-price matrix; its price mapping is quarantined.
- MG SELECT lists Cyberster and M9 with single product prices; official Couture Editions are limited special editions and are not treated as general retail trims. Exact standard grade labels remain to be confirmed.
- No MG price is approved for production import. Price effective date, city scope, exact powertrain mapping, dealer orderability and OEM content-reuse permission remain review gates.

The variant worklog now contains 46 model rows: Hyundai 14, Kia 9, Toyota 13 and MG 10. This is source-review coverage only, not a production import manifest.


## Tata Motors variant-source pilot (2026-11-06)

The companion variant-source worklog now contains reviews for all **16 Tata model candidates** from the current model audit: Sierra, Sierra.ev, Harrier, Harrier.ev, Safari, Nexon, Nexon.ev, Punch, Punch.ev, Altroz, Tiago, Tiago.ev, Curvv, Curvv.ev, Tigor and Tigor.ev.

- **EV pages with usable variant evidence:** Sierra.ev (63/75 kWh families, ACFC and AWD/QWD derivatives); Harrier.ev (65/75 kWh, RWD/QWD, ACFC and Stealth); Nexon.ev (30 kWh MR and 45 kWh LR); Punch.ev (30/40 kWh); Tiago.ev (19.2/24 kWh); Curvv.ev (Series X current trim/price evidence); Tigor.ev (legacy trim labels observed, current retail orderability unconfirmed).
- **ICE product-page access:** the official catalogue links to Sierra, Harrier, Safari, Nexon, Punch, Altroz and Curvv product pages, but those detail-page fetches returned HTTP 403 in this audit session. No trim or price values were inferred from the corresponding EV models or older third-party listings.
- **Tiago ICE:** the official 2026 price page exposes Smart/Pure and CNG trim cards, including Pure+A CNG at ₹7,49,990 and Pure+A CNG Automatic at ₹8,04,990. Other dynamic price cells were blank in the captured result; do not fill them from secondary launch reporting.
- **Tigor ICE:** the model remains in the existing candidate list, but it was absent from the current official Tata Cars model navigation captured on 2026-11-06. Current retail availability needs confirmation.
- **Catalogue reconciliation lead:** the current Tata Cars homepage also displays **Aeris**, which is not in the 16-row Tata model candidate set. Add it to the Step 4 model reconciliation queue for identity, current India retail orderability and source verification. The homepage also lists XPRES, which remains outside this private passenger-car scope unless a distinct retail passenger variant is substantiated.

The Tata worklog has 16 model rows, but it is not a complete approved variant catalogue. The official EV price pages contain dynamic blank price cells, the ICE detail pages were inaccessible to the research fetch, and Tigor orderability is unresolved. No Tata variant price is approved for production import. Preserve ex-showroom All India prices, model-year context, battery capacity, drivetrain, charger pack and edition as separate attributes. Review OEM terms and permitted reuse before bulk ingestion.


## MINI variant-source pilot (2026-11-06)

The companion variant-source worklog now contains reviews for all **five MINI model candidates** from the current model audit: Cooper, Cooper Convertible, Countryman C, Countryman Electric and John Cooper Works Countryman ALL4.

- **Cooper:** official India page shows a Classic Trim example and refers to four engine/performance options and four style levels, but the captured page does not expose the exact India retail variant combinations or prices.
- **Cooper Convertible:** official FAQ confirms Cooper and Cooper S performance levels and Classic/Favoured/JCW style packages. The page shows ₹58,50,000, but no grade-wise price matrix or exact performance/style combination mapping was captured.
- **Countryman C:** official range page displays a ₹47,50,000 model starting amount; the product page confirms 156 HP. Favoured Style appears in imagery, not as a separately priced retail grade.
- **Countryman Electric:** official page confirms a 64.6 kWh battery, 204 PS and 462 km WLTP range; official range page shows ₹55,65,000 as a model starting amount. No India variant-price matrix was captured.
- **John Cooper Works Countryman ALL4:** official page confirms 300 HP, 400 Nm and ALL4 AWD; official range page displays ₹66,15,000 as a model-level amount. No additional India grade/price matrix was exposed.

The MINI India range page currently lists these five product families. Do not import international-market trim names or manufacture variant combinations by crossing engine/performance levels with style packages. Model-level starting prices and a single page price are not variant-level price rows. Exact configurator output, price effective date, city scope and source-reuse permission remain review gates. No MINI variant price is approved for production import.
