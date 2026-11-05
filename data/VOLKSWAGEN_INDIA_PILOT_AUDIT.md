# Volkswagen India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.volkswagen.co.in/en/models.html

## Official catalogue snapshot

Volkswagen India's official models page currently exposes six product cards:
- New Virtus — marked "Coming soon"
- The new Taigun
- Tayron
- Virtus Sport
- Virtus Chrome
- Golf GTI

The official homepage card carousel repeats the same six entries. The official product page labels Virtus Sport and Virtus Chrome as separate cards with starting prices; they are Virtus editions/grade families, not distinct vehicle nameplates. Keep the canonical model entity as Virtus and store Sport/Chrome as variant/edition names.

The official range page also has a filter summary with body types and engine/transmission counts, but the page's disclaimer states international cars/models may be shown for representation and equipment may not currently be offered in India. Use India-specific product pages and brochures for model and trim validation.

## Audit matrix

| Canonical model | Official India status | Powertrain / variant evidence | Price status |
|---|---|---|---|
| Virtus | Current Virtus Sport and Virtus Chrome cards; New Virtus refresh marked Coming Soon | Existing Virtus editions are separate variant/edition groups; refresh must be a separate model-year applicability boundary | Official starting prices: Chrome ₹10,70,900; Sport ₹14,34,900. These are edition starting prices, not complete trim matrix |
| Taigun | The new Taigun product page and 2026 launch release | 1.0 TSI 85kW/178Nm with 6MT or 8-speed AQ300 automatic; 1.5 TSI 110kW/250Nm with 7-speed DSG. Current trims: Comfortline, Highline, Highline Plus, Topline, GT Line, GT Chrome, GT Sport (brochure wording to verify exact GT grouping) | Official page starts ₹10,99,900; full current trim-by-transmission price list not captured |
| Tayron | Official India product card; starts ₹41,99,000 | India-specific grade/seat layout/powertrain and booking status need OEM brochure/booking confirmation | Starting price only |
| Golf GTI | Official India product card; ex-showroom ₹50,90,900 | Imported performance hatchback; exact current allocation and any limited-volume booking status need confirmation | Official price observation captured |
| Tiguan | Not displayed on the current official six-card India model page in this pass | Older brochure/third-party references are not sufficient to classify it as currently orderable | Hold outside current OEM catalogue until official current product/price page is found |
| New Virtus | Officially marked Coming Soon | Future refresh, not current orderable until booking/launch confirmation | No current variant prices |

## Dated OEM evidence captured

### New Taigun — 2026-04-09

Volkswagen India announced the new Taigun on 2026-04-09 and opened pre-bookings. The official release confirms:
- 1.0-litre TSI: 85 kW / 178 Nm, paired with 6-speed manual or 8-speed AQ300 automatic.
- 1.5-litre TSI: 110 kW / 250 Nm, paired with 7-speed DSG and Active Cylinder Technology.
- Current refreshed range: Comfortline, Highline, Highline Plus, Topline and GT trims.
- New Taigun page starting price: ₹10,99,900.

The OEM brochure names the design/trim families as Chrome (Comfortline, Highline, Highline Plus, Topline) and Sport (GT Line, GT Plus). The press release uses GT-line, GT Chrome and GT Sport labels in describing variant-exclusive details. Preserve exact source wording and flag the nomenclature mismatch for brochure/configurator reconciliation; do not silently normalize the GT labels.

Official sources:
- https://www.volkswagen.co.in/en/discover-volkswagen/news/news-and-updates/the-new-volkswagen-taigun-is-here-welcome-to-driving.html
- https://www.volkswagen.co.in/idhub/content/dam/onehub_pkw/importers/in/models/new-taigun/the-new-taigun-brochure.pdf

### Virtus editions and refresh

The current official model page lists:
- Virtus Chrome from ₹10,70,900
- Virtus Sport from ₹14,34,900
- New Virtus marked Coming Soon

Do not treat the refreshed New Virtus as already orderable. Keep existing Virtus edition prices tied to the current official page observation date until the OEM publishes a dated full price list and refresh launch/booking status.

### Tayron

The official India model page lists Tayron from ₹41,99,000. Exact India grade/variant, seating configuration, powertrain and current booking details were not fully captured from official source content in this pass. Third-party pages describe multiple seat/grade configurations, but those remain discovery only.

### Golf GTI

The official India model page lists Golf GTI with an ex-showroom price of ₹50,90,900. Preserve it as a performance hatchback and verify limited allocation/orderability before assuming continuous stock.

## Price evidence and import boundary

Official homepage/model-page observations:
- New Taigun: from ₹10,99,900 (price type should be confirmed from the page's linked footnote/price flow before final ledger acceptance).
- Tayron: from ₹41,99,000 (same price-type/footnote check required).
- Virtus Chrome: from ₹10,70,900.
- Virtus Sport: from ₹14,34,900.
- Golf GTI: ex-showroom ₹50,90,900.

No full official variant-level price matrix was captured in this pass. Do not convert these model/edition starting prices into all-variant prices. No city-wise on-road prices captured. Keep ex-showroom and on-road observations separate and attach city/state/RTO, observation date, effective date and source for on-road values.

## Current / future / discontinued boundary

- Current official product cards: Taigun, Tayron, Virtus Sport, Virtus Chrome, Golf GTI.
- New Virtus is explicitly marked Coming Soon and must remain outside the orderable current catalogue until launch/booking evidence.
- Virtus Sport and Virtus Chrome are editions under canonical Virtus, not independent model entities.
- Tiguan is not on the current official six-card range snapshot; hold until fresh OEM evidence supports orderability.
- Do not include discontinued Polo, Vento, Ameo, Passat or Jetta as current models.
- Do not import global ID.4 or other global EV models without a Volkswagen India launch/booking/price source.

## Source register

Official:
- https://www.volkswagen.co.in/en/models.html — current six-card model page and official starting prices.
- https://www.volkswagen.co.in/en.html — homepage range carousel and current product promotion.
- https://www.volkswagen.co.in/en/discover-volkswagen/news/news-and-updates/the-new-volkswagen-taigun-is-here-welcome-to-driving.html — new Taigun launch, powertrain and trim details, 2026-04-09.
- https://www.volkswagen.co.in/idhub/content/dam/onehub_pkw/importers/in/models/new-taigun/the-new-taigun-brochure.pdf — India-specific new Taigun brochure and variant-family naming.

Discovery only:
- https://www.autocarindia.com/cars/volkswagen — model and variant cross-check; not used as price authority.

No Firestore import or publication performed. This is a source-audit workpaper, not an approved import manifest. Exact OEM price observations still require source-reuse/licensing review before production import.
