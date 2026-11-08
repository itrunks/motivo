# BMW 3 Series Long Wheelbase India normalization

Checked: 2026-11-06

## Deliverables

- `data/bmw-3-series-long-wheelbase-variant-structure.csv`: two official brochure powertrain/trim configurations.
- `data/bmw-3-series-long-wheelbase-price-observations.csv`: current official model/listing price observations, with the diesel price basis flagged for confirmation.

## Variants and specifications

| Variant | Engine | Power | Torque | Transmission | Drive |
|---|---|---:|---:|---|---|
| 330Li M Sport | 1,998 cc petrol | 258 hp | 400 Nm | 8-speed Steptronic Sport | RWD |
| 320Ld M Sport | 1,995 cc diesel | 190 hp | 400 Nm | 8-speed Steptronic Sport | RWD |

The official November 2023 India specification sheet provides the technical matrix and 0–100 km/h times (6.2 s petrol; 7.6 s diesel).

## Price evidence and limitation

- 330Li M Sport: BMW India dedicated 3 Series LWB page lists ₹62,70,000 starting price.
- 320Ld M Sport: BMW India all-models listing shows ₹64,20,000, but the dedicated current product page describes only the 2.0L petrol engine and does not surface the diesel derivative. The listing price basis is not fully explained in the captured text.

The 320Ld remains a current-orderability/price-basis confirmation item. It is not removed from the structure because it is explicitly listed on BMW India's all-models page.

## Status

Partial. Both official technical configurations and current price-list observations are captured, but current 320Ld orderability and price basis need confirmation against the live configurator/dealer.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- BMW India 3 Series Long Wheelbase product page: https://www.bmw.in/en/all-models/3-series/bmw-3-series-long-wheelbase.html
- BMW India current all-models listing: https://www.bmw.in/en/all-models.html?series=3
- BMW India official 2023 3 Series Gran Limousine specification sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-3-series/3gl/BMW_Specsheet_3GL_Petrol%20%26%20Diesel_A4_Nov_2023.pdf.asset.1700720638950.pdf
