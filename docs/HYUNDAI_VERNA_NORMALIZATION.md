# Hyundai VERNA variant normalization — evidence notes

Checked: 2026-11-06

## Deliverables

- `data/hyundai-verna-variant-structure.csv`: 12 exact trim/powertrain/transmission combinations from Hyundai India's current engine & trim matrix.
- `data/hyundai-verna-variant-price-normalization.csv`: 12 official 2026 launch-price observations from Hyundai Motor India's 9 March 2026 press release.

## Current OEM structure

Hyundai's official features matrix lists HX 2, HX 4, HX 6, HX 6+, HX 8 and HX 10.

1.5 l MPi Petrol:
- HX 2: 6-speed manual
- HX 4: 6-speed manual
- HX 6: 6-speed manual / IVT
- HX 6+: 6-speed manual / IVT
- HX 8: 6-speed manual / IVT
- HX 10: IVT

1.5 l Turbo GDi Petrol:
- HX 8: 6-speed manual / 7-speed DCT
- HX 10: 7-speed DCT

The structure file therefore contains 12 exact combinations. Fuel is recorded as Petrol for both engine families. Hyundai's official model listing classifies Verna as a Sedan. Model year remains blank because the cited feature and price sources do not state a catalogue model-year field.

## Price evidence

Hyundai Motor India's press release dated 9 March 2026 publishes 12 ex-showroom INR observations:
- MPi manual: HX 2 ₹10,98,400; HX 4 ₹12,25,400; HX 6 ₹13,19,400; HX 6+ ₹13,81,400; HX 8 ₹14,88,400.
- MPi IVT: HX 6 ₹14,40,400; HX 6+ ₹15,02,400; HX 8 ₹16,09,400; HX 10 ₹17,15,400.
- Turbo GDi manual: HX 8 ₹16,28,400.
- Turbo GDi DCT: HX 8 ₹17,62,400; HX 10 ₹18,25,400.

Observed launch-price range: ₹10,98,400–₹18,25,400. The current official price page shows a starting price of ₹10,99,200 and notes that prices vary by variant and engine, may change without notice, and require dealer confirmation. This differs from the March launch price table, so the two sources are not silently merged. The CSV retains the dated launch observations; current city-specific prices remain unverified and must not be quoted as current dealer prices.

## Reconciliation and gaps

The current feature matrix and launch price table align on the 12 structure combinations. The price page's starting figure (₹10,99,200) differs from the dated launch announcement's HX 2 figure (₹10,98,400); this is explicitly retained as a source-version/price-change discrepancy. No effective date beyond the 9 March 2026 announcement date is inferred.

## Rights and import gate

Source status remains `review_required`; commercial reuse and redistribution remain `unknown`. Public OEM pages are not proof of commercial reuse permission. These CSVs are research/normalization outputs, not approved import manifests. No Firestore write or publication has been performed.

## Sources

- Features matrix: https://www.hyundai.com/in/en/find-a-car/verna/features
- Current price page: https://www.hyundai.com/in/en/find-a-car/verna/price
- 9 March 2026 launch announcement: https://www.hyundai.com/in/en/hyundai-story/media-center/press-release/hmil-launches-mid-size-sedan-segment-new-hyundai-verna
- Official model listing / body type: https://www.hyundai.com/in/en/find-a-car
