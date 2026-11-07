# BMW M2 India normalization

Checked: 2026-11-07

## Audit outcome

**Status: partial — four India-relevant technical configurations identified, current model-level price captured, CS launch price retained historically, and M2 xDrive Turbo Edition price remains unannounced.**

BMW India's current all-models catalogue lists the M2 Coupé from ₹1,06,50,000. Official India sources identify the standard M2, limited-run M2 CS and limited-run M2 xDrive Turbo Edition. These are separate configurations, not one interchangeable trim.

## India configurations

| Configuration | Engine output | Torque | Transmission | Drive | 0–100 km/h | India price evidence |
|---|---:|---:|---|---|---:|---|
| M2 Coupé automatic | 480 hp | 600 Nm | 8-speed M Steptronic | Not stated in captured India release | 4.0 s | Current catalogue model-level starting price ₹1,06,50,000; not transmission-mapped |
| M2 Coupé manual | 480 hp | 550 Nm | Optional 6-speed manual | Not stated in captured India release | 4.2 s | No separate manual price |
| M2 CS | 530 hp / 390 kW | 650 Nm | 8-speed M Steptronic with Drivelogic | Rear-wheel drive | 3.8 s | ₹1,66,00,000 launch price on 18 Mar 2026; historical |
| M2 xDrive Turbo Edition | 480 hp / 353 kW | Not stated | Not stated in India release | xDrive AWD | 3.7 s | India price not announced as of 7 Nov 2026 |

### Standard M2

BMW India launched the refreshed M2 in November 2024. The India release confirms a 3.0-litre six-cylinder in-line engine, 480 hp, 600 Nm with automatic transmission and 550 Nm with manual transmission. Eight-speed M Steptronic is standard; a six-speed manual is optional. The release gives 4.0 s and 4.2 s respectively for 0–100 km/h and identifies the car as a four-seater. The current all-models page displays the M2 Coupé from ₹1,06,50,000; that model-level figure is not assigned separately to either transmission.

### M2 CS

BMW India launched the first M2 CS in India on 18 March 2026 as a limited-quantity CBU. Its India release confirms 390 kW/530 hp, 650 Nm, rear-wheel drive, eight-speed M Steptronic with Drivelogic, 3.8 s 0–100 km/h and 302 km/h top speed. The launch price was ₹1,66,00,000 ex-showroom. BMW separately announced an up-to-2% price increase across its range effective 1 April 2026, so the March launch price is historical, not a confirmed current dealer quote.

### M2 xDrive Turbo Edition

BMW India opened pre-orders on 13 October 2026, with limited numbers and first-come, first-served allocation. The India release confirms 353 kW/480 hp, 3.7 s 0–100 km/h, 250 km/h top speed or 285 km/h with the optional M Driver's Package, plus the xDrive designation. The India release does not state torque, transmission or price. Those fields remain blank; global-market specifications are not substituted.

## Deliverables

- `data/bmw-m2-variant-structure.csv` — four India configurations, with unreported values blank.
- `data/bmw-m2-price-observations.csv` — current catalogue starting price, historical CS launch price and explicit Turbo Edition not-announced observation.
- `docs/BMW_M2_NORMALIZATION.md` — source hierarchy and normalization decisions.

## Sources

1. BMW India current all-models catalogue: https://www.bmw.in/en/all-models.html
2. BMW India, refreshed M2 launch, 28 November 2024: https://www.press.bmwgroup.com/india/article/detail/T0446601EN/sensational-obsession-the-new-bmw-m2-debuts-in-india
3. BMW India, M2 CS launch, 18 March 2026: https://www.press.bmwgroup.com/india/article/detail/T0456445EN/accelerate-your-senses-the-new-bmw-m2-cs-launched-in-india
4. BMW India, M2 xDrive Turbo Edition pre-orders, 13 October 2026: https://www.press.bmwgroup.com/india/article/detail/T0461732EN/the-first-ever-bmw-m2-xdrive-turbo-edition-open-for-pre-orders-in-india
5. BMW India, price increase effective 1 April 2026: https://www.press.bmwgroup.com/india/article/attachment/T0456478EN/645764

## Data governance

All source records remain `review_required`; commercial reuse and redistribution remain `unknown`. Staging only. No Firestore production write or publication was performed.
