# Mahindra Thar OG normalization

Checked: 2026-11-06

## Deliverables

- `data/mahindra-thar-og-variant-structure.csv`: 15 current Thar OG engine/trim/transmission/drive configurations.
- `data/mahindra-thar-og-price-observations.csv`: 15 official introductory ex-showroom price observations.

## Current variant matrix

Mahindra's 22 September 2026 Thar OG launch release defines 15 configurations across AXT, LXT and ZXT:

- 1.5-litre D117 CRDe diesel: AXT, LXT and ZXT, all 6-speed manual and rear-wheel drive.
- 2.2-litre D22 mHawk diesel: LXT and ZXT in rear-wheel-drive automatic, 4WD manual and 4WD automatic.
- 2.0-litre G20 mStallion TGDi petrol: LXT and ZXT in rear-wheel-drive automatic, 4WD manual and 4WD automatic.

All are 3-door, 4-seat off-road SUVs. The engine/drive/gearbox combinations are captured exactly from the official launch matrix; no unsupported combinations are created.

## Powertrain specifications

- D117 CRDe 1.5-litre diesel, 1493 cc: 87.2 kW / 118.6 PS, 300 Nm.
- D22 mHawk 2.2-litre diesel, 2184 cc: 111.9 kW / 152.1 PS, 330 Nm.
- G20 mStallion TGDi 2.0-litre turbo-petrol, 1997 cc: 119 kW / 161.8 PS, 330 Nm.

The D117 is paired with 6-speed manual RWD. D22 and G20 are paired with 6-speed manual or 6-speed automatic depending on RWD/4WD configuration.

## Price basis and validity

Mahindra's official launch announcement lists introductory ex-showroom prices from ₹10,32,000 to ₹18,99,000. The introductory prices are valid for deliveries made until **30 November 2026**. The price file records the 15 exact grade/powertrain/drive combinations with the stated launch price. These are not on-road prices and should not be used after the stated validity window without a new OEM quote.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Mahindra official Thar OG launch release and 15-variant price matrix, 22 September 2026: https://www.mahindra.com/news-room/press-release/en/mahindra-launches-thar-og-built-on-legacy-engineered-for-a-new-era-introductory-price-starting-at-rupees-10.32-lakh
- Mahindra official Thar OG product page: https://auto.mahindra.com/suv/thar-og
- Mahindra official online variant selector: https://auto.mahindra.com/own-online/variant-selection?mgc=THRN
- Autocar India Thar OG variant and price summary: https://www.autocarindia.com/car-news/new-mahindra-thar-og-launched-at-rs-1032-lakh-440990
