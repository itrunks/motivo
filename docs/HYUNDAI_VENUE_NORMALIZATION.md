# Hyundai VENUE variant structure — evidence notes

Checked: 2026-11-06

## Normalized OEM matrix

`data/hyundai-venue-variant-structure.csv` contains 23 exact trim/powertrain/transmission combinations across 13 OEM trim labels from the Hyundai India features matrix.

- 1.2 l Kappa MPi petrol: 5-speed manual
- 1.0 l Kappa Turbo GDi petrol: 6-speed manual and 7-speed DCT
- 1.5 l U2 CRDi diesel: 6-speed manual and 6-speed automatic
- Body style: compact SUV
- Model year and price intentionally blank.

## Sources

- Official features/engine-trim matrix: https://www.hyundai.com/in/en/find-a-car/venue/features
- Official price page: https://www.hyundai.com/in/en/find-a-car/venue/price

The OEM matrix explicitly lists 13 trims: HX2, HX4, HX5, HX5+, HX5 Knight, HX6, HX6T, HX6T Knight, HX7, HX8, HX8 Knight, HX10 and HX10 Knight. The raw audit observation was incomplete and omitted some Knight trims; the matrix is retained as the more detailed current OEM source.

The official price page returned no individual variant price rows in the captured page content. It states a starting ex-showroom price of ₹7,99,900, but that model-level starting price is not copied into any variant row.

## Import limitations

The OEM price page explicitly says prices and variants may change without notice and asks buyers to confirm current details with a Hyundai dealer. No price effective date is provided. City-specific prices must be checked separately.

The source registry remains `review_required`; commercial reuse and redistribution are `unknown`. This is a factual normalization work product only, not an approved import manifest. No model year or variant price has been inferred.
