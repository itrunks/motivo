# BMW i5 India normalization

Checked: 2026-11-06

## Audit outcome

**Status: complete — one currently listed India configuration with official technical and price evidence.**

BMW India's current all-models catalogue identifies the standard-wheelbase i5 M Model as the **BMW i5 M60** and lists it from **₹1,19,50,000** ex-showroom. The same catalogue separately lists **i5 LWB** as another model line; it is not included in this i5 record and will be audited under the separate i5 Long Wheelbase queue entry.

## Current India configuration

| Variant | Fuel | Output | Torque | Drive | 0–100 km/h | Price |
|---|---|---:|---:|---|---:|---:|
| BMW i5 M60 xDrive | Electric | 442 kW / 601 hp | 795 Nm | xDrive AWD | 3.8 s | ₹1,19,50,000 |

BMW India's technical data specifies a 1-speed automatic transmission, 83.9 kWh battery, WLTP range 455–516 km, maximum DC charging power 205 kW and AC charging power 11 kW. The 442 kW / 601 hp and 795 Nm values are the combined powertrain figures; the source page does not provide an India-specific individual motor output split in the captured table.

## Price basis

The current BMW India all-models catalogue lists ₹1,19,50,000 for the i5 M Model / BMW i5 M60. BMW states that the invoice-time price applies; the displayed ex-showroom price includes GST as applicable and excludes road tax, TCS, RTO, statutory taxes/fees, local levies and insurance. Dealer confirmation is required before treating the observation as a customer quotation.

## Deliverables

- `data/bmw-i5-variant-structure.csv` — one current India i5 M60 configuration.
- `data/bmw-i5-price-observations.csv` — one current official price observation.

## Sources

1. BMW India current i5 M60 technical data: https://www.bmw.in/en/all-models/m-series/bmw-i5-m60/bmw-i5-m60-xdrive-technical-data.html
2. BMW India current all-models catalogue: https://www.bmw.in/en/all-models.html
3. BMW India i5 M60 model overview: https://www.bmw.in/en/all-models/m-series/bmw-i5-m60/bmw-i5-m60xdrive-overview.html

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. This work is staging-only. No Firestore write or publication was performed.
