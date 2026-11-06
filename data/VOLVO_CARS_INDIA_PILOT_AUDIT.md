# Volvo Cars India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Current model discovery and OEM price observations; variant ingestion held pending complete current price sheet

## Executive result

The current Volvo Cars India site promotes the **XC90**, **XC60**, **EC40**, **EX30** and **EX90**. The official family-car page gives starting prices for XC90, XC60, EX30 and EC40; it shows EX90 as an electric SUV without a price in the captured page. The India homepage also promotes the all-electric EX90.

The official homepage/family page are the primary current-market sources. Third-party pages list more models, but older EX40/XC40 and S90 entries must not be assumed current merely because they remain indexed.

## Current India candidate inventory

| Canonical model | Powertrain/body | Official India evidence | Disposition |
|---|---|---|---|
| EX30 | Fully electric SUV | Official family page; starting price ₹41,00,000 | Current candidate |
| EC40 | Fully electric crossover | Official homepage and family page; starting price ₹59,00,000 | Current candidate |
| EX90 | Fully electric SUV | Official homepage and family page | Current candidate; official price not captured |
| XC60 | Mild-hybrid SUV | Official homepage and family page; starting price ₹70,90,000 | Current candidate |
| XC90 | Mild-hybrid SUV | Official homepage and family page; starting price ₹98,80,000 | Current candidate |

## Official starting-price observations

All values below are OEM page-level starting-price observations, not a complete variant matrix.

| Model | Amount (INR) | Price level | Observation date | Effective date |
|---|---:|---|---|---|
| EX30 | 4,100,000 | Model-level “Purchase from” | 2026-11-06 | Not stated |
| EC40 | 5,900,000 | Model-level “Purchase from” | 2026-11-06 | Not stated |
| XC60 | 7,090,000 | Model-level “Purchase from” | 2026-11-06 | Not stated |
| XC90 | 9,880,000 | Model-level “Purchase from” | 2026-11-06 | Not stated |
| EX90 | — | Price not displayed in captured official family page | 2026-11-06 | — |

Do not convert these model-level observations into exact trim prices. No city-wise on-road prices were captured.

## Historical price-list evidence — do not treat as current

An official Volvo Cars India PDF titled “VOLVO CAR INDIA PRICE LIST” contains:
- XC60 B5 Mild Hybrid (MY’26): ₹68,10,000
- XC90 B5 Mild Hybrid (MY’26): ₹96,97,240
- EX30 Ultra (MY’26): ₹41,00,000
- EC40 E80 Ultra (MY’25): ₹59,00,000
- EX40 E60 Ultra (MY’25): ₹50,10,000
- XC40 Recharge E60 Plus (MY’24): ₹49,00,000

The PDF is an older price-list snapshot and must not overwrite the newer official family-page prices. It is useful for historical model-year/grade evidence only. The PDF explicitly says the price prevailing at invoicing applies, excludes road tax, RTO statutory taxes/fees, other local taxes/cess and insurance, and that prices/options may change without notice.

## Lifecycle and naming controls

- **EX40:** Secondary reporting in June 2026 says EX40 was discontinued/removed from the official India website, with an updated version potentially planned. Current official homepage/family-page evidence captured for this audit does not list EX40. Hold as discontinued/not currently listed until a fresh official India launch/configurator record confirms return.
- **XC40 / XC40 Recharge:** Do not create as current products from old price-list or dealer microsite references.
- **S90:** Do not include in current inventory. Secondary current-lineup reporting says the S90 was discontinued in India in June 2025; current official homepage/family page does not list it.
- **ES90:** Treat as upcoming/announced only, not current, unless official India orderability is confirmed.
- **EX60:** Treat as future product only; no current India retail evidence captured.
- Keep electric and mild-hybrid powertrains explicit; do not flatten them into generic “petrol” or “hybrid” without OEM grade-level proof.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Volvo Cars India homepage | https://www.volvocars.com/in/ | Current product promotion and model presence | High |
| Volvo Cars India family cars | https://www.volvocars.com/in/cars/family-cars/ | Current model list, powertrain descriptions and displayed starting prices | High for displayed values |
| Official Volvo India pricing PDF | https://www.volvocarindia.com/data/Volvo-Pricing-Sheet.pdf | Historical MY'24–MY'26 grade/price observations and price exclusions | High for the PDF snapshot; not current price authority |
| Autocar India Volvo listing | https://www.autocarindia.com/cars/volvo | Secondary cross-check for current/upcoming/discontinued context | Medium; not price authority |
| Autocar India price-hike report (16 Apr 2026) | https://www.autocarindia.com/car-news-amp/volvo-india-announces-price-hike-for-all-models-439487 | Dated announcement of up-to-₹1 lakh increase effective 2026-05-01 | Medium; exact model-wise increases not stated |
| CarWale EX40 report (02 Jun 2026) | https://www.carwale.com/news/volvo-ex40-discontinued-in-india-2-new-cars-to-launch-in-2026/ | EX40 lifecycle cross-check | Medium; official confirmation still required |

## Staging decision

**Do not import as a production variant catalogue yet.**

Safe workpaper records:
1. Five current model candidates from the official India pages.
2. Four OEM model-level starting-price observations.
3. Historical price-list rows with their original model-year labels and explicit historical status.
4. EX40/XC40/S90/ES90 lifecycle review queue.

Required before variant ingestion:
1. Current India configurator or dated official price list with exact grade names and variant-level prices.
2. Engine/motor, fuel/powertrain, transmission, drivetrain and model-year mapping.
3. Effective dates and price-type/exclusion terms for each price.
4. City-wise on-road observations from permitted/reusable sources.
5. Confirmation of EX90 exact India grade and official price.

No Firestore import, provider API credit usage, or publication was performed.
