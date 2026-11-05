# Hyundai pilot source audit

Checked: 2026-11-06
Primary source: https://www.hyundai.com/in/en/find-a-car

The official catalogue currently exposes model-level ex-showroom price ranges, fuel type, transmission availability, seating capacity, and brochure/detail links. These are model ranges, not exact variant-level price records.

| Model | Ex-showroom range | Fuel | Transmission | Seats |
|---|---:|---|---|---:|
| Verna | ₹10.99–18.41 lakh | Petrol | Manual / DCT / IVT | 5 |
| Aura | ₹5.99–8.59 lakh | Petrol / CNG | Manual / AMT | 5 |
| Venue | ₹7.99–15.82 lakh | Petrol / Diesel | Manual / Automatic / DCT | 5 |
| BAYON | ₹9.99–18.14 lakh | Petrol | Manual / IVT | 5 |
| Venue N Line | ₹10.66–15.66 lakh | Petrol | Manual / DCT | 5 |
| Creta | ₹10.90–20.11 lakh | Petrol / Diesel | Manual / Automatic / IVT / DCT | 5 |
| Creta N Line | ₹19.03–20.09 lakh | Petrol | Manual / DCT | 5 |
| Exter | ₹5.80–9.41 lakh | Petrol / CNG | Manual / AMT | 5 |
| Alcazar | ₹14.50–21.24 lakh | Petrol / Diesel | Manual / Automatic / DCT | 6 / 7 |
| Grand i10 NIOS | ₹5.59–8.04 lakh | Petrol / CNG | Manual / AMT | 5 |
| i20 | ₹5.99–10.63 lakh | Petrol | Manual / IVT | 5 |
| i20 N Line | ₹9.27–11.73 lakh | Petrol | Manual / DCT | 5 |
| IONIQ 5 | ₹55.70 lakh | Electric | Single-speed reduction gear | 5 |
| Creta Electric | ₹18.02–24.70 lakh | Electric | Single-speed reduction gear | 5 |

## Important audit notes

- Do not turn model-level price ranges into variant-level prices.
- Exact variant names, individual prices, model-year applicability, and city-wise on-road prices remain to be audited from official brochures or price lists.
- Hyundai's official page currently has BAYON content and a dated blog describing HX 2 through HX 10 trims; confirm orderability and exact trim-price mapping before import.
- The current Find-a-Car page lists IONIQ 5 with a 72.6 kWh battery, while Hyundai's 2025-26 annual report describes an April 2026 refresh with an 84 kWh battery. Treat these as potentially different model-year records and reconcile before import.
- Prime-HB and Prime-SD are classified as Taxi on the official catalogue. Exclude from retail passenger catalogue unless scope is explicitly expanded.
- Source terms and commercial redistribution rights still require review. This file is an audit artifact, not an approved import manifest.

Sources:
- https://www.hyundai.com/in/en/find-a-car
- https://www.hyundai.com/in/en
- https://www.hyundai.com/in/en/investor-relations/financial-information/reports/annual-report-2025-26


## Current catalogue recheck

Rechecked: 2026-11-06
Primary sources:
- https://www.hyundai.com/in/en
- https://www.hyundai.com/in/en/find-a-car
- https://org2.hyundai.com/in/en/connect-to-service/hyundai-service/owners-manual

The live official homepage and Find-a-Car catalogue confirm these retail passenger model families: Grand i10 NIOS, i20, i20 N Line, Aura, Verna, Exter, Venue, Venue N Line, BAYON, Creta, Creta N Line, Alcazar, IONIQ 5 and Creta Electric. Prime-HB and Prime-SD remain separately classified as Taxi and are excluded from the retail passenger set.

The official owner-manual archive gives explicit current model-year boundaries for several refreshed models:
- Grand i10 NIOS: Jan 2026 to present
- Exter: Mar 2026 to present
- Aura: Jan 2026 to present
- Venue and Venue N Line: Nov 2025 to present
- BAYON: Oct 2026 to present
- Creta and Creta N Line: Jan 2024 to present
- Alcazar: Jun 2024 to present
- Verna: Mar 2026 to present
- i20 and i20 N Line: Oct 2023 to present

Use these ranges to distinguish current model-year variants from discontinued model-year manuals; they do not prove exact variant availability or dealer stock.

### Current official homepage starting-price observations

These are starting prices only, not complete variant price matrices:

| Model | Official homepage starting price (INR) |
|---|---:|
| BAYON | 999900 |
| Exter | 580600 |
| Venue | 799900 |
| Venue N Line | 1066100 |
| Creta | 1090700 |
| Alcazar | 1450700 |
| Creta N Line | 1903300 |
| Verna | 1099200 |
| Aura | 599990 |
| Grand i10 NIOS | 559700 |
| i20 | 599700 |
| i20 N Line | 932200 |
| IONIQ 5 | 5570600 |
| Creta Electric | 1802800 |

The Find-a-Car page provides model-level ranges and specifications; the homepage starting figures differ slightly from the ranges captured in the earlier pilot audit. Preserve each as a dated source observation and reconcile page/version differences before price import. Do not overwrite one with another silently.

### Freshness and source-quality flags

- BAYON is explicitly listed on the official India catalogue, with owner-manual coverage from Oct 2026 to present. It should no longer be treated merely as an unclear candidate.
- IONIQ 5 remains a data conflict: Find-a-Car still describes a 72.6 kWh battery while annual-report material describes a 2026 refresh with an 84 kWh battery. Keep model-year/specification records separate until Hyundai's current brochure and orderable variant are reconciled.
- The homepage and Find-a-Car show model-level starting prices/ranges, not variant-level price cards. No exact variant prices have been inferred.
- No city-wise on-road prices captured.
- Source reuse / redistribution permission remains review required.
- Firestore import not performed.

Sources:
- https://www.hyundai.com/in/en
- https://www.hyundai.com/in/en/find-a-car
- https://org2.hyundai.com/in/en/connect-to-service/hyundai-service/owners-manual
- https://www.hyundai.com/in/en/investor-relations/financial-information/reports/annual-report-2025-26
