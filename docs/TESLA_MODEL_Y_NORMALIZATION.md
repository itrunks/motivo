# Tesla Model Y India normalization

Checked: 2026-11-06

## Deliverables

- `data/tesla-model-y-variant-structure.csv`: two current India retail configurations.
- `data/tesla-model-y-price-observations.csv`: official base ex-showroom prices plus separate Tesla inventory displayed totals.

## Current India lineup

Tesla India's official website lists two current Model Y configurations:

- Model Y Premium RWD: single rear motor, rear-wheel drive, 5 seats, 500 km WLTP range.
- Model Y L Premium AWD: dual-motor all-wheel drive, 6 seats, 681 km WLTP range.

Both use automatic electric drive. The long-wheelbase L is a distinct 6-seat body/drive configuration. Tesla's India product page does not expose battery capacity or motor power/torque figures in the captured official specifications; those fields are deliberately blank rather than filled with third-party estimates.

The older Long Range Premium RWD (661 km, ₹67.89 lakh) was discontinued in May 2026 and is not included in the current lineup.

## Price evidence and basis separation

Tesla's official configurator currently displays:
- Premium RWD: ₹50,89,000 ex-showroom base vehicle price.
- Model Y L Premium AWD: ₹61,99,000 ex-showroom base vehicle price.

Tesla's official new-inventory page also displayed configuration-specific totals:
- Premium RWD Stealth Grey: ₹52,02,460.
- Premium RWD Pearl White: ₹53,94,360.
- Model Y L Premium AWD inventory: ₹63,23,560 to ₹66,06,360 across the captured inventory options.

The inventory totals are not the same price basis as the ex-showroom base vehicle prices. They may include paint, interior or other configuration/transaction charges. The exact paint/interior mapping for the Model Y L low/high totals was not captured, so the file retains them as range observations and does not invent a trim mapping.

## Performance caveat

Autocar's May 2026 reporting estimates the Premium RWD motor at 299 hp and 420 Nm and the Model Y L at approximately 514 hp and 590 Nm; Tesla does not publish those India power/torque figures in the captured official page. These estimates are documented here but are not populated as normalized official fields.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. This is staging normalization only. No Firestore write or public catalogue publication has been performed.

## Sources

- Tesla India Model Y product page: https://www.tesla.com/en_in/modely
- Tesla India configurator and base prices: https://www.tesla.com/en_in/modely/design?redirect=no
- Tesla India new inventory: https://www.tesla.com/en_in/inventory/new/my
- Tesla India Model Y L announcement and specifications: https://www.tesla.com/event/modelyl-cfg
- Autocar India, May 29 2026 Model Y Premium RWD lineup update: https://www.autocarindia.com/car-news/tesla-model-y-premium-rwd-variant-price-revised-to-rs-5089-lakh-439830
- Autocar India, October 17 2026 Model Y L powertrain update: https://www.autocarindia.com/car-news/tesla-model-y-l-powertrain-upgrade-brings-performance-boost-441075
