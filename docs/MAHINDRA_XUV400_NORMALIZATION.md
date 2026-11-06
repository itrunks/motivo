# Mahindra XUV400 current selector observation

Checked: 2026-11-06

## Deliverable

- `data/mahindra-xuv400-current-selector-observation.csv`: one current OEM selector card captured with the corresponding 2024 OEM Pro-range powertrain family evidence.

## Current selector result

Mahindra's current online selector renders only one card: `EL PRO ST 39.4KW 7.2KW`, at ₹17,49,000 ex-showroom. The current selector therefore supports one current price observation, not proof that all historical XUV400 configurations remain orderable.

## Powertrain crosswalk and limitation

Mahindra's official 2024 Pro-range brochure describes EL Pro 39.4 kWh with a 7.2 kW AC charger, 110 kW / 150 PS, 310 Nm, front-wheel drive and shift-by-wire automatic transmission, with 456 km MIDC range. The current selector label adds the suffix `ST`; the captured page does not explain that suffix or explicitly confirm whether the 7.2 kW wallbox is included in the current quoted price. Keep the crosswalk provisional and obtain dealer confirmation before production import.

The same 2024 OEM release documented EC Pro 34.5 kWh / 3.3 kW and EL Pro 34.5 kWh / 7.2 kW variants, but those cards are absent from the current selector capture. Their historical launch prices are not treated as current prices.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. Current orderability and charger inclusion remain `dealer_confirmation_required`. No Firestore write or public catalogue publication has been performed.

## Sources

- Current Mahindra XUV400 selector: https://auto.mahindra.com/own-online/variant-selection?mgc=X400
- Mahindra official XUV400 Pro-range brochure: https://auto.mahindra.com/on/demandware.static/-/Sites-amc-Library/default/dw4dc915da/mahindraelectricimages/images/xuv400images/XUV400ProRangeBrochure.pdf
- Mahindra January 11, 2024 Pro-range launch announcement: https://www.mahindra.com/news-room/press-release/en/mahindra-introduces-allelectric-xuv400-pro-range-starting-at-an-introductory-price-of-inr-1549-lakh
