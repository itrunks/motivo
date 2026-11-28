# Motivo master roadmap

Owner direction (2026-11-28): full India passenger-car catalogue before public launch; no pending audits. Firebase access only after stages 1–5. This roadmap supersedes earlier launch sequencing.

| Stage | Gate | Status |
|---|---|---|
| 1 | Current OEM brand/model/exact variant inventory reconciled | In progress |
| 2 | All audits resolved; unknown fields explicitly documented | Pending |
| 3 | Source approvals, normalized production catalogue, validation | Pending |
| 4 | Website search, filters, recommendations, comparison and local QA | Pending |
| 5 | Ads code disabled by default, privacy, terms, consent, hosting eligibility | Pending |
| 6 | Firebase import, API, rules, backup and rollback | On hold |
| 7 | End-to-end QA and owner acceptance; zero release blockers | Pending |
| 8 | Public launch and monitoring; ads only after approval | Pending |

## Stage 1 baseline

Recovered historical inventory: 251 model rows, 35 brands. This is not a current OEM-verified inventory. Historical model status: 60 complete, 33 partial, 157 pending, 1 blocked. Exact SKU count remains unknown.

| Brand | Historical model rows | OEM reconciliation |
|---|---:|---|
| Maruti Suzuki | 17 | Pending |
| Hyundai | 14 | Pending |
| Mahindra | 13 | Pending |
| Kia | 9 | Pending |
| Toyota | 13 | Pending |
| MG Motor | 10 | Pending |
| Tata Motors | 16 | Pending |
| MINI | 5 | Pending |
| Force Motors | 1 | Pending |
| Tesla | 1 | Pending |
| VinFast | 3 | Pending |
| Audi | 9 | Pending |
| BMW | 22 | Pending |
| BYD | 4 | Pending |
| Citroën | 5 | Pending |
| Honda | 5 | Pending |
| Jeep | 4 | Pending |
| Lamborghini | 3 | Pending |
| Land Rover | 7 | Pending |
| Lexus | 5 | Pending |
| Maserati | 7 | Pending |
| Aston Martin | 4 | Pending |
| Bentley | 5 | Pending |
| Ferrari | 7 | Pending |
| McLaren | 3 | Pending |
| Mercedes-Benz | 24 | Pending |
| Nissan | 3 | Pending |
| Porsche | 5 | Pending |
| Renault | 4 | Pending |
| Rolls-Royce | 4 | Pending |
| Škoda | 6 | Pending |
| Volkswagen | 4 | Pending |
| Volvo Cars | 5 | Pending |
| Isuzu | 1 | Pending |
| Lotus | 3 | Pending |

No Firebase writes or production publication authorized. Do not mark a brand complete without dated OEM lineup evidence and explicit disposition of each historical model.
