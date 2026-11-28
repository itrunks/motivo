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
