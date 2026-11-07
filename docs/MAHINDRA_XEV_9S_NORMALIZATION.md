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


## Current FAQ price and seating reconciliation — 2026-11-07

The current Mahindra Electric SUVs FAQ now provides a complete full-battery ex-showroom matrix for both seating layouts, plus a variant-wise BaaS matrix. The previous 2025 launch starting/top prices are retained as historical observations only.

### Current full-battery prices

| Grade | Battery | 7-seat price | 6-seat price |
|---|---:|---:|---:|
| Pack One Above | 59 kWh | ₹21,40,000 | Not listed |
| Pack One Above | 79 kWh | ₹23,40,000 | Not listed |
| Pack Two Above | 70 kWh | ₹25,80,000 | ₹26,00,000 |
| Pack Two Above | 79 kWh | ₹26,70,000 | ₹26,90,000 |
| Pack Three | 79 kWh | ₹28,80,000 | ₹28,80,000 |
| Pack Three Above | 79 kWh | ₹30,70,000 | ₹30,90,000 |

The FAQ states that these listed prices include the 11.2 kW wall charger. It also says a 3.3 kW portable charger is included as standard; a 7.2 kW wall charger can be bought as an accessory for ₹60,000, and a no-wall-charger configuration is available. No effective date is shown on the FAQ; these are current source observations checked 2026-11-07.

### Current variant-wise BaaS upfront prices

| Grade | Battery | BaaS vehicle upfront |
|---|---:|---:|
| Pack One Above | 59 kWh | ₹12,65,000 |
| Pack One Above | 79 kWh | ₹12,65,000 |
| Pack Two Above | 70 kWh | ₹16,05,000 |
| Pack Two Above | 79 kWh | ₹15,95,000 |
| Pack Three | 79 kWh | ₹17,85,000 |
| Pack Three Above | 79 kWh | ₹19,95,000 |

The BaaS table is grade/battery-level and does not split by 6-seat vs 7-seat; these amounts are therefore stored at grade/battery level, not copied onto each seating derivative. BaaS is dual-loan financing, not a battery subscription or per-kilometre rental. The FAQ explains that customers own both vehicle and battery, with the battery financed separately. The ₹3.75/km figure is an EMI illustration based on assumed 60 km/day usage and a specific down payment, not a usage fee. BaaS amounts exclude wall charger, road tax, insurance, TCS and other statutory levies.

### Current powertrain and seating structure

The current XEV 9S brochure confirms:
- Pack One Above: 59 kWh / 170 kW or 79 kWh / 210 kW
- Pack Two Above: 70 kWh / 180 kW or 79 kWh / 210 kW
- Pack Three and Pack Three Above: 79 kWh / 210 kW
- 380 Nm torque, RWD, single-speed electric transmission
- MIDC P1+P2 range: 521 km (59 kWh), 600 km (70 kWh), 679 km (79 kWh)

The current FAQ confirms 7-seat configurations for Pack One Above, Pack Two Above, Pack Three and Pack Three Above; 6-seat captain-seat configurations are available from Pack Two Above onwards. The updated structure file now contains 10 grade/battery/seating combinations.

The old 2025 release headline price ₹19.95L and top Pack Three Above ₹29.45L are historical and superseded by the current FAQ matrix. They are not used as current values. Source reuse and redistribution remain review_required/unknown; no Firestore import or publication is approved.

Current sources:
- Current Mahindra eSUV FAQ and full XEV 9S price/seating matrix: https://www.mahindraelectricsuv.com/faq.html
- Current variant-wise BaaS price matrix: https://www.mahindraelectricsuv.com/be-6-sporteq/baas-faq.html
- Official XEV 9S brochure and powertrain matrix: https://www.mahindraelectricsuv.com/on/demandware.static/-/Library-Sites-eSUVSharedLibrary/default/dw4aa4db0b/XEV9S%20BROCHURE.pdf
- 2025 launch announcement (historical price context): https://www.mahindra.com/news-room/press-release/en/mahindra-unveils-xev-9s-indias-big-new-electric-7-seater-suv-starting-at-rupees-19.95-lakh
