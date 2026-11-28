# Motivo master roadmap

Owner direction (2026-11-28): full India passenger-car catalogue before public launch; no pending audits. Firebase access only after stages 1–5. This roadmap supersedes earlier launch sequencing.

| Stage | Gate | Status |
|---|---|---|
| 1 | Current OEM brand/model/exact variant inventory reconciled | In progress |
| 2 | All audits resolved; unknown fields explicitly documented | Pending |
| 3 | Source approvals, normalized production catalogue, validation | Pending |
| 4 | Website search, filters, recommendations, comparison and local QA | Pending |
| 5 | Ads code disabled by default, privacy, terms, consent, hosting eligibility | Pending |
| 6 | Firebase import, API, rules, backup and rollback | On hold |
| 7 | End-to-end QA and owner acceptance; zero release blockers | Pending |
| 8 | Public launch and monitoring; ads only after approval | Pending |

## Stage 1 baseline

Recovered historical inventory: 251 model rows, 35 brands. This is not a current OEM-verified inventory. Historical model status: 60 complete, 33 partial, 157 pending, 1 blocked. Exact SKU count remains unknown.

| Brand | Historical model rows | OEM reconciliation |
|---|---:|---|
| Maruti Suzuki | 17 | Nameplates matched; SKU pending |
| Hyundai | 14 | Nameplates matched; SKU and Tucson exception pending |
| Mahindra | 13 | Initial lineup checked; Neo Plus candidate and orderability open |
| Kia | 9 | Initial lineup checked; two new candidates and EV9 exception |
| Toyota | 13 | Nameplates matched; SKU and generation conflict pending |
| MG Motor | 10 | Nameplates matched; Windsor Pro and Gloster exceptions |
| Tata Motors | 16 | 15 matched; Tigor ICE exception; Aeris candidate |
| MINI | 5 | Nameplates matched; Cooper SE and Stardust candidates |
| Force Motors | 1 | Gurkha confirmed; complete range and SKU check pending |
| Tesla | 1 | Model Y matched; Y L configuration candidate |
| VinFast | 3 | All three matched; exact SKUs pending |
| Audi | 9 | Eight matched; Q3 Sportback exception |
| BMW | 22 | 19 matched; i4, iX, XM exceptions |
| BYD | 4 | 4 matched; 13 regional configuration leads |
| Citroën | 5 | 4 confirmed; C5 Aircross unresolved |
| Honda | 5 | 5 matched; ALPHA future only |
| Jeep | 4 | 4 matched; exact SKUs pending |
| Lamborghini | 3 | Global OEM and India secondary evidence; local OEM range pending |
| Land Rover | 7 | All seven matched; Defender body configurations pending |
| Lexus | 5 | Dealer and historical OEM evidence; current national OEM check pending |
| Maserati | 7 | All seven matched; MY2026/2027 configuration conflict |
| Aston Martin | 4 | Global OEM matched; India orderability pending |
| Bentley | 5 | India OEM confirms three; two unresolved |
| Ferrari | 7 | Global OEM evidence partial; India lineup pending |
| McLaren | 3 | Secondary India evidence; OEM pending |
| Mercedes-Benz | 24 | 24 matched across India navigation and model listings; SKU pending |
| Nissan | 3 | Pending |
| Porsche | 5 | Pending |
| Renault | 4 | Pending |
| Rolls-Royce | 4 | Global OEM matched; India evidence pending |
| Škoda | 6 | Pending |
| Volkswagen | 4 | 4 matched; Virtus generation transition |
| Volvo Cars | 5 | Pending |
| Isuzu | 1 | mu-X confirmed; pickup scope pending |
| Lotus | 3 | 3 matched; Evija candidate orderability pending |

No Firebase writes or production publication authorized. Do not mark a brand complete without dated OEM lineup evidence and explicit disposition of each historical model.

## Stage 1 — Maruti Suzuki checkpoint (2026-11-28)

OEM passenger retail lineup matched all 17 historical nameplates: Arena 10, Nexa 7. Sources: https://www.marutisuzuki.com/arena and https://www.nexaexperience.com/ ; corroborating configurators https://www.marutisuzuki.com/arena/configurator and https://www.nexaexperience.com/configurator . Tour commercial range excluded under passenger retail scope, not claimed discontinued. Exact SKU inventory and dealer orderability remain open. Arena comparison and landing page show inconsistent price references; no price imported. This is nameplate reconciliation only.

## Stage 1 — Hyundai checkpoint (2026-11-28)

All 14 historical passenger nameplates match the current India retail finder: Verna, Aura, Venue, Venue N Line, Creta, Creta N Line, Exter, Alcazar, Grand i10 NIOS, i20, i20 N Line, IONIQ 5, Creta Electric, Bayon. Sources checked: https://www.hyundai.com/in/en/find-a-car and https://www.hyundai.com/in/en.html . Prime-HB and Prime-SD explicitly classified as taxis in the finder, outside passenger retail scope. Tucson and Kona Electric occur in the sitemap/owner support but not current retail finder; do not infer discontinuation or dealer stock. Tucson also appears in corporate about page, so retain orderability as an open exception. Exact SKU inventory pending. No price or production data imported.

## Stage 1 — Mahindra and Kia checkpoints (2026-11-28)

Mahindra: all 13 historical nameplates have OEM listing or launch evidence. Thar is now labelled Thar OG. Bolero Neo Plus is an additional SUV listing missing from legacy inventory; retain as candidate pending passenger vs fleet configuration classification. XUV400 remains in navigation but current orderability unresolved. BE 6, XEV 9e and XEV 9S have OEM evidence; electric configurator and exact SKU check pending. Sources https://auto.mahindra.com/ , https://auto.mahindra.com/suv , https://www.mahindra.com/annual-report-FY2026/171/ .

Kia: all nine legacy nameplates appear on OEM homepage, including EV9; EV9 absent from current buy navigation, so orderability unresolved. Two additional nameplates appear on OEM homepage and buy navigation: Sorento and Syros EV. Add as candidates; exact launch/retail availability and variants to confirm. Sources https://www.kia.com/in/home.html and https://www.kia.com/in/buy/kid.html . Do not add Carnival HEV solely from investor plans. No production prices imported.

## Stage 1 — Toyota checkpoint (2026-11-28)

All 13 legacy nameplates match Toyota India's current product navigation: Glanza, Taisor, Rumion, Hyryder, Ebella, Innova Crysta, Innova Hycross, Hilux, Fortuner, Legender, Camry, Vellfire, Land Cruiser 300. Sources https://www.toyotabharat.com/ and https://www.toyotabharat.com/brochure/?model=29 . Retain Hilux in existing scope pending consistent pickup scope decision. October 14 Glanza release https://www.toyotabharat.com/news/2026/tkm-introduces-the-new-toyota-glanza.html identifies new three-cylinder engine and CNG AMT, while https://www.toyotabharat.com/showroom/glanza/ still exposes four-cylinder specifications. Record generation conflict; do not join old features to new variants. October 9 Fortuner Leader Edition announcement indexed at https://www.toyotabharat.com/news/index.html requires exact edition mapping. No prices imported. Exact SKU/orderability and source publication review pending.

## Stage 1 — MG Motor checkpoint (2026-11-28)

All ten legacy records have current OEM homepage evidence: Comet EV, Windsor EV, ZS EV, Hector, Astor, Hector Tomahawk EV and PHEV, Majestor, Cyberster, M9. Windsor Pro is separately presented in the configurator; retain as configuration candidate rather than automatically creating a new model. Gloster appears in service navigation but not current retail product lineup; orderability unresolved. Majestor homepage starting reference INR 43.49L differs from configurator INR 40.99L and May 27 launch release for 4x2 automatic; resolve variant and effective-date scope before publication. Separate BaaS from outright battery-inclusive purchase prices. Sources checked: https://www.mgmotor.co.in/ ; https://cars.mgmotor.co.in/ ; https://www.mgmotor.co.in/tools/brochures ; https://www.mgmotor.co.in/media-center/newsroom/mg-majestor-4x2-automatic-top-trim-launched-at-inr-40-99-lakhs-e . Exact SKU inventory pending. No production data imported.

## Stage 1 — MINI, Force and Tata access checkpoint (2026-11-28)

MINI: all five historical entries appear on https://www.mini.in/en_IN/home/range.html . Additional Cooper SE EV listing requires separate powertrain/model classification; footer also links Convertible Stardust Edition, exact edition availability pending. Range page contains generic German VAT and European consumption disclaimers; do not import India prices or mileage from those disclaimers. Exact SKUs pending.

Force: Gurkha nameplate confirmed at https://forcegurkha.co.in/ . Homepage mixes 2021 imagery and updated equipment claims; current 3-door/5-door configuration evidence and full passenger range inventory remain pending. No historical specs promoted.

Tata: https://cars.tatamotors.com/ returned HTTP 403 in this inspection; full lineup not verified. Existing Punch and Nexon research remains evidence, not brand reconciliation. Retry accessible official catalogue or authorized alternate evidence; do not bypass access restrictions.

## Stage 1 — Tata, Tesla, VinFast, Audi and BMW checkpoint (2026-11-28)

- Tata: accessible indexed official catalogue https://tatamotors-prod.adobecqms.net/ and EV range https://ev.tatamotors.com/product-compare.html resolve prior access blocker for lineup research. Eight historical ICE names and seven EV names matched. Tigor ICE absent from current retail navigation; do not declare discontinued. Aeris is a new listed candidate; XPRES requires fleet scope classification. Sierra Dark is an edition candidate.
- Tesla: https://www.tesla.com/en_in/modely lists five-seat Premium RWD and six-seat L Premium AWD; preserve as separate configurations pending exact order selector. https://www.tesla.com/en_IN/model3 explicitly excludes India orders.
- VinFast: https://vinfastauto.in/en/press-release/vinfast-india-named-ev-manufacturer-of-the-year-at-ht-auto-leaderboard-awards-2026 confirms three India models. https://vinfastauto.in/en/vf6 lists Earth, Wind, Wind Infinity; https://vinfastauto.in/en/vf7 and https://vinfastauto.in/en/mpv7 provide further SKU leads. Global-spec disclaimers require India-specific verification.
- Audi: https://www.audi.in/en/models/ lists eight historical names; Q3 Sportback absent, orderability unresolved.
- BMW: https://www.bmw.in/en/all-models.html matches 19 of 22 historical nameplates (including X1 diesel and X1 LWB petrol as separate legacy records pending taxonomy). i4, iX and XM absent from current listing; do not infer discontinuation. Separate X3 petrol grades and X7 diesel grades. No concept or protection vehicle added to retail scope. Some price disclaimers reference German VAT; no prices promoted.

All five initial inspections complete; exact SKU verification and exceptions remain open. No production imports.

## Stage 1 — BYD, Citroën, Honda and Jeep checkpoint (2026-11-28)

- BYD: all four historical models confirmed at https://bydautoindia.com/car-dealer/byd-car-price . Regional table https://www.bydautoindia.com/car-dealer/electric-car-price/telangana identifies 13 configuration leads: ATTO 3 Dynamic/Premium/Superior; eMAX 7 Comfort/Superior each six/seven seats; SEAL Dynamic/Premium/Performance; SEALION 7 Dynamic/Premium/Performance. National starting price for SEALION 7 conflicts with regional Dynamic listing; verify effective date and market before pricing publication. Exact orderability pending.
- Citroën: https://www.citroen.in/about-citroen/news/citroen-variants-extended.html confirms AircrossX, BasaltX, ë-C3X and new September 7 configurations; https://www.citroen.in/models/c3.html confirms C3X but mixes Basalt copy. C5 Aircross current retail status unresolved; no discontinuation inference. Separate BaaS from outright EV pricing.
- Honda: https://www.hondacarindia.com/?pr_id=306 matches New City, New Amaze, Amaze 2nd Gen, ZR-V and New Elevate. ALPHA explicitly future, excluded from current retail. https://www.hondacarindia.com/download-brochure provides generation-specific leads; City petrol and hybrid taxonomy pending.
- Jeep: https://www.jeep-india.com/ confirms Compass, Meridian, Wrangler and Grand Cherokee. Exact powertrain/edition/orderability inventory pending.

No production records or prices imported. All four initial inspections performed; open exceptions retained.

## Stage 1 — Maserati checkpoint (2026-11-28)

India range https://www.maserati.com/in/en/models and configurator https://www.maserati.com/in/en/shopping-tools/configurator match all seven historical records. Configurator lists 13 MY2026/2027 configurations across Grecale (4), GranTurismo (3), GranCabrio (3), MCPURA, MCPURA Cielo and GT2 Stradale. Grecale Folgore is a powertrain within Grecale; preserve legacy mapping. Current India homepage https://www.maserati.com/in/en shows five new Grecale configurations including Modena V6. MY2027 Modena starting price differs from MY2026 configurator; keep model years separate, do not import prices. GranTurismo and GranCabrio Folgore are configuration leads. MC20 and MC20 Cielo remain on older range page but not configurator; orderability unresolved. Track-only GT2 and MCXtrema excluded. India debut of updated range confirmed by https://www.maserati.com/gb/en/brand/stories-of-audacity/maserati-partnership-navnit-india . Exact current orderability and SKU completeness pending. Other brands searched in this batch yielded insufficient market-specific evidence; no completion marks assigned.

## Stage 1 — Luxury lineup evidence checkpoint (2026-11-28)

- Land Rover: India OEM brochure index https://www.landrover.in/download-a-brochure/index.html matches all seven legacy nameplates. Defender 90/110/130 are body configuration leads, not automatically separate models. Current exact orderable SKUs pending.
- Lexus: https://www.toyotabharat.com/documents/toyota-in-india/environment/tkm-sustainability-report-2024.pdf confirms historical five-nameplate portfolio. Current dealer https://lexusmumbai.co.in/ lists ES, NX, RX, LX, LM, including ES 500e electric candidate. Dealer figures not approved as national OEM prices; current national OEM lineup confirmation pending.
- Lamborghini: global OEM https://www.lamborghini.com/en-en includes all three legacy names and additional global candidates Temerario Spyder, Revuelto SV, Urus SE Performante; no India orderability inferred. India corporate release https://skoda-vw.co.in/lamborghini/lamborghini-conquers-new-heights-with-the-inaugural-esperienza-terra-india/ confirms Urus SE India activity. Secondary corroboration https://www.autocarindia.com/cars/lamborghini supports three local models, but India-specific OEM evidence for remaining models and completeness is pending.

No production imports. Only Land Rover reaches initial India OEM lineup reconciliation in this batch.

## Stage 1 — Aston Martin, Bentley, Ferrari checkpoint (2026-11-28)

Aston Martin: https://media.astonmartin.com/section/current-models/?lang=eng confirms all four global core nameplates. https://www.astonmartin.com/en/models and June 29 2026 Goodwood OEM announcement identify S and Volante derivatives; India availability not established. Bentley: https://www.bentleymotors.com/in/en.html explicitly promotes Bentayga EWB, Flying Spur and Continental GT in India. Standard Bentayga and Continental GT Convertible not confirmed by this page; retain as unresolved. Ferrari: https://cdn.ferrari.com/cms/network/media/pdf/2.%20Ferrari%20Capital%20Markets%20Day%202025%20-%20Unique%20Proposition%2C%20Clients%20and%20Experiences.pdf confirms six historical global records and additional 296 GTS and 849 Testarossa Spider candidates. Amalfi Spider and current India orderability not established by this source. McLaren search did not yield sufficient official India evidence; status unchanged. No new brand marked fully initially reconciled, no production data imported.

## Stage 1 — Additional India evidence checkpoint (2026-11-28)

- Mercedes-Benz: https://www.mercedes-benz.co.in/ and https://www.mercedes-benz.co.in/passengercars/models.html?showOnly=new together cover all 24 legacy model labels. EQS sedan/SUV differentiated by body; GLC Electric separate from ICE. Listing counts are configuration cards, not exact SKUs.
- Volkswagen: https://www.volkswagen.co.in/en/models.html covers Taigun, Tayron, Virtus and Golf GTI. New Virtus explicitly coming soon; Virtus Sport and Chrome listed separately. Preserve generation and edition distinctions.
- Lotus: https://www.lotuscars.com/en-IN lists Eletre, Emeya, Emira and additional limited-production Evija candidate; India orderability not inferred for Evija. Emira 420 Sport derivative lead.
- Isuzu: https://www.isuzu.in/mux confirms mu-X, 4x2/4x4 configuration leads; pickup scope and exact SKU pending.
- McLaren: https://www.autocarindia.com/cars/mclaren/ supports Artura, GTS and 750S; secondary only, OEM India verification outstanding.
- Rolls-Royce: https://newsroom.rolls-roycemotorcars.com/all-products/ confirms four global names plus Extended and Black Badge derivatives; India-specific evidence pending.
- Nissan, Porsche, Renault, Skoda and Volvo: no sufficient results returned in this search batch; status unchanged. No production imports or prices approved.
