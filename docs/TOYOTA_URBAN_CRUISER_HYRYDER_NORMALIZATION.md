# Toyota Urban Cruiser Hyryder variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/toyota-urban-cruiser-hyryder-variant-structure.csv`: 13 current configurator variants across CNG, Neodrive and strong-hybrid powertrains.
- `data/toyota-urban-cruiser-hyryder-price-observations.csv`: 11 numeric configurator price observations. E MT and V AT AWD have no numeric value in the captured output and remain unpriced.

## Current configurator variants

The current Toyota configurator identifies 13 variants (8 Neodrive, 2 CNG and 3 Hybrid):
- Neodrive petrol: E MT 2WD; S MT 2WD; S AT 2WD; G(O) MT 2WD; G(O) AT 2WD; V MT 2WD; V AT 2WD; V AT AWD.
- E-CNG: S MT 2WD; G MT 2WD.
- Strong hybrid: S e-Drive 2WD; G(O) e-Drive 2WD; V e-Drive 2WD.

All are 5-seater SUVs. Neodrive and CNG use the 1.5 l K-series petrol engine family; CNG is bi-fuel Petrol+CNG. Neodrive offers 5MT/6AT, with AWD on the V AT AWD configuration. The hybrid uses a 1.5 l petrol engine with lithium-ion hybrid battery and e-Drive transmission. The Toyota current specification page confirms 1462 cc Neodrive/CNG, 1490 cc hybrid, 177.6 V lithium-ion hybrid battery, 115.56 PS total hybrid output and 141 Nm hybrid motor torque.

## Price observations

The configurator displays numeric values for 11 variants: S MT Neodrive ₹12.82 lakh; S MT CNG ₹13.71 lakh; S AT Neodrive ₹14.17 lakh; G(O) MT Neodrive ₹14.87 lakh; G MT CNG ₹15.72 lakh; G(O) AT Neodrive ₹16.18 lakh; V MT Neodrive ₹16.42 lakh; V AT 2WD Neodrive ₹17.67 lakh; Hybrid S ₹17.18 lakh; Hybrid G(O) ₹19.24 lakh; Hybrid V ₹19.99 lakh. V AT AWD is shown with price N/A; E MT has no numeric price in the extracted list. Toyota's model page separately shows a starting ex-showroom price of ₹11,31,000; it is not assigned to E MT because the exact trim mapping is not explicit in that summary.

Configurator price basis and effective date are not stated in the extracted result. Treat these as price observations only; confirm current dealer quote before customer quotation.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. No Firestore write or publication has been performed.

## Sources

- Toyota online configurator / exact 13 variants and displayed prices: https://www.toyotabharat.com/virtual-showroom/urbancruiserhyryder.html
- Toyota current model specifications: https://tweb.toyotabharat.com/urban-cruiser-hyryder.html
- Toyota showroom powertrain and grade overview: https://www.toyotabharat.com/showroom/urbancruiser-hyryder/index.html
- Toyota 2025 specification brochure: https://www.toyotabharat.com/documents/brochures/e-brochure-urbancruiser-hyryder-spec.pdf
