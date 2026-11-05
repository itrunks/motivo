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
