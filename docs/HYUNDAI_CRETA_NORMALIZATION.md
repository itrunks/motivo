# Hyundai CRETA variant normalization — evidence notes

Checked: 2026-11-06

## Scope

The companion CSV `data/hyundai-creta-variant-normalization.csv` contains 38 exact price-table rows transcribed from Hyundai Motor India's CRETA price page:

- 22 petrol rows
- 16 diesel rows
- 3 engine families: 1.5 l MPi petrol, 1.5 l Turbo GDi petrol, 1.5 l U2 CRDi diesel
- 4 transmission labels: 6-speed manual, IVT, 6-speed automatic, 7-speed DCT
- Body style: SUV
- Model year: intentionally blank because the cited price page does not state a model year.

## Primary OEM evidence

- Price and exact row labels: https://www.hyundai.com/in/en/find-a-car/creta/price
- Official CRETA brochure: https://www.hyundai.com/content/dam/hyundai/in/en/data/brochure/creta.pdf
- Official CRETA features/engine-trim matrix: https://www.hyundai.com/in/en/find-a-car/creta/features

The price page identifies its prices as ex-showroom. The individual rows explicitly state engine family, fuel and transmission shorthand; the brochure resolves the transmission shorthand as 6MT/IVT, 6MT/6AT and 7DCT respectively. The official find-a-car catalogue identifies CRETA as an SUV.

## Deliberate limitations

- The price page does not state an effective date for the displayed price table. `source_checked_at` is the retrieval date, not a price-effective date.
- The page offers city-specific price links and explains that prices vary by city. The generic India page values must not be treated as a confirmed Tiruchirappalli/Chennai dealer quotation.
- The price table contains 38 powertrain-specific rows. The official features matrix is a separate equipment applicability matrix and has a narrower/different trim presentation. Do not collapse the two sources into one variant count or invent mappings where the matrix does not show them.
- Model year remains blank. No model year is inferred from the page's current availability or retrieval date.
- No claim is made that these facts may be commercially reused or redistributed. The source registry remains `review_required`, with commercial reuse and redistribution both `unknown`.
- This file is a factual research/normalization work product, not an approved import manifest. It must not pass the source-approval gate or be written to Firestore staging until the source rights are explicitly reviewed and approved.

## Review required before import

1. Confirm current city-specific prices and their effective date with the OEM configurator or dealer.
2. Resolve any trim naming or equipment-matrix discrepancies against the live configurator.
3. Obtain documented commercial reuse and redistribution permission, or replace the source with an appropriately licensed dataset.
4. Keep any later year/model-year field empty unless the OEM explicitly supplies it.
