# Mahindra XUV 3XO EV normalization

Checked: 2026-11-06

## Deliverable

- `data/mahindra-xuv-3xo-ev-variant-price-observations.csv`: two OEM launch-grade price observations.

## Official launch matrix

Mahindra's January 6, 2026 announcement defines two variants:

| Grade | Battery | Ex-showroom launch price |
|---|---:|---:|
| AX5 | 39.4 kWh | ₹13,89,000 |
| AX7L | 39.4 kWh | ₹14,96,000 |

The announcement states a 110 kW / 150 PS motor, 310 Nm torque, 0–100 km/h in 8.3 seconds and a real-world range claim up to 285 km. Deliveries began February 23, 2026. The optional 7.2 kW wall charger is ₹50,000 extra.

## Current-price limitation

No current Mahindra XUV 3XO EV selector page or newer grade-wise price matrix was captured in this pass. The two amounts are retained as dated January 2026 launch prices, not represented as verified November 2026 prices. Current orderability, current price and charger inclusion need current OEM selector/dealer confirmation.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Source

- Mahindra official XUV 3XO EV launch release, January 6, 2026: https://auto.mahindra.com/press-release/mahindra-introduces-xuv-3xo-ev-range.html


## Current OEM model-range and brochure recheck — 2026-11-07

Mahindra's current SUV homepage lists XUV3XO EV at **₹13.89L–₹14.96L** ex-showroom. These endpoints match the January 2026 launch prices for AX5 (₹13.89L) and AX7L (₹14.96L), but the current homepage does not map the range endpoints to the individual grades. The two current model-level endpoints are therefore recorded separately and are not duplicated into the variant rows.

The official AX5 and AX7L brochure pages confirm the current technical structure for both grades:
- 39.4 kWh battery
- 110 kW / 150 PS motor
- 310 Nm torque
- Front-wheel drive
- 5 seats
- 351 km MIDC P1+P2 range and 456 km MIDC P1 range
- 7.2 kW AC charging time 6.5 hours; 50 kW DC 0–80% in 50 minutes

The January launch release states a real-world range claim up to 285 km and prices of ₹13.89L (AX5) / ₹14.96L (AX7L); the optional 7.2 kW wall charger costs ₹50,000 extra. Those remain dated launch-price observations. Current model-range endpoints matching those values are corroboration, not a fresh variant-wise price list.

The current homepage has an Explore link for XUV3XO EV but no explicit Book Now link in the captured model card. Exact current dealer orderability, price effective date and current grade-wise price confirmation remain pending. Transmission type was not explicitly captured in the brochure and is left blank rather than inferred.

New evidence:
- Current model range: https://auto.mahindra.com/suv
- AX5 brochure page: https://auto.mahindra.com/xuv3xo-ev-ax5-electr/X3XEM096218043888.html
- AX7L brochure page: https://auto.mahindra.com/xuv3xo-ev-ax7l-electr/X3XEM096118043892.html
