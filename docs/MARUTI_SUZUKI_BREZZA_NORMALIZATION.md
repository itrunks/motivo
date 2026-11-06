# Maruti Suzuki Brezza 2026 normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-brezza-variant-structure.csv`: 13 confirmed current powertrain/trim combinations.
- `data/maruti-suzuki-brezza-price-observations.csv`: 13 October 2026 ex-showroom price observations.

## Current variant matrix

The 2026 Brezza has four trims—LXi, VXi, ZXi and ZXi+—and three engine families. The current official price page's selector labels and July 2026 official launch release confirm the 1.0-litre Turbo Boosterjet variants; the earlier workqueue warning that these labels might be anomalous is resolved by the official launch release.

**1.0-litre Turbo Boosterjet petrol**
- LXi, VXi, ZXi and ZXi+ — all 6-speed manual.
- 998 cc, 81 kW / 110.12 PS, 170 Nm.

**1.5-litre K15C Smart Hybrid naturally aspirated petrol**
- LXi, VXi and ZXi — 6-speed manual.
- VXi, ZXi and ZXi+ — 6-speed torque-converter automatic.
- 1462 cc, 75.8 kW / 103.06 PS, 139 Nm.

**1.5-litre K15C S-CNG**
- LXi, VXi and ZXi — 6-speed manual.
- 1462 cc, 64.6 kW / 87.8 PS, 121.5 Nm in CNG mode.

All are front-wheel-drive, 5-seat compact SUVs. Turbo Boosterjet is not conflated with the K15C Smart Hybrid engine.

## Price evidence and date separation

The current October 30, 2026 secondary-source price table lists:
- Turbo petrol: LXi ₹7,49,900; VXi ₹8,64,900; ZXi ₹9,94,900; ZXi+ ₹11,25,900.
- 1.5 petrol manual: LXi ₹8,34,900; VXi ₹9,30,900; ZXi ₹10,54,900.
- 1.5 petrol automatic: VXi ₹10,60,900; ZXi ₹11,84,900; ZXi+ ₹13,54,900.
- CNG manual: LXi ₹9,39,900; VXi ₹9,99,000; ZXi ₹11,59,900.

These are ex-showroom INR observations from Cars24's October 30, 2026 revision report. The official Maruti price page captured in the source audit states that its listed prices are effective from 24 July 2026 and shows older amounts for some 1.5-litre variants. Those earlier OEM amounts are not silently substituted for the October revision. The October values remain secondary-source evidence and require dealer/invoice confirmation before customer-facing use.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Brezza price/variant page: https://www.marutisuzuki.com/arena/brezza/price
- Maruti Suzuki official July 2026 Turbo Boosterjet launch release: https://www.marutisuzuki.com/corporate/media/press-releases/2026/july/maruti-suzuki-launches-new-brezza-turbo-boosterjet-with-powerpacked-performance
- Maruti Suzuki official Brezza product page: https://www.marutisuzuki.com/arena/brezza
- Cars24, October 30, 2026 Brezza price revision: https://www.cars24.com/news/auto/maruti-suzuki-brezza-price-hike-in-october-2026/
- Autocar India, July 27, 2026 full variant price matrix: https://www.autocarindia.com/car-news-amp/2026-maruti-brezza-full-price-list-revealed-440298
