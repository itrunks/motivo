# Mahindra XEV 9e variant and price evidence

Checked: 2026-11-06

## Deliverable

- `data/mahindra-xev-9e-variant-price-observations.csv`: four historical OEM pack-price observations and one 2026 Cineluxe special-edition price observation.

## Standard pack structure — historical prices

| Grade | Battery | Historical ex-showroom price |
|---|---:|---:|
| PACK ONE | 59 kWh | ₹21,90,000 |
| PACK TWO | 59 kWh | ₹24,90,000 |
| PACK THREE SELECT | 59 kWh | ₹27,90,000 |
| PACK THREE | 79 kWh | ₹30,50,000 |

The official leaflet dates these prices to February 2025. They are preserved as historical OEM evidence only and are not treated as current 2026 retail prices. The leaflet states that charger and installation are extra: ₹50,000 for 7.2 kW or ₹75,000 for 11.2 kW.

## 2026 Cineluxe Edition

Mahindra announced the XEV 9e Cineluxe Edition at ₹29,35,000 ex-showroom on March 1, 2026. It is based on Pack Three with a 79 kWh battery. It remains a separate special edition and is not merged into the standard Pack Three row.

## BaaS update

Mahindra's August 28, 2026 announcement expanded BaaS to all XEV 9e variants and gives a model-level starting upfront amount of ₹13,90,000 with battery financing at ₹3.75/km (example usage 60 km/day). The release does not provide a grade-by-grade BaaS upfront matrix or current full-battery prices for the four standard packs. The BaaS starting amount is therefore documented here but not assigned to a specific grade or battery capacity.

## Status and import gate

Current full-battery grade-wise price coverage remains incomplete; standard-pack values are historical. Current BaaS grade pricing and current dealer orderability require confirmation. Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Official XEV 9e leaflet (February 2025 price basis): https://booking.mahindra.com/on/demandware.static/-/Library-Sites-eSUVSharedLibrary/default/dwbe1e0571/Xev-9e/XEV-9E-Leaflet.pdf
- Official Cineluxe Edition announcement (March 1, 2026): https://www.mahindra.com/news-room/press-release/en/mahindra-elevates-luxury-with-the-exclusive-xev-9e-cineluxe-edition-at-Rs-29.35-lakh
- Official BaaS expansion announcement (August 28, 2026): https://www.mahindra.com/news-room/press-release/en/mahindra-expands-battery-as-a-service-across-its-entire-electric-origin-suv-portfolio


## Current 2026 pack structure and BaaS price matrix — 2026-11-07

A current Mahindra Electric SUV specification brochure now confirms five standard pack/battery combinations:

| Pack | Battery | Motor | Torque | MIDC P1+P2 range |
|---|---:|---:|---:|---:|
| Pack One | 59 kWh | 170 kW | 380 Nm | 522 km |
| Pack Two | 59 kWh | 170 kW | 380 Nm | 522 km |
| Pack Two | 79 kWh | 210 kW | 380 Nm | 656 km |
| Pack Three Select | 59 kWh | 170 kW | 380 Nm | 522 km |
| Pack Three | 79 kWh | 210 kW | 380 Nm | 656 km |

All five are rear-wheel drive with automatic transmission. The brochure lists 7.2 kW and 11.2 kW AC wall-charger options. The current specification brochure supersedes the earlier 2024/2025 range figures for current specification work: 59 kWh is now listed at 522 km, not the earlier 542 km figure.

The current official BaaS FAQ now provides a variant-wise upfront price matrix:

| Pack / edition | Battery | BaaS vehicle upfront price |
|---|---:|---:|
| Pack One | 59 kWh | ₹13,90,000 |
| Pack Two | 79 kWh | ₹16,50,000 |
| Three Cineluxe | 79 kWh | ₹19,35,000 |
| Pack Three | 79 kWh | ₹20,50,000 |

These are BaaS vehicle-upfront amounts, not full-battery ex-showroom prices. Mahindra describes BaaS as a dual-loan structure: the customer owns both vehicle and battery, with battery financing handled separately. It is not a battery subscription or pay-per-kilometre rental. Prices exclude wall charger/installation, road tax, insurance, TCS and other statutory levies; financing terms and approval depend on the financier, down payment and tenure. The ₹3.75/km figure is an example financing calculation based on assumed usage, not a per-km usage charge.

The BaaS FAQ states the programme is available across all XEV 9e variants, while the variant-wise BaaS table lists the four combinations above. It does not provide current full-battery ex-showroom prices for all five standard pack/battery combinations. The four 2025 standard-pack prices remain historical observations and are not promoted as current 2026 full-battery prices. The Cineluxe March 2026 ₹29.35 lakh full-price observation remains a separate special-edition observation.

The current selector/order flow does not expose a full XEV 9e grade-wise full-battery price matrix in the captured text. Dealer confirmation is still required for current full-battery prices and order acceptance. Source reuse/redistribution remain review_required/unknown. No Firestore import or publication is approved.

New current sources:
- Current XEV 9e specification brochure: https://www.mahindraelectricsuv.com/on/demandware.static/-/Library-Sites-eSUVSharedLibrary/default/MXV9/XEV-9e-Brochure-Specification.pdf
- Current variant-wise BaaS FAQ: https://www.mahindraelectricsuv.com/be-6-sporteq/baas-faq.html
