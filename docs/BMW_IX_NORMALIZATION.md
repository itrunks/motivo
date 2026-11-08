# BMW iX India normalization

Checked: 2026-11-06

## Audit outcome

**Status: partial — two historical India configurations and dated OEM launch prices captured; current India orderability and price are not verified.**

BMW India's current all-models catalogue, checked on 2026-11-06, lists iX1 LWB, i5, i5 LWB and i7 under its full-electric range, but does not list the iX. The iX should therefore not be treated as currently orderable based on the available current catalogue evidence. This absence does not establish the formal discontinuation date or dealer stock status.

## India-market configurations documented

| Variant | Power | Battery | Range | 0–100 km/h | Dated official launch price |
|---|---:|---:|---:|---:|---:|
| BMW iX xDrive40 | 326 hp | 76.6 kWh | Up to 425 km (India launch release does not state test cycle) | 6.1 s | ₹1,15,90,000 (Dec 2021 introductory) |
| BMW iX xDrive50 | 385 kW / 523 hp | 111.5 kWh gross | Up to 635 km WLTP | 4.6 s | ₹1,39,50,000 (Mar 2024) |

Both use dual electric motors, xDrive all-wheel drive and a single-speed transmission. The xDrive40 India launch release specifies 11 kW AC charging; the 2024 xDrive50 release specifies up to 195 kW DC and up to 22 kW AC charging. The xDrive40 torque and DC charging figures are left blank because the cited India launch release does not state them.

## Price treatment

Both price observations are historical OEM launch prices, not current official prices. No current iX price is recorded. BMW's 2024 launch release describes the xDrive50 as available from that date; the current model catalogue no longer lists iX. Dealer confirmation would be needed to establish any remaining stock or orderability.

## Deliverables

- `data/bmw-ix-variant-structure.csv` — two historical India configurations with unreported fields left blank.
- `data/bmw-ix-price-observations.csv` — two dated official launch-price observations, explicitly historical.

## Sources

1. BMW India, iX xDrive50 launch, 21 March 2024: https://www.press.bmwgroup.com/india/article/detail/T0440521EN/stay-ahead-of-the-curve-the-new-all-electric-bmw-ix-xdrive50-launched-in-india
2. BMW India, first iX launch, 13 December 2021: https://www.press.bmwgroup.com/india/article/detail/T0362593EN/joy-born-again-the-bmw-ix-first-bmw-electric-all-wheel-drive-vehicle-debuts-in-india
3. BMW India current all-models catalogue: https://www.bmw.in/en/all-models.html

## Data governance

Source review remains `review_required`; commercial reuse and redistribution remain `unknown`. This work is staging-only. No Firestore write or publication was performed.
