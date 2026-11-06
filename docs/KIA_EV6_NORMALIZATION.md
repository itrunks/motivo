# Kia EV6 powertrain normalization — evidence notes

Checked: 2026-11-06

## Deliverable

- `data/kia-ev6-powertrain-normalization.csv`: one current India retail configuration, GT-Line AWD.
- No price observation is created because the current showroom page does not render a numeric India price in the captured content.

## Current India retail configuration

Kia's current showroom lists one trim available: GT-Line AWD. The current specifications page lists an 84 kWh lithium-ion battery, permanent-magnet synchronous motor, front and rear motor placement for AWD, 325 PS, 605 Nm, automatic transmission and 5 seats. The current specification page also describes a separate 84 kWh RWD technical variant, but the current showroom does not expose it as a separate India retail trim; it is not added as a retail row.

The existing workqueue contains an older 77.4 kWh GT-Line / GT-Line AWD observation. The current 84 kWh official India specification supersedes that older source snapshot. The old RWD retail configuration is not assumed current.

## Price

The current showroom page shows the GT-Line AWD trim but no numeric starting MSRP in the captured page. Price remains blank. Do not reuse the historical workqueue price without confirming its effective date and current India basis.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- Current showroom / one India retail trim: https://www.kia.com/in/our-vehicles/ev6/showroom.html
- Current specification / 84 kWh battery and motor variants: https://www.kia.com/in/our-vehicles/ev6/specs.html
- Current 84 kWh brochure: https://www.kia.com/content/dam/kia2/in/en/images/buy/download-brochure/Ev6-Latest-brochure.pdf
- Older 77.4 kWh brochure retained for historical comparison only: https://www.kia.com/content/dam/kia2/in/en/our-vehicles/showroom/ev6/prebooking/section2/pre-new/EV6_Brochure_For_Mobile.pdf
