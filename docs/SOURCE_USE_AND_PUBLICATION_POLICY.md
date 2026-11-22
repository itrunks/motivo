# Source use and publication policy

Last reviewed: 2026-11-22
Status: **Research may continue; publication is evidence- and use-review-gated**

## Purpose

Motivo is a free, open-source community vehicle-research platform. It is not a paid dealer-lead marketplace. This policy separates (a) researching vehicle facts and writing original structured records from (b) copying or redistributing a publisher's protected expression or dataset.

Free access and an open-source code licence do not automatically grant permission to reuse third-party website content. This policy is an operational risk-control framework, not legal advice.

## Four separate questions for every source

1. **Factual reference use** — Can a researcher consult this source and independently author a factual record in Motivo's own schema and wording?
2. **Expressive-content reuse** — May Motivo copy the source's prose, brochure tables, photographs, diagrams, logos, videos, page layout or PDF pages?
3. **Automated access / extraction** — Do the website terms, robots instructions, technical controls or licence restrict bots, scraping, bulk extraction, caching or database reuse?
4. **Attribution and freshness** — What source URL, publisher, observed date, effective/model year and verification date must accompany the fact?

These permissions are not interchangeable. Approval for one does not imply approval for the others.

## Allowed workflow while research is in progress

- Read and manually inspect public pages for research where access terms permit it.
- Record audit findings in private research notes with exact source URLs and checked dates.
- Write concise facts in Motivo's own wording and normalized fields; do not reproduce distinctive OEM phrasing or copy complete source tables.
- Cross-check important fields against another independent source where possible.
- Preserve unknowns and conflicts explicitly; never infer a trim-level feature from a model-level marketing claim.
- Link users to the OEM page or brochure instead of hosting a copied OEM document.
- Keep source evidence and publication approval separate. Research notes are not automatically production data.

If a source's terms expressly prohibit manual copying, extraction or the intended use, do not treat paraphrasing as a workaround. Keep it as a research lead only until the source-specific use is reviewed or a different suitable source is found.

## Content that must not be reused without a suitable licence or written permission

- OEM brochure/page images, photographs, diagrams, videos and artwork;
- copied brochure tables or substantial compilations;
- copied prose, marketing descriptions or distinctive wording;
- OEM logos, trademarks used as branding, or page designs;
- complete downloaded brochures or source PDFs hosted by Motivo;
- bulk scraped datasets or cached copies where terms or law do not permit that use.

A source link and attribution are not a substitute for permission to reproduce protected content.

## Source registry and publication gate

The source registry now tracks factual-reference approval separately from expressive-content permissions:

- `factual_use_basis=independently_authored_facts`
- `factual_use_review=pending|approved|rejected`
- `factual_use_notes`

A published catalogue record must cite a source whose factual-reference review is explicitly approved. This approval must be made source-by-source after reviewing its current terms, intended use, access method and the proposed field. It is not granted automatically to OEM sources, and it does not permit copying images, tables, prose, PDFs or databases.

The existing `commercial_reuse_allowed` and `redistribution_allowed` fields remain authoritative for workflows that reproduce or redistribute source content. They must not be changed to `yes` merely because Motivo is free or open source.

Until factual-reference review is complete, continue research in private audit notes, but do not publish normalized catalogue records from that source. If no acceptable source is available, leave the value unavailable or find a separately licensed/independent source.

## Practical examples

| Activity | Treatment |
|---|---|
| Read an OEM feature page and note a factual claim in private audit notes | Research only; check terms/access restrictions |
| Independently author a normalized fact after source-specific review | Eligible for publication only when factual-use review is approved |
| Copy an OEM feature table into Motivo | Requires permission/licence for the table/compilation |
| Reuse brochure images or PDF pages | Requires permission/licence |
| Scrape a site that prohibits automated extraction | Do not scrape; use a permitted alternative |
| Link to the OEM brochure without hosting it | Preferred over republishing the brochure |

## Legal context

Copyright generally protects original expression rather than bare facts, but compilations, databases, tables and the manner of presentation may attract protection. Contractual website terms and restrictions on automated access are separate considerations. The fact that Motivo is free and open source does not by itself resolve those issues. Obtain Indian IP/legal review for uncertain or high-volume publication decisions.
