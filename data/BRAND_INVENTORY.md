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
