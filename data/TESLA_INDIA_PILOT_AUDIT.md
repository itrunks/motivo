# Tesla India pilot audit

**Audit date:** 2026-11-06  
**Market:** India  
**Decision:** Active India retail brand. One canonical model family (Model Y) with two currently sold derivatives.

## Current India range

Tesla's India retail range is confirmed as:
- **Model Y Premium RWD** — five-seat electric SUV.
- **Model Y L Premium AWD** — six-seat, three-row electric SUV.

Treat Model Y L as a derivative/variant of the Model Y family unless Tesla's India catalogue assigns it a separate canonical model identity. Preserve seating, drivetrain, range and model-year attributes per exact derivative.

Model 3, Roadster, Model S, Model X and Cybertruck are not current India retail products based on the checked evidence; do not import aggregator launch estimates or speculative listing cards.

## Price evidence

| Derivative | Starting ex-showroom price | Evidence | Disposition |
|---|---:|---|---|
| Model Y Premium RWD | ₹50,89,000 | Tesla India official configurator (2026-05-29) | Official ex-showroom base vehicle price; separate from inventory totals. |
| Model Y L Premium AWD | ₹61,99,000 | Tesla India official configurator and Model Y L event page (2026-04-24) | Official ex-showroom base vehicle price; separate from inventory totals. |

No variant matrix beyond these two derivatives is accepted. Do not import EMI, down-payment, FSD option or charging prices as vehicle ex-showroom prices.

## Source register

- Tesla India official site: https://www.tesla.com/en_in
- Autocar India current Tesla India lineup and price snapshot: https://www.autocarindia.com/cars/tesla
- Autocar Professional current India sales/offer reporting: https://www.autocarpro.in/news/tesla-india-opens-roadster-reservations-adds-acceleration-boost-to-model-y-l-135307

## Import decision

Model Y family and both current derivatives are normalized from Tesla India OEM product and configurator endpoints. Official base ex-showroom prices and inventory displayed totals are stored separately. Battery capacity and motor power/torque remain blank where not published in the captured India sources. Source reuse terms remain unapproved; no Firestore write or public catalogue publication has been performed.
