# Hyundai CRETA Electric variant normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-creta-ev-variant-structure.csv`: 9 trim/battery-pack combinations from Hyundai India's current features and highlights pages.
- No variant-level price rows are created because the available official price evidence is a model-level range and BaaS offer, not a complete variant-price matrix.

## Current battery and trim plan

**42 kWh battery pack:** Executive, Executive Tech, Premium, Excellence, Excellence Knight.

**51.4 kWh battery pack:** Executive (O) LR, ESmart (O) LR, Excellence LR, Excellence LR Knight.

Total: 9 combinations. Hyundai's official highlights page gives claimed ranges of 420 km for the 42 kWh pack and 510 km for the 51.4 kWh pack. The current model catalogue classifies the vehicle as an SUV, Electric, automatic transmission. Engine is left blank because this is a battery-electric vehicle. Battery capacity is retained in a dedicated `battery_kwh` column.

## Price evidence

The official model catalogue gives a broad ex-showroom range of ₹18.02–24.70 lakh. The highlights page separately advertises a Battery-as-a-Service starting price of ₹10.99 lakh plus battery EMI from ₹3.90/km. These are different commercial price bases and are not variant-level ex-showroom prices. No price is assigned to individual rows. Current city/variant pricing and the exact BaaS price basis must be confirmed through the official selector/dealer.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This CSV is a research/normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Features / battery-pack and trim matrix: https://www.hyundai.com/in/en/find-a-car/creta-electric/features
- Highlights / battery capacities, range, BaaS and configurations: https://www.hyundai.com/in/en/find-a-car/creta-electric/highlights
- Current model catalogue / price range and fuel/transmission classification: https://www.hyundai.com/in/en/find-a-car
