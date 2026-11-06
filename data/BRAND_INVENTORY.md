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
