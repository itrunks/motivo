# Nissan India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.nissan.in/

## Official current catalogue snapshot

Nissan India's official homepage and "Discover the Nissan Range" currently promote three product families:
- All-New Nissan Tekton
- All-New Nissan Gravite
- New Nissan Magnite

The official homepage displays model-level starting prices:
- Tekton: ₹10,49,000
- Gravite: ₹5,73,400
- Magnite: ₹5,69,400

The official homepage also promotes the Gravite CNG retrofitment kit. Treat this as an accessory/retrofit price component, not a separate factory-built model or trim unless the OEM's documentation explicitly defines it as such.

X-Trail is present in some third-party catalogue pages but is not displayed in the current official Nissan India product range or official price-list page captured in this audit. Do not include it as current orderable without fresh OEM confirmation.

## Exact official price-list observations captured

The official price page https://www.nissan.in/prices-list.html exposes trim-level ex-showroom prices. Capture the observation date and source URL with every row. Prices below are INR and are official listed ex-showroom values, not on-road values.

### Tekton — manual transmission

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| NISSAN TEKTON VISIA T160 MT | 10,49,000 |
| NISSAN TEKTON VISIA+ T160 MT | 11,14,000 |
| NISSAN TEKTON ACENTA T160 MT | 11,79,000 |
| NISSAN TEKTON N-CONNECTA T160 MT | 13,69,000 |
| NISSAN TEKTON N-CONNECTA T280 MT | 14,99,000 |
| NISSAN TEKTON TEKNA T160 MT | 15,39,000 |
| NISSAN TEKTON TEKNA T280 MT | 16,39,000 |
| NISSAN TEKTON TEKNA+ T160 MT | 16,49,000 |

### Tekton — dual-clutch transmission

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| NISSAN TEKTON ACENTA T280 DCT | 14,99,000 |
| NISSAN TEKTON N-CONNECTA T280 DCT | 16,49,000 |
| NISSAN TEKTON TEKNA T280 DCT | 17,79,000 |
| NISSAN TEKTON TEKNA+ T280 DCT | 18,59,000 |

### Gravite — manual transmission

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| Nissan Gravite Visia MT | 5,73,400 |
| Nissan Gravite Acenta MT | 6,68,400 |
| Nissan Gravite N-Connecta MT | 7,38,400 |
| Nissan Gravite Tekna MT | 8,08,000 |
| Nissan Gravite Tekna Launch Edition MT | 8,52,500 |

### Gravite — automated manual transmission

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| Nissan Gravite N-Connecta EZ Shift | 7,95,000 |
| Nissan Gravite Tekna EZ Shift | 8,64,000 |
| Nissan Gravite Tekna Launch Edition EZ Shift | 9,08,500 |

### Magnite — manual transmission

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| Nissan Magnite MT VISIA | 5,69,400 |
| Nissan Magnite MT VISIA+ | 6,26,000 |
| Nissan Magnite MT ACENTA | 6,87,000 |
| Nissan Magnite MT N-CONNECTA | 7,50,000 |
| Nissan Magnite MT TEKNA | 8,43,000 |
| Nissan Magnite MT TEKNA+ | 8,76,000 |
| Nissan Magnite TURBO MT N-CONNECTA | 8,81,000 |
| Nissan Magnite TURBO MT TEKNA | 9,61,000 |
| Nissan Magnite TURBO MT TEKNA+ | 9,95,000 |

### Magnite — EZ-Shift AMT

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| Nissan Magnite EZ-SHIFT VISIA | 6,30,000 |
| Nissan Magnite EZ-SHIFT ACENTA | 7,42,000 |
| Nissan Magnite EZ-SHIFT N-CONNECTA | 8,05,000 |
| Nissan Magnite EZ-SHIFT TEKNA | 8,98,000 |
| Nissan Magnite EZ-SHIFT TEKNA+ | 9,31,000 |

### Magnite — Turbo X-TRONIC CVT

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| Nissan Magnite Turbo X-TRONIC CVT ACENTA | 9,30,000 |
| Nissan Magnite Turbo X-TRONIC CVT N-CONNECTA | 9,74,000 |
| Nissan Magnite Turbo X-TRONIC CVT TEKNA | 10,69,000 |
| Nissan Magnite Turbo X-TRONIC CVT TEKNA+ | 10,99,000 |

### Magnite Kuro special edition

| Official variant name | Ex-showroom price (INR) |
|---|---:|
| NEW NISSAN MAGNITE MT Kuro Edition | 7,85,000 |
| NEW NISSAN MAGNITE EZ-SHIFT Kuro Edition | 8,40,000 |
| NEW NISSAN MAGNITE Turbo MT Kuro Edition | 9,16,000 |
| NEW NISSAN MAGNITE Turbo CVT Kuro Edition | 9,99,400 |

The official price-list page also presents separate Gravite CNG retrofitment line items (kit, cylinder/installation/gas, RTO endorsement, insurance endorsement and third-party warranty). These are not vehicle variant prices. Preserve them as accessory/fitment charges if the product schema supports them; otherwise exclude from variant price records. The price page's CNG table has a historic introductory-offer column and a post-30-06-2026 amount; use the latter only with the relevant date/context.

## Model and powertrain classification

| Model | Current official status | Powertrain / body type | Notes |
|---|---|---|---|
| Tekton | Official homepage promoted; official variant-price list present | Petrol SUV; T160/T280 engine codes; MT/DCT | Exact official variant names and prices captured above |
| Gravite | Official homepage promoted; official variant-price list present | Petrol 7-seat MPV; MT/EZ Shift; CNG retrofitment offer | Exact official variant names and prices captured above |
| Magnite | Official homepage promoted; official variant-price list present | Petrol NA/turbo; MT/AMT/CVT | Exact official variant names and prices captured above |
| X-Trail | Not on current official range/price page in this pass | Third-party listing only | Hold outside current catalogue pending OEM confirmation |

## Price evidence, date and caveats

- Official price page labels listed amounts "Ex-Showroom Price (INR)".
- The price page does not provide a clear per-row effective date in the captured table. Record the audit observation date as 2026-11-06 and set effective date to unknown/null until a dated OEM notice or price sheet confirms it.
- Preserve exact official variant strings, including T160/T280, EZ Shift, DCT, X-TRONIC CVT and Kuro Edition.
- Do not infer that every special edition is currently orderable solely because it remains on the price-list page; cross-check configurator and dealer booking status.
- Do not convert CNG retrofitment charges into a factory CNG variant price.
- No city-wise on-road prices captured.
- No Firestore import or publication performed.

## Source register

Official:
- https://www.nissan.in/ — current official product range and homepage price claims.
- https://www.nissan.in/prices-list.html — exact trim-level ex-showroom prices for Tekton, Gravite and Magnite.
- https://www.nissan.in/latest-news/nissan-on-track-for-2026-resurgence-in-india.html — official product-roadmap background.

Discovery only:
- https://www.cardekho.com/cars/Nissan — November 2026 model and variant discovery; X-Trail presence not accepted as OEM current status.
- https://www.autocarindia.com/cars/nissan — cross-check of current retail range; not used as price authority.
- https://www.zigwheels.com/nissan-cars/ — November 2026 model-level discovery.

This is a source-audit workpaper, not an approved import manifest. Price rows are audit observations and still require source-reuse/licensing review before production import.
