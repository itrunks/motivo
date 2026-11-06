# Maruti Suzuki Baleno 2026 normalization

Checked: 2026-11-06

## Deliverables

- `data/maruti-suzuki-baleno-variant-structure.csv`: 13 current petrol/S-CNG trim and transmission combinations.
- `data/maruti-suzuki-baleno-price-observations.csv`: 13 current official NEXA ex-showroom price observations.

## Current variant matrix

NEXA's current Baleno price page lists 13 combinations across Sigma, Delta, Zeta, Alpha and Alpha (O):
- Petrol: Sigma MT; Delta, Zeta, Alpha and Alpha (O) in MT and AGS.
- S-CNG: Delta and Zeta in MT and AGS.

This current 13-variant matrix includes CNG AGS configurations that were not in the September 10 launch price table. The current official NEXA selector is used for the structure and current price list; older petrol-only trim matrices are not carried forward.

## Powertrain

The new 1197 cc three-cylinder Z12E engine produces 61 kW / 82.93 PS and 112.4 Nm in petrol mode. The S-CNG version produces 51.3 kW / 69.75 PS and 101.8 Nm in CNG mode. Both petrol and CNG variants are offered with 5-speed manual or 5-speed AGS, as listed on the current NEXA page. All variants are front-wheel-drive, 5-seat premium hatchbacks.

## Price basis

Current official NEXA price page values, ex-showroom:
- Sigma MT ₹5,98,900
- Delta MT ₹6,99,900; Delta AGS ₹7,49,900
- Delta CNG MT ₹7,92,400; Delta CNG + AGS ₹8,32,400
- Zeta MT ₹7,99,900; Zeta AGS ₹8,49,900
- Zeta CNG MT ₹8,92,400; Zeta CNG + AGS ₹9,32,400
- Alpha MT ₹9,09,900; Alpha AGS ₹9,59,900
- Alpha (O) MT ₹9,49,900; Alpha (O) AGS ₹9,99,000

The September 5, 2026 launch release initially announced ₹6,09,900 as the starting price, while the current NEXA page displays ₹5,98,900 for Sigma MT. These are retained as dated observations; the current NEXA price page is the current catalogue value, and invoice-date dealer pricing prevails.

## Rights and import gate

Every row remains `review_required`; commercial reuse and redistribution remain `unknown`. No Firestore write or public catalogue publication has been performed.

## Sources

- NEXA official Baleno variant and price page: https://www.nexaexperience.com/baleno/price
- NEXA official Baleno product page: https://www.nexaexperience.com/baleno
- Maruti Suzuki official September 2026 launch release and engine specifications: https://www.marutisuzuki.com/corporate/media/press-releases/2026/september/dare-to-go-glam-with-the-stunning-new-baleno-designed-for-dynamic-achievers
- Autocar India, 10 September 2026 full price list: https://www.autocarindia.com/car-news/2026-baleno-full-price-list-revealed-440706
- Autocar India, 22 October 2026 variant feature breakdown: https://www.autocarindia.com/auto-features/2026-maruti-baleno-variants-and-features-explained-441020
