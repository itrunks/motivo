# Aston Martin India — current model and price audit

**Audit date:** 2026-11-06  
**Market:** India  
**Status:** Research workpaper only — not approved for catalogue import or publication  
**Repository:** `feature/catalogue-source-audit-ingestion`

## Executive outcome

Aston Martin's India retail range is represented by four current model families: **Vantage, DB12, DBX and Vanquish**. In August 2026, Aston Martin announced revised India prices after implementation of the India–UK Free Trade Agreement (FTA). A 3 November 2026 report re-confirms the seven derivative prices.

The latest reported revised prices are:
- Vantage S: ₹3.15 Cr; Vantage S Roadster: ₹3.35 Cr
- DB12 S: ₹4.10 Cr; DB12 S Volante: ₹4.35 Cr
- DBX S: ₹4.15 Cr
- Vanquish: ₹6.40 Cr; Vanquish Volante: ₹6.90 Cr

**Important identity / data-quality issue:** The official Aston Martin global model site presents broader current families and derivative labels, including Vantage / Vantage S, DB12 / DB12 S, DBX GT / DBX S / DBX707, Vanquish and special editions. India price reporting is specifically for Vantage S, DB12 S and DBX S, not necessarily the base derivatives. Do not collapse all trims under the family starting price or treat all global derivatives as India-orderable.

Autocar India’s India catalogue page continues to show legacy price values (Vantage ₹4.25 Cr, DB12 ₹5.15 Cr, DBX ₹5.89 Cr, Vanquish ₹8.85 Cr), conflicting with the post-FTA revised prices. Retain as separate source observations and prefer the dated revised-price reporting for the named S/Volante derivatives, pending written dealer confirmation.

## Current India model candidates

| Canonical family / derivative | Body / powertrain | India status | Latest reported ex-showroom price | Catalogue decision |
|---|---|---|---:|---|
| Vantage S | Coupe; 4.0L twin-turbo V8 petrol | India range; revised post-FTA price reported | ₹3.15 Cr | Include derivative; confirm dealer quote |
| Vantage S Roadster | Convertible; 4.0L twin-turbo V8 petrol | India range; revised post-FTA price reported | ₹3.35 Cr | Include separately from Coupe |
| DB12 S | Super Tourer coupe; 4.0L twin-turbo V8 petrol | India range; revised post-FTA price reported | ₹4.10 Cr | Include derivative; confirm dealer quote |
| DB12 S Volante | Convertible; 4.0L twin-turbo V8 petrol | India range; revised post-FTA price reported | ₹4.35 Cr | Include separately from Coupe |
| DBX S | Performance SUV; 4.0L twin-turbo V8 petrol | India range; revised post-FTA price reported | ₹4.15 Cr | Include derivative; confirm dealer quote |
| Vanquish | Coupe; 5.2L twin-turbo V12 petrol | India range; revised post-FTA price reported | ₹6.40 Cr | Include; confirm dealer quote |
| Vanquish Volante | Convertible; 5.2L twin-turbo V12 petrol | India range; revised post-FTA price reported | ₹6.90 Cr | Include separately from Coupe |

**Family-vs-derivative note:** The current India press coverage labels the range as Vantage S, DB12 S, DBX S and Vanquish. The official global page separately lists base Vantage, DB12 and DBX GT/DBX707 derivatives. For the India catalogue, create a family only where schema supports it; do not invent a base trim from a global configurator page.

## Price evidence register

| Derivative | Revised amount | Previous amount | Price basis | Source / observation date | Confidence |
|---|---:|---:|---|---|---|
| Vantage S | ₹3,15,00,000 | ₹4,99,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting of announced price revision |
| Vantage S Roadster | ₹3,35,00,000 | ₹5,26,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |
| DB12 S | ₹4,10,00,000 | ₹6,62,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |
| DB12 S Volante | ₹4,35,00,000 | ₹7,00,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |
| DBX S | ₹4,15,00,000 | ₹6,80,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |
| Vanquish | ₹6,40,00,000 | ₹10,11,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |
| Vanquish Volante | ₹6,90,00,000 | ₹10,92,00,000 | Ex-showroom | Autocar India, 2026-08-01; corroborated HT Auto, 2026-11-03 | Secondary reporting |

No city-wise on-road price observations are accepted. Do not calculate or infer registration, insurance, TCS, handling, options or city-specific charges.

## Conflicting catalogue observations

Autocar India’s general Aston Martin catalogue page (last month snapshot) lists:
- Vantage ₹4.25 Cr
- DB12 ₹5.15 Cr
- DBX ₹5.89 Cr
- Vanquish ₹8.85 Cr

These values do not map cleanly to the named post-FTA derivatives. They may represent older base-model or stale aggregator data. Keep them as distinct source observations with the source's model labels; do not overwrite the dated derivative-specific revised prices or assume they refer to the same specification.

ZigWheels' November 5 2026 listing also shows four family labels with revised values, but its family names (DB12, DBX, Vantage, Vanquish) obscure the exact S / Volante derivative identity. Use only as secondary cross-check, not as canonical variant mapping.

## Global product context — not automatic India availability

Aston Martin's official global models page lists:
- **Valhalla:** mid-engine PHEV supercar; Coupe and Spider.
- **DBX:** DBX GT, DBX S and DBX707.
- **DB12:** DB12 S, DB12 S Volante, DB12, DB12 Volante and 60th Anniversary edition.
- **Vantage:** Vantage S, Vantage S Roadster, Vantage and Vantage Roadster.
- **Vanquish:** Vanquish Coupe and Vanquish Volante, plus anniversary editions.
- **Valkyrie:** Coupe, Spider and track-only AMR Pro / LM.
- **Valour / Valiant:** limited-production special models.

These are global model references only. India-specific orderability, allocation and pricing must be independently confirmed before import. In particular, do not add Valhalla, Valkyrie, Valour, Valiant, AMR26 or special editions to the current India catalogue based solely on global web presence.

## India market / dealer evidence

Autocar India describes Aston Martin's India retail footprint as limited, with an authorised dealer facility in New Delhi and historic presence in Mumbai. Dealer network data is not sufficient to infer stock, allocation or price. Obtain a current authorised-dealer confirmation for the exact model and city before creating inventory or on-road price records.

## Source register

1. Autocar India, “Aston Martin reveals post-India-UK FTA car prices” (1 Aug 2026): https://www.autocarindia.com/car-news-amp/aston-martin-reveals-post-india-uk-fta-car-prices-440362  
   Detailed derivative-level revised and previous ex-showroom prices for all seven India derivatives.
2. Hindustan Times Auto, “Aston Martin prices drop in India by up to ₹4 crore” (3 Nov 2026): https://auto.hindustantimes.com/auto/cars/aston-martin-prices-drop-in-india-by-up-to-rs-4-crore/amp-41793680191145.html  
   Recent corroboration of all seven revised India prices and previous values.
3. CarWale, “Aston Martin Prices Drop by Rs. 4 Crore Following India-UK FTA Implementation” (5 Aug 2026): https://www.carwale.com/news/aston-martin-cars-prices-drop-by-rs-4-crore-following-india-uk-fta-implementation/  
   Independent corroboration of derivative prices.
4. Aston Martin official global models page: https://www.astonmartin.com/en/models  
   Primary source for global model families, body styles and current derivative naming; not India orderability or pricing evidence.
5. Aston Martin official media current-models index: https://media.astonmartin.com/section/current-models/?lang=eng  
   Primary source for global current-model index (DB12, Vanquish, DBX, Vantage).
6. Autocar India, Aston Martin India model and price overview: https://www.autocarindia.com/cars/aston-martin  
   Secondary source for India family catalogue and conflicting legacy price observations; also identifies Delhi retail presence.
7. ZigWheels, Aston Martin India prices (last updated 5 Nov 2026): https://www.zigwheels.com/aston-martin-cars/  
   Secondary cross-check for four family labels and revised price ranges; derivative identity is less precise.

## Import gate / unresolved items

- Obtain a dated, written authorised-dealer/OEM price sheet for each of the seven derivatives, including model year, exact specification, price validity and orderability.
- Confirm whether the revised prices are effective for all new customer orders or depend on order date, import date, FTA origin qualification or allocation.
- Confirm whether base Vantage, base DB12, DB12 Volante, DBX GT and DBX707 are separately orderable in India; do not infer from global pages.
- Confirm current dealer network and aftersales service points.
- Capture city-specific on-road quotes only with city/RTO, quote date, insurance, TCS, registration, options and fees itemised.
- Review source licensing and permitted reuse before public catalogue ingestion.

**Disposition:** Seven India derivatives may be retained as research-only candidates with dated secondary price observations. Do not publish as OEM-verified until the dealer/OEM price sheet and current orderability are confirmed. No Firestore import or publication is authorised by this audit.
