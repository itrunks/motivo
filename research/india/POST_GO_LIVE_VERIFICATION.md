# Post Go-Live Verification Backlog

Owner decision (2026-11-28): missing optional model/variant information is non-blocking. Keep model identity, publish only supported facts, display unavailable information, and defer unresolved gaps. Do not treat unattempted models as audited or unverified candidates as facts.

| Brand | Model / scope | Missing information | Status |
|---|---|---|---|
| Aston Martin | India lineup | Local variant availability | Deferred |
| Bentley | India lineup | Local model and variant availability | Deferred |
| Ferrari | India lineup | Local model and variant availability | Deferred |
| Lamborghini | India lineup | Local configurations | Deferred |
| Lexus | India lineup | Current grade combinations | Deferred |
| McLaren | India lineup | Local model and variant availability | Deferred |
| Toyota | Fortuner | Exact powertrain/drive/edition combinations | Deferred |
| Toyota | Camry | Exact grade applicability | Deferred |
| Toyota | Vellfire | Exact trim matrix | Deferred |
| Toyota | Hyryder | Remaining combinations and orderability | Deferred |
| Toyota | Legender | 48V mapping | Deferred |
| Toyota | Innova Hycross | Fleet grade applicability | Deferred |
| Tata Motors | Nexon | Exact gearbox and edition identity | Deferred |

Append model, field, source URL, attempt date, reason and status for subsequent gaps. Existing research candidates lacking independently confirmed evidence remain unverified and must not be published as facts. Unattempted models remain in the active inventory queue. Mandatory legal, security, data integrity and launch testing gates remain unchanged.

## Owner requirement: selectable vehicles and missing-data export

Retain known in-scope vehicle identities in selection lists even when variant or specification data is missing. Display `Not available` for missing information, not a claim that the vehicle is discontinued or the feature absent. Use machine-readable `not_available` for missing-data availability, retaining separate evidence/reason statuses. Do not invent placeholder variants. Provide a filterable/exportable missing-vehicle and missing-field report with brand, model, variant (nullable), field, source, attempt date, reason and review status. After launch, re-audit these entries and replace missing values only with supported evidence. Website and export implementation are pending roadmap tasks, not implemented by this documentation change.

## Stage 2 Arena bounded brochure checks (2026-11-28)

- Alto K10: brochure feature matrix not_available; PDF exceeds retrieval limit. https://www.marutisuzuki.com/arena/alto-k10/price. Price effective date and full variant feature mapping unresolved.
- Celerio: brochure feature matrix not_available; PDF exceeds retrieval limit; card transmission bullet conflicts with header. https://www.marutisuzuki.com/arena/celerio/price. Price effective date and full variant feature mapping unresolved.
- Eeco: brochure feature matrix not_available; PDF returned no extracted text. https://www.marutisuzuki.com/arena/eeco/price. Price effective date and full variant feature mapping unresolved.
- Ertiga: brochure feature matrix not_available; PDF viewer returned no brochure text. https://www.marutisuzuki.com/arena/ertiga/price. Price effective date and full variant feature mapping unresolved.

## Maruti bounded pass

All 17 model identities retained; full variant features and prices, real-world mileage, NVH, suspension, ownership and OEM accessories remain gaps unless separately established. Wagon R price URL inaccessible in this run. First four models' previously asserted observations remain unconfirmed; do not publish as verified. See `research/india/stage2-maruti-bounded-evidence-2026-11-28.json` for 13 model outcomes and per-field backlog.

## Hyundai selected-feature bounded pass

14 model outcomes, 13 retrieved feature pages and one inaccessible URL (IONIQ 5). 112 model-field gaps in `research/india/stage2-hyundai-bounded-2026-11-28.json`. Earlier generated safety matrix is superseded for selected observations; unrechecked cells remain unconfirmed. Retail availability and publication rights not established by this pass.

## Tata bounded pass

16 existing identities reviewed using retrieved catalogue and EV support results; 160 field gaps in `research/india/stage2-tata-bounded-2026-11-28.json`. Aeris newly listed: scope reconciliation pending before publication; XPRES retail applicability not assumed. Tigor and Tigor.ev retained; no discontinuation inferred. Individual model feature pages not freshly checked.

## Mahindra 2026-11-28

13 existing models reviewed: 10 listing-only, 3 selected FAQ facts. 117 unresolved field records in `research/india/stage2-mahindra-bounded-2026-11-28.json`. Bolero Neo Plus passenger scope review pending. Individual model pages not checked. Earlier brand claims not reverified.
