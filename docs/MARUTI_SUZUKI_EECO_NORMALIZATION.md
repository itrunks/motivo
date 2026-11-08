# Maruti Suzuki Eeco passenger-variant normalization

Checked: 2026-11-08

## Deliverable

- `data/maruti-suzuki-eeco-passenger-variant-normalization.csv`: four current passenger configurations.
- `data/maruti-suzuki-eeco-price-observations.csv`: 12 city-scoped and legacy price observations (4 Delhi, 4 Latur, 4 legacy unscoped).

## Scope and exclusions

The workqueue is specifically the passenger Eeco catalogue. The four included variants are:
- 5 Seater Standard — petrol.
- 6 Seater Standard — petrol.
- 5 Seater AC — petrol.
- 5 Seater AC CNG — factory-fitted S-CNG.

Ambulance, Ambulance Shell, Cargo, Cargo AC and Tour commercial configurations are excluded from this passenger-car workqueue. They must not be merged into passenger variants.

## Powertrain and seating

All passenger variants use the 1197 cc K12N 1.2-litre Advanced K-Series Dual Jet, Dual VVT engine with a 5-speed manual gearbox. Petrol output is 60.5 kW / 82.2 PS and 105.5 Nm. CNG output is 52.7 kW / 71.7 PS and 95 Nm. The 5 Seater AC CNG variant is the only passenger CNG configuration in the current official matrix. The 5-seat and 6-seat labels are retained as exact configurations.

## Price basis

The official price page exposes four passenger variant cards with Book Now actions and a stated waiting period of 2+ months. Displayed ex-showroom starting amounts differ by city:

| Passenger variant | Delhi page | Latur city page |
|---|---:|---:|
| 5 Seater Standard | ₹5,23,400 | ₹5,28,400 |
| 6 Seater Standard | ₹5,49,900 | ₹5,54,900 |
| 5 Seater AC | ₹5,56,300 | ₹5,61,300 |
| 5 Seater AC CNG | ₹6,40,800 | ₹6,45,800 |

The previous normalized amounts match the Latur snapshot, but the original city scope was not retained. They are preserved as legacy observations and removed from city-agnostic normalized rows. The official page states invoice-date prices and schemes prevail and does not publish an effective date. Do not use one national amount without a defined city basis.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Eeco model page: https://www.marutisuzuki.com/arena/eeco
- Maruti Suzuki official Delhi-default Eeco passenger price page: https://www.marutisuzuki.com/arena/eeco/price
- Maruti Suzuki official Latur city price page: https://www.marutisuzuki.com/arena/eeco/price?city=latur
- Maruti Suzuki official Eeco passenger brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/eeco/document/EECO-Passenger-Brochure-Arena.pdf
- V3Cars October 2026 price revision, used only to distinguish passenger vs commercial catalogue scope: https://www.v3cars.com/news/oct-2026-maruti-suzuki-eeco-price-change
