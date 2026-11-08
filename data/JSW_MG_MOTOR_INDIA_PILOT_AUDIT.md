# JSW MG Motor India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.mgmotor.co.in/

## Official catalogue snapshot

JSW MG Motor India's official homepage currently promotes the following product families / offers:
- MG Hector
- MG Hector Tomahawk EV
- MG Hector Tomahawk PHEV
- MG Majestor
- MG Windsor EV
- MG Comet EV
- MG ZS EV
- MG Astor
- MG Cyberster
- MG M9

The official homepage also promotes MG Windsor EV PRO / INDULGE and lists brochure links for Hector, Comet EV, ZS EV and Astor. The MG SELECT channel separately handles premium products Cyberster and M9. Do not treat product banners, service-information links, and current retail orderability as interchangeable signals.

## Canonical model and product-family rules

- Hector Tomahawk EV and Hector Tomahawk PHEV are presented by MG as distinct electrified product offerings based on the Hector name. Keep each powertrain/product as its own model-family record until MG confirms whether these are production variants under a shared canonical Hector entity.
- Hector ICE remains a separate petrol/diesel family from the Tomahawk EV and PHEV products.
- Windsor EV and Windsor EV PRO are editions/range configurations within the Windsor EV family, not separate nameplates.
- Cyberster and M9 belong to MG SELECT premium retail channel; preserve the channel and special-edition context.
- Majestor is a distinct SUV nameplate; do not merge with Gloster.
- MG's homepage links Gloster in the service-information section, but does not promote it in the current sales lineup. Keep Gloster on hold as current orderable until an official current product/price/booking page is verified.
- Astor, ZS EV and Comet EV are still present in the homepage product/service/brochure ecosystem; confirm active configurator and dealer orderability before accepting current trim rows.

## Audit matrix

| Product family | Official evidence | Price / variant evidence |
|---|---|---|
| Hector | Homepage current product card; official all-new Hector release dated 2025-12-15; current homepage starts ₹12.14 lakh | Starting price only on homepage; official 2025 release says ₹11.99 lakh starting price at launch. Do not use launch price as current price |
| Hector Tomahawk EV | Homepage banner with "Book Now"; starts ₹13.99 lakh + ₹4.90/km | Official homepage price presentation is subscription/BaaS-style; preserve ₹/km separately from vehicle ex-showroom price |
| Hector Tomahawk PHEV | Homepage banner with "Book Now"; starts ₹21.79 lakh + ₹3.20/km | Same: preserve subscription/km component; no full trim price list captured |
| Majestor | Homepage product card and booking CTA; starts ₹43.49 lakh | Model starting-price observation only; exact grades/prices not captured |
| Windsor EV | Homepage current product card; range price starts ₹9.99 lakh + ₹4.3/km | Official range-price / BaaS claim; do not store as conventional ex-showroom price. Windsor EV PRO also promoted |
| Comet EV | Homepage current product card; starts ₹4.99 lakh + ₹3.3/km | Subscription/km component must be retained separately; exact trim prices not captured |
| ZS EV | Homepage product card; starts ₹13 lakh + ₹4.5/km | Price presentation appears to include a usage/km component; confirm plan and price basis before importing |
| Astor | Homepage product card; starts ₹9.65 lakh | Model starting-price observation only; exact current trim matrix not captured |
| Cyberster | Official MG SELECT newsroom; Couture Edition launched at ₹87.49 lakh, bookings open | Exact special-edition price observation from OEM release dated 2026-08-03; retain Couture Edition name and MG SELECT channel |
| M9 | Official MG SELECT newsroom; Couture Edition launched at ₹84.94 lakh, bookings open | Exact special-edition price observation from OEM release dated 2026-08-03; retain Couture Edition name and MG SELECT channel |
| Gloster | Service-information link present, but not in homepage current sales carousel | Hold pending current official price/configurator/booking evidence |

## Dated OEM evidence captured

### All-New Hector — 2025-12-15

Official release states the All-New Hector starts at ₹11.99 lakh ex-showroom at launch, with petrol variants first and diesel to be introduced later in 2026. This is a launch-time price, not the November 2026 current price. The homepage now shows a ₹12.14 lakh starting-price claim. Use the homepage observation for current starting-price tracking, but exact variant-level values require a current official price sheet.

Official source:
https://www.mgmotor.co.in/media-center/newsroom/jsw-mg-motor-india-launches-the-all-new-hector

### MG SELECT Couture Editions — 2026-08-03

Official newsroom release states:
- MG M9 Couture Edition: ₹84.94 lakh.
- MG Cyberster Couture Edition: ₹87.49 lakh.
- Bookings open; deliveries began August 10, 2026.

These are special-edition prices and must not overwrite the base M9/Cyberster variant price rows. Keep exact edition name, MG SELECT channel, announcement date and booking status in the source record.

Official source:
https://www.mgmotor.co.in/media-center/newsroom/mg-select-launches-the-couture-edition-of-m9-at-inr-84-94-lakh-and-cyberster-at-inr-87-49-lakh

## Price evidence and import boundary

- Homepage price claims include multiple ₹/km amounts alongside upfront starting amounts. These are not directly comparable with conventional ex-showroom prices; preserve pricing model, upfront amount, recurring/km charge and applicable terms separately.
- The official homepage's current Hector starting price is ₹12.14 lakh; its 2025 launch release's ₹11.99 lakh is historical launch context only.
- Exact official variant-level price matrices were not captured for the ICE/EV range in this pass.
- Exact OEM special-edition observations captured: M9 Couture Edition ₹84.94 lakh and Cyberster Couture Edition ₹87.49 lakh (2026-08-03).
- Third-party November 2026 model/variant ranges conflict with MG's current price presentation and product taxonomy. Use them only as discovery leads, never as the authoritative price ledger.
- A 2026-04-01 industry-reported MG price revision of up to 2% was reported for ICE/EV models, excluding MG SELECT Cyberster/M9. Do not apply a flat uplift to historical rows; obtain exact current OEM values per trim.
- No city-wise on-road prices captured.
- No Firestore import or publication performed.

## Current / orderability / discontinued boundary

- Official homepage promoted: Hector, Hector Tomahawk EV, Hector Tomahawk PHEV, Majestor, Windsor EV, Comet EV, ZS EV, Astor, Cyberster and M9.
- The homepage's "Book Now" labels for Tomahawk products are stronger order-intent evidence than a brochure link, but exact booking terms and delivery/retail status still need capture.
- Gloster appears in service information but not the homepage sales carousel; do not mark it current-orderable without stronger OEM evidence.
- Keep future global MG products such as IM5/IM6 out of the current India catalogue until MG India publishes local launch/booking and price details.
- MG SELECT is a distinct sales channel; preserve it in product and price provenance.

## Source register

Official:
- https://www.mgmotor.co.in/ — current homepage lineup, product banners and price presentations.
- https://cars.mgmotor.co.in/ — MG virtual showroom/configurator entry point; product selection includes Majestor, Hector, Hector Tomahawk PHEV, Astor, Windsor, Windsor Pro, Hector Tomahawk EV and Comet.
- https://www.mgmotor.co.in/media-center/newsroom/jsw-mg-motor-india-launches-the-all-new-hector — official Hector launch and historical launch-price evidence, 2025-12-15.
- https://www.mgmotor.co.in/media-center/newsroom/mg-select-launches-the-couture-edition-of-m9-at-inr-84-94-lakh-and-cyberster-at-inr-87-49-lakh — exact MG SELECT Couture Edition prices, 2026-08-03.
- https://www.mgmotor.co.in/brand/history — MG brand/product-history context.

Discovery only:
- https://www.cardekho.com/cars/MG — November 2026 model/variant price ranges; not accepted as official price authority.
- https://www.zigwheels.com/mg-motor-cars/ — November 2026 lineup and model-price discovery.
- https://www.autocarindia.com/cars/mg — current model/variant discovery and taxonomy cross-check.
- https://www.autocarindia.com/car-news/jsw-mg-motor-to-hike-car-prices-from-april-439321 — reports the April 1, 2026 up-to-2% price revision; do not use for exact current variant prices.

This is a source-audit workpaper, not an approved import manifest. Price observations still require source-reuse/licensing review before production import.
