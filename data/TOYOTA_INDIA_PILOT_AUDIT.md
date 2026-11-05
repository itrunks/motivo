# Toyota India current-model and source audit

Checked: 2026-11-06
Market: India
Primary source: https://www.toyotabharat.com/

## Official catalogue snapshot

Toyota Kirloskar Motor's official homepage currently exposes these product entries under Products / Discover the Toyota range:

- Glanza
- Urban Cruiser Taisor
- Rumion
- Urban Cruiser Hyryder
- Urban Cruiser Ebella
- Innova Crysta
- Innova Hycross
- Hilux
- Fortuner
- Legender
- Camry
- Vellfire
- Land Cruiser 300

These are **13 official catalogue entries**. Treat this as the OEM catalogue snapshot, not proof of current stock or orderability in every dealer/RTO market. Keep Toyota's model naming exactly as displayed; do not merge Urban Cruiser Taisor, Urban Cruiser Hyryder and Urban Cruiser Ebella.

## Audit matrix

| Official catalogue entry | Initial classification | Variant / orderability audit |
|---|---|---|
| Glanza | ICE hatchback | Verify current model-year, fuel and trim matrix from OEM price list/brochure |
| Urban Cruiser Taisor | ICE compact SUV | Verify current trims and powertrain combinations |
| Rumion | ICE MPV | Verify petrol/CNG and transmission/trim combinations |
| Urban Cruiser Hyryder | ICE SUV with petrol / strong-hybrid / CNG offerings to verify | Verify current trim and powertrain matrix |
| Urban Cruiser Ebella | Electric SUV | Newer EV entry; battery/trim and retail orderability need OEM confirmation |
| Innova Crysta | Diesel MPV | OEM press release dated 2026-11-05 confirms GX, GX+, VX and ZX grades; separate fleet LIMO offer is described below |
| Innova Hycross | Petrol / strong-hybrid MPV | Verify current grade and powertrain matrix |
| Hilux | Diesel pickup | Verify current grade / transmission |
| Fortuner | Diesel SUV | Verify current grades and 4x2 / 4x4 / transmission combinations |
| Legender | Premium Fortuner derivative / separately listed catalogue entry | Preserve separate OEM catalogue name; verify distinct current grade matrix |
| Camry | Hybrid sedan | Verify current model-year and grade |
| Vellfire | Hybrid luxury MPV | Verify current grade matrix |
| Land Cruiser 300 | Diesel luxury SUV | Verify current grade / drivetrain |

## Dated OEM evidence captured

### Innova Crysta and fleet LIMO (2026-11-05)

Toyota Kirloskar Motor's official press release dated 2026-11-05 announces the Innova Crysta LIMO Edition for fleet and commercial mobility customers, exclusively in GX-SLF grade. The release also says the regular Innova Crysta continues in four grades: GX, GX+, VX and ZX.

The release publishes these LIMO-specific ex-showroom prices:
- GX Fleet 7S: ₹19,95,000
- GX Fleet 8S: ₹19,99,000

Classification boundary:
- Keep the LIMO grades as fleet/commercial offer records, not ordinary retail trims by default.
- Do not treat the LIMO name as a new passenger-car model.
- The release says prices remain unchanged for the LIMO offer. This does not establish the complete current retail variant-price matrix for Innova Crysta.

Official source:
https://www.toyotabharat.com/news/2026/toyota-kirloskar-motor-introduces-innova-crysta-limo-a-dedicated-brand-for-fleet-customers.html

## Price evidence and import boundary

- Toyota's official homepage exposes a Price List entry point, but this pass did not capture a complete dated official variant-price file or city-wise on-road schedule.
- The two Innova Crysta LIMO ex-showroom values above are exact OEM-published special fleet offer observations; they must retain fleet classification and the 2026-11-05 source/effective context.
- Do not use third-party model-level ranges as variant prices.
- Do not infer current price from an older brochure or apply a flat price-hike percentage.
- Store ex-showroom and on-road as separate price types. On-road observations require city, state/RTO, effective date, observation date and source.
- No Firestore import or publication performed.

## Third-party discovery only

November 2026 snapshots from CarDekho, Autocar India, ZigWheels and CarWale can help identify candidate model/variant names and potential conflicts. Their model price ranges are not accepted as official OEM variant-price evidence. In particular, the Urban Cruiser Ebella's presence in the OEM catalogue should be retained even if third-party catalogues lag or classify its availability differently.

## Source register

Official:
- https://www.toyotabharat.com/ — current OEM catalogue snapshot, Price List and Brochure entry points.
- https://www.toyotabharat.com/news/2026/toyota-kirloskar-motor-introduces-innova-crysta-limo-a-dedicated-brand-for-fleet-customers.html — dated OEM announcement and exact LIMO fleet prices.

Discovery only:
- https://www.cardekho.com/toyota-cars
- https://www.autocarindia.com/cars/toyota/
- https://www.zigwheels.com/toyota-cars/
- https://www.carwale.com/toyota-cars/

This is a source-audit workpaper, not an approved import manifest.
