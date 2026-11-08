# Tata Motors India current model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://tatamotors-prod.adobecqms.net/

## Official catalogue candidates

The Tata Cars official web catalogue currently displays these passenger-car nameplates:

- Aeris
- Curvv / Curvv.ev
- Sierra / Sierra.ev
- Harrier / Harrier.ev
- Safari
- Nexon / Nexon.ev
- Punch / Punch.ev
- Altroz
- Tiago / Tiago.ev
- XPRES

The official catalogue also has model pages for Sierra, Punch, Harrier, Safari, Nexon, Altroz, Tiago and Curvv. Treat this as official catalogue evidence, not proof that every model/variant is currently orderable at every dealer. Confirm current orderability and model-year/variant matrix against the live OEM configurator or current dated price list before import.

## Current model discovery cross-check

Autocar India's current Tata range page (discovery only, not a primary source for vehicle facts) reports these retail models: Tiago, Tiago EV, Punch, Punch EV, Sierra, Sierra EV, Nexon, Nexon EV, Curvv, Curvv EV, Harrier, Harrier EV, Safari, Altroz, Tigor, Tigor EV and Aeris. It separately lists commercial/fleet models such as XPRES and pickup Yodha; keep those outside the retail passenger scope unless explicitly approved.

## Model audit queue

| Model family | Fuel/powertrain families to verify | Exact variant-price capture |
|---|---|---|
| Tiago | Petrol / CNG | Not captured from OEM price cards |
| Tiago EV | Electric | Not captured from OEM price cards |
| Punch | Petrol / CNG | Not captured from OEM price cards |
| Punch EV | Electric | Not captured from OEM price cards |
| Sierra | Petrol / Diesel | Not captured from OEM price cards |
| Sierra EV | Electric | Not captured from OEM price cards |
| Nexon | Petrol / Diesel / CNG | Not captured from OEM price cards |
| Nexon EV | Electric | Not captured from OEM price cards |
| Curvv | Petrol / Diesel | Not captured from OEM price cards |
| Curvv EV | Electric | Not captured from OEM price cards |
| Harrier | Petrol / Diesel | Not captured from OEM price cards |
| Harrier EV | Electric | Not captured from OEM price cards |
| Safari | Petrol / Diesel | Not captured from OEM price cards |
| Altroz | Petrol / Diesel / CNG | Not captured from OEM price cards |
| Tigor | Petrol / CNG | Current official orderability needs confirmation |
| Tigor EV | Electric | Current official orderability needs confirmation |
| Aeris | Powertrain and exact product identity require OEM confirmation |

## Important identity and scope flags

- The official web catalogue labels a model as **Aeris**. Do not silently rename it to another Tata nameplate or assume the identity/specifications; obtain an official model page, brochure and variant list before creating catalogue entities.
- The official catalogue includes XPRES. Treat XPRES fleet/taxi products separately from retail passenger cars unless the product scope explicitly includes fleet-only vehicles.
- Tata's commercial vehicle and pickup range must not be mixed into passenger-car records.
- EV and ICE versions are separate model entities where the OEM markets them as distinct products (for example Nexon and Nexon.ev).
- A third-party November 2026 listing reports many exact variant prices, but those figures are not accepted as OEM observations. Use only as a reconciliation lead after official source confirmation.
- No model-level starting price or third-party price range is converted into variant prices.
- No city-wise on-road prices captured.
- OEM source reuse / redistribution permission remains review required.
- No Firestore import performed.

## Sources

Official:
- https://tatamotors-prod.adobecqms.net/

Discovery/cross-check only:
- https://www.autocarindia.com/cars/tata
- https://www.cardekho.com/cars/Tata
- https://www.zigwheels.com/tata-cars/

This is a source-audit workpaper, not an approved import manifest.


## OEM catalogue and price-source recheck

Rechecked: 2026-11-06
Primary source: https://tatamotors-prod.adobecqms.net/

The official Tata Cars navigation and model catalogue currently expose these distinct entries:
- Sierra, Sierra.ev
- Harrier, Harrier.ev
- Safari
- Nexon, Nexon.ev
- Punch, Punch.ev
- Altroz
- Tiago, Tiago.ev
- Curvv, Curvv.ev
- Tigor, Tigor.ev
- XPRES

The homepage states that displayed prices are ex-showroom and subject to change without prior notice, and advises customers to contact a Tata dealer for exact prices. However, the captured official page does not expose exact variant price cards or a complete downloadable current price matrix. Consequently, **no exact Tata variant prices are approved from this OEM page capture**.

### Corrections to the initial candidate list

- The official catalogue confirms Tigor and Tigor.ev as named model entries. Keep them in the audit queue, but validate retail orderability and model-year applicability before import.
- XPRES is listed on the official passenger-car web catalogue. Keep it as a separately classified fleet/taxi-oriented product and do not mix it with ordinary retail passenger trims until its catalogue scope is decided.
- Aeris appears on the official site but the captured official navigation does not expose a separate Aeris model link alongside the other model links. Treat identity, model category, variant lineup and orderability as unresolved pending a dedicated official model page/brochure. Do not create a fully specified vehicle entity from its name alone.
- Sierra and Sierra.ev, and the other ICE/EV pairs, are distinct catalogue entries on the official website; keep them as separate model entities.

### Variant-price discovery leads (not accepted as source-of-truth)

Third-party sources updated in November 2026 publish extensive Tata variant-level tables. For example, V3Cars lists 20 Tiago petrol/CNG variants and gives variant-level ex-showroom and Delhi on-road prices. This is a discovery lead only. The values are not imported into this OEM audit as official price observations because:
1. Tata's official page capture did not expose a matching variant-price table.
2. The third-party page itself records a Tiago May 2026 launch and a September 2025 GST price revision, while Tata's wider portfolio had a September 2026 price revision.
3. Without a matching dated OEM price list, exact variant names and amounts cannot be certified as current.

A November 2026 third-party overview reports Tiago from ₹4.77 lakh and Aeris from ₹5.30 lakh, but these model-level amounts are not converted into variant-level prices.

### Current evidence status

| Model family | OEM catalogue presence | Exact OEM variant price evidence in this pass |
|---|---|---|
| Sierra / Sierra.ev | Listed | Not exposed |
| Harrier / Harrier.ev | Listed | Not exposed |
| Safari | Listed | Not exposed |
| Nexon / Nexon.ev | Listed | Not exposed |
| Punch / Punch.ev | Listed | Not exposed |
| Altroz | Listed | Not exposed |
| Tiago / Tiago.ev | Listed | Not exposed |
| Curvv / Curvv.ev | Listed | Not exposed |
| Tigor / Tigor.ev | Listed | Not exposed |
| XPRES | Listed; separate scope | Not exposed |
| Aeris | Name shown on OEM homepage; identity details unresolved | Not exposed |

No city-wise on-road prices captured. No variant prices inferred from third-party sources. OEM terms/reuse permission remain review required. No Firestore import performed.

Sources:
- Official OEM catalogue: https://tatamotors-prod.adobecqms.net/
- Third-party discovery only: https://www.v3cars.com/tata-cars/tiago
- Third-party discovery only: https://www.autocarindia.com/cars/tata
- Third-party discovery only: https://www.zigwheels.com/tata-cars/
- Third-party discovery only: https://www.mycarhelpline.com/index.php?Itemid=2&brand=7&option=com_newcar&view=category
