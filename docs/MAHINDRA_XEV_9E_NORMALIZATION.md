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
