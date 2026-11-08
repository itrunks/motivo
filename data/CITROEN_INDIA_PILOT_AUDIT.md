# Citroën India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.citroen.in/

## Official catalogue snapshot

Citroën India's current official homepage promotes five product entries:
- Citroën AircrossX
- Citroën ë-C3X
- Citroën C5 Aircross
- Citroën C3X
- Citroën BasaltX

The homepage "Origins" copy repeats C3X, ë-C3X, BasaltX, AircrossX and C5 Aircross as the India range. Preserve the current OEM suffix X in the model/edition label. Do not silently collapse AircrossX to Aircross, BasaltX to Basalt, or C3X to C3 without model-year/identity reconciliation.

## Canonical model and product-family rules

- C3X and ë-C3X are separate ICE and EV product records. Do not merge powertrain or price histories.
- AircrossX and BasaltX are separate nameplates.
- C5 Aircross is a separate premium diesel SUV; verify its current retail orderability and current-generation model-year before treating its homepage presence as active dealer orderability.
- Citroën's official news release calls the enhanced-range EV "ë-C3X EXTENDED"; treat EXTENDED as a range/variant edition under ë-C3X, not a separate nameplate.
- YOU Turbo and MAX NA are official trim/edition labels used on AircrossX and BasaltX. Preserve powertrain suffixes and edition labels rather than flattening them into generic grade names.
- "MAX NA" is available in petrol and CNG according to the release; retain fuel as a variant dimension.

## Audit matrix

| Official model | Product class / powertrain | Exact official price evidence |
|---|---|---|
| C3X | Petrol/CNG hatchback; NA and turbo/MT/AT mapping needs current brochure/configurator validation | Homepage and third-party price ranges are discovery only; no exact current OEM trim price table captured |
| ë-C3X | Electric hatchback; standard/extended range, BaaS offer | ë-C3X EXTENDED BaaS price starts ₹6.99 lakh + battery EMI ₹2.26/km (2026-09-07 OEM release); this is not a conventional ex-showroom vehicle price |
| AircrossX | Petrol SUV/MPV-style 5/7-seat product; YOU Turbo and MAX NA editions; petrol/CNG MAX NA availability | YOU Turbo Comfort Edition ₹10.69 lakh; MAX NA ₹11.62 lakh (introductory ex-showroom, 2026-09-07) |
| BasaltX | Petrol coupe-SUV; YOU Turbo and MAX NA editions; petrol/CNG MAX NA availability | YOU Turbo ₹9.99 lakh; MAX NA ₹11.34 lakh (introductory ex-showroom, 2026-09-07) |
| C5 Aircross | Diesel premium SUV; official homepage lists product page | Homepage price/trim/orderability not captured in this pass; third-party ₹37.32 lakh figure is discovery only |

## Dated OEM evidence captured

### AircrossX, BasaltX and ë-C3X EXTENDED — 2026-09-07

Official Citroën India / Stellantis Media press release dated 2026-09-07 announces new AircrossX and BasaltX variants and an enhanced-range ë-C3X:
- AircrossX YOU Turbo Comfort Edition: ₹10.69 lakh.
- AircrossX MAX NA: ₹11.62 lakh.
- BasaltX YOU Turbo: ₹9.99 lakh.
- BasaltX MAX NA: ₹11.34 lakh.
- ë-C3X EXTENDED: BaaS price starts ₹6.99 lakh + battery EMI ₹2.26/km.
- ë-C3X EXTENDED certified range: 330 km (MIDC-I/II).
- New editions available nationwide from 2026-09-07.
- MAX NA variants are available in petrol and CNG.
- The release describes the amounts as introductory ex-showroom prices, except the EV BaaS amount which is explicitly separated into upfront vehicle price and battery EMI per km.

Official source:
https://www.media.stellantis.com/in-en/citroen/press/citroen-india-expands-customer-choices-with-new-aircrossx-basaltx-variants-and-e-c3x-extended

### Additional 2026 official product updates

Citroën's official news page lists:
- 2026-07-21: Basalt X Comfort Edition.
- 2026-06-23: Aircross Comfort Edition limited run.
- 2026-06-17: all-new ë-C3X with BaaS.
- 2026-01-23: bookings-led portfolio update, including Aircross X Max Turbo (5-seater) and C3 Live (O).

These releases are variant discovery and lifecycle evidence. Do not assume all historic editions remain orderable solely because their press releases remain indexed.

## Price evidence and import boundary

- Four exact introductory ex-showroom price observations were captured from the 2026-09-07 OEM release: two AircrossX and two BasaltX editions.
- The ë-C3X EXTENDED BaaS price must be stored as a distinct pricing model: upfront vehicle amount plus battery EMI per kilometre. Do not store ₹6.99 lakh as a full ex-showroom vehicle price.
- The homepage does not expose a complete variant-level price matrix for C3X or C5 Aircross in the captured content.
- Third-party November 2026 model price ranges are discovery-only; they may use legacy model labels (C3, Aircross, Basalt) and may not reflect OEM X edition naming.
- No city-wise on-road prices captured.
- Preserve the "introductory" price qualifier and source date; do not assume those prices remain effective indefinitely.
- No Firestore import or publication performed.

## Current / lifecycle boundary

- Current OEM homepage entries: AircrossX, ë-C3X, C5 Aircross, C3X, BasaltX.
- AircrossX/BasaltX September 2026 editions and ë-C3X EXTENDED have explicit nationwide availability from 2026-09-07.
- C5 Aircross appears on the current homepage, but exact current booking and price evidence still needs confirmation.
- Older pre-X C3, Aircross and Basalt variants should not be merged into the new X-branded model-year catalogue without explicit OEM lineage confirmation.
- Keep concept or global Citroën EV products out of the India current catalogue unless Citroën India publishes local launch/booking and price evidence.

## Source register

Official:
- https://www.citroen.in/ — current OEM homepage and five product entries.
- https://www.citroen.in/about-citroen/news.html — dated 2026 product and variant updates.
- https://www.media.stellantis.com/in-en/citroen/press/citroen-india-expands-customer-choices-with-new-aircrossx-basaltx-variants-and-e-c3x-extended — exact edition prices, BaaS details, range and availability date, 2026-09-07.

Discovery only:
- https://www.cardekho.com/cars/Citroen — November 2026 model and price discovery; legacy naming may differ from OEM X branding.
- https://www.autocarindia.com/cars/citroen-suv-cars — model/variant cross-check only, not price authority.

This is a source-audit workpaper, not an approved import manifest. Exact OEM observations still require source-reuse/licensing review before production import.
