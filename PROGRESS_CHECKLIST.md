# Motivo Catalogue Progress Checklist

Last verified: 2026-11-07  
Branch: `feature/catalogue-source-audit-ingestion`  
PR: https://github.com/itrunks/motivo/pull/1

## Overall status

- Audited work queue: 251 models across 35 brands.
- Models with normalization work committed and fetched back: 122.
- Completed/staging-ready model evidence: 83.
- Partial models needing exact trim/price mapping: 30.
- Explicitly blocked models: 2.
- Not yet started: 136 models across 30 brands.

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
| Mahindra | 13 | 12 | 1 | 0 | 0 | Audited with partial evidence |
| Audi | 9 | 0 | 9 | 0 | 0 | Audited with official price gaps |
| BMW | 22 | 11 | 10 | 0 | 1 | In progress |
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
- Carens Clavis — live comparison page rechecked 2026-11-07; 11 named grade prices and 28 configurations unchanged. Twelfth column still blank header, ₹ only and 7DCT included; showroom GT-Line/X-Line selector does not identify it. Keep quarantined.

### Toyota
- Glanza — current 2026 showroom maps E/S/G/V petrol and S/G CNG across MT/AMT (11 explicit combinations). Feature matrix also shows V(O) MT/AMT, but technical Variant Type summary omits V(O); hold as two candidates. ₹6.99L is model-level starting price only; Toyota price-list portal requires dealer selection.
- Urban Cruiser Taisor — only historical 2024 launch matrix captured; current 2026 grade/price matrix needed.
- Fortuner — powertrain families and special edition prices captured; complete grade mapping needed.
- Legender — powertrain families and historical prices captured; current grade/drive mapping needed.

### MG
- Hector — current 2026 Storm editions captured; full 49-row trim/powertrain matrix still needed.
- Majestor — 2WD/4WD grade families captured; exact 6/7-seat and grade price mapping needed.

### Mahindra
- XUV 7XO — 12 current selector grade/fuel price observations captured; exact transmission and seating mapping remain unavailable in the captured OEM selector. Introductory launch prices are not reused as current prices.
- Scorpio Classic — two grades and shared powertrain structure captured. Current selector and both model detail pages now agree on ₹13,43,200 (S) and ₹17,48,400 (S11) after 2026-11-07 recheck; effective date/city and rights remain pending.
- Bolero Neo — five current selector grades and shared 7-seat diesel/manual/2WD powertrain captured. Live selector rechecked 2026-11-07; N8/N10 OPT/N11 detail pages agree, while N4/N10 (R) are selector-only. Prior values retained as superseded snapshots.
- Bolero — four current grades and shared powertrain structure captured. Current selector/detail pages agree for B6, B6 OPT and B8; B4 retains a ₹1 selector/detail delta. Prior values are superseded captures.
- XUV400 — current selector exposes one EL PRO ST 39.4 kWh / 7.2 kW card. The 2024 brochure supports the powertrain crosswalk, but the suffix, charger inclusion and current orderability require dealer confirmation.
- XEV 9e — current FAQ confirms five main grade prices plus Cineluxe and four variant-wise BaaS upfront prices. Current brochure confirms six pack/battery configurations. Pack Two ₹24.90L is not mapped to 59 vs 79 kWh; no price effective date is published. BaaS is dual-loan financing, not per-km rental.
- XUV 3XO EV — AX5 and AX7L launch prices from January 6, 2026 are captured; no current selector price/orderability confirmation found.
- XEV 9S — current FAQ provides 10 full-battery prices across 6/7-seat configurations and six grade/battery BaaS upfront prices. Current brochure confirms battery, power, torque, RWD and range. Price effective date is not shown; source rights remain pending.

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
- MINI: Cooper Convertible — current MINI India page shows ₹58.50L for Favoured Trim (204PS); JCW Pack page starts at ₹58.50L; Stardust page confirms 204hp/300Nm but no price. Base Cooper performance-level price and Stardust official price remain unresolved; Autocar Delhi on-road observations remain secondary.
- Mahindra: XUV 3XO, Thar OG, Thar ROXX, Scorpio-N, XUV 7XO, Scorpio Classic, Bolero Neo, Bolero, XUV400, XEV 9e, XEV 9S, BE 6 SPORTEQ (complete); XUV 3XO EV (partial evidence).

## Resume protocol

1. Read this checklist and `ROADMAP.md` before doing new work.
2. Read the 251-row work queue and continue from the first model not yet complete.
3. Use official manufacturer sources first; use secondary price sources only when clearly labelled.
4. Preserve city scope, price basis and effective date; never mix ex-showroom and on-road prices.
5. Leave unknown trim/engine/gearbox/seat/price fields blank. Do not infer combinations.
6. Commit each model's data and evidence notes to the feature branch; fetch back and verify row counts.
7. Update this checklist after each brand/model batch.
8. No Firestore production writes or publication until rights, data reconciliation, CI and explicit authorization gates pass.


### BMW
- i4 — two India-market variants (eDrive35 M Sport and eDrive40 M Sport) normalized from the official December 2023 specification sheet. BMW India's current all-models catalogue does not list i4; no current official price or orderability confirmation was found. Retained as partial; no price inferred.


### BMW
- i5 — one current India configuration, BMW i5 M60 xDrive, normalized from BMW India technical data. Current all-models catalogue lists ₹1,19,50,000 ex-showroom. i5 LWB is tracked separately and is not merged into this record.


### BMW
- i5 Long Wheelbase — one current India configuration, eDrive35L M Sport, normalized from BMW India product page and 7 September 2026 OEM launch release. Current product page displays ₹79,60,000 ex-showroom; launch release describes it as introductory pricing. Limited First Edition was sold out before launch and is not treated as current orderable variant.


### BMW
- iX — historical India iX xDrive40 (December 2021) and iX xDrive50 (March 2024) technical configurations and dated OEM launch prices captured. Current BMW India full-electric catalogue no longer lists iX; current orderability and price remain unverified.

### BMW
- iX1 Long Wheelbase — current eDrive20L M Sport normalized from BMW India September 2026 brochure and product page: 150 kW/204 hp, 250 Nm, FWD, 66.4 kWh, 546 km MIDC, 8.6 s, 130 kW DC and 11 kW AC. Current BMW India product page displays ₹54.70L; page tax basis and city applicability require dealer confirmation. Transmission not stated and left blank.

### BMW
- M2 — standard M2 automatic/manual (480 hp; 600/550 Nm; 8-speed auto/optional 6-speed manual), M2 CS (530 hp/650 Nm, RWD, 8-speed auto, ₹1.66Cr March 2026 launch price) and M2 xDrive Turbo Edition (480 hp, 3.7 s, limited pre-orders opened Oct 2026) recorded separately. Current catalogue displays standard M2 from ₹1.065Cr. Turbo Edition India price, torque and transmission not announced in OEM release; CS launch price retained as historical after Apr 2026 range price increase. Partial.

### BMW
- M4 Competition — current India M4 Competition M xDrive Coupé normalized: 3.0L S58 petrol, 2,993 cc, 390 kW/530 hp, 650 Nm, 8-speed automatic, AWD, 3.5 s 0–100, 250 km/h. Current product page displays ₹1.629Cr; 2024 launch price ₹1.53Cr retained historically. M4 CS excluded as a separate model.\n\n### BMW\n- M5 — current India M5 Sedan M Hybrid normalized: 4.4L S68 V8 PHEV, system 535 kW/727 hp and 1,000 Nm, ICE 430 kW/585 hp and 750 Nm, electric drive 145 kW/197 hp and 280 Nm, 8-speed M Steptronic, M xDrive AWD, 3.5 s 0–100, 69 km WLTP electric range, 5 seats. Current catalogue price ₹2.115Cr; 2024 launch price ₹1.99Cr historical. 100 Jahre Nürburgring appearance edition included; battery capacity left blank due to source unit inconsistency.
