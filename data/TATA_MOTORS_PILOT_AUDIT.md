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
