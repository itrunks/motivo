# Kia India current passenger-car model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.kia.com/in/

## Official model catalogue audit

Kia India's official website exposes the India passenger-car model catalogue and model pages. Current catalogue candidates to validate include:
- Sonet
- Seltos
- Carens
- Carens Clavis
- Carens Clavis EV
- Syros
- Carnival
- EV6
- EV9

This is an audit queue, not a declaration that every model is currently orderable or that all variants are available in every city. Check current configurator status, official brochure model year and dealer orderability before variant import.

## Audit matrix

| Model | Product class / powertrain audit | Exact official variant-price cards |
|---|---|---|
| Sonet | ICE compact SUV; exact current fuel/gearbox combinations to verify from live configurator | Not captured |
| Seltos | ICE SUV; exact current fuel/gearbox combinations to verify | Not captured |
| Syros | ICE SUV; exact current fuel/gearbox combinations to verify | Not captured |
| Carens | ICE MPV; confirm whether legacy Carens remains orderable alongside Clavis | Not captured |
| Carens Clavis | ICE MPV; current variant matrix to verify | Not captured |
| Carens Clavis EV | Electric MPV; current variant/battery matrix to verify | Not captured |
| Carnival | Premium MPV; current model-year and orderability need confirmation | Not captured |
| EV6 | Electric; current facelift/model-year and orderability need confirmation | Not captured |
| EV9 | Electric; current India orderability and variant configuration need confirmation | Not captured |

## Price evidence and import boundary

- No exact current official variant price cards were captured in this pass.
- Do not use model starting prices as variant prices.
- Do not copy third-party variant tables into the official price ledger without matching them to a dated Kia India price list or dealer quote.
- Record ex-showroom price and city-wise on-road price as separate observations. On-road values must retain city, state/RTO, effective date, observation date and source.
- Preserve variant model-year applicability; do not merge discontinued Carens and current Carens Clavis trims.
- Source terms and commercial reuse permission require review.
- No Firestore import performed.

## Sources

Official:
- https://www.kia.com/in/
- https://www.kia.com/in/our-vehicles.html

Discovery only:
- https://www.autocarindia.com/cars/kia
- https://www.cardekho.com/cars/Kia

This is a source-audit workpaper, not an approved import manifest.


## Official catalogue recheck — 2026-11-06

The live Kia India homepage and its "Explore the Range" section were rechecked on 2026-11-06. The official site now explicitly exposes the following India product families:

- Sonet
- Syros
- All-new Seltos
- Sorento
- Carens
- Carens Clavis
- Carnival
- Syros EV
- Carens Clavis EV
- EV6
- EV9

This expands the initial queue: **Sorento** and **Syros EV** must be represented as distinct model families; Syros EV must not be folded into ICE Syros. The official homepage also promotes the 2026 Syros and all-new Seltos. The product listing page at https://www.kia.com/in/buy/kid.html repeats the same 11 names.

### What is actually price-verifiable from the official page

- The homepage advertises the all-new Seltos from **₹11,24,900**, with the site disclaimer stating ex-showroom price all India. This is a **model-level starting-price observation only**, not a variant row; it is not eligible for variant-price import.
- The official homepage does not expose a complete, machine-readable variant-price matrix in the captured page content.
- No exact official variant price card was accepted in this recheck.
- The homepage's presence of a model in the product range proves official catalogue promotion, but by itself does not prove local dealer stock, booking availability, or orderability in every city.

### Third-party discovery cross-check (not importable evidence)

A 2026-11-05 ZigWheels snapshot reports 11 Kia models and gives model-level ex-showroom ranges. Autocar India and CarDekho also list the newly promoted Sorento and Syros EV, but their current-sale/orderability descriptions are not fully consistent. These sources are discovery leads only and must not populate the official variant-price ledger. Kia announced a price increase of up to 2% effective 2026-07-01, with the actual change varying by model and variant; therefore older third-party variant prices must not be carried forward by applying a flat uplift.

### Revised audit matrix

| Officially promoted model | Classification | Current variant matrix / orderability |
|---|---|---|
| Sonet | ICE SUV | Exact current trims and orderability not verified |
| Syros | ICE SUV | Exact current trims and orderability not verified |
| All-new Seltos | ICE SUV; 2026 refresh promoted | Starting price ₹11,24,900 observed on Kia homepage; exact trim matrix not captured |
| Sorento | SUV; official India range promotion includes hybrid powertrain messaging | India variant matrix and orderability require direct confirmation |
| Carens | ICE MPV; CNG messaging also present on official homepage | Confirm current orderability separately from Clavis |
| Carens Clavis | ICE MPV; CNG messaging also present | Exact current trims and orderability not verified |
| Carnival | Premium MPV | Exact current model-year/trim orderability not verified |
| Syros EV | Electric SUV | Distinct from ICE Syros; exact variant/battery matrix not captured |
| Carens Clavis EV | Electric MPV | Exact variant/battery matrix not captured |
| EV6 | Electric crossover | Exact current model-year/trim orderability not verified |
| EV9 | Electric SUV | Exact current model-year/trim orderability not verified |

## Revised source register

Official source pages checked 2026-11-06:
- https://www.kia.com/in/home.html — official homepage, current promoted range, Seltos starting-price claim and ex-showroom disclaimer.
- https://www.kia.com/in/buy/kid.html — official product listing, 11 model names.
- https://www.kia.com/in/buy/download-brochure.html — official brochure index; use each model's current brochure to verify model-year, powertrain and trim nomenclature before importing.
- https://www.kia.com/in/our-vehicles.html — official vehicle catalogue entry point.

Third-party discovery only:
- https://www.zigwheels.com/kia-cars/ — 2026-11-05 model-level snapshot.
- https://www.autocarindia.com/cars/kia — model/variant discovery; not accepted as price authority.
- https://www.cardekho.com/cars/Kia — model/variant discovery; not accepted as price authority.
- https://www.autocarindia.com/car-news-amp/kia-to-hike-car-prices-by-up-to-2-per-cent-440006 — reports Kia's up-to-2% price revision effective 2026-07-01; model/variant changes vary.

No variant prices were imported and no Firestore write was performed.
