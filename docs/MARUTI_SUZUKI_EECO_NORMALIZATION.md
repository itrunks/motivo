# Maruti Suzuki Eeco passenger-variant normalization

Checked: 2026-11-06

## Deliverable

- `data/maruti-suzuki-eeco-passenger-variant-normalization.csv`: four current passenger configurations with official ex-showroom prices.

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

Official Maruti Suzuki price page observations, ex-showroom:
- 5 Seater Standard ₹5,28,400
- 6 Seater Standard ₹5,54,900
- 5 Seater AC ₹5,61,300
- 5 Seater AC CNG ₹6,45,800

The official price page states invoice-date prices and schemes prevail. These are ex-showroom prices, not on-road quotes.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Maruti Suzuki official Eeco model page: https://www.marutisuzuki.com/arena/eeco
- Maruti Suzuki official Eeco passenger price page: https://www.marutisuzuki.com/arena/eeco/price
- Maruti Suzuki official Eeco passenger brochure: https://www.marutisuzuki.com/content/dam/msil/arena/in/en/assets/cars/eeco/document/EECO-Passenger-Brochure-Arena.pdf
- V3Cars October 2026 price revision, used only to distinguish passenger vs commercial catalogue scope: https://www.v3cars.com/news/oct-2026-maruti-suzuki-eeco-price-change
