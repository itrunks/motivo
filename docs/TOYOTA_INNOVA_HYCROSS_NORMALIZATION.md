# Toyota Innova Hycross variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-innova-hycross-variant-structure.csv`: 12 exact grade/powertrain/seating configurations.
- `data/toyota-innova-hycross-price-observations.csv`: one model-level starting price; no grade-level prices are inferred.

## Current grade and powertrain mapping

Toyota's current specification matrix lists seven grades:
- Petrol: G-SLF, GX and GX(O), each available in 7- and 8-seat configurations.
- Strong hybrid: VX and VX(O), each available in 7- and 8-seat configurations; ZX and ZX(O) are 7-seat only.

This yields 12 configurations. Petrol uses the 2.0 l TNGA four-cylinder engine with Direct Shift CVT. Strong hybrid uses the 2.0 l TNGA engine with fifth-generation self-charging hybrid system, 168-cell Ni-MH battery and e-Drive sequential shift. The official current page lists 128 kW / 171.6 hp petrol output and 137 kW / 183.7 hp hybrid output, with 206 Nm hybrid motor torque. Body positioning is MPV with SUV styling; model year remains blank.

## Price

Toyota's current online booking page displays a starting ex-showroom price of ₹18,70,000. This is captured as a model-level starting price only and is not assigned to a particular trim or seating configuration. No complete current grade-wise price table was found in the captured official sources. The 2024 GX(O) price release and 2022 launch price list are historical and are not used as current prices.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- Toyota current grade/specification matrix: https://www.toyotabharat.com/showroom/innova/features-specs.html
- Toyota current grade cards: https://www.toyotabharat.com/showroom/innova/
- Toyota online booking and starting price: https://tweb.toyotabharat.com/innova-hycross.html
- Toyota current overview: https://www.toyotabharat.com/showroom/innova/index.html
