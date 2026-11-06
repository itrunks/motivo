# Motivo Catalogue Completion Roadmap

**Project target:** 100% evidence-backed catalogue normalization and validation.  
**Working branch:** `feature/catalogue-source-audit-ingestion`  
**Current PR:** #1 — https://github.com/itrunks/motivo/pull/1  
**Last checkpoint:** 2026-11-06 — BE 6 SPORTEQ eight-grade full-battery matrix and published BaaS observations committed; BaaS gaps remain explicit

## Progress rules

- Mark a task complete only after source evidence is captured, normalized files and notes are committed, and the committed files are fetched back and checked.
- Keep unknown values blank. Never infer trim, engine, fuel, transmission, body style, model year, price, or price effective dates.
- Keep OEM observations separate from confirmed current city-specific prices.
- Source rights remain `review_required` and commercial reuse/redistribution remain `unknown` until explicitly verified. Do not publish/import rights-unapproved data.
- Validate only changed/new files and affected logic; do not repeat the full baseline audit without a concrete reason.
- Update this roadmap and the checkpoint after each completed model/brand so work can resume in a new conversation.

## Master completion checklist

- [x] Initial source and catalogue audit baseline (224 URLs, 251 model records, 251 variant records, 502 crosswalk mappings, 35 brands)
- [x] Variant normalization work queue generated (251 model rows)
- [x] Staging/import safety documentation and validation tooling added
- [x] Hyundai — Creta normalization and evidence notes
- [x] Hyundai — Venue structure normalization and evidence notes
- [x] Hyundai — Exter structure + launch-price observations + evidence notes
- [x] Hyundai — Verna normalization and evidence notes
- [x] Hyundai — Aura structure normalization and evidence notes
- [x] Hyundai — Grand i10 NIOS structure normalization and evidence notes
- [x] Hyundai — i20 structure normalization and evidence notes
- [x] Hyundai — i20 N Line structure normalization and evidence notes
- [x] Hyundai — i20 N Line structure normalization and evidence notes
- [x] Hyundai — Alcazar structure normalization and evidence notes
- [x] Hyundai — Creta Electric structure normalization and evidence notes
- [x] Hyundai — IONIQ 5 current powertrain normalization and evidence notes
- [x] Hyundai — Venue N Line structure normalization and evidence notes
- [x] Hyundai — Creta N Line structure normalization and evidence notes
- [x] Hyundai — BAYON structure normalization and evidence notes
- [x] All 14 Hyundai work-queue models have a normalization evidence record
- [x] Hyundai — BAYON structure normalization and evidence notes
- [x] Hyundai — all 14 work-queue models normalized (staging only)
- [x] Mahindra — Scorpio-N 31 populated OEM grade/powertrain/drive/seating combinations normalized with dated ex-showroom observations (staging only)
- [ ] Mahindra — XUV 7XO full current gearbox/seating normalization (12 selector grade/fuel price observations captured; exact applicability still incomplete)
- [ ] Mahindra — Scorpio Classic current OEM price conflict resolved (two grades normalized; selector/detail-page amounts disagree)
- [ ] Mahindra — Bolero Neo price-version discrepancies reconciled (five grades normalized; four current/prior selector amounts differ)
- [ ] Mahindra — Bolero B4/B6 price-version discrepancies reconciled (four grades normalized; two current/prior selector amounts differ)
- [ ] Mahindra — XUV400 full current range/orderability verified (only one selector card exposed; EL PRO ST crosswalk and charger inclusion need confirmation)
- [x] Mahindra — BE 6 SPORTEQ eight-grade full-battery price matrix captured; BaaS upfront observations and charger exclusion kept separate
- [ ] Remaining brands/models in the work queue (process one evidence-backed model at a time)
- [ ] Reconcile normalized model/variant rows against the 251-row work queue and 502-row crosswalk
- [ ] Resolve source permission / commercial reuse / redistribution status for every source intended for production
- [ ] Confirm price scope, currency, tax basis, geography, and effective date wherever prices are to be production-ready
- [ ] Run final changed-file validation, complete test suite, typecheck, Functions build, emulator dry-run, and CI checks
- [ ] Produce final import-readiness report with explicit blocked / approved / unknown counts
- [ ] Production import approval gate (requires verified rights and explicit authorization)
- [ ] Firestore production import and publication (only after all gates pass and authorization is present)

## Brand/model work ledger

| Brand | Model | Structure | Price evidence | Evidence notes | Commit verification | Status |
|---|---|---|---|---|---|---|
| Hyundai | Creta | [x] | [x] OEM observations; current city price needs confirmation | [x] | [x] | Complete — staging only |
| Hyundai | Venue | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Exter | [x] | [x] launch observations; effective date/current city quote not confirmed | [x] | [x] | Complete — staging only |
| Hyundai | Verna | [x] | [x] dated launch observations; current city quote needs confirmation | [x] | [x] | Complete — staging only |
| Hyundai | Aura | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Grand i10 NIOS | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | i20 | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | i20 N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Alcazar | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Creta Electric | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | IONIQ 5 | [x] | [ ] | [x] | [x] | Complete — powertrain only |
| Hyundai | Venue N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | Creta N Line | [x] | [ ] | [x] | [x] | Complete — structure only |
| Hyundai | BAYON | [x] | [ ] | [x] | [x] | Complete — structure only |
| Kia | Sonet | [x] | [x] 8 trim prices; HTK missing | [x] | [x] | Complete — 24 combinations |
| Kia | Seltos | [x] | [x] 12 trim prices | [x] | [x] | Partial — T-GDi 6iMT trim mapping unresolved |
| Kia | Carens Clavis EV | [x] | [x] 9 trim prices | [x] | [x] | Complete — 17 battery/seating combinations |
| Kia | Syros | [x] | [x] 7 trim prices | [x] | [x] | Complete — 17 combinations |
| Kia | Carens Clavis | [ ] | [ ] | [x] | [x] | Blocked — unnamed trim column and price/powertrain reconciliation |
| Kia | Carnival | [x] | [x] 1 price | [x] | [x] | Complete — one India retail trim |
| Kia | EV6 | [x] | [ ] | [x] | [x] | Complete — current GT-Line AWD only; price unavailable |
| Kia | EV9 | [x] | [x] 1 price observation | [x] | [x] | Complete — one India retail trim |
| Toyota | Innova Crysta | [x] | [x] dated prices | [x] | [x] | Complete — 9 grade/seating configurations |
| Toyota | Innova Hycross | [x] | [x] model-level starting price | [x] | [x] | Complete — 12 grade/seating configurations |
| Toyota | Urban Cruiser Hyryder | [x] | [x] 11 configurator observations | [x] | [x] | Complete — 13 configurator variants |
| Toyota | Glanza | [ ] | [x] model starting price | [x] | [x] | Partial — 2026 trim mapping not published |
| Toyota | Urban Cruiser Taisor | [ ] | [x] historical launch prices | [x] | [x] | Blocked — current 2026 matrix/price not captured |
| Toyota | Fortuner | [ ] | [x] model start + Leader Edition prices | [x] | [x] | Partial — grade mapping unavailable |
| Toyota | Hilux | [x] | [x] 3 launch prices | [x] | [x] | Complete — 3 current grades |
| Toyota | Camry | [x] | [x] 1 current price | [x] | [x] | Complete — one current hybrid configuration |
| Toyota | Rumion | [x] | [x] 4 current + 1 historical price observation | [x] | [x] | Complete — 8 grade/powertrain combinations |
| Toyota | Urban Cruiser Ebella | [x] | [x] E3 price; E1/E2 unavailable | [x] | [x] | Complete — 3 battery/grade configurations |
| Toyota | Vellfire | [x] | [x] historical grade prices; current model start only | [x] | [x] | Complete — 2 grades |
| Toyota | Land Cruiser 300 | [x] | [x] dated grade prices + current listing discrepancy | [x] | [x] | Complete — 2 grades |
| Toyota | Legender | [ ] | [x] model start + dated launch prices | [x] | [x] | Partial — current grade mapping unavailable |
| Tata | Sierra.ev | [x] | [x] 8 price observations (secondary source) | [x] | [x] | Complete — 8 battery/drive configurations; dealer price cross-check required |
| Tata | Harrier.ev | [x] | [x] 6 prices (secondary source) | [x] | [x] | Complete — 12 battery/drive/charger configurations; dealer price cross-check required |
| Tata | Nexon.ev | [x] | [x] 7 current price observations (secondary source) | [x] | [x] | Complete — 7 battery/trim configurations |
| Tata | Punch.ev | [x] | [x] 6 official launch prices | [x] | [x] | Complete — 6 grade/battery configurations |
| Tata | Tiago.ev | [x] | [x] 4 facelift prices (secondary source) | [x] | [x] | Complete — 4 battery/grade configurations |
| Tata | Curvv.ev | [x] | [x] 3 official Series X prices | [x] | [x] | Complete — current Series X only |
| Tata | Tigor.ev | [x] | [x] model starting price only | [x] | [x] | Complete — 4 grades; trim prices not exposed |
| Tata | Sierra (ICE) | [x] | [x] 59 Delhi on-road prices (secondary source) | [x] | [x] | Complete — 59 unique variants; official price matrix still required |
| Tata | Harrier (ICE) | [x] | [x] 50 Delhi on-road prices (secondary source) | [x] | [x] | Complete — 50 variants; dealer quote and rights review required |
| Tata | Safari | [ ] | [ ] | [ ] | [ ] | Pending — next model |
| Tata | Safari | [x] | [x] 64 Delhi on-road prices (secondary source) | [x] | [x] | Complete — 64 variants; 6/7-seat combinations preserved |
| Tata | Nexon (ICE) | [x] | [x] 63 Delhi on-road prices (secondary source) | [x] | [x] | Complete — 63 petrol/diesel/CNG combinations |
| Tata | Punch (ICE) | [x] | [x] 26 Delhi on-road prices (secondary source) | [x] | [x] | Complete — petrol, CNG and turbo-petrol combinations |
| Tata | Altroz | [x] | [x] 27 Balod on-road prices (secondary source) | [x] | [x] | Complete — petrol, CNG and diesel combinations |
| Tata | Tiago (ICE) | [x] | [x] 20 Delhi on-road prices (secondary source) | [x] | [x] | Complete — 12 petrol and 8 CNG variants |
| Tata | Curvv (ICE) | [x] | [x] 26 Delhi on-road prices (secondary source) | [x] | [x] | Complete — current Series X; three engine families kept distinct |
| Tata | Tigor (ICE) | [x] | [x] 14 historical last-recorded prices | [x] | [x] | Complete — discontinued September 2026; historical-only |
| Tata | Tata ICE workqueue review | [ ] | [ ] | [ ] | [ ] | Reconcile remaining queue models and check catalogue completeness |
| Tata | Nexon (ICE) | [ ] | [ ] | [ ] | [ ] | Pending |
| Tata | Punch (ICE) | [ ] | [ ] | [ ] | [ ] | Pending |
| Tata | Altroz | [ ] | [ ] | [ ] | [ ] | Pending |
| Tata | Tiago (ICE) | [ ] | [ ] | [ ] | [ ] | Pending |
| Tata | Curvv (ICE) | [ ] | [ ] | [ ] | [ ] | Pending |
| Tata | Tigor (ICE) | [ ] | [ ] | [ ] | [ ] | Pending |
| Maruti Suzuki | Alto K10 | [x] | [x] 8 official ex-showroom prices | [x] | [x] | Complete — 6 petrol and 2 S-CNG variants |
| Maruti Suzuki | Celerio | [x] | [x] 8 official ex-showroom prices | [x] | [x] | Complete — 7 petrol and 1 S-CNG configurations |
| Maruti Suzuki | Eeco | [x] | [x] 4 official ex-showroom prices | [x] | [x] | Complete — passenger variants only; ambulance/cargo excluded |
| Maruti Suzuki | Ertiga | [x] | [x] 9 official ex-showroom prices | [x] | [x] | Complete — 7 petrol and 2 S-CNG variants |
| Maruti Suzuki | S-Presso | [x] | [x] 8 official ex-showroom prices | [x] | [x] | Complete — 6 petrol and 2 S-CNG variants |
| Maruti Suzuki | Swift | [x] | [x] 17 official ex-showroom prices | [x] | [x] | Complete — petrol and CNG manual/AGS including new CNG AGS |
| Maruti Suzuki | Victoris | [x] | [x] 21 official ex-showroom prices | [x] | [x] | Complete — petrol, S-CNG, strong hybrid and ALLGRIP AWD |
| Maruti Suzuki | Wagon R | [x] | [x] 12 official ex-showroom prices | [x] | [x] | Complete — 1.0L/1.2L petrol, S-CNG and flex-fuel selector entry |
| Maruti Suzuki | Baleno | [x] | [x] 13 official NEXA ex-showroom prices | [x] | [x] | Complete — current petrol/S-CNG manual and AGS matrix |
| Maruti Suzuki | Fronx | [x] | [x] 12 official NEXA ex-showroom prices | [x] | [x] | Complete — K-Series petrol/CNG and Turbo Boosterjet kept distinct |
| Maruti Suzuki | XL6 | [x] | [x] 7 official NEXA ex-showroom prices | [x] | [x] | Complete — 6-seat petrol Smart Hybrid and CNG variants |
| Maruti Suzuki | Invicto | [x] | [x] 3 official NEXA ex-showroom prices | [x] | [x] | Complete — 7-seat and 8-seat strong-hybrid configurations |
| Maruti Suzuki | e Vitara | [x] | [x] 3 battery-grade prices (secondary) + official BaaS offer | [x] | [x] | Complete — 49/61 kWh LFP, Delta/Zeta/Alpha; BaaS separated |
| Mahindra | XUV 3XO | [x] | [x] 31 Fatehabad on-road + 18 OEM ex-showroom observations | [x] | [x] | Complete — 31 variants; official selector price coverage partial, price sets kept separate |
| Mahindra | Thar OG | [x] | [x] 15 official introductory ex-showroom prices | [x] | [x] | Complete — 3 engines, RWD/4WD, MT/AT; launch price valid through 30 Nov 2026 |
| Mahindra | Thar ROXX | [x] | [x] 21 Delhi on-road prices (secondary source) | [x] | [x] | Complete — petrol/diesel, RWD/4WD, manual/automatic; Mocha interior codes kept separate |
| Mahindra | Scorpio N | [x] | [x] 31 populated OEM ex-showroom observations (2026-08-05 matrix) | [x] | [x] | Complete — 31 populated grade/powertrain/drive/seating combinations; price freshness and source rights still require review |
| Mahindra | XUV 7XO | [ ] | [x] 12 current selector grade/fuel price observations | [x] | [x] | Partial — current selector does not expose exact gearbox/seating applicability; launch prices were introductory and kept separate |
| Mahindra | Scorpio Classic | [x] | [ ] 4 official observations quarantined due price conflict | [x] | [x] | Partial — two grades normalized; selector and detail pages disagree on both prices |
| Mahindra | Bolero Neo | [x] | [ ] 5 current selector prices; 4 version conflicts | [x] | [x] | Partial — five grades normalized; prior/current selector captures disagree for four grades |
| Mahindra | Bolero | [x] | [ ] 4 current selector prices; 2 version conflicts | [x] | [x] | Partial — four grades normalized; current/prior selector captures disagree for B4 and B6 |
| Mahindra | XUV400 | [ ] | [x] 1 current selector price observation | [x] | [x] | Partial — only one card exposed; current orderability and charger inclusion require dealer confirmation |
| Mahindra | BE 6 SPORTEQ | [x] | [x] 10 full-battery + 2 BaaS price observations | [x] | [x] | Complete — eight OEM grades and all published battery-price combinations; BaaS and charger caveats preserved |
| Maruti Suzuki | Dzire | [x] | [x] 11 official ex-showroom prices | [x] | [x] | Complete — petrol/CNG manual and AGS including new CNG AGS |
| Maruti Suzuki | Brezza | [x] | [x] 13 October 2026 ex-showroom prices (secondary source) | [x] | [x] | Complete — turbo Boosterjet, K15C petrol and S-CNG kept distinct |
| Maruti Suzuki | Grand Vitara | [x] | [x] 20 Delhi on-road prices (secondary source) | [x] | [x] | Complete — petrol, CNG, strong hybrid and ALLGRIP AWD kept distinct |
| Maruti Suzuki | Jimny | [x] | [x] 4 official Delhi ex-showroom prices | [x] | [x] | Complete — 4-seat ALLGRIP PRO 4WD, MT/AT |
| Maruti Suzuki | Ignis | [ ] | [ ] | [ ] | [ ] | Pending — next model |
| VinFast | VF 6 | [x] | [x] model-level starting price only | [x] | [x] | Complete — Earth/Wind/Wind Infinity; no trim prices inferred |
| VinFast | VF 7 | [x] | [x] model-level starting price only | [x] | [x] | Complete — five variants; 70.8 gross/70 usable battery distinction retained |
| VinFast | VF MPV 7 | [x] | [x] current + historical launch price | [x] | [x] | Complete — single 7-seat configuration; November 2026 price reduction recorded |
| Tesla | Model Y | [x] | [x] 2 official base prices + inventory total observations | [x] | [x] | Complete — Premium RWD and 6-seat Model Y L AWD; price bases separated |
| Force Motors | Gurkha | [x] | [x] 2 official ex-showroom price observations | [x] | [x] | Complete — 3-door 4-seat and 5-door 7-seat 4WD configurations |
| MINI | Cooper (3-Door) | [x] | [x] 3 Delhi on-road observations | [x] | [x] | Complete — 3 petrol trim/edition variants |
| MINI | Cooper Convertible | [x] | [x] 3 Delhi on-road observations | [x] | [x] | Complete — 3 petrol convertible editions |
| MINI | Countryman C | [x] | [x] 1 Delhi on-road observation | [x] | [x] | Complete — one locally assembled petrol configuration |
| MINI | Countryman Electric | [x] | [x] 4 Delhi on-road observations | [x] | [x] | Complete — single-motor E trims and dual-motor SE ALL4 kept distinct |
| MINI | John Cooper Works Countryman ALL4 | [x] | [x] 1 Delhi on-road observation | [x] | [x] | Complete — one 2.0L AWD petrol configuration |
| MG | Comet EV | [x] | [x] 5 standard-purchase prices | [x] | [x] | Complete — 5 current variants |
| MG | Windsor EV | [x] | [x] 6 standard/edition prices | [x] | [x] | Complete — 5 grades + INDULGE |
| MG | ZS EV | [x] | [x] 6 current prices | [x] | [x] | Complete — 6 retail/interior configurations |
| MG | Hector | [ ] | [x] 2 current Storm edition prices | [x] | [x] | Partial — full trim/powertrain matrix unavailable |
| MG | Astor | [x] | [x] 7 prices effective 2026-01-02 | [x] | [x] | Complete — dealer order availability caveat |
| MG | Hector Tomahawk EV | [x] | [x] 4 full-ownership prices | [x] | [x] | Complete — 4 grade/seating configurations |
| MG | Hector Tomahawk PHEV | [x] | [x] 2 full-ownership prices | [x] | [x] | Complete — 2 current 7-seat configurations |
| MG | Majestor | [ ] | [x] 2 model-level price observations | [x] | [x] | Partial — grade/seat/drive mapping unavailable |
| MG | Cyberster | [x] | [x] full ownership + BaaS price bases | [x] | [x] | Complete — one roadster configuration |
| MG | M9 | [x] | [x] launch + BaaS + Couture price bases | [x] | [x] | Complete — standard and Couture Edition |

## Resume/checkpoint protocol

1. Read this file first on every continuation.
2. Confirm the current branch and PR head; do not assume the previous session's last write succeeded.
3. Fetch the latest work-queue and relevant evidence files. Continue from the first unchecked model.
4. Research official/manufacturer sources first; capture exact source URLs and checked date.
5. Keep structure and price evidence separate when their source scope/date differs.
6. Commit each completed model's data and evidence notes to the working branch.
7. Fetch the committed files back and verify row/column counts and key fields.
8. Update this ledger and the master checklist in the same branch.
9. Report only verified completion. If a session/window ends, the next session resumes from this file and the branch state.

## Safety / publication gates

- [x] No automatic production writes during normalization
- [x] No automatic publication of source material
- [ ] Source rights verified for every production-bound source
- [ ] Data quality and crosswalk reconciliation passed
- [ ] Final validation and CI passed on the final PR head
- [ ] Explicit production-import authorization received
