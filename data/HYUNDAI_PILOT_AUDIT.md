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
