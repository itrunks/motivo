# Lexus India — pilot catalogue audit

**Audit date:** 2026-11-06  
**Market:** India (IN)  
**Status:** Current model discovery and reported OEM price-list snapshot; direct OEM price-page extraction still required  
**Scope:** India retail catalogue only; no Firestore import or publication

## Executive result

The current India candidate lineup consists of five model families: **ES, NX, RX, LX and LM**. The ES family has two distinct powertrains: ES 350h strong hybrid and ES 500e battery electric. The remaining current families are NX 350h, RX 350h / RX 500h, LX 500d diesel and LM 350h hybrid.

A 26 October 2026 report reproduces 13 variant prices and says they were taken from the Lexus India price list. However, the reported page's own "From" price wording does not identify the city or unambiguously state whether every amount is ex-showroom. Treat these as **reported OEM price-list observations**, not fully verified first-party price rows, until the actual Lexus India price list is directly captured with its terms.

## Current model family inventory

| Model family | India product / powertrain | Current-catalogue evidence | Disposition |
|---|---|---|---|
| ES | ES 350h strong hybrid | Launched in India 2026-07-15; Exquisite and Luxury trims reported | Current candidate |
| ES | ES 500e battery electric | Official dealer site and current secondary reporting list it | Current candidate; verify current OEM page and exact trim |
| NX | NX 350h strong hybrid | Official dealer site lists Exquisite, Luxury, Overtrail and F Sport | Current candidate |
| RX | RX 350h strong hybrid | Official dealer site lists Exquisite | Current candidate |
| RX | RX 500h turbo hybrid | Official dealer site lists F Sport+ | Current candidate |
| LX | LX 500d diesel | Official dealer site lists Urban and Overtrail | Current candidate |
| LM | LM 350h hybrid MPV | Official dealer site lists 7-Seater VIP and 4-Seater Ultra Luxury | Current candidate |

**Canonical identity rules**
- ES 350h and ES 500e are powertrain variants/products under the ES family, not unrelated model families.
- RX 350h and RX 500h are distinct powertrain/grade combinations under RX.
- NX grade labels must remain exact; do not normalize Overtrail to a generic off-road package unless OEM data supports that.
- LM 7-Seater VIP and 4-Seater Ultra Luxury are distinct seating/cabin configurations.
- LX 500d Urban and Overtrail are distinct grades; preserve diesel fuel mapping.
- Do not count upcoming NX facelift as current until the official India launch/order page confirms availability.

## Variant price observations — reported from Lexus India price list

A report published 2026-10-26 says its prices were checked against the Lexus India price-list page at 01:00 IST on 2026-10-26. The article describes the values as "From" prices, but notes that the page does not clearly specify the city or whether all values are ex-showroom. These observations are therefore staged as **source-reported candidates only**.

| Model | Variant | Reported amount (INR) | Powertrain | Classification |
|---|---|---:|---|---|
| ES 350h | Exquisite | 66,10,000 | Petrol-electric strong hybrid | Reported OEM list observation |
| ES 350h | Luxury | 71,80,000 | Petrol-electric strong hybrid | Reported OEM list observation |
| NX 350h | Exquisite | 67,93,000 | Petrol-electric hybrid | Reported OEM list observation |
| NX 350h | Overtrail | 71,79,000 | Petrol-electric hybrid | Reported OEM list observation |
| NX 350h | Luxury | 72,70,000 | Petrol-electric hybrid | Reported OEM list observation |
| NX 350h | F Sport | 74,88,000 | Petrol-electric hybrid | Reported OEM list observation |
| RX 350h | Exquisite | 90,44,000 | Petrol-electric hybrid | Reported OEM list observation; audio-system caveat |
| RX 350h | Exquisite (Mark Levinson audio) | 93,87,000 | Petrol-electric hybrid | Reported OEM list observation; separate audio equipment |
| RX 500h | F Sport+ | 1,11,00,000 | Turbo petrol-electric hybrid | Reported OEM list observation |
| ES 500e | Luxury | 91,20,000 | Battery electric | Reported OEM list observation |
| LM 350h | 7-Seater VIP | 2,27,00,000 | Petrol-electric hybrid | Reported OEM list observation |
| LM 350h | 4-Seater Ultra Luxury | 2,84,00,000 | Petrol-electric hybrid | Reported OEM list observation |
| LX 500d | Urban | 2,91,00,000 | Diesel | Reported OEM list observation |
| LX 500d | Overtrail | 3,03,00,000 | Diesel | Reported OEM list observation |

**Count note:** The 26 October report describes 13 variants but its body text includes the RX 350h Mark Levinson audio alternative in addition to the 13-row headline list. Keep the Mark Levinson audio option as a separate equipment/price observation only if the OEM price page confirms it is a separately orderable grade or priced option. Do not silently increase the canonical variant count.

## Price discrepancies and source caveats

1. **ES 500e:** An Autocar India article from 2026-07-15 reports ₹89.99 lakh ex-showroom. A 2026-10-26 report of the Lexus India price-list page gives ₹91.20 lakh. A Lexus Mumbai dealer site also displays ₹91.20 lakh. Keep both dated observations; do not overwrite without confirming the official effective date.
2. **NX:** Lexus Mumbai's dealer website displays NX 350h Exquisite ₹67.59 lakh, Luxury ₹72.33 lakh, Overtrail ₹71.43 lakh and F-Sport ₹74.50 lakh. The October report of the Lexus India list gives ₹67.93 lakh, ₹72.70 lakh, ₹71.79 lakh and ₹74.88 lakh respectively. Preserve source and observation dates separately; do not blend or average them.
3. **RX:** Lexus Mumbai dealer website displays RX 350h Exquisite ₹89.99 lakh and RX 500h F-Sport+ ₹1.10 crore. The October report gives ₹90.44 lakh and ₹1.11 crore, plus an RX 350h Mark Levinson alternative ₹93.87 lakh.
4. **LM:** Lexus Mumbai dealer website displays ₹2.1969 crore and ₹2.7462 crore; the October report gives ₹2.27 crore and ₹2.84 crore.
5. **LX:** Lexus Mumbai dealer website displays ₹2.814 crore and ₹2.9266 crore; the October report gives ₹2.91 crore and ₹3.03 crore.

The dealer-site prices and reported national price-list values are materially different. Do not treat a dealer microsite as a national price authority, and do not assume the October values are ex-showroom where the source does not clearly state the basis.

## Lifecycle and exclusions

- **Previous-generation ES:** Treat older ES 300h / prior-generation ES pricing as historical, not current, after the 2026 new-generation ES introduction.
- **LS and LC 500h:** Third-party portals report these as discontinued; current India lineup pages reviewed for this audit do not include them. Keep out of current retail catalogue.
- **Older RX and LX model-year entries:** Do not import old price rows or historical engine/grade combinations based on aggregator listings.
- **NX facelift:** Autocar reports an expected late-2026 facelift with an estimated price range. This is upcoming/estimated evidence, not current India orderability. Do not create a current sellable variant until OEM launch and booking evidence exists.
- **LBX, UX, GX, IS and GS:** Third-party expected-launch pages are not proof of India launch. Keep as unverified future candidates only; do not import.
- Do not infer fuel type from a generic "hybrid" label. Preserve OEM powertrain names (350h, 500h, 500e, 500d) and map to normalized fuel/powertrain only when confirmed by an OEM brochure.

## Source register

| Source | URL | Use | Confidence |
|---|---|---|---|
| Lexus India official site | https://www.lexusindia.co.in/ | Primary source for India product pages, brochures and price-list entry point; direct price-page extraction still pending | High when directly captured |
| Lexus NX official brochure hosted on Lexus India | https://www.lexusindia.co.in/wp-content/uploads/2025/08/NX-Brochure_edited-22-08-25.pdf | OEM grade/equipment evidence for NX; brochure snapshot is not current pricing | High for brochure content |
| Lexus Mumbai dealer site | https://lexusmumbai.co.in/ | Dealer-displayed grade names and "From" prices; regional dealer source only | Medium; not national price authority |
| Autocar India — new ES 350h launch (2026-07-15) | https://www.autocarindia.com/car-news/new-lexus-es-350h-launched-at-rs-6610-lakh-440224 | Dated ES 350h trim, powertrain and launch price evidence | Medium-high secondary reporting |
| Autocar India — Lexus ES details (2026-09-01) | https://www.autocarindia.com/auto-features-amp/all-you-need-to-know-about-lexus-es-440993 | ES 350h / ES 500e powertrain and price cross-check | Medium-high secondary reporting |
| Dalimss News — Lexus India price list (2026-10-26) | https://dalimss.news/articles/lexus-price-list-india-rs-66-10-lakh-to-rs-3-03-crore-oct-2026 | Dated reproduction of 13 variant prices said to be sourced from Lexus India price list | Medium; verify directly with OEM |
| Autocar India Lexus listing | https://www.autocarindia.com/cars/lexus | Current model and lifecycle cross-check | Medium; not price authority |
| CarDekho Lexus listing | https://www.cardekho.com/cars/Lexus | Secondary model and price discovery | Medium; not price authority |
| ZigWheels Lexus listing | https://www.zigwheels.com/lexus-cars/ | Secondary model and price discovery | Medium; not price authority |

## Staging decision

**Do not import the price rows as production variant prices yet.**

Safe workpaper evidence:
1. Five current model families and their candidate powertrain products.
2. Dated 26 October reported OEM price-list observations, explicitly labelled as secondary reproduction with uncertain price basis.
3. Lexus Mumbai dealer price observations, retained separately as regional dealer data.
4. Dated ES 350h launch prices and ES 500e price discrepancy.
5. Lifecycle exclusion queue for LS, LC 500h, previous-generation ES and unlaunched future candidates.

Required before production staging:
1. Capture the actual Lexus India national price-list page and its price-basis disclaimer.
2. Verify the 13 reported variant prices against the live OEM page or a dated OEM PDF.
3. Resolve ES 500e ₹89.99 lakh vs ₹91.20 lakh with effective dates.
4. Resolve NX/RX/LM/LX dealer-vs-national price discrepancies.
5. Confirm whether RX Mark Levinson is a separate priced grade or an option package.
6. Capture model-year, powertrain, transmission, drivetrain and seating configuration from current OEM brochures.
7. Collect city-specific on-road prices only from sources with approved reuse rights.

No Firestore import, provider API credit usage, or publication was performed.
