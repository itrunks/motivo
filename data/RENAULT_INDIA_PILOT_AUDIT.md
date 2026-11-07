# Renault India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.renault.co.in/

## Official current catalogue snapshot

Renault India's official homepage currently promotes four current passenger-car families:
- Duster
- Triber
- Kiger
- Kwid

The homepage also separately promotes the Duster strong-hybrid E-Tech 160 powertrain. This is a powertrain/variant family under Duster, not a separate vehicle model.

The OEM press-release index lists the new Duster launch in March 2026, Triber 100PS expansion in September 2026, and current 2026 price/variant updates for Kwid and Kiger. The homepage price observations are:
- Duster turbo petrol: from ₹10,49,000
- Duster strong hybrid E-Tech 160: from ₹16,99,000
- Triber: from ₹5,80,875
- Kiger: from ₹5,81,000
- Kwid: from ₹4,52,900

These are model/powertrain starting prices, not a complete variant-price ledger.

## Model and variant audit matrix

| Model | Official powertrain / grade evidence | Exact current variant price status |
|---|---|---|
| Duster | Turbo TCe 100: 999cc, 100PS, 166Nm, 6MT; 3 versions: Authentic, Evolution, Adventure. Turbo TCe 160: 1333cc, 163PS, 280Nm, 6MT or 6-speed DCT; 5 versions: Evolution, Adventure, Techno+, Iconic, Iconic Launch Edition. Strong hybrid E-Tech 160: 1789cc, 160PS, 205Nm, 8-speed DHT; 3 versions: Evolution, Techno, Emotion. | Official pre-configurator gives powertrain-specific starting prices only: ₹10,49,000; ₹12,99,000; ₹16,99,000. Full trim-by-trim price cards not captured |
| Triber | Petrol; 2026 official update; TCe 100PS family announced 2026-09-28. | Homepage starts ₹5,80,875; exact grade/transmission matrix and trim prices not captured |
| Kiger | Petrol naturally aspirated and turbo ranges; official 2026-06-23 release confirms four new variants across Turbo and NA powertrains. | Homepage starts ₹5,81,000; turbo range starts ₹7,93,000; exact current grade matrix/prices not captured |
| Kwid | Petrol hatchback; 2026-07-03 official release says fully loaded Climber variant now at ₹4.99 lakh. | Homepage starts ₹4,52,900; exact current grade matrix/prices not captured |

## Dated OEM evidence captured

### Duster — current 2026 range

Official Renault Duster pre-configurator lists three powertrains and their version names:
- Turbo TCe 100: Authentic, Evolution, Adventure; starts ₹10,49,000.
- Turbo TCe 160: Evolution, Adventure, Techno+, Iconic, Iconic Launch Edition; starts ₹12,99,000.
- Strong hybrid E-Tech 160: Evolution, Techno, Emotion; starts ₹16,99,000.

Do not combine the 3 powertrain variant lists into one undifferentiated grade list. Price starts are per powertrain family; they are not prices for every listed version.

### Triber 100PS — 2026-09-28

Official press release announces expansion of the Triber family with the TCe 100PS engine. Keep this as a current powertrain/variant-family update and verify exact transmission and grade mapping against the current official configurator before import.

### Kiger — 2026-06-23

Official press release confirms four new variants across turbo and naturally aspirated powertrains. The official homepage states Kiger turbo range starts at ₹7,93,000. Do not infer the four grade names from third-party catalogues.

### Kwid Climber — 2026-07-03

Official press release states the fully loaded Climber variant is now available at ₹4.99 lakh. Treat this as an edition/variant price observation only after confirming the official price type, effective date and current grade mapping from the linked release/configurator.

## Price evidence and import boundary

- Homepage and pre-configurator values are official model/powertrain starting-price observations.
- No full official trim-by-trim price matrix was captured in this pass.
- Do not turn starting prices into all-variant prices.
- Third-party November 2026 ranges can be used only as discovery leads, not official source-of-truth.
- On-road prices must be stored separately by city/state/RTO, with observation and effective dates.
- No Firestore import or publication performed.

## Current vs discontinued / upcoming boundary

- Current OEM-promoted passenger models: Duster, Triber, Kiger, Kwid.
- Legacy Duster model-year variants from 2019–2022 must not be mixed into the new 2026 Duster model-year family.
- Older Kiger and Triber 2019–2025/2021–2025 generations shown as discontinued in third-party catalogue listings are discovery clues only; the current OEM product pages and 2025 refresh/2026 updates determine the current variant boundary.
- Bigster and Bridger are future products in third-party launch trackers, not part of Renault's current official passenger-car homepage catalogue. Keep them in a separate future-product queue, not the current catalogue.
- Do not create a Renault EV record for India based on future concept/product announcements alone.

## Source register

Official:
- https://www.renault.co.in/ — current OEM product range and homepage starting prices.
- https://www.renault.co.in/press-and-media.html — official press release index, including dated 2026 model/variant updates.
- https://www.renault.co.in/cars/renault-duster/pre-configurator.html — official Duster powertrain, version names and starting prices.
- https://www.renault.co.in/cars/renault-duster.html — Duster product page.
- https://www.renault.co.in/cars/renault-kiger.html — Kiger product page.
- https://www.renault.co.in/cars/renault-triber.html — Triber product page.
- https://www.renault.co.in/cars/renault-kwid.html — Kwid product page.

Discovery only:
- https://www.autocarindia.com/cars/renault — model/variant discovery and upcoming-product cross-check.
- https://www.cardekho.com/cars/Renault — November 2026 model-level ranges and discontinued-model discovery.

This is a source-audit workpaper, not an approved import manifest.
