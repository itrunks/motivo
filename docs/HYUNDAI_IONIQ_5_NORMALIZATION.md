# Hyundai IONIQ 5 powertrain normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/hyundai-ioniq-5-powertrain-normalization.csv`: one current India-market powertrain configuration.
- No retail trim-level variants are invented because the captured India sources do not expose distinct retail trim labels.

## Current official specification

Hyundai's current specification page lists:
- Electric motor: Permanent Magnet Synchronous Motor (PMSM)
- Configuration: Rear-wheel drive (RWD)
- Maximum power: 168 kW (228.5 PS)
- Battery: 84 kWh liquid-cooled lithium-ion with battery heating
- Transmission: single-speed reduction gear

The current highlights page identifies the body style as SUV and gives a claimed range of 690 km. Hyundai's April 28, 2026 launch announcement confirms the 84.0 kWh battery and up to 690 km range.

The earlier audit workqueue observation mentioned 72.6 kWh. That is stale relative to the April 2026 updated India model. The current 84 kWh source is recorded, and the stale value is not carried forward.

## Price and variant limitation

The current official price page lists ₹55,70,600 ex-showroom at model level. Since no distinct retail trim labels or complete variant price matrix were exposed, the amount is not assigned to a fabricated trim. The CSV keeps price blank and records the model-level limitation in reviewer notes.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. This file is a research/powertrain normalization output, not an approved import manifest. No Firestore write or publication has been performed.

## Sources

- Current specification: https://www.hyundai.com/in/en/find-a-car/ioniq-5/specification
- Highlights / battery, range and body style: https://www.hyundai.com/in/en/find-a-car/ioniq-5/highlights
- Features: https://www.hyundai.com/in/en/find-a-car/ioniq-5/features
- Current price page: https://www.hyundai.com/in/en/find-a-car/ioniq-5/price
- April 28, 2026 updated model launch: https://www.hyundai.com/in/en/hyundai-story/media-center/press-release/new-ioniq5-with-enhanced-range-advanced-technology-and-refined-design
