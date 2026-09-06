# Comprehensive Backlink Tracker — Zazie Productions

Exact-name census of every public appearance of the artist names **Zazie Productions** and
**Zazie Kanwar-Torge**: backlinks, media features, stream credits, engine indexes, mirror
syndication and archival records. Research baseline through **2026-09-05**.

## The two deliverables (read these)

| PDF | What it is |
|---|---|
| **`Zazie_Master_Directory_COLOUR_CODED.pdf`** | The directory itself — 720 catalogued links in 14 colour-coded media-type sections, tier-ranked (A–D), every URL clickable, with per-category stats and the engine-endpoint appendix. |
| **`Zazie_Research_Annex_COLOUR_CODED.pdf`** | The research record behind it — 12 colour-coded sections + endpoint appendix: census rules, 11 engine/discovery passes (audits, evidence ledgers, query inventories, access logs), the quarantine register with its safety charter, the 2026 Accomplishment Register → public-link map, listen-link appearance table, seed-index coverage, and every tool/query template used. |

The CSV/JSON registries below are the **source of truth**; the PDFs are their organised,
permanent reading edition. No narrative Markdown reports are kept — everything readable
lives in the two PDFs.

## Data layout

```
sources/            original inputs (link-dump PDF, media-master PDF, 2026 register DOCX)
data/master/        consolidated_directory.json (canonical: 720 records + 73 endpoints),
                    master_index.csv, listen_links.csv, register_link_map.csv
data/research/      engine_audit.csv (per-pass engine access results)
registry/           per-pass machine registers (CSV/JSON only):
                    magazine_zine_features/ · regional_alt_engine_pass_2026-09-05/ ·
                    maxdepth_pass_2026-09-05/ · phase3_editorial_literary/ ·
                    spam_scraper_syndication_lowtrust_2026-09-05/ ·
                    web_presence_expansion/ · seed/
scripts/            ingest_all_links.py · build_master_directory_pdf.py ·
                    build_research_annex_pdf.py
```

## Regenerate

```bash
python scripts/ingest_all_links.py            # rebuilds data/master/* from the registries
python scripts/build_master_directory_pdf.py  # rebuilds the Master Directory PDF
python scripts/build_research_annex_pdf.py    # rebuilds the Research Annex PDF
```

## Reading the colour code

Media type (Master volume): red = press/editorial · purple = publications & recognition ·
magenta = film/festivals · indigo = podcasts/broadcasts · blue = profiles/catalogs ·
pink = discography · sky = streaming · teal = lyrics DBs · orange = compilations ·
green = official properties · search-index teal · mirror slate · spam grey.
Trust tiers everywhere: **A** dark green · **B** blue · **C** amber · **D** dark red.
Status chips: green = worked/live · amber = partial · red = blocked/broken ·
grey = unreachable/unchecked · slate = lead or archive-only · brown = DO-NOT-OPEN.
