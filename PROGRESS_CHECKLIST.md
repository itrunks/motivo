# Motivo Catalogue Progress Checklist

Last verified: 2026-11-06  
Branch: `feature/catalogue-source-audit-ingestion`  
PR: https://github.com/itrunks/motivo/pull/1

## Overall status

- Audited work queue: 251 models across 35 brands.
- Models with normalization work committed and fetched back: 103.
- Completed/staging-ready model evidence: 68.
- Partial models needing exact trim/price mapping: 33.
- Explicitly blocked models: 2.
- Not yet started: 148 models across 30 brands.

**Important:** “Complete” means research/normalization files and evidence notes are committed and verified. It does not mean commercial reuse rights are approved or production import is authorized. Source rights remain `review_required` / `unknown` unless separately proven.

## Brand checklist

| Brand | Models in queue | Completed | Partial | Blocked | Pending | Status |
|---|---:|---:|---:|---:|---:|---|
| Hyundai | 14 | 14 | 0 | 0 | 0 | Complete — staging |
| Kia | 9 | 8 | 1 | 0 | 0 | Audited with partial evidence |
| Toyota | 13 | 9 | 3 | 1 | 0 | Partial |
| MG | 10 | 8 | 2 | 0 | 0 | Partial |
| Tata | 16 | 16 | 0 | 0 | 0 | Complete — source/price caveats documented |
| MINI | 5 | 3 | 2 | 0 | 0 | Audited with partial price evidence |
| Force Motors | 1 | 0 | 1 | 0 | 0 | Audited with official price conflict |
| Tesla | 1 | 1 | 0 | 0 | 0 | Complete — two current India derivatives and official base prices verified |
| VinFast | 3 | 1 | 2 | 0 | 0 | Audited with partial grade-price evidence |
| Maruti Suzuki | 17 | 0 | 0 | 0 | 17 | Pending |
| Mahindra | 13 | 5 | 8 | 0 | 0 | Audited with partial evidence |
| Audi | 9 | 0 | 9 | 0 | 0 | Audited with official price gaps |
| BMW | 22 | 3 | 6 | 0 | 13 | In progress |
| BYD | 4 | 0 | 0 | 0 | 4 | Pending |
| Citroën | 5 | 0 | 0 | 0 | 5 | Pending |
| Honda | 5 | 0 | 0 | 0 | 5 | Pending |
| Jeep | 4 | 0 | 0 | 0 | 4 | Pending |
| Lamborghini | 3 | 0 | 0 | 0 | 3 | Pending |
| Land Rover | 7 | 0 | 0 | 0 | 7 | Pending |
| Lexus | 5 | 0 | 0 | 0 | 5 | Pending |
| Maserati | 7 | 0 | 0 | 0 | 7 | Pending |
| Aston Martin | 4 | 0 | 0 | 0 | 4 | Pending |
| Bentley | 5 | 0 | 0 | 0 | 5 | Pending |
| Ferrari | 7 | 0 | 0 | 0 | 7 | Pending |
| McLaren | 3 | 0 | 0 | 0 | 3 | Pending |
| Mercedes-Benz | 24 | 0 | 0 | 0 | 24 | Pending |
| Nissan | 3 | 0 | 0 | 0 | 3 | Pending |
| Porsche | 5 | 0 | 0 | 0 | 5 | Pending |
| Renault | 4 | 0 | 0 | 0 | 4 | Pending |
| Rolls-Royce | 4 | 0 | 0 | 0 | 4 | Pending |
| Škoda | 6 | 0 | 0 | 0 | 6 | Pending |
| Volkswagen | 4 | 0 | 0 | 0 | 4 | Pending |
| Volvo Cars | 5 | 0 | 0 | 0 | 5 | Pending |
| Isuzu | 1 | 0 | 0 | 0 | 1 | Pending |
| Lotus | 3 | 0 | 0 | 0 | 3 | Pending |

## Current model-level exceptions

### Kia
- Seltos — T-GDi 6iMT grade mapping still unresolved.
- Carens Clavis — unnamed trim column and powertrain/price reconciliation blocker.

### Toyota
- Glanza — 2026 trim-to-powertrain mapping not published in captured official source.
- Urban Cruiser Taisor — only historical 2024 launch matrix captured; current 2026 grade/price matrix needed.
- Fortuner — powertrain families and special edition prices captured; complete grade mapping needed.
- Legender — powertrain families and historical prices captured; current grade/drive mapping needed.

### MG
- Hector — current 2026 Storm editions captured; full 49-row trim/powertrain matrix still needed.
- Majestor — 2WD/4WD grade families captured; exact 6/7-seat and grade price mapping needed.

### Mahindra
- XUV 7XO — 12 current selector grade/fuel price observations captured; exact transmission and seating mapping remain unavailable in the captured OEM selector. Introductory launch prices are not reused as current prices.
- Scorpio Classic — two grades and shared powertrain structure captured. Selector and model detail pages disagree on both ex-showroom amounts; all four observations remain quarantined.
- Bolero Neo — five current selector grades and shared powertrain structure captured. Four current/prior selector price pairs differ; no amount selected for import.
- Bolero — four current selector grades and shared powertrain structure captured. Current/prior selector values differ for B4 and B6; both observations are retained.
- XUV400 — current selector exposes one EL PRO ST 39.4 kWh / 7.2 kW card. The 2024 brochure supports the powertrain crosswalk, but the suffix, charger inclusion and current orderability require dealer confirmation.
- XEV 9e — standard pack prices are February 2025 historical observations; Cineluxe Edition has a March 2026 price; BaaS starts at ₹13.90L with ₹3.75/km battery financing, but no grade-wise current matrix is published in the captured source.
- XUV 3XO EV — AX5 and AX7L launch prices from January 6, 2026 are captured; no current selector price/orderability confirmation found.
- XEV 9S — six grade/battery configurations captured; launch source provides only starting and top prices, while BaaS release provides only a model-level start. Intermediate grade-wise prices remain missing.

### Tata
- Harrier — four engine/transmission families captured; full 49-variant grade matrix still needed.
- Safari — four engine/transmission families captured; full 64-variant grade/seating matrix still needed.
- Sierra — 59 variants captured in three files; prices are secondary-source on-road Delhi observations.
- Remaining queued Tata models: Nexon, Punch, Altroz, Tiago, Curvv and Tigor.

## Verified work artifacts

- Hyundai: Creta, Venue, Exter, Verna, Aura, Grand i10 NIOS, i20, i20 N Line, Alcazar, Creta Electric, IONIQ 5, Venue N Line, Creta N Line, BAYON.
- Kia: Sonet, Seltos, Carens Clavis EV, Syros, Carens Clavis, Carnival, EV6, Carens, EV9.
- Toyota: Innova Crysta, Innova Hycross, Urban Cruiser Hyryder, Glanza, Urban Cruiser Taisor, Fortuner, Hilux, Camry, Rumion, Urban Cruiser Ebella, Vellfire, Land Cruiser 300, Legender.
- MG: Comet EV, Windsor EV, ZS EV, Hector, Astor, Hector Tomahawk EV, Hector Tomahawk PHEV, Majestor, Cyberster, M9.
- Tata: Sierra.ev, Harrier.ev, Nexon.ev, Punch.ev, Tiago.ev, Curvv.ev, Tigor.ev, Sierra, Harrier, Safari.
- Mahindra: XUV 3XO, Thar OG, Thar ROXX, Scorpio-N, BE 6 SPORTEQ (complete); XUV 7XO, Scorpio Classic, Bolero Neo, Bolero, XUV400, XEV 9e, XUV 3XO EV and XEV 9S (partial evidence).

## Resume protocol

1. Read this checklist and `ROADMAP.md` before doing new work.
2. Read the 251-row work queue and continue from the first model not yet complete.
3. Use official manufacturer sources first; use secondary price sources only when clearly labelled.
4. Preserve city scope, price basis and effective date; never mix ex-showroom and on-road prices.
5. Leave unknown trim/engine/gearbox/seat/price fields blank. Do not infer combinations.
6. Commit each model's data and evidence notes to the feature branch; fetch back and verify row counts.
7. Update this checklist after each brand/model batch.
8. No Firestore production writes or publication until rights, data reconciliation, CI and explicit authorization gates pass.
