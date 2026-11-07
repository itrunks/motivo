# BMW M5 India normalization

Checked: 2026-11-07

## Audit outcome

**Status: complete — one current India M5 Sedan M Hybrid powertrain configuration and a current official catalogue price captured.**

BMW India's current all-models catalogue lists the M5 under plug-in hybrid sedans from ₹2,11,50,000. The current M5 Sedan product page describes the seventh-generation plug-in hybrid with 535 kW/727 hp system output, 1,000 Nm system torque, M xDrive AWD and 3.5 s 0–100 km/h. BMW India's India-specific launch release (21 Nov 2024) provides the component outputs, transmission and 69 km WLTP electric range.

## Normalized India configuration

| Field | India-market value |
|---|---|
| Variant | BMW M5 Sedan M Hybrid |
| Fuel | Plug-in hybrid petrol/electric |
| Engine | 4.4-litre S68 M TwinPower Turbo V8 + integrated electric drive |
| Combustion engine output | 430 kW / 585 hp; 750 Nm |
| Electric drive output | 145 kW / 197 hp; 280 Nm |
| System output | 535 kW / 727 hp; 1,000 Nm |
| Transmission | 8-speed M Steptronic with Drivelogic |
| Drivetrain | M xDrive all-wheel drive |
| 0–100 km/h | 3.5 seconds |
| Top speed | 250 km/h standard; 305 km/h with optional M Driver's Package |
| Seats | 5 |
| Pure-electric range | Up to 69 km WLTP |
| Battery capacity | Left blank: India launch release prints “18.6 kW” for the battery, not an energy unit; no silent correction to kWh. |
| DC/AC charging | Not stated in captured India OEM sources; left blank. |

## 100 Jahre Nürburgring Edition

BMW India announced the limited-run 100 Jahre Nürburgring collection on 5 October 2026 and opened pre-orders through authorised dealers. The M5 Sedan derivative is described with exclusive Nürburgring Green/Sapphire Black styling, carbon roof, special wheel accents and anniversary interior embroidery. The announcement does not disclose a separate M5 powertrain, battery, price or output; it is treated as a special appearance/collector edition of the M5 Sedan, not a second technical configuration.

## Price observations

- **Current BMW India catalogue display:** ₹2,11,50,000, checked 2026-11-07.
- **Historical India launch price:** ₹1,99,00,000 ex-showroom, announced 2024-11-21.
- Current catalogue price is GST-inclusive ex-showroom and excludes road tax, TCS, RTO/statutory fees, local levies and insurance. Price prevailing at invoicing applies; confirm dealer quotation.

## Deliverables

- `data/bmw-m5-variant-structure.csv` — one India M5 M Hybrid technical configuration.
- `data/bmw-m5-price-observations.csv` — current catalogue starting price and dated launch price.
- `docs/BMW_M5_NORMALIZATION.md` — evidence and decisions.

## Sources

1. BMW India current M5 Sedan product page: https://www.bmw.in/en/all-models/m-series/m5-series/2024/bmw-m5-sedan.html
2. BMW India all-models catalogue: https://www.bmw.in/en/all-models.html?series=5
3. BMW India M5 launch release, 21 November 2024: https://www.press.bmwgroup.com/india/article/detail/T0446483EN/duality-untamed:-the-all-new-bmw-m5-launched-in-india
4. BMW India 100 Jahre Nürburgring India announcement, 5 October 2026: https://www.press.bmwgroup.com/india/article/detail/T0461393EN/bmw-and-bmw-motorrad-bring-the-ultra-exclusive-%E2%80%9C100-jahre-nuerburgring%E2%80%9D-editions-to-india-open-for-pre-orders

## Data governance

All source records remain `review_required`; commercial reuse and redistribution remain `unknown`. Staging only. No production Firestore write or publication performed.
