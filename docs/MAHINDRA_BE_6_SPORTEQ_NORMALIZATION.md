# Mahindra BE 6 SPORTEQ normalization

Checked: 2026-11-06

## Deliverable

- `data/mahindra-be-6-sporteq-variant-price-observations.csv`: 12 OEM price observations covering all eight SPORTEQ grades and their published battery capacities.

## Current SPORTEQ lineup and full-battery prices

| Grade | Battery | Ex-showroom INR |
|---|---:|---:|
| ONE | 59 kWh | ₹19,45,000 |
| TWO | 59 kWh | ₹20,95,000 |
| THREE | 59 kWh | ₹21,95,000 |
| THREE | 70 kWh | ₹22,95,000 |
| THREE+ | 70 kWh | ₹23,95,000 |
| THREE+ | 79 kWh | ₹24,95,000 |
| FOUR | 79 kWh | ₹26,95,000 |
| LAUNCH EDITION | 79 kWh | ₹26,95,000 |
| FE | 79 kWh | ₹24,45,000 |
| FE FOUR | 79 kWh | ₹26,95,000 |

Mahindra's August 15, 2026 OEM release lists eight grades: ONE, TWO, THREE, THREE+, FOUR, FE, FE FOUR and Launch Edition. The price matrix maps all published full-battery grade/capacity combinations.

## BaaS treatment

The same OEM matrix publishes BaaS upfront prices for ONE 59 kWh (₹11,45,000) and TWO 59 kWh (₹12,95,000), with battery at ₹3.75/km. These are not full-battery ex-showroom prices. Mahindra's August 28, 2026 release extends BaaS availability across all SPORTEQ variants, but does not provide a complete grade-wise BaaS upfront matrix in the captured content. No missing BaaS amounts have been inferred.

## Charger and technical details

- Wall charger and installation are explicitly excluded from the published ex-showroom amounts.
- The August 2026 owner manual identifies IPMSM motor variants with 170/180/210 kW maximum power, 380 Nm torque, 59/70/79 kWh battery capacities and single-speed transmission. The manual does not map each motor output to every grade/battery combination in the captured table, so no grade-level motor output is invented.
- Formula E Freedom Edition and Launch Edition remain separate special-edition grade labels; they are not merged into standard trims.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra August 15, 2026 BE 6 SPORTEQ launch and full price matrix: https://www.mahindra.com/news-room/press-release/en/mahindra-introduces-the-be-6-sporteq-a-bold-new-expression-of-sport-technology-and-electric-performance
- Mahindra August 28, 2026 BaaS expansion: https://www.mahindra.com/news-room/press-release/en/mahindra-expands-battery-as-a-service-across-its-entire-electric-origin-suv-portfolio
- Mahindra August 2026 BE 6 SPORTEQ owner manual: https://mvault-cloudfront.mahindra.com/Owner%27s-Manual/BE%206%20SPORTEQ_HTML_17AUG2026/file3Dc405Busers5B500103205Bdownloads5Bm114-be6ns-vehiclemanual.ditamap.html
