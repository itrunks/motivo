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


## Force Motors variant-source audit (2026-11-06)

The companion variant-source worklog now includes the Force Motors **Gurkha** candidate, completing this brand's single-model review.

- The current official Gurkha product page presents two body/seating configurations: **3 Door (4-seater)** at **₹16,68,400 ex-showroom** and **5 Door (7-seater)** at **₹18,01,200 ex-showroom**. These are live OEM page observations captured on 2026-11-06; the page does not state a price effective date.
- The official e-brochure and Force Motors' 2024 launch release describe a 2.6L (2596cc) turbocharged intercooled diesel engine, 140PS and 320Nm, 5-speed manual transmission and shift-on-the-fly 4WD (2H/4H/4L). The 3-door and 5-door seating configurations remain derivatives of the same Gurkha model, not separate model identities.
- Some third-party 2026 listings show different prices. Keep the current official OEM page amounts as source observations, but confirm the price effective date and dealer quotation before production import. The official page excludes insurance, registration, road tax and accessories.
- No additional trim, fuel or transmission combinations have been inferred. No price is approved for production import; source-reuse review and dealer/orderability confirmation remain required.

The variant-source worklog now contains **68 model rows**: Hyundai 14, Kia 9, Toyota 13, MG Motor 10, Tata Motors 16, MINI 5 and Force Motors 1. This remains a research worklog, not a production import manifest.


## Tesla variant-source audit (2026-11-06)

The companion variant-source worklog now includes the Tesla **Model Y** candidate.

- Tesla India's official Model Y page presents **Model Y Premium** and **Model Y L** as the two current product families. The official India new-inventory page names **Premium Rear-Wheel Drive** (five seats) and **L All-Wheel Drive** (six seats).
- Tesla's official India model page states up to **500 km WLTP** for the rear-wheel-drive Model Y and **681 km WLTP** for Model Y L. It confirms dual-motor AWD and up to six seats for Model Y L. These are OEM WLTP claims, not India-certified range values.
- The official new-inventory page currently displays configuration-specific rupee totals: Premium Rear-Wheel Drive at ₹52,02,460 (Stealth Grey) and ₹53,94,360 (Pearl White Multi-Coat); L All-Wheel Drive listings range from ₹63,23,560 to ₹66,06,360 across the displayed paint/interior combinations. The page labels these as new-vehicle inventory amounts but does not identify them as ex-showroom base prices.
- Tesla launch pricing reported from company announcements was ₹50,89,000 for Premium RWD and ₹61,99,000 starting for Model Y L. Those launch/base amounts differ from current live inventory configuration totals; preserve them as separate observations, not a single price field. Current price basis, option/paint uplifts, effective date, taxes and delivery charges require direct configurator/dealer confirmation.
- Tesla's captured India product page does not expose battery capacity in kWh. Do not import third-party estimated battery capacities or motor outputs as OEM-confirmed facts. The discontinued earlier Model Y RWD/Long Range RWD entries are not carried forward as current variants.

The Tesla row is a source observation only. No Tesla variant price is approved for production import; exact configurator price basis, current orderability, model-year applicability and OEM content-reuse permission remain review gates.


## VinFast variant-source audit (2026-11-06)

The companion variant-source worklog now includes all **three VinFast model candidates** from the current model audit: VF 6, VF 7 and VF MPV 7.

- **VF 6:** the official India launch release identifies Earth, Wind and Wind Infinity. All use a 59.6 kWh battery and FWD; Earth is specified at 130 kW/250 Nm and 468 km ARAI range, while Wind/Wind Infinity use 150 kW/310 Nm and 463 km. Wind Infinity adds the fixed panoramic glass roof. The current official product page displays ₹18,19,000 as a model-level starting amount, not a per-trim price.
- **VF 7:** the official launch release identifies Earth, Wind, Wind Infinity, Sky and Sky Infinity. Earth uses 59.6 kWh, 130 kW/250 Nm, FWD and 438 km ARAI range. Wind/Wind Infinity use 70.8 kWh, 150 kW/310 Nm, FWD and 532 km. Sky/Sky Infinity use 70.8 kWh, dual-motor AWD, 260 kW/500 Nm and 510 km. Infinity grades add the fixed panoramic glass roof. The official product page displays a ₹22,99,000 model-level starting amount, but no current trim-wise price matrix was captured.
- **VF MPV 7:** the official 2026-04-15 launch release describes one seven-seat FWD configuration, 60.13 kWh usable battery, 150 kW/280 Nm and 517 km ARAI range. No individual grade/trim names are exposed in the captured India product page. The page displays ₹20,39,000, while the official homepage displays ₹24.49 lakh as the starting amount. This is a material OEM source conflict; do not choose either amount or infer a BaaS/price-basis explanation without confirmation.
- Third-party 2026 variant price tables were consulted only as discrepancy leads. They are not substituted for missing official OEM variant price rows. The official VinFast total-cost page itself warns that displayed pricing is general reference and final pricing varies by model, variant, configuration, location, taxes, fees and promotions.
- No variant prices are approved for production import. Obtain dated official dealer/configurator quotations, reconcile current price basis, and confirm the current homologated battery/specification values before staging.

The VinFast batch adds three source-review rows. The overall variant-source worklog now contains **72 model rows**: Hyundai 14, Kia 9, Toyota 13, MG Motor 10, Tata Motors 16, MINI 5, Force Motors 1, Tesla 1 and VinFast 3. This remains a research worklog, not a production import manifest.


## Cross-brand variant-source quality review (2026-11-06)

A structural and source-quality review was completed across the 72-row `variant-source-audit.csv` and the 251-row `current-model-audit.csv`.

### Integrity and coverage

- 72 variant-source rows, 8 columns, no blank fields, malformed rows, or duplicate brand/model pairs.
- All 72 rows match an existing model candidate; no extra rows.
- 179 of 251 model candidates (71.3%) still have no variant-source row. Coverage is 28.7% across 9 of 35 brands; 26 brands have not yet entered the variant-source pass.
- The file currently uses 23 distinct audit-status labels. None is an approved/import-ready status. A controlled status vocabulary should be introduced in a later schema cleanup.

### Source and price exceptions

- **Hyundai Creta:** current official price page displays 38 petrol/diesel price rows, with the highest displayed at ₹20,45,700. The highlights page describes seven broader variant families. The earlier ₹20.11 lakh model-listing ceiling does not align with the detailed price table. Reclassified as a source-scope/version discrepancy, not a confirmed current price conflict. Verify effective date and city scope before import.
- **MG Majestor:** official current product page lists three Savvy seating/drivetrain configurations and a ₹43.49 lakh starting price. The May launch release contains historical prices; November secondary reporting says all three variants received a ₹1 lakh increase, to ₹43.49 lakh (4X2 6S/7S) and ₹45.99 lakh (4X4 7S). No updated official variant-price matrix was captured; obtain a dated dealer/configurator price list.
- **Tesla Model Y:** official inventory shows configuration-specific totals by paint/interior. These are not directly comparable with launch ex-showroom prices. Reclassified as price-basis pending, not a direct source conflict.
- **VinFast source-domain correction:** the candidate audit previously referenced `vinfastautos.in`. The manufacturer's India product pages are on `vinfastauto.in`; all three candidate and variant-source links now point to the exact VF 6, VF 7 and VF MPV 7 product pages.
- **VinFast VF MPV 7:** official product page currently displays ₹20,39,000 for the single configuration. A 2026-11-04 secondary report attributes this to a ₹4.10 lakh reduction from the ₹24.49 lakh launch price. The official homepage does not display a conflicting price. The row remains subject to effective-date and dealer confirmation.
- **Kia Carnival:** the official page renders ₹0,00,000 as a placeholder; it is invalid and must not be ingested.
- **Tata Motors:** seven official ICE product-page fetches returned HTTP 403. No variant or price data was inferred from those pages.

### Import gate

- Zero prices are approved for production import by this worklog.
- Before import, capture exact OEM variant identity, model-year applicability, powertrain/transmission/seating mapping, numeric price and price basis, effective date, city/state scope where applicable, current orderability, and OEM content-reuse permission.
- Keep ex-showroom, inventory totals, on-road prices, BaaS upfront payments and per-kilometre rentals as separate price types.
- The remaining 179 candidates remain unreviewed. This 72-row pilot is not a complete India passenger-car variant catalogue.


## Maruti Suzuki variant-source audit (2026-11-06)

The variant-source worklog now includes all **17 Maruti Suzuki model candidates** from the model audit: Alto K10, Celerio, Eeco, Ertiga, S-Presso, Swift, Victoris, Wagon R, Dzire, Brezza, Baleno, Grand Vitara, Fronx, Jimny, XL6, Invicto and eVitara.

### Arena models

- **Alto K10:** official page exposes Std (O), LXi (O), VXi (O), VXi+ (O), CNG and AGS families. Some exact card prices are visible; complete selector-to-price matrix still needs capture.
- **Celerio:** official price page exposes LXi/VXi/ZXi and AGS variants, plus S-CNG filter. Captured card prices are partial; some rendered transmission text is inconsistent, so use exact card headings and confirm the remaining rows.
- **Eeco:** official page mixes passenger and ambulance products. Only 5-seat/6-seat passenger, AC and 5-seat AC CNG configurations were retained. Ambulance and ambulance shell were excluded from this passenger catalogue. The page FAQ contains stale/conflicting cargo-price copy.
- **Ertiga:** official price page exposes nine grade/powertrain combinations (LXi/VXi/ZXi/ZXi+ petrol manual/automatic and VXi/ZXi CNG) with numeric displayed prices. 1.5L K15C Smart Hybrid petrol and S-CNG are separate fuel configurations; 5MT/6AT mapping is retained.
- **S-Presso:** eight petrol/CNG manual/AGS grade combinations are exposed. Seven displayed card amounts were captured; VXi+ (O) AGS price is not captured.
- **Swift:** official price page exposes LXi/VXi/VXi(O)/ZXi/ZXi+ petrol, AMT and S-CNG variants. Multiple card prices were captured, but the CNG AGS selector rows need a full configurator check before the matrix is considered complete.
- **Victoris:** official price page exposes a broad 21-card matrix across petrol, S-CNG, strong hybrid, 2WD/4WD and manual/automatic. Individual displayed prices were captured from the official page, but the full matrix still requires current effective-date and grade-mapping validation.
- **Wagon R:** official page exposes petrol, S-CNG and a FLEX FUEL filter. LXi/VXi/ZXi grade observations and some prices were captured. Flex-fuel retail orderability and full AGS/CNG mapping need confirmation.
- **Dzire:** official price page exposes nine named petrol/S-CNG grades with numeric displayed prices. Its top-price FAQ amount does not match the price-card amount; retain the card observation and verify before import.
- **Brezza:** official price page explicitly says Delhi ex-showroom prices effective 2026-07-24 and exposes grade prices. The selector also renders anomalous “Turbo MT” labels, inconsistent with the 1.5L petrol/S-CNG powertrain evidence. Do not create turbo variants until Maruti clarifies the selector.

### NEXA models

- **Baleno:** official NEXA page lists Sigma/Delta/Zeta/Alpha/Alpha(O) petrol MT/AMT and Delta/Zeta CNG MT/AGS families. No numeric grade-wise price matrix captured.
- **Grand Vitara:** official NEXA page separates petrol, strong hybrid, S-CNG and ALLGRIP SELECT 4x4. Exact grade and transmission mapping was captured from the official variant comparison; full current prices were not captured.
- **Fronx:** official NEXA page maps 1.0L Boosterjet turbo, 1.2L K-series petrol and S-CNG to distinct trim families. No numeric grade-wise price matrix captured.
- **Jimny:** official NEXA page lists Zeta/Alpha with MT/AT; brochure identifies 1.5L K15B petrol, 5MT/4AT and ALLGRIP PRO 4WD. Current orderability and price still require confirmation.
- **XL6:** official NEXA page lists six Smart Hybrid combinations and Zeta CNG, with 6-seat layout. A FAQ typo “Apha+” was normalized to Alpha+ based on the official variant heading.
- **Invicto:** official NEXA page lists Zeta+ 7-seat, Zeta+ 8-seat and Alpha+ 7-seat, strong hybrid only. Do not carry forward an older Alpha+ 8-seat combination without current evidence.
- **eVitara:** official NEXA India page and configurator entry point are confirmed, but current India grade names, battery-to-grade mapping and prices were not extractable. Do not infer from international specifications or third-party variant pages; inspect the India configurator/brochure in a follow-up.

The Maruti Suzuki batch adds 17 source-review rows. The overall variant-source worklog now contains **89 model rows** across 10 brands. It remains a research worklog: no Maruti price is approved for production import. Confirm exact price basis/effective date, live city/dealer orderability, model-year applicability and OEM content-reuse permission before staging.


## Mahindra variant-source audit

Added 13 Mahindra source-review rows to `data/variant-source-audit.csv`. Current total: 102 rows across 11 brands. No prices approved for production import; current orderability, exact variant mapping, price date/scope, EV charger/BaaS basis and OEM reuse permission remain validation gates.

## Audi variant-source audit (2026-11-06)

Added source-review rows for all **nine Audi model candidates**: Q3, Q5, Q7, Q8, A4, A6, Q3 Sportback, SQ8 and RS Q8 Performance.

- Audi India's current model overview groups the lineup into six families: Q3, Q5, Q7, Q8, A4 and A6. Q8 contains three distinct products: Q8, SQ8 and RS Q8 Performance. The audit preserves those three candidate identities separately.
- **Q3:** the 2026-10-16 OEM launch release confirms the new 2.0L TFSI quattro configuration and a ₹51.99 lakh introductory ex-showroom model price, but does not publish grade names or a full variant-price matrix. Secondary-reported Nova/Zenith details were not treated as OEM-confirmed variant data.
- **A4:** the official product page identifies Premium, Premium Plus and Technology trim/equipment labels, but current grade-wise numeric prices and full equipment mapping were not captured.
- **Q5, Q7 and A6:** current official product pages confirm the product identities, but the captured OEM pages did not expose a complete current India trim-price matrix. Older brochure labels are not assumed to be current orderable variants.
- **Q3 Sportback:** it remains in the candidate audit, but is not independently shown in the current Audi India model grid. A legacy sitemap/navigation link is not sufficient evidence of current orderability; dealer confirmation is required.
- **SQ8 and RS Q8 Performance:** official India product/teaser pages identify each separately and describe their performance configurations. Current India grade-wise prices and full orderable configuration tables were not captured.
- Audi's official Price Reckoner states that ex-showroom prices exclude TCS, but the embedded dynamic price table did not render in this research capture. No third-party price was substituted as OEM evidence.

No Audi price is approved for production import. Confirm current orderability, exact trim identity, model-year applicability, price basis/effective date and dealer scope, and OEM content-reuse permission before staging. The Audi batch adds nine rows; the overall variant-source worklog now contains **111 model rows** across 12 brands, with 140 of 251 model candidates still uncovered.

## BMW variant-source audit (2026-11-06)

Added source-review rows for all **22 BMW model candidates**: 2 Series Gran Coupe, 3 Series Long Wheelbase, 5 Series Long Wheelbase, 7 Series, M340i, X1, X1 Long Wheelbase, X3, X5, X6 M60i, X7, i4, i5, i5 Long Wheelbase, i7, iX, iX1 Long Wheelbase, M2, M4 Competition, M5, M440i Convertible and XM.

- The current BMW India model catalogue distinguishes standard, M Performance, M and electric products. Model-level starting prices are displayed for many entries, but those amounts are not automatically grade-level prices.
- **India configuration names captured:** 218 M Sport; 330Li M Sport; 530Li M Sport LWB; 740 M Sport; M340i xDrive; X1 sDrive18i/sDrive18d; X3 30 xDrive and X3 20 xDrive/20d family references; X5 xDrive40i/xDrive30d; X6 M60i xDrive; X7 xDrive40i/xDrive40d; i5 M60; i5 eDrive35L M Sport; i7 50 xDrive M Sport; iX1 eDrive20L M Sport; M4 Competition M xDrive; M440i xDrive Convertible.
- **Separate model identities preserved:** standard X1 vs X1 LWB; standard i5 vs i5 LWB; ICE 7 Series vs i7; X6 M60i; M340i; M2; M4 Competition; M5; XM. Do not merge global-market derivatives or optional equipment packages into India retail variants.
- **Price observations:** BMW India model pages show starting amounts for the 2 Series Gran Coupe, 3 Series LWB, 5 Series LWB, X1, X3, X5, X6 M60i, X7, i5 LWB, iX1 LWB, M2, M4 Competition, M5 and M440i Convertible, among others. Most are model/one-configuration starting prices, not full variant-price matrices. BMW states prices are subject to change and the invoice-date price applies; ex-showroom amounts exclude road tax, TCS, RTO, statutory/local levies and insurance.
- **Price/source caveats:** i7's current model-page starting price and special-offer starting amount differ; X7 petrol/diesel/M-model price cards require exact configuration reconciliation; X3 listing contains multiple engine/grade family labels and should not be cross-joined. These are preserved as scope/price-basis checks, not normalized into one price.
- **Orderability exception:** i4 and X1 LWB are not independently substantiated with complete current India variant matrices in the captured official model-page content. i4 in particular is not visible in the current model-navigation capture; confirm current retail orderability with BMW India/dealer before treating it as active.
- BMW Group India's July 2026 announcement confirms a price increase of up to 2% effective 2026-07-01 across BMW/MINI range. Current page prices remain subject to invoice-date confirmation; the announcement does not supply variant-level price lists.

No BMW price is approved for production import. Confirm current orderability, exact India trim identity, model-year, price basis/effective date, city/dealer scope and OEM content-reuse permission before staging. The BMW batch adds 22 rows; the overall variant-source worklog now contains **133 model rows** across 13 brands, with 118 of 251 model candidates still uncovered.

## BYD variant-source audit (2026-11-06)

Added source-review rows for all **four BYD India model candidates**: ATTO 3, eMAX 7, SEAL and SEALION 7.

- **ATTO 3:** current BYD India price page exposes Dynamic (₹24.99 lakh), Premium (₹30.35 lakh) and Superior (₹34.49 lakh). OEM launch release maps Dynamic to 49.92 kWh and Premium/Superior to 60.48 kWh; range claims are retained with their ARAI/NEDC test basis.
- **eMAX 7:** current OEM price page lists Comfort 6/7-seat and Superior 6/7-seat configurations at ₹27.90/28.30 lakh and ₹29.30/29.90 lakh respectively, all with 71.8 kWh. The 2024 launch release used Premium/Superior and a 55.4/71.8 kWh battery split; current price page and historical launch matrix are not merged. The Premium-to-Comfort rename is also reported in July 2026 secondary coverage; confirm 55.4 kWh availability directly with BYD before restoring it to the current range.
- **SEAL:** current OEM page lists Dynamic, Premium and Performance at ₹41.50/46.20/53.65 lakh. The 2025 MY release maps Dynamic RWD to 61.44 kWh, Premium RWD to 82.56 kWh and Performance AWD to 82.56 kWh; its earlier price amounts are retained only as historical reference.
- **SEALION 7:** current OEM page lists Dynamic ₹41.90 lakh, Premium ₹49.90 lakh and Performance ₹55.90 lakh. OEM releases confirm Premium/Performance 82.56 kWh and their NEDC range claims. The First Anniversary Edition was a limited booking/offer window, not a separate ongoing standard trim.

The current OEM price page is used for current displayed grade amounts; historical dated launch/price releases are retained only for specification mapping and price-history context. Confirm price effective date, dealer quotation, exact battery/drive mapping for the Dynamic SEALION 7, and OEM content-reuse permission before staging. No BYD price is approved for production import.

The BYD batch adds four rows. The overall variant-source worklog now contains **137 model rows** across 14 brands; 114 of 251 model candidates remain without variant-source rows.

## Citroën variant-source audit (2026-11-06)

Added source-review rows for all **five Citroën model candidates**: AircrossX, ë-C3X, C5 Aircross, C3X and BasaltX.

- **AircrossX:** official brochure identifies YOU/PLUS/MAX and 1.2L PureTech 82 naturally aspirated 5MT and PureTech 110 turbo 6MT/6AT powertrains, with 5/7-seat applicability. The 2026-09-07 OEM release adds YOU Turbo Comfort Edition (₹10.69 lakh introductory) and MAX NA (₹11.62 lakh introductory); all NA variants are available in petrol and CNG. Full current price/grade matrix is not captured.
- **ë-C3X:** official page and launch releases confirm Live, Live(O), Shine, Extended range and single-speed electric configuration, with up to 330km MIDC-I/II. BaaS starting amount (₹6.99 lakh + ₹2.26/km in September release) is kept separate from full-battery price. No official grade-wise full-purchase price matrix captured.
- **C5 Aircross:** current official page displays one Shine automatic, 2.0L diesel configuration (177PS/400Nm). No numeric current variant price rendered. Do not carry forward historic grades/prices without fresh OEM confirmation.
- **C3X:** official product page exposes Live, Live(O), Feel, Feel(O) and Shine trim families, with selected manual/automatic, petrol turbo/NA and CNG applicability. The exact current trim-to-powertrain mapping and numeric price matrix need configurator confirmation.
- **BasaltX:** official page confirms PureTech 82 NA 5MT and PureTech 110 turbo 6MT/6AT. The September OEM release adds YOU Turbo (₹9.99 lakh introductory) and MAX NA (₹11.34 lakh introductory); MAX NA is offered in petrol and CNG. The YOU Turbo Comfort Edition is an equipment package; it is not automatically treated as a separate mechanical variant.

The September 2026 OEM release is the latest captured official update for AircrossX, BasaltX and ë-C3X. Introductory prices and BaaS are preserved with their specific basis; they are not generalized into a complete variant-price catalogue. Confirm current dealer/configurator matrix, price effective date, CNG availability by exact trim, seating/powertrain mapping and OEM content-reuse permission before staging. No Citroën price is approved for production import.

The Citroën batch adds five rows. The overall variant-source worklog now contains **142 model rows** across 15 brands; 109 of 251 model candidates remain without variant-source rows.

## Honda variant-source audit (2026-11-06)

Added source-review rows for all **five Honda model candidates**: New City, New Amaze, Amaze - 2nd Gen, All New ZR-V and New Elevate.

- **New City:** official Honda pages confirm petrol SV/V/ZX/ZX+ MT and V/ZX/ZX+ CVT, plus e:HEV ZX+ e-CVT. The 2026 OEM launch price matrix provides Delhi ex-showroom grade prices; reconfirm city and invoice-date amounts before import.
- **New Amaze:** official OEM release confirms V/VX/ZX with 5MT and CVT. The launch prices were explicitly introductory for 45 days in December 2024 and are not treated as current. Current homepage displays a model starting price but no full grade-wise price matrix.
- **Amaze - 2nd Gen:** current Honda homepage still lists the second-generation model. The captured official city price page displays S MT/S CVT amounts inconsistent with the homepage starting amount, so the row is marked price-source conflict and current orderability requires dealer confirmation. It remains separate from the third-generation V/VX/ZX New Amaze.
- **All New ZR-V:** official release confirms one India CBU configuration with a 2.0L e:HEV hybrid system and e-CVT. The current homepage amount is higher than the July 2026 introductory launch price; preserve those as separate dated observations and confirm current invoice price.
- **New Elevate:** the October 6, 2026 OEM facelift release provides a full Delhi ex-showroom price matrix for SV/V/VX/ZX/ZX+ and ZX+ Black Edition across MT/CVT. This current facelift matrix supersedes older pre-facelift pricing observations.

No Honda price is approved for production import. Confirm current dealer/city price, price effective date, model-year and orderability (especially 2nd Gen Amaze), and OEM content-reuse permission before staging.

The Honda batch adds five rows. The overall variant-source worklog now contains **147 model rows** across 16 brands; 104 of 251 model candidates remain without variant-source rows.

## Jeep variant-source audit (2026-11-06)

Added source-review rows for all **four Jeep India model candidates**: Compass, Meridian, Wrangler and Grand Cherokee.

- **Compass:** OEM comparator lists Sport, Longitude, Trail, Limited (O), Model S (O), Track and BlackShark. The 2026-10-26 OEM press release adds Sport FWD 9AT at ₹21.99 lakh; keep it distinct from Sport MT. The full matrix uses 2.0L diesel with 6MT/9AT and selected 4x4 AT combinations; do not cross-join all trims and drivetrains.
- **Meridian:** official comparator lists Longitude, Longitude Plus, Limited (O), Trail, Overland and Track. The July 2026 OEM release adds the 85th Anniversary Edition, limited to 85 units and based on Overland. Current comparator amounts and anniversary announcement differ by source snapshot; confirm exact current price, seating and drivetrain mapping.
- **Wrangler:** standard India variants are Unlimited and Rubicon, both 2.0L petrol automatic 4WD. The 1941 Willys Edition is based on Rubicon and limited to 41 units; the Rubicon Whitecap Edition allocation of 25 units sold out in October 2026. Sold-out special editions are not marked as currently orderable.
- **Grand Cherokee:** current official page lists Limited (O) at ₹63 lakh; an authorized Jeep dealer portal also lists Signature Edition. The Signature Edition is an equipment derivative of Limited (O), and current orderability/price needs confirmation. Do not import SRT or other global-market grades from legacy pages.

Jeep's current model/variant pages and recent OEM releases provide useful price observations, but model-year, effective date, city scope, edition availability and exact powertrain/drive mapping must be reconfirmed before staging. No Jeep price is approved for production import.

The Jeep batch adds four rows. The overall variant-source worklog now contains **151 model rows** across 17 brands; 100 of 251 model candidates remain without variant-source rows.

## Lamborghini variant-source audit (2026-11-06)

Added source-review rows for all **three Lamborghini model candidates**: Urus SE, Temerario and Revuelto.

- **Urus SE:** one current India model configuration is observed: 4.0L twin-turbo V8 plug-in hybrid, 25.9kWh battery, AWD and 8-speed automatic. Earlier Urus S/Performante configurations are not carried forward as current India variants.
- **Temerario:** official model page confirms the HPEV V8 hybrid model with three electric motors and an 8-speed dual-clutch transmission. First India delivery was reported in June 2026, but India allocation, dealer orderability and exact customer configuration remain dealer-confirmation items.
- **Revuelto:** official model page confirms the V12 HPEV coupe configuration. India allocation, Ad Personam options and final dealer pricing require direct authorized-dealer confirmation. Revuelto Roadster is not added as a coupe variant.

Lamborghini's public global pages provide product identity/specifications, but no official India grade-wise price matrix was captured. Third-party price estimates are not used as OEM price evidence. All three candidates retain dealer-confirmation-required status; obtain authorized India dealer quotations, allocation/orderability and price/tax basis before staging. No Lamborghini price is approved for production import.

The Lamborghini batch adds three rows. The overall variant-source worklog now contains **154 model rows** across 18 brands; 97 of 251 model candidates remain without variant-source rows.

## Land Rover variant-source audit (2026-11-06)

Added source-review rows for all **seven Land Rover model candidates**: Range Rover, Range Rover Sport, Range Rover Velar, Range Rover Evoque, Defender, Discovery and Discovery Sport.

- **Range Rover / Range Rover Sport:** current official India Range Rover site confirms both model families and displays model-level starting prices (₹2.40 crore and ₹1.43 crore respectively). Exact current India retail grades, engine codes and body-style combinations were not exposed in the captured India pages. Do not import global grade/powertrain matrices without local confirmation.
- **Range Rover Velar:** official India page displays ₹88.50 lakh starting. A historical official MY24 price list names 2.0L petrol/diesel Dynamic HSE at ₹87.90 lakh; this is retained only as historical evidence, not a current 2026 trim-price row.
- **Range Rover Evoque:** official India page displays ₹64.86 lakh starting. Historical official MY24 material names Dynamic SE on petrol/diesel; current 2026 grade mapping remains unverified.
- **Defender:** official India models page identifies body styles 90/110/130 and product grades/editions including OCTA, OCTA Black, X-Dynamic HSE, X, V8 and Trophy Edition. The 130 page exposes D350 diesel mild hybrid and P425 petrol selectors for selected grades. Do not cross-join all body styles, trims and engines.
- **Discovery:** current official India page confirms the seven-seat Discovery family. S, Dynamic HSE and Metropolitan Edition labels appear in a 2024 official MY24 price list only; they are not assumed to be current 2026 grades.
- **Discovery Sport:** official India family page displays model-level starting price ₹63.37 lakh. The 2024 MY24 Dynamic SE petrol/diesel price entry is historical, not current variant pricing.

Land Rover's current India pages explicitly caution that global-market specifications/options may differ locally and direct customers to authorized retailers for current availability and pricing. The 2024 price PDF and retail-offer pages are historical; they are not used as current prices. Confirm exact India grade/engine/body-style combinations, current stock/orderability, price effective date and dealer quotation before staging. No Land Rover price is approved for production import.

The Land Rover batch adds seven rows. The overall variant-source worklog now contains **161 model rows** across 19 brands; 90 of 251 model candidates remain without variant-source rows.

## Lexus variant-source audit (2026-11-06)

Added source-review rows for all **five Lexus model candidates**: ES, NX, RX, LX and LM.

- **ES:** the India range contains ES 350h Exquisite/Luxury and ES 500e electric. Keep the 2.5L strong-hybrid and 74.68kWh dual-motor AWD electric configurations separate. 2026 launch reporting lists ₹66.10/71.80 lakh for 350h; authorized retailer page displays ES 500e from ₹91.20 lakh. A current OEM grade-price matrix was not captured.
- **NX:** the official Lexus India 2025 brochure identifies NX 350h Exquisite, Overtrail, Luxury and F SPORT. An authorized retailer page displays current amounts for those four grades, but those are retailer observations, not a dated manufacturer price list. The global NX facelift announced in 2026 is not assumed to be the India-spec model before local launch.
- **RX:** India grade names observed include RX 350h Exquisite and RX 500h F SPORT+. The 350h Exquisite also appears with Lexus Audio/Mark Levinson equipment distinctions in reporting; do not treat audio package as a separate grade unless the official configurator does so. Keep 350h and 500h powertrains separate.
- **LX:** India model is LX 500d diesel; Urban and Overtrail Edition grade labels are observed in current variant reporting. Exact current manufacturer grade-price matrix was not captured. Do not import international petrol/hybrid derivatives.
- **LM:** official brochure confirms LM 350h 7-Seater VIP and 4-Seater Ultra Luxury layouts. These are seating/grade configurations of one MPV model, not separate model identities. Authorized retailer page displays separate prices; confirm current manufacturer quote and allocation.

Lexus India model/variant evidence is split across official brochures, 2026 launch material and authorized retailer pages. Retailer-displayed amounts are clearly kept separate from manufacturer-issued price evidence. Confirm current OEM price sheets, model-year, exact equipment/grade mapping, dealer allocation and content-reuse permission before staging. No Lexus price is approved for production import.

The Lexus batch adds five rows. The overall variant-source worklog now contains **166 model rows** across 20 brands; 85 of 251 model candidates remain without variant-source rows.

## Maserati variant-source audit (2026-11-06)

Added source-review rows for all **seven Maserati model candidates**: Grecale, Grecale Folgore, GranTurismo, GranCabrio, MCPURA, MCPURA Cielo and GT2 Stradale.

- **Grecale:** the current official India configurator lists Grecale 300PS mild hybrid, Modena 330PS mild hybrid, Modena V6 390PS petrol and Trofeo 530PS petrol. Official configurator starting prices are ₹1.14 crore, ₹1.29 crore, ₹1.39 crore and ₹2.00 crore respectively. These are manufacturer page observations; confirm delivery-date quote and option/tax scope.
- **Grecale Folgore:** retained as a separate electric model identity. Official configurator lists 550PS AWD and ₹1.90 crore starting price. The October 30 OEM India release confirms updated Folgore range improvements.
- **GranTurismo:** official India configurator lists 490, Trofeo and Folgore configurations. V6 490/Trofeo are AWD; Folgore is electric AWD. Current numeric India variant prices did not render in the captured configurator output.
- **GranCabrio:** official India configurator lists 490, Trofeo and Folgore configurations. Kept separate from the GranTurismo coupe; current numeric India prices were not captured.
- **MCPURA / MCPURA Cielo:** official India configurator lists 2027 model-year coupe and convertible entries, each with 630PS Nettuno V6 and RWD. No India price captured; verify local allocation and orderability.
- **GT2 Stradale:** October 30 OEM release confirms India debut/display and the 640hp road-legal GT2 derivative; configurator lists a 2027 entry but does not prove retail booking or price. Dealer confirmation required. MCXtrema is track-only and excluded from the passenger retail model queue.

The 2026-10-30 OEM India announcement confirms the refreshed Grecale, GranTurismo and GranCabrio range and India debut of GT2 Stradale. The current India configurator is used for exact product configurations and visible Grecale pricing; media-reported GranTurismo/GranCabrio amounts are not substituted for OEM price evidence. No Maserati price is approved for production import except as a recorded source observation pending effective-date/dealer verification.

The Maserati batch adds seven rows. The overall variant-source worklog now contains **173 model rows** across 21 brands; 78 of 251 model candidates remain without variant-source rows.

## Aston Martin variant-source audit (2026-11-06)

Added source-review rows for all **four Aston Martin model candidates**: Vantage, DB12, DBX and Vanquish.

- **Vantage:** India FTA price reporting identifies Vantage S Coupe (₹3.15 crore) and Vantage S Roadster (₹3.35 crore).
- **DB12:** India FTA price reporting identifies DB12 S Coupe (₹4.10 crore) and DB12 S Volante (₹4.35 crore).
- **DBX:** India FTA price reporting identifies DBX S at ₹4.15 crore.
- **Vanquish:** India FTA price reporting identifies Vanquish Coupe (₹6.40 crore) and Vanquish Volante (₹6.90 crore).

These August 2026 India-UK FTA prices were reported as manufacturer-announced revised prices, but a direct OEM India price list was not captured in this pass. Current global OEM pages confirm the model families; exact India allocation, suffix/grade, model-year, options, tax eligibility and orderability require authorized dealer confirmation. Do not infer global DBX707 or other international variants as India retail options. No Aston Martin price is approved for production import.

The Aston Martin batch adds four rows. The overall variant-source worklog now contains **177 model rows** across 22 brands; 74 of 251 model candidates remain without variant-source rows.

## Bentley variant-source audit (2026-11-06)

Added source-review rows for all **five Bentley model candidates**: Bentayga, Bentayga Extended Wheelbase, Continental GT, Continental GT Convertible and Flying Spur.

- **India model catalogue:** Bentley's current official India page lists Bentayga Extended Wheelbase, Flying Spur and Continental GT. It does not separately list standard-wheelbase Bentayga or Continental GTC convertible.
- **Bentayga:** standard-wheelbase India orderability is not independently confirmed. Keep separate from EWB; do not infer standard Bentayga price from EWB.
- **Bentayga EWB:** official India page confirms 4.0L V8 petrol. Global grade families include EWB, Azure and Mulliner, but India-specific grade mapping is not published on the captured India page. July 2026 reporting described an estimated ₹4.20 crore post-FTA EWB amount and explicitly noted Bentley had not confirmed the exact reduction; this is not an OEM price observation.
- **Continental GT:** official India page confirms the current 782PS/1,000Nm Ultra Performance Hybrid V8. Global GT/Azure/S/Speed/Mulliner grade families are not assumed to be India orderable without a local configurator/dealer matrix.
- **Continental GT Convertible:** global OEM calls the convertible Continental GTC and lists GTC/Azure/S/Speed/Mulliner families. The India page does not separately show GTC; local orderability requires dealer confirmation.
- **Flying Spur:** official India page confirms the Ultra Performance Hybrid V8, 782PS/1,000Nm. Global Flying Spur/Azure/S/Speed/Mulliner grades are not assumed to map directly to India retail.

No current official India grade-wise price list was captured for these candidates. The India-UK FTA reporting indicates the Bentayga petrol model may qualify for reduced-duty order intake subject to quota, while hybrid Continental GT/Flying Spur do not receive the same immediate reduction. Confirm exact model/grade, import eligibility, current allocation, orderability and written dealer quote. No Bentley price is approved for production import.

The Bentley batch adds five rows. The overall variant-source worklog now contains **182 model rows** across 23 brands; 69 of 251 model candidates remain without variant-source rows.

## Ferrari variant-source audit (2026-11-06)

Added source-review rows for all **seven Ferrari model candidates**: Amalfi, Amalfi Spider, 296 GTB, 849 Testarossa, 12Cilindri Coupe, 12Cilindri Spider and Purosangue.

- **Amalfi:** current India coverage identifies the V8 coupe; reported list price is ₹5.59 crore before options. A ₹4.08 crore FTA-anticipatory booking amount is an estimate only, conditional on future agreement implementation and delivery timing.
- **Amalfi Spider:** global OEM product identity is confirmed, but India retail launch/orderability and price were not independently established in the captured official India source. Dealer confirmation required.
- **296 GTB:** reported India reference price is ₹5.40 crore, but Ferrari's FY2025 results presentation lists 296 GTB as phased out in 2026. Treat as existing stock/remaining allocation only until dealer confirms factory orderability.
- **849 Testarossa:** current 2026 model, reported India amount ₹10.37 crore; hybrid FTA treatment and local allocation require dealer confirmation.
- **12Cilindri Coupe / Spider:** V12 coupe and convertible are separate body identities. Reported pre-FTA amounts are ₹8.50/9.15 crore; estimated FTA-anticipatory booking amounts are ₹5.89/6.38 crore, not confirmed final prices.
- **Purosangue:** four-seat V12 AWD SUV. Reported list amount ₹10.50 crore; estimated FTA-anticipatory booking amount ₹7.59 crore before options, conditional on FTA implementation, import quota and delivery timing.

Ferrari's public India price information is reported through dealer/industry coverage; a current OEM India variant-price sheet was not captured. The 30% lower FTA-anticipatory prices are estimates, not final invoice prices, and apply only to certain pure-petrol models. Hybrid models (296 GTB and 849 Testarossa) have uncertain tariff treatment. Confirm direct Ferrari dealer allocation, order acceptance, final written price, tax/FTA eligibility and delivery-date applicability before staging. No Ferrari price is approved for production import.

The Ferrari batch adds seven rows. The overall variant-source worklog now contains **189 model rows** across 24 brands; 62 of 251 model candidates remain without variant-source rows.

## McLaren variant-source audit (2026-11-06)

Added source-review rows for all **three McLaren model candidates**: Artura, GTS and 750S.

- **Artura:** current India range includes the V6 plug-in hybrid model. Coupe/Spider body-style availability in India and exact local price mapping need confirmation. The reported ₹5.10 crore amount is a model-level reference; no OEM grade-specific price list was captured. Do not apply pure-petrol FTA reductions to the hybrid without written confirmation.
- **GTS:** current India model is the GTS, the successor identity to the old McLaren GT. The ₹6.15 crore pre-FTA amount is a reported price reference. A ₹3.83 crore FTA-anticipatory amount was reported but McLaren had not publicly confirmed it; do not treat it as a final price.
- **750S:** India Coupe and Spider body styles are documented. Production is scheduled to end in 2027 and final orders are being accepted. Reported anticipated FTA amounts are ₹4.94 crore (Coupe) and ₹5.46 crore (Spider), before options; actual invoice amount depends on duty eligibility, quota and delivery date.

All McLaren models are CBU imports and India retail is handled through Infinity Cars. Current order acceptance, local allocation, body-style availability, final FTA price basis and written dealer quote remain mandatory gates. No McLaren price is approved for production import.

The McLaren batch adds three rows. The overall variant-source worklog now contains **192 model rows** across 25 brands; 59 of 251 model candidates remain without variant-source rows.

## Mercedes-Benz variant-source audit (2026-11-06)

Added source-review rows for all **24 Mercedes-Benz model candidates**. The official India configurator currently displays 26 model entries, including separate fuel/body-style/powertrain entries under the same family.

- **ICE/hybrid limousines:** CLA (electric-only in captured India catalogue); C-Class petrol/diesel and separate PHEV entry; E-Class Sedan Long petrol/diesel; separate E-Class Sedan PHEV; S-Class PHEV; Mercedes-Maybach S-Class PHEV.
- **Electric limousines:** EQS electric; the configurator lists model-level starting prices, but exact India battery/grade/drive mapping needs brochure validation.
- **SUVs:** GLA petrol/diesel; GLC ICE petrol/diesel and separate GLC Electric; GLE petrol/diesel; GLS petrol/diesel; Mercedes-Maybach GLS petrol; G-Class electric, diesel and petrol entries; GLC Coupé petrol; GLE Coupé petrol.
- **Other body styles:** CLE Cabriolet petrol; CLE Coupé petrol; Mercedes-Maybach SL Monogram Series petrol; A-Class Hatchback petrol; V-Class; Mercedes-AMG GT Coupé petrol; Mercedes-Maybach EQS SUV electric; standard EQS SUV electric.
- The current official configurator displays model-level starting amounts, e.g. CLA ₹56.50L, C-Class ₹61.20L, E-Class Sedan Long ₹82L, S-Class ₹2.20Cr, GLA ₹51.80L, GLC ICE ₹77L / Electric ₹78.50L, GLE ₹1Cr, GLS ₹1.375Cr, G-Class electric/diesel/petrol ₹3.15/2.90/3.80Cr, CLE Cabriolet ₹1.16Cr, CLE Coupé ₹1.34Cr, Maybach SL Monogram ₹4.40Cr. These are model-entry starting amounts, not grade-level prices.
- **Price discrepancy:** standard EQS SUV is shown at ₹1.35Cr in the configurator and ₹1.335Cr in the separate model overview. This remains a source display discrepancy until live dealer/configurator confirmation.
- **Orderability and exact grade mapping:** several candidates (V-Class, A-Class Hatchback, CLA, Maybach variants and the new GLC Electric) have model-level listings but no complete grade matrix in the captured page. Use India brochures and current configurator selections; do not infer global AMG/4MATIC or engine combinations.

No Mercedes-Benz grade-level prices are approved for production import from this batch. Confirm exact model-year, India-specific engine/trim/gearbox mapping, price effective date, current stock/orderability and OEM content-reuse permission before staging. The configurator observations are model-level starting prices only.

The Mercedes-Benz batch adds 24 rows. The overall variant-source worklog now contains **216 model rows** across 26 brands; 35 of 251 model candidates remain without variant-source rows.

## Nissan variant-source audit (2026-11-06)

Added source-review rows for all **three Nissan model candidates**: Tekton, Gravite and Magnite.

- **Tekton:** official Nissan price list exposes six trim families (Visia, Visia+, Acenta, N-Connecta, Tekna, Tekna+) across explicit 1.0L turbo T160 MT and 1.3L turbo T280 MT/DCT combinations. The official price table provides each populated combination from ₹10.49 lakh to ₹18.59 lakh. Do not fill missing trim/engine/gearbox cells.
- **Gravite:** official price list exposes Visia/Acenta/N-Connecta/Tekna and Launch Edition across 5MT and EZ Shift AMT combinations. It is a 7-seat 1.0L naturally aspirated petrol MPV. CNG is an approved retrofit kit with separate installation/endorsement costs, not a factory-built CNG variant.
- **Magnite:** official price list exposes Visia, Visia+, Acenta, N-Connecta, Tekna, Tekna+ and KURO special edition across 1.0L NA petrol MT/AMT and 1.0L turbo petrol MT/CVT. CNG is a retrofit kit and its costs remain separate from vehicle grade prices.

Nissan's current official price-list page provides exact ex-showroom grade/powertrain rows. Current homepage starting prices and price-list values can differ slightly due to page timing or offers; the dated OEM price list is retained as the audit observation, with current dealer/state quotation still required. No Nissan price is approved for production import until effective date, city scope, current orderability and content-reuse permission are confirmed.

The Nissan batch adds three rows. The overall variant-source worklog now contains **219 model rows** across 27 brands; 32 of 251 model candidates remain without variant-source rows.

## Porsche variant-source audit (2026-11-06)

Added source-review rows for all **five Porsche model candidates**: 911, Taycan, Panamera, Macan and Cayenne.

- **911:** current India configurator lists Carrera, Carrera 4 GTS, Turbo S and GT3, with individual incl.-VAT starting prices. Do not import global Targa, Carrera S/GTS or GT3 Touring variants absent from the India configurator capture.
- **Taycan:** India configurator lists 4S, 4S Black Edition and Turbo, all electric AWD configurations with individual incl.-VAT prices.
- **Panamera:** current India configurator capture exposes one Sport Saloon petrol RWD configuration, 353PS, with ₹1.7912 crore incl.-VAT starting price. Older hybrid derivatives are not carried forward without current India evidence.
- **Macan:** official India configurator lists one petrol AWD Macan plus three electric families: Macan Electric RWD, Macan 4S Electric AWD and Macan Turbo Electric AWD. The current model audit has one Macan candidate; Step 4 reconciliation should decide whether the electric Macan deserves its own model identity rather than combining propulsion families under one model.
- **Cayenne:** official India configurator lists petrol SUV, Black Edition, GTS, Coupé, Coupé Black Edition and GTS Coupé, plus Cayenne Electric and Cayenne Turbo Electric. The model audit currently has one Cayenne candidate; Step 4 should assess whether coupe and electric product families need separate model rows.

Porsche India configurator amounts are displayed inclusive of VAT. The prices in the worklog are manufacturer-configurator observations, not dealer on-road quotations. Keep model-level/body-style/powertrain identities separate, and verify model year, availability and current dealer quotation before import. No Porsche price is approved for production import.

The Porsche batch adds five rows. The overall variant-source worklog now contains **224 model rows** across 28 brands; 27 of 251 model candidates remain without variant-source rows.

## Renault variant-source audit (2026-11-06)

Added source-review rows for all **four Renault model candidates**: Duster, Triber, Kiger and Kwid.

- **Duster:** official Renault pre-configurator exposes three powertrain groups: Turbo TCe 100 (Authentic/Evolution/Adventure, 6MT); Turbo TCe 160 (Evolution/Adventure/Techno+/Iconic and Iconic Launch Edition, 6MT/6DCT); Strong Hybrid E-Tech 160 (Evolution/Techno/Emotion, dedicated 8-speed DHT). The hybrid's ₹16.99/18.99/19.49 lakh prices are introductory for deliveries through 2026-12-31. Dual-tone is a ₹20,000 appearance option, not a variant.
- **Triber:** official page lists Authentic, Evolution, Techno and Emotion, with grade starting prices. It now describes both 72PS naturally aspirated petrol and TCe 100PS turbo families, plus flexible 5–7 seating. Exact engine/gearbox-to-grade mapping needs configurator confirmation.
- **Kiger:** official page lists Authentic, Evolution, Evolution+, Techno and Emotion. Configurator exposes 1.0L NA manual/AMT and 1.0L turbo manual/CVT powertrains. Grade starting prices are visible, but full trim-to-powertrain matrix is not.
- **Kwid:** official page currently lists Evolution and Climber with grade starting prices. Exact current transmission applicability requires configurator confirmation; historic RXT/AMT names are not carried forward without current evidence.

Renault's official price pages state ex-showroom prices are subject to city/local tax and purchase-date changes. Grade starting amounts are not treated as full price matrices. Confirm exact powertrain/gearbox/grade combinations, hybrid introductory-price expiry, city scope and dealer orderability before staging. No Renault price is approved for production import.

The Renault batch adds four rows. The overall variant-source worklog now contains **228 model rows** across 29 brands; 23 of 251 model candidates remain without variant-source rows.
