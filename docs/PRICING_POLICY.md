# Motivo pricing policy — India

Last reviewed: 2026-11-20
Status: **Ex-showroom only for the initial catalogue and closed beta**

## Decision

Motivo will collect and display **official variant-wise ex-showroom prices only** for the initial India catalogue and closed beta. Dealer-specific on-road quotations are out of scope for now.

Do not request dealer quotations, call multiple dealers, or attempt to standardise dealer quote bundles during catalogue research. Dealers can quote different insurance, registration/RTO, accessories, extended warranty, handling/logistics and optional packages. Discounts and exchange/corporate offers also vary by dealer, customer eligibility, city and date. Combining these into one purportedly comparable on-road number would be misleading and costly to maintain.

## Required ex-showroom price fields

For each exact variant and market:
- amount in INR;
- price type = `ex_showroom`;
- source URL and source publisher;
- source classification = `official` only when published by the OEM or an authorised official OEM price tool;
- effective/observed date;
- model year / exact variant mapping;
- last verified date.

Prefer OEM India product price selectors or official OEM price lists. Record the price exactly as published. If the official source does not expose a value or its variant mapping is ambiguous, leave the price unavailable; do not fill it from an unverified dealer message or a third-party page without a separately approved source policy.

## Explicit exclusions for now

- dealer on-road totals and dealer quotations;
- RTO/road tax and registration estimates;
- insurance quotes;
- extended warranty;
- accessories, kits and handling/logistics charges;
- dealer discounts, exchange bonuses, corporate offers and finance schemes;
- any bundled or negotiated amount.

Do not create estimated on-road prices by adding assumed taxes, insurance or charges to ex-showroom. Do not label ex-showroom as on-road.

The existing schema may retain future-compatible on-road fields, but no on-road records should be ingested or shown in this phase. A later product decision and a defensible source/methodology are required before enabling them.

## User-facing note

Where helpful, show a short note near the price:

> Ex-showroom price shown. On-road price varies by city, RTO, insurance and dealer-specific offers. Contact a nearby authorised dealer for an exact quotation.

This is an optional contextual hint, not a promise that Motivo has verified a dealer quotation. It may be omitted from screens where it adds clutter.

## Freshness and display

- Store the OEM source's observed date and effective date separately.
- Display the price as current only while it passes the configured freshness policy; otherwise label it as last-known / price needs rechecking.
- Show exact variant name and model year beside the price.
- If only a model starting price is available, label it as a starting price and never map it to every variant.
- If prices are not publicly available from an acceptable source, display "Price unavailable" rather than inventing or requesting a dealer quote.

## Source rights

A public OEM price page is not automatically licensed for commercial republication. Apply docs/SOURCE_USE_AND_PUBLICATION_POLICY.md. A price is a factual field, but its source-specific factual-reference use must still be reviewed before publication, especially where a site restricts extraction or reuse of price databases. Do not copy price-page layout, tables or other expressive content. Keep pending observations in private audit notes.
