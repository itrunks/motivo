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
| MG Motor | 10 | Pending |
| Tata Motors | 16 | Pending |
| MINI | 5 | Pending |
| Force Motors | 1 | Pending |
| Tesla | 1 | Pending |
| VinFast | 3 | Pending |
| Audi | 9 | Pending |
| BMW | 22 | Pending |
| BYD | 4 | Pending |
| Citroën | 5 | Pending |
| Honda | 5 | Pending |
| Jeep | 4 | Pending |
| Lamborghini | 3 | Pending |
| Land Rover | 7 | Pending |
| Lexus | 5 | Pending |
| Maserati | 7 | Pending |
| Aston Martin | 4 | Pending |
| Bentley | 5 | Pending |
| Ferrari | 7 | Pending |
| McLaren | 3 | Pending |
| Mercedes-Benz | 24 | Pending |
| Nissan | 3 | Pending |
| Porsche | 5 | Pending |
| Renault | 4 | Pending |
| Rolls-Royce | 4 | Pending |
| Škoda | 6 | Pending |
| Volkswagen | 4 | Pending |
| Volvo Cars | 5 | Pending |
| Isuzu | 1 | Pending |
| Lotus | 3 | Pending |

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
