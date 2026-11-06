# Land Rover India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Model discovery complete; variant and price ingestion held pending OEM evidence  
**Primary source:** Land Rover India official website

## Executive result

The official India site organizes the portfolio into three families: **Range Rover, Defender and Discovery**. The official navigation also exposes **SV** as a portfolio/grade destination, not as a separate vehicle family. Do not count Range Rover Sport, Velar, Evoque, Defender 90/110/130, or Discovery Sport as unrelated brands.

The official India homepage does not provide a complete, dated, downloadable variant price list in the captured source. One exact official starting-price observation was captured for Discovery Sport: **₹63,37,000**. It is a model-level starting price, not a variant price or on-road quote.

## Official model and family inventory

| Canonical family | India-market product candidate | Evidence / disposition |
|---|---|---|
| Defender | Defender 90 | Official configurator family/body-style choice; verify current India orderability and grades |
| Defender | Defender 110 | Official configurator family/body-style choice; verify current India orderability and grades |
| Defender | Defender 130 | Official configurator family/body-style choice; verify current India orderability and grades |
| Defender | Defender OCTA | Official configurator lists OCTA; verify India-specific price and current availability |
| Range Rover | Range Rover | Official India family and configurator |
| Range Rover | Range Rover Sport | Official India family and configurator |
| Range Rover | Range Rover Velar | Official India family and configurator |
| Range Rover | Range Rover Evoque | Official India family and configurator |
| Discovery | Discovery | Official India family; seven-seat positioning |
| Discovery | Discovery Sport | Official India family; official starting price ₹63,37,000 |

**Important:** The configurator landing page is a builder entry point and not conclusive proof that every displayed body style or edition is currently orderable in India. Individual product pages, India-specific configurator selection and retailer confirmation are required before marking a variant current.

## Official evidence captured

### Discovery family

Official Discovery India page identifies Discovery as a seven-seat SUV and displays Discovery Sport with **“Price from ₹6,337,000”**.

- Price type: model-level starting price, interpreted as ex-showroom only after confirming OEM price disclaimer for the applicable product.
- Amount: INR 6,337,000.
- Observation date: 2026-11-06.
- Effective date: not stated in captured evidence.
- Variant mapping: not stated; do not assign to a specific trim.

### Configurator inventory

The official India Build Your Own page exposes these configurable product families/entries:
- Range Rover
- Range Rover Sport
- Range Rover Velar
- Range Rover Evoque
- Defender OCTA
- Defender 130
- Defender 110
- Defender 90
- Discovery
- Discovery Sport

The configurator supports choosing a model and then exploring equipment, colours and technology. It is not a published price matrix.

## Third-party price discovery — not approved for ingestion

Third-party portals crawled on 2026-11-06 list seven India models and indicative price bands:
- Defender: ₹99.00 lakh–₹2.62 crore
- Range Rover: ₹2.40–₹4.90 crore
- Range Rover Velar: ₹88.50 lakh (some portals report a different range)
- Range Rover Sport: ₹1.43–₹2.35 crore
- Range Rover Evoque: approximately ₹64.86–₹64.90 lakh
- Discovery: approximately ₹1.25–₹1.39 crore
- Discovery Sport: ₹63.37 lakh

These are discovery-only observations. Different portals disagree (for example Velar and Discovery upper prices), and some values may aggregate old/new model years, engine types, limited editions or retailer offers. They must not be written to Firestore or represented as verified OEM variant prices.

## Lifecycle and classification cautions

- Range Rover Electric and Range Rover Sport Electric are presented in JLR media materials as current global product programmes, but the evidence captured here does not establish India retail orderability. Keep them in an **announced / India availability unverified** queue, not the current India retail catalogue.
- Defender 90/110/130 are body-style variants within Defender, not separate brand/model families.
- Defender OCTA is a distinct high-performance derivative/grade under Defender; model-family relationship should be retained.
- SV is a performance/luxury sub-brand or grade destination; do not create a standalone passenger-vehicle model called “SV”.
- Historical model-year listings on third-party sites are not sufficient evidence of current orderability.
- Do not import expected prices, launch estimates, or upcoming electric-product prices.

## Price evidence register

| Product | Amount | Price level | Source | Effective date | Import status |
|---|---:|---|---|---|---|
| Discovery Sport | ₹63,37,000 | Model-level starting price | Official Land Rover India Discovery page | Not stated | Hold pending price terms and variant mapping |

No city-wise on-road observations were captured.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Land Rover India homepage | https://www.landrover.in/ | Official portfolio navigation and India market context | High |
| Land Rover India Discovery page | https://www.landrover.in/discovery/index.html | Discovery family positioning and Discovery Sport starting price | High for displayed page value |
| Land Rover India Build Your Own | https://www.landrover.in/build-your-own/index.html | Configurator model/body-style discovery | High for configurator presence; not full price evidence |
| JLR Range Rover media newsroom | https://media.jlr.com/range-rover/en-in/mobile-vehicle-menu | Global current/past/EV programme classification | High for global newsroom classification; not India retail availability |
| ZigWheels India Land Rover listing | https://www.zigwheels.com/land-rover-cars/ | Secondary model/price discovery only | Medium; not accepted as price authority |
| CarDekho India Land Rover listing | https://www.cardekho.com/cars/Land_Rover | Secondary model/price and discontinued-model cross-check | Medium; not accepted as price authority |
| Autocar India Land Rover listing | https://www.autocarindia.com/cars/land-rover | Secondary model/variant discovery | Medium; not accepted as price authority |
| CarWale India Land Rover listing | https://www.carwale.com/land-rover-cars/ | Secondary price/news discovery | Medium; not accepted as price authority |

## Staging decision

**Do not import this audit as a production variant catalogue.**

Safe to retain as workpaper evidence:
1. Official family and configurator product discovery.
2. One official model-level starting-price observation for Discovery Sport.
3. Third-party price discrepancies as a research queue only.
4. India availability uncertainty for global EV products.

Still required before staging:
1. Individual India product page and current brochure review for each model.
2. Exact India variant/grade names and engine/fuel/transmission mapping.
3. OEM variant-level price evidence with effective dates.
4. Clarification of whether each displayed amount is ex-showroom and what it excludes.
5. City-wise on-road observations from licensed/reusable sources.
6. Current orderability confirmation for each model/grade.

No Firestore import, provider API credit usage, or publication was performed.
