# India catalogue reconciliation checkpoint — 2026-11-08

## Status

**Blocked: master reconciliation cannot be executed from the files currently committed to the repository.**

This checkpoint follows completion of initial research documents for Aston Martin, Bentley, Ferrari and McLaren. The repository was inspected through the recursive Git tree for the current `main` branch.

## 1. Research artefacts confirmed in the repository

| Brand | Research file | Current checkpoint |
|---|---|---|
| Aston Martin | `research/india/aston-martin/brand-audit-2026-11-08.md` | Initial India-market research documented |
| Bentley | `research/india/bentley/brand-audit-2026-11-08.md` | Initial India-market research documented |
| BMW | `research/india/bmw/pending-models-audit-2026-11-08.md` | Pending model groups documented; brand-wide reconciliation still open |
| Ferrari | `research/india/ferrari/brand-audit-2026-11-08.md` | Initial India-market research documented |
| McLaren | `research/india/mclaren/brand-audit-2026-11-08.md` | Initial India-market research documented |

These files are research evidence, not a normalized master inventory. They cannot be treated as import-ready records without exact model-year/variant normalization, source provenance, rights review and field-level validation.

## 2. Repository inventory inspection

The recursive Git tree on `main` contains the five research artefacts above, `data/source-audit-template.csv`, and `docs/VEHICLE_CATALOGUE_ARCHITECTURE.md`.

The following expected reconciliation artefacts were **not found** in the committed tree at the time of inspection:

- Canonical India brand registry.
- Canonical model audit dataset.
- Canonical exact-variant audit dataset.
- Source registry populated with reviewed source records.
- Model/variant-to-source crosswalk.
- `validate_source_crosswalk.py` or an equivalent committed validation script.
- Reproducible validation output tied to a commit and dataset revision.

The source audit template is only a blank/example schema. It is not evidence of approved source rights.

## 3. Previously reported validation result — historical, not rerun

A validator output previously shared in the project conversation reported:

| Metric | Previously reported value |
|---|---:|
| Registry sources | 224 |
| Model audit rows | 251 |
| Variant audit rows | 251 |
| Crosswalk rows | 502 |
| Missing/invalid mappings | 2 |
| Rights-approved sources | 0 |
| Production import approved | No |

The two errors were reported as:
1. Two audit rows missing from the crosswalk.
2. Two unexpected crosswalk rows.

**Important:** this is a historical result from 2026-11-06. The validator and its input datasets are not present in the currently inspected repository tree, so this report does not claim to have rerun or independently reproduced those counts.

## 4. Reconciliation decisions

1. Keep the four completed brand audits as research documents only.
2. Do not infer a canonical brand/model/variant ID from a folder name or display name.
3. Do not create substitute source records or crosswalk rows to make row counts balance.
4. Preserve the two previously reported mapping discrepancies until the original audit rows and crosswalk are available.
5. Keep source-rights status unapproved. Publicly accessible web pages do not automatically grant commercial reuse or redistribution rights.
6. Keep Firestore rules closed and do not import or publish any of these records.

## 5. Required inputs to unblock the next validation pass

Recover or commit the exact files used for the earlier validator run:

- Source registry dataset (224 rows).
- Model audit dataset (251 rows).
- Variant audit dataset (251 rows).
- Crosswalk dataset (502 rows).
- Validator script and its dependency/runtime instructions.
- The exact commit or revision from which the 2026-11-06 result was generated.

Once available, the next pass must:
1. Re-run the validator without changing source data.
2. Print the exact two missing audit-row identifiers and two unexpected crosswalk-row identifiers.
3. Trace each discrepancy to its source row and intended canonical mapping.
4. Correct only mappings supported by evidence.
5. Re-run until missing/invalid mappings and structural errors are zero.
6. Separately review licence/terms for every source before setting any rights-approved flag.
7. Produce a versioned reconciliation report and obtain explicit approval before any production import.

## 6. Production gate

**Production import remains blocked.** No Firebase write or publication was performed by this checkpoint. This is consistent with the catalogue architecture: verified provenance, acceptable reuse rights, normalized exact variants, validation and a review/publish step are prerequisites.
