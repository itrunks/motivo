# BMW i4 India normalization

Checked: 2026-11-06

## Audit outcome

**Status: partial — historical India technical configurations normalized; current India orderability and price not established.**

BMW India's current all-models catalogue, checked on 2026-11-06, does not list the i4. The catalogue currently presents other electric models, including iX1 LWB, i7, i5 and i5 LWB. Absence from this current catalogue is evidence that the i4 is not currently listed there; it is not, by itself, proof of a formal discontinuation date or a definitive dealer-stock position.

The official BMW India December 2023 i4 specification sheet identifies two India-market configurations:

| India specification-sheet variant | Motor output | Torque | Gross battery | WLTP range | 0–100 km/h |
|---|---:|---:|---:|---:|---:|
| i4 eDrive35 M Sport | 210 kW / 286 hp | 430 Nm | 70.2 kWh | 406–483 km | 6.0 s |
| i4 eDrive40 M Sport | 250 kW / 340 hp | 430 Nm | 83.9 kWh | 493–590 km | 5.7 s |

Both use fifth-generation BMW eDrive technology with a rear-axle-mounted electric motor, a single-speed fixed-ratio transmission and rear-wheel drive. The specification sheet gives maximum DC charging power of 180 kW for eDrive35 and 205 kW for eDrive40; AC three-phase charging is supported up to 11 kW.

## Price treatment

No current official BMW India i4 price was found in the current catalogue. No current price observation is therefore populated. Historical/third-party advertised prices are deliberately excluded from the official price-observation file rather than being represented as current OEM prices.

## Deliverables

- `data/bmw-i4-variant-structure.csv` — two India-market technical configurations from the official 2023 BMW India specification sheet.
- `data/bmw-i4-price-observations.csv` — header-only; no current official price observation verified.

## Sources

1. BMW India, December 2023 i4 specification sheet: https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/brochure%20download/specsheets/2023/bmw-i-series/i4/bmw-specsheet-i4-december-2023.pdf.asset.1703656608180.pdf
2. BMW India current all-models catalogue: https://www.bmw.in/en/all-models.html

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. This work is staging-only. No Firestore write or publication was performed.
