# Jaguar India — current model and price audit

**Audit date:** 2026-11-06  
**Market:** India  
**Status:** Research workpaper only — not approved for catalogue import or publication  
**Repository:** `feature/catalogue-source-audit-ingestion`

## Executive outcome

Jaguar's India retail position is in transition. The official Jaguar India range and offers pages still present **F-PACE** and provide retailer / build / price links. However, Autocar India's F-PACE model page records it as discontinued in October 2026, and its brand overview says there are no Jaguar models currently on sale while the brand prepares its all-electric relaunch.

Therefore:
- Do **not** treat F-PACE as an unqualified current retail model. Record it as **recently discontinued / dealer-stock verification required**.
- The last recorded F-PACE ex-showroom price is ₹72.90 lakh for both R-Dynamic S petrol and diesel variants.
- The F-PACE production end was reported in December 2025; the India discontinuation was recorded in October 2026. These are separate lifecycle dates.
- The future **Type 01** is a global electric four-door GT, with India launch reported for mid-2027 by secondary catalogue sources. India price is only an estimate, not an official announced price. Keep it on the future-product watchlist.
- Previous India models XE, XF, E-PACE, I-PACE and F-TYPE are discontinued; do not include them as current new-car models.

## India model candidates and lifecycle status

| Canonical model | Derivative / powertrain | India status | Price observation | Catalogue decision |
|---|---|---|---|---|
| F-PACE | R-Dynamic S 2.0L petrol, 8-speed automatic, AWD | Discontinued in India per Autocar October 2026; dealer stock may remain | ₹72.90 lakh last recorded ex-showroom | Move to discontinued / stock-only; not current catalogue |
| F-PACE | R-Dynamic S 2.0L mild-hybrid diesel, 8-speed automatic, AWD | Discontinued in India per Autocar October 2026; dealer stock may remain | ₹72.90 lakh last recorded ex-showroom | Move to discontinued / stock-only; not current catalogue |
| Type 01 | All-electric four-door GT | Future India launch expected mid-2027 in secondary reporting; no official India launch date or price | ₹2.00–3.00 Cr estimated by secondary sites | Watchlist only; do not import as current |

## Price evidence register

| Model / derivative | Amount | Price basis / class | Observation date | Source confidence | Notes |
|---|---:|---|---|---|---|
| F-PACE R-Dynamic S Petrol | ₹72,90,000 | Last recorded ex-showroom | 2026-11-06 | Autocar India secondary listing | Not proof of current factory orderability |
| F-PACE R-Dynamic S Diesel | ₹72,90,000 | Last recorded ex-showroom | 2026-11-06 | Autocar India secondary listing | Not proof of current factory orderability |
| Type 01 | ₹2,00,00,000–₹3,00,00,000 | Estimated upcoming price | 2026-11-06 | Secondary estimate only | No official India price; no production India order guide |

Do not treat dealer-stock F-PACE vehicles as factory-current catalogue models. If the app later supports used / dealer-stock inventory, create a separate inventory record with build year, VIN-specific stock, retailer, location, quote date and warranty status. Do not merge stock price with current model MSRP.

No city-wise on-road price observations are accepted. A third-party page shows a Navsari on-road estimate, but this is not a dated itemised dealer quotation and is not approved for ingestion.

## Official India website evidence vs current orderability

- Official Jaguar India range page lists F-PACE, describes petrol/diesel AWD and links to build, price, retailer and test-drive journeys.
- Official Jaguar India retail-offers page still promotes F-PACE offers.
- The official site includes a semiconductor availability disclaimer and directs customers to authorised retailers for local availability and price.
- This website presence is not enough to override the explicit October 2026 discontinued status recorded by Autocar's F-PACE page. Treat this as a stale / transitional site state until Jaguar India supplies a current order guide.
- Autocar India's Jaguar overview says the brand currently has no models officially on sale as it transitions to an all-electric product line. Its F-PACE page separately records discontinued in October 2026.

## Future-product watchlist — Type 01

- Jaguar's new electric four-door GT concept / production direction is associated with the Type 00 design study and the future production Type 01 naming in recent reporting.
- Autocar India and CarDekho list Type 01 as expected in India around mid-2027, with estimates ranging from ₹2.00 Cr to ₹3.00 Cr.
- These are secondary expected-launch and price estimates only. No official India launch date, India variant, battery specification, homologation, booking date or retail price is accepted in this audit.
- Do not use concept-car images or specifications as production Type 01 data.
- Keep the global brand relaunch separate from India retail availability.

## Discontinued India model families

The following were previously sold in India but are not current new-car catalogue candidates:
- XE
- XF
- E-PACE
- I-PACE
- F-TYPE
- Earlier F-PACE model years and SVR special editions

A pre-owned listing or residual dealer inventory is not evidence of current new-car orderability.

## Source register

1. Jaguar official India model range: https://www.jaguar.com/en-in/jdx/jaguar-range/index.html  
   Primary source for current India site model navigation, F-PACE powertrain/body and retailer/build links. The site contains an availability disclaimer; it does not conclusively establish current orderability.
2. Jaguar official India retail offers: https://www.jaguar.com/en-in/jdx/offers-and-finance/retail-offers/index.html  
   Primary source for F-PACE retail-offer promotion and retailer contact path; may be stale during transition.
3. Autocar India, Jaguar India brand and price overview (crawled 6 Nov 2026): https://www.autocarindia.com/cars/jaguar  
   Secondary source says no models currently on sale, identifies F-PACE as discontinued, and lists Type 01 as upcoming around mid-2027.
4. Autocar India, Jaguar F-PACE model page (updated 21 Sep 2026; status subsequently marked discontinued Oct 2026): https://www.autocarindia.com/cars/jaguar/f-pace  
   Secondary evidence for ₹72.90 lakh last recorded price, two R-Dynamic S powertrain variants, specs and discontinued status.
5. CarDekho, Jaguar India price list (Nov 2026): https://www.cardekho.com/cars/Jaguar  
   Secondary cross-check for one model / F-PACE at ₹72.90 lakh, Type 01 expected May 2027, and discontinued previous model list.
6. Autocar India, F-PACE production ends after 10 years (22 Dec 2025): https://www.autocarindia.com/car-news/jaguar-f-pace-production-ends-after-10-years-438864  
   Lifecycle evidence for global F-PACE production end; distinct from India discontinuation date.
7. Jaguar official India homepage / new era: https://www.jaguar.com/en-in/  
   Primary source for brand relaunch context; no India retail price for Type 01 accepted.

## Import gate / unresolved items

- Obtain a dated written statement or current price/order guide from Jaguar Land Rover India confirming whether any new F-PACE factory orders are still accepted or only dealer stock remains.
- If F-PACE is dealer stock only, keep it out of current model catalogue; optionally support a separate retailer-stock dataset with exact vehicle identity.
- Confirm final F-PACE sales / discontinuation effective date and whether remaining dealer units carry 2025/2026 build years.
- Confirm production Type 01 official name, India launch date, homologation, specifications and price before catalogue inclusion.
- Do not infer Type 01 price from secondary estimates or Type 00 concept data.
- Review source licensing and reuse rights before public catalogue ingestion.

**Disposition:** No confirmed current Jaguar new-car model can be safely marked orderable from the evidence captured. F-PACE is discontinued / stock-only pending OEM clarification; Type 01 remains future watchlist. No Firestore import or publication is authorised by this audit.
