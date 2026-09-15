# 🎨 Comprehensive Backlink Tracker — Zazie Productions

**Exact-name census** of every public appearance of the artist names **Zazie Productions** and
**Zazie Kanwar-Torge** — backlinks, media features, stream credits, engine indexes, mirror
syndication and archival records. Every link is **tier-ranked**, **status-checked** and
**colour-coded**: *the colour is the meaning.*

📅 Research baseline through **2026-09-05** · extended by three user-submitted passes through **2026-09-15**

[![records 754](https://img.shields.io/badge/records-754-0b6e4f?style=flat-square)](data/master/consolidated_directory.json)
[![engine endpoints 73](https://img.shields.io/badge/engine%20endpoints-73-1a73e8?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)
[![media types 14](https://img.shields.io/badge/media%20types-14-7b1fa2?style=flat-square)](Zazie_Master_Directory_COLOUR_CODED.pdf)
[![baseline 2026-09-05](https://img.shields.io/badge/baseline-2026--09--05-b06000?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)
[![extended 2026-09-15](https://img.shields.io/badge/extended-2026--09--15-188038?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)

> [!TIP]
> ### 🧭 The 30-second map
> - **Just want to read the links?** → open 📕 [`Zazie_Master_Directory_COLOUR_CODED.pdf`](Zazie_Master_Directory_COLOUR_CODED.pdf) — 754 clickable links in 14 colour-coded sections.
> - **Want the method and the evidence?** → open 📓 [`Zazie_Research_Annex_COLOUR_CODED.pdf`](Zazie_Research_Annex_COLOUR_CODED.pdf) — 15 colour-coded research sections + appendix.
> - **Want to use the data?** → `data/master/` (CSV/JSON — the source of truth).
> - **Colour question?** → jump to [Reading the colour code](#reading-the-colour-code): the legend below uses the **exact hex values** from both PDFs.

## 📑 Contents

- [🧭 Where to start](#where-to-start)
- [📦 The two deliverables](#the-two-deliverables)
- [🔢 At a glance](#at-a-glance)
- [🎨 Reading the colour code](#reading-the-colour-code)
- [🗂️ Repository map](#repository-map)
- [♻️ Regenerate](#regenerate)
- [✅ Ground rules](#ground-rules)

## 🧭 Where to start

Pick your goal — each row is a complete route, no archaeology needed:

| If you want to… | Start with | Then |
|---|---|---|
| 📖 Get the big picture | The 30-second map above | [At a glance](#at-a-glance) |
| 🔗 Read every catalogued link | 📕 Master Directory PDF | [The colour code](#reading-the-colour-code) |
| 🔬 See how each link was found & judged | 📓 Research Annex PDF | §1 — Census rules, colour code & method |
| 🧮 Crunch the data (spreadsheet / code) | `data/master/` — `master_index.csv`, `consolidated_directory.json` | [Repository map](#repository-map) |
| 🕵️ Trace one link back to the pass that found it | `registry/<pass>/` ledgers + `source_access_log.csv` | Annex §2–8, §12–15 |
| 🛡️ Avoid the quarantined, low-trust links | ⛔ Tier D rows — printed last, in the quarantine section | Annex §8 — Low-Trust Quarantine Register |
| 🏗️ Rebuild the PDFs from the data | [Regenerate](#regenerate) | `scripts/` |

## 📦 The two deliverables

| | Volume | What it is |
|---|---|---|
| <span style="background-color:#37424e; color:#ffffff;"> MASTER </span> | 📕 [`Zazie_Master_Directory_COLOUR_CODED.pdf`](Zazie_Master_Directory_COLOUR_CODED.pdf) | **The directory itself** — 754 catalogued links in 14 colour-coded media-type sections, tier-ranked A–D, every URL clickable, per-category stats and the engine-endpoint appendix. |
| <span style="background-color:#0b5d8f; color:#ffffff;"> ANNEX </span> | 📓 [`Zazie_Research_Annex_COLOUR_CODED.pdf`](Zazie_Research_Annex_COLOUR_CODED.pdf) | **The research record behind it** — 15 colour-coded sections + endpoint appendix: census rules, 15 engine/discovery passes & submitted batches (audits, evidence ledgers, query inventories, access logs), the quarantine register with its safety charter, the 2026 Accomplishment Register → public-link map, listen-link appearance table, seed-index coverage, and every tool/query template used. |

### 🗺️ Inside the Research Annex — every section has its own banner colour

| § | Section | Banner colour |
|---|---|---|
| <span style="background-color:#37424e; color:#ffffff;"> 1 </span> | 📐 Census Rules, Colour Code & Method | `#37424e` |
| <span style="background-color:#1a73e8; color:#ffffff;"> 2 </span> | 🔎 Search-Engine Audit — Passes 1–8 | `#1a73e8` |
| <span style="background-color:#0f9d8f; color:#ffffff;"> 3 </span> | 🌐 Regional & Alt-Engine Sweep — Pass 9 (2026-09-05) | `#0f9d8f` |
| <span style="background-color:#5e35b1; color:#ffffff;"> 4 </span> | 🕳️ Maximum-Depth Research Pass (2026-09-05) | `#5e35b1` |
| <span style="background-color:#c2185b; color:#ffffff;"> 5 </span> | 📰 Magazine & Zine Features Registry (2026-09-05) | `#c2185b` |
| <span style="background-color:#7b1fa2; color:#ffffff;"> 6 </span> | 🖋️ Editorial & Literary Evidence Ledger — Phase 3 | `#7b1fa2` |
| <span style="background-color:#00796b; color:#ffffff;"> 7 </span> | 🕸️ Web-Presence Blind-Spot Expansion — Pass 11 (2026-09-05) | `#00796b` |
| <span style="background-color:#616161; color:#ffffff;"> 8 </span> | ⛔ Low-Trust Quarantine Register — Pass 10 (2026-09-05) | `#616161` |
| <span style="background-color:#e8710a; color:#ffffff;"> 9 </span> | 🗺️ Accomplishment Register → Link Map | `#e8710a` |
| <span style="background-color:#039be5; color:#ffffff;"> 10 </span> | 🎧 Listen Links — Every Compilation Appearance | `#039be5` |
| <span style="background-color:#2e7d32; color:#ffffff;"> 11 </span> | 🌱 Seed Index & Domain Coverage | `#2e7d32` |
| <span style="background-color:#8a6d3b; color:#ffffff;"> 12 </span> | 🧾 Query Inventories & Source-Access Logs | `#8a6d3b` |
| <span style="background-color:#6d4c41; color:#ffffff;"> 13 </span> | 📥 User-Submitted Intake Pass (2026-09-15) | `#6d4c41` |
| <span style="background-color:#d84315; color:#ffffff;"> 14 </span> | 📤 Second User-Supplied Backlink Pass (2026-09-15) | `#d84315` |
| <span style="background-color:#ad1457; color:#ffffff;"> 15 </span> | 💠 User-Submitted Link Batch — third batch (2026-09-15) | `#ad1457` |
| <span style="background-color:#0b5d8f; color:#ffffff;"> A </span> | 🧰 Appendix — Tools, Endpoints & Query Templates | `#0b5d8f` |

## 🔢 At a glance

| | Figure | What it counts |
|---|---|---|
| <span style="background-color:#0b6e4f; color:#ffffff;"> 754 </span> | catalogued links | every public exact-name appearance (all records, all tiers) |
| <span style="background-color:#1a73e8; color:#ffffff;"> 73 </span> | engine endpoints | discovery/search endpoints, printed in Annex appendix A |
| <span style="background-color:#7b1fa2; color:#ffffff;"> 14 </span> | media types | the colour-coded sections of the Master Directory |
| <span style="background-color:#37424e; color:#ffffff;"> 15 + 1 </span> | Annex sections | research sections 1–15 plus the tools/endpoint appendix |
| <span style="background-color:#1a73e8; color:#ffffff;"> 15 </span> | passes & batches | engine/discovery passes and user-submitted batches documented in the Annex |
| <span style="background-color:#039be5; color:#ffffff;"> 61 </span> | listen links | compilation appearances — 32 confirmed · 28 label pages · 1 unresolved |
| <span style="background-color:#e8710a; color:#ffffff;"> 56 </span> | register links | 2026 Accomplishment Register entries mapped to public links (of 203 register records) |
| <span style="background-color:#7b1fa2; color:#ffffff;"> 10 </span> | pass registries | machine passes under `registry/` |
| <span style="background-color:#b06000; color:#ffffff;"> 3 </span> | source files | original inputs under `sources/` |

## 🎨 Reading the colour code

> [!NOTE]
> The hex values below are the **exact palette** of both PDFs — a single colour system defined once in `scripts/build_master_directory_pdf.py` and `scripts/build_research_annex_pdf.py`.
> **Same colour = same meaning** in the PDFs, in the data, and in this README.

### 1 · 🏷️ Media types — the 14 sections of the Master Directory

In PDF order. The bar shows each section's share of the 754 records.

| # | Swatch | Section (PDF order) | Hex | Count | Share of 754 |
|---|---|---|---|---|---|
| 1 | <span style="background-color:#d93025;">&nbsp;&nbsp;&nbsp;</span> | 📰 Press & Editorial | `#d93025` | 98 | ██████ |
| 2 | <span style="background-color:#7b1fa2;">&nbsp;&nbsp;&nbsp;</span> | 🏆 Publications & Recognition | `#7b1fa2` | 28 | ██ |
| 3 | <span style="background-color:#d81b60;">&nbsp;&nbsp;&nbsp;</span> | 🎬 Film, Festivals & Exhibitions | `#d81b60` | 61 | ████ |
| 4 | <span style="background-color:#3949ab;">&nbsp;&nbsp;&nbsp;</span> | 🎙️ Podcasts & Broadcasts | `#3949ab` | 7 | █ |
| 5 | <span style="background-color:#1a73e8;">&nbsp;&nbsp;&nbsp;</span> | 📇 Profiles & Catalogs | `#1a73e8` | 107 | ███████ |
| 6 | <span style="background-color:#c2185b;">&nbsp;&nbsp;&nbsp;</span> | 💿 Music Discography | `#c2185b` | 1 | █ |
| 7 | <span style="background-color:#039be5;">&nbsp;&nbsp;&nbsp;</span> | 🎧 Streaming & Music Platforms | `#039be5` | 59 | ████ |
| 8 | <span style="background-color:#00897b;">&nbsp;&nbsp;&nbsp;</span> | 📖 Lyrics & Music Databases | `#00897b` | 1 | █ |
| 9 | <span style="background-color:#e8710a;">&nbsp;&nbsp;&nbsp;</span> | 📦 Music Compilations | `#e8710a` | 162 | ██████████ |
| 10 | <span style="background-color:#2e7d32;">&nbsp;&nbsp;&nbsp;</span> | 🏛️ Official Properties & Channels | `#2e7d32` | 51 | ███ |
| 11 | <span style="background-color:#188038;">&nbsp;&nbsp;&nbsp;</span> | 👥 Community, Wiki & Fan Indexes | `#188038` | 54 | ███ |
| 12 | <span style="background-color:#0f9d8f;">&nbsp;&nbsp;&nbsp;</span> | 🔍 Search-Engine Index | `#0f9d8f` | 3 | █ |
| 13 | <span style="background-color:#607d8b;">&nbsp;&nbsp;&nbsp;</span> | 🪞 Video Mirror / Backlink Sites | `#607d8b` | 5 | █ |
| 14 | <span style="background-color:#616161;">&nbsp;&nbsp;&nbsp;</span> | ⛔ Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust | `#616161` | 117 | ███████ |

### 2 · 🥇 Trust tiers — evidence quality, on every row

A = strongest → D = weakest (quarantined). Full tier definitions: **Annex §1**.

| Tier | Chip | Hex | Row tint | What it means |
|---|---|---|---|---|
| <span style="background-color:#0b6e4f; color:#ffffff;"> A </span> | <span style="background-color:#eaf6ef; color:#0b6e4f;"> A </span> | `#0b6e4f` | `#eaf6ef` | Strongest evidence — verified exact-name appearance |
| <span style="background-color:#1a73e8; color:#ffffff;"> B </span> | <span style="background-color:#eaf1fc; color:#1a73e8;"> B </span> | `#1a73e8` | `#eaf1fc` | Solid, well-supported |
| <span style="background-color:#b06000; color:#ffffff;"> C </span> | <span style="background-color:#fdf4e5; color:#b06000;"> C </span> | `#b06000` | `#fdf4e5` | Partial or thinner support |
| <span style="background-color:#8c1d18; color:#ffffff;"> D </span> | <span style="background-color:#fbeceb; color:#8c1d18;"> D </span> | `#8c1d18` | `#fbeceb` | Low-trust — quarantined rows, printed last |

### 3 · 🚦 Status chips — what happened when the URL was checked

| Chip | Hex | Meaning |
|---|---|---|
| <span style="background-color:#188038; color:#ffffff;"> LIVE </span> | `#188038` | worked / live |
| <span style="background-color:#0f9d58; color:#ffffff;"> IDX-OK </span> | `#0f9d58` | verified in the search-index |
| <span style="background-color:#b06000; color:#ffffff;"> PARTIAL </span> | `#b06000` (olive variant `#5f8b3a`) | partially verified |
| <span style="background-color:#7b8794; color:#ffffff;"> UNCHECKED </span> | `#7b8794` | unreachable / unchecked |
| <span style="background-color:#b3261e; color:#ffffff;"> BROKEN </span> | `#b3261e` | blocked / broken |
| <span style="background-color:#607d8b; color:#ffffff;"> LEAD </span> | `#607d8b` | lead, or archive-only |
| <span style="background-color:#8a6d3b; color:#ffffff;"> DO-NOT-OPEN </span> | `#8a6d3b` | safety — quarantined, do not open |

### 4 · 🌡️ Credibility heat — the per-record score cell in the Master rows

| Score | Cell colour |
|---|---|
| ≥ 80 | <span style="background-color:#bfe8cf; color:#0b5d2b;">&nbsp;&nbsp;high&nbsp;&nbsp;</span> `#bfe8cf` |
| 62–79 | <span style="background-color:#e4f3d6; color:#33691e;">&nbsp;&nbsp;good&nbsp;&nbsp;</span> `#e4f3d6` |
| 45–61 | <span style="background-color:#fff2cc; color:#8a6d3b;">&nbsp;&nbsp;middling&nbsp;&nbsp;</span> `#fff2cc` |
| 28–44 | <span style="background-color:#ffe0b2; color:#a04000;">&nbsp;&nbsp;weak&nbsp;&nbsp;</span> `#ffe0b2` |
| &lt; 28 | <span style="background-color:#fbd6d3; color:#8c1d18;">&nbsp;&nbsp;poor&nbsp;&nbsp;</span> `#fbd6d3` |

## 🗂️ Repository map

**One-line data flow** — every file sits somewhere on this pipeline:

```
📥 raw inputs ──▶ 📚 per-pass evidence ──▶ ⚙️ build scripts ──▶ 📊 canonical data ──▶ 📕📓 colour-coded PDFs
 (sources/)        (registry/)             (scripts/)           (data/master/)        (repo root — reading editions)
```

```
📦 Comprehensive Backlink Tracker
├── 📕 Zazie_Master_Directory_COLOUR_CODED.pdf      ← READ: the directory (754 links, 14 sections)
├── 📓 Zazie_Research_Annex_COLOUR_CODED.pdf        ← READ: the method (14 sections + appendix)
├── 📥 sources/                                     ← raw original inputs (3 files)
│   ├── Random_Zazie_Productions_links.pdf          raw link dump
│   ├── Zazie_Media_Master.pdf                      133 verified URL-level records (+leads)
│   └── Zazie_2026_Accomplishment_Register_Maximal_Edition.docx
├── 📊 data/master/                                 ← CANONICAL (source of truth)
│   ├── consolidated_directory.json                 754 records + 73 engine endpoints
│   ├── master_index.csv                            canonical index, one row per URL
│   ├── listen_links.csv                            61 compilation appearances
│   └── register_link_map.csv                       Accomplishment Register → public links
├── 🧪 data/research/
│   └── engine_audit.csv                            passes 1–8 engine access results
├── 📚 registry/                                    ← per-pass machine registers (CSV/JSON only)
│   ├── seed/                                       starting-point domains & unique URLs
│   ├── magazine_zine_features/                     pass 5: feature directory & ledgers
│   ├── regional_alt_engine_pass_2026-09-05/        pass 9: engine access matrix
│   ├── maxdepth_pass_2026-09-05/                   max-depth discoveries & reverified URLs
│   ├── spam_scraper_syndication_lowtrust_2026-09-05/  pass 10: quarantine ledgers
│   ├── phase3_editorial_literary/                  editorial & literary evidence ledger
│   ├── web_presence_expansion/                     pass 11: backlinks, discoveries, entity map
│   ├── user_submitted_pass_2026-09-15/             intake ledgers & duplicate map
│   ├── user_supplied_backlinks_2026-09-15/          second backlink pass: submission ledger & access log
│   └── user_submitted_batch_2026-09-15/             third batch: submission ledger, adjacent leads, access log
└── ⚙️ scripts/                                     ← rebuild everything
    ├── ingest_all_links.py                         registries → data/master/*
    ├── build_master_directory_pdf.py               → Master Directory PDF
    └── build_research_annex_pdf.py                 → Research Annex PDF
```

| Path | Colour | Role in the pipeline |
|---|---|---|
| `sources/` | <span style="background-color:#b06000; color:#ffffff;"> raw </span> | original inputs — never edited downstream |
| `registry/` | <span style="background-color:#7b1fa2; color:#ffffff;"> evidence </span> | per-pass machine registers — the proof trail |
| `scripts/` | <span style="background-color:#e8710a; color:#ffffff;"> build </span> | rebuilds the canonical data and both PDFs |
| `data/master/` | <span style="background-color:#0b6e4f; color:#ffffff;"> canonical </span> | **source of truth** — 754 records + 73 endpoints |
| `data/research/` | <span style="background-color:#0f9d8f; color:#ffffff;"> audit </span> | engine access results for passes 1–8 |
| root PDFs | <span style="background-color:#37424e; color:#ffffff;"> reading </span> | the organised, permanent reading editions |

## ♻️ Regenerate

Requirements: Python 3 + `reportlab` (and `pymupdf`) — a local `.venv/` is git-ignored.

| Step | Run | Result |
|---|---|---|
| <span style="background-color:#e8710a; color:#ffffff;"> 1 </span> | `python scripts/ingest_all_links.py` | rebuilds `data/master/*` from all the registries |
| <span style="background-color:#37424e; color:#ffffff;"> 2 </span> | `python scripts/build_master_directory_pdf.py` | rebuilds the 📕 Master Directory PDF |
| <span style="background-color:#0b5d8f; color:#ffffff;"> 3 </span> | `python scripts/build_research_annex_pdf.py` | rebuilds the 📓 Research Annex PDF |

> [!TIP]
> Run steps 1 → 2 → 3 in order. Page-number caches (`data/master/.pdf_pagemap.json`, `.annex_pagemap.json`) are regenerated on every build and are git-ignored.

## ✅ Ground rules

> [!IMPORTANT]
> **Source of truth:** the CSV/JSON files in `data/` and `registry/` are the source of truth. The two PDFs are their organised, **permanent reading edition** — never edit the PDFs by hand; regenerate them.

> [!NOTE]
> **No narrative Markdown reports are kept** — everything readable lives in the two PDFs. If it isn't in `data/`, `registry/`, `sources/` or `scripts/`, it belongs in one of the PDFs.

> [!TIP]
> **One palette, everywhere.** Every colour in the PDFs is defined once in `scripts/build_master_directory_pdf.py` / `scripts/build_research_annex_pdf.py`. The legend in this README is that same palette — so if the PDFs change colour, this page changes with them.
