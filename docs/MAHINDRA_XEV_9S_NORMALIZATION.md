# Mahindra XEV 9S normalization

Checked: 2026-11-06

## Deliverables

- `data/mahindra-xev-9s-variant-structure.csv`: six grade/battery configurations from the official launch feature matrix.
- `data/mahindra-xev-9s-price-observations.csv`: official launch starting/top prices and the later BaaS starting observation, without inventing intermediate grade prices.

## Six grade/battery configurations

| Grade | Battery | Motor power |
|---|---:|---:|
| PACK ONE ABOVE | 59 kWh | 170 kW |
| PACK ONE ABOVE | 79 kWh | 210 kW |
| PACK TWO ABOVE | 70 kWh | 180 kW |
| PACK TWO ABOVE | 79 kWh | 210 kW |
| PACK THREE | 79 kWh | 210 kW |
| PACK THREE ABOVE | 79 kWh | 210 kW |

The official launch release confirms a 7-seat SUV. It identifies 380 Nm torque and power mappings of 170 kW (59 kWh), 180 kW (70 kWh) and 210 kW (79 kWh). The XEV 9S is based on the INGLO electric platform and uses a single-speed electric transmission, per the official owner manual.

## Price evidence and missing data

- Model launch starting price: ₹19,95,000 ex-showroom. The headline does not explicitly map this amount to a specific grade/battery row in the captured release.
- Pack Three Above 79 kWh: ₹29,45,000 ex-showroom, explicitly identified as the top variant.
- Intermediate prices for the remaining four configurations are not present in the captured official launch page; they remain blank and are not interpolated.
- Mahindra's August 28, 2026 BaaS release gives a model starting upfront amount of ₹12,65,000 with battery financing at ₹3.75/km and makes BaaS available across all XEV 9S variants. This is a finance product, not pay-per-use. Battery EMI varies by battery size, downpayment and tenure; the cited example assumes 60 km/day and a specific downpayment. The BaaS amount is not mapped to a particular grade.

The 2025 launch price and 2026 BaaS starting amount are separate commercial price bases and must not be merged.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra XEV 9S launch and variant feature matrix, November 27, 2025: https://www.mahindra.com/news-room/press-release/en/mahindra-unveils-xev-9s-indias-big-new-electric-7-seater-suv-starting-at-rupees-19.95-lakh
- Mahindra BaaS expansion, August 28, 2026: https://www.mahindra.com/news-room/press-release/en/mahindra-expands-battery-as-a-service-across-its-entire-electric-origin-suv-portfolio
- Mahindra XEV 9S owner manual, released May 2026: https://mvault-cloudfront.mahindra.com/Owner%27s-Manual/XEV%209S%20HTML%2013MAY2026/file3D0000794814.html
