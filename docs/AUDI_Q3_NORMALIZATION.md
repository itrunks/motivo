# Audi Q3 India normalization

Checked: 2026-11-06

## Deliverable

- `data/audi-q3-model-level-observation.csv`: current new-generation India product-page status and missing variant/price fields.

## Current official model status

Audi India currently promotes the **New Audi Q3** on a dedicated page with Register Interest and Pre-book Now actions. The captured current India page does not publish a named trim/variant matrix, India-specific engine or drivetrain combinations, or a numeric current ex-showroom price.

Audi India's official Price Reckoner is live and notes that ex-showroom prices exclude TCS, but its embedded price data does not render in the captured page text. No numeric price is copied from third-party listings.

## Historical source kept separate

The older Q3 brochure describes a 2.0L TFSI quattro configuration with 190 hp and 320 Nm. It is a legacy-generation source and is not applied to the new Q3 product page. The new India generation requires its own official specification sheet and grade/price release.

## Status

Partial. Current model identity and pre-booking status are verified, but exact India variant structure and numeric price are not yet published in the captured official sources. Keep the legacy Q3 technical specification separate until Audi confirms it applies to the new India model.

## Rights and import gate

Source reuse and redistribution remain `review_required` / `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- Audi India New Q3 page: https://www.audi.in/en/models/q3/q3-suv/
- Audi India all-models listing: https://www.audi.in/en/models/
- Audi India Price Reckoner: https://www.audi.in/en/customer-area/price-reckoner/
- Older Q3 brochure (historical only): https://www.audi.in/dam/nemo/in/Downloads/Q3/Q3%20Brochure%20Final%20Small.pdf
