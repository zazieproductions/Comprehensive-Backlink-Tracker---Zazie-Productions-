# 🎨 Comprehensive Backlink Tracker — Zazie Productions

**Exact-name census** of every public appearance of the artist names **Zazie Productions** and
**Zazie Kanwar-Torge** — backlinks, media features, stream credits, engine indexes, mirror
syndication and archival records. Every link is **tier-ranked**, **status-checked** and
**colour-coded**: *the colour is the meaning.*

📅 Research baseline through **2026-09-05** · extended by user-submitted intake passes through **2026-09-15**

[![records 727](https://img.shields.io/badge/records-727-0b6e4f?style=flat-square)](data/master/consolidated_directory.json)
[![engine endpoints 73](https://img.shields.io/badge/engine%20endpoints-73-1a73e8?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)
[![media types 14](https://img.shields.io/badge/media%20types-14-7b1fa2?style=flat-square)](Zazie_Master_Directory_COLOUR_CODED.pdf)
[![baseline 2026-09-05](https://img.shields.io/badge/baseline-2026--09--05-b06000?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)
[![extended 2026-09-15](https://img.shields.io/badge/extended-2026--09--15-188038?style=flat-square)](Zazie_Research_Annex_COLOUR_CODED.pdf)

> [!TIP]
> ### 🧭 The 30-second map
> - **Want one thing at a time — a commission, a compilation, an anthology, a film?** → 📕 Master Directory **PART I · Project sections**: 102 projects, every link about the same project side by side (its own page first, the scraped copies of it walled off last).
> - **Just want to read the links?** → open 📕 [`Zazie_Master_Directory_COLOUR_CODED.pdf`](Zazie_Master_Directory_COLOUR_CODED.pdf) — 727 clickable links: 102 project sections (PART I), 5 thematic reading paths (PART II), 14 colour-coded media-type sections (PART III), 4 appendices.
> - **Want the method and the evidence?** → open 📓 [`Zazie_Research_Annex_COLOUR_CODED.pdf`](Zazie_Research_Annex_COLOUR_CODED.pdf) — 13 colour-coded research sections + appendix.
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
| 🧩 Read one project end-to-end | 📕 Master Directory PDF → **PART I** → the project index | `data/master/project_clusters.json`, register: `registry/project_sections/projects.csv` |
| 🔗 Read every catalogued link | 📕 Master Directory PDF → PART III (media-type sections) | [The colour code](#reading-the-colour-code) |
| 🔬 See how each link was found & judged | 📓 Research Annex PDF | §1 — Census rules, colour code & method |
| 🧮 Crunch the data (spreadsheet / code) | `data/master/` — `master_index.csv`, `consolidated_directory.json` | [Repository map](#repository-map) |
| 🕵️ Trace one link back to the pass that found it | `registry/<pass>/` ledgers + `source_access_log.csv` | Annex §2–8, §12–13 |
| 🛡️ Avoid the quarantined, low-trust links | ⛔ Tier D rows — printed last, in the quarantine section | Annex §8 — Low-Trust Quarantine Register |
| 🏗️ Rebuild the PDFs from the data | [Regenerate](#regenerate) | `scripts/` |

## 📦 The two deliverables

| | Volume | What it is |
|---|---|---|
| <span style="background-color:#37424e; color:#ffffff;"> MASTER </span> | 📕 [`Zazie_Master_Directory_COLOUR_CODED.pdf`](Zazie_Master_Directory_COLOUR_CODED.pdf) | **The directory itself** — 727 catalogued links, organised three ways: **PART I project sections** (102 projects: every link about the same commission, compilation, anthology, film, exhibition or press wave in one place), **PART II five thematic reading paths**, **PART III the 14 colour-coded media-type sections**. Tier-ranked A–D, every URL clickable, role bands inside every project, per-category stats, 4 appendices. |
| <span style="background-color:#0b5d8f; color:#ffffff;"> ANNEX </span> | 📓 [`Zazie_Research_Annex_COLOUR_CODED.pdf`](Zazie_Research_Annex_COLOUR_CODED.pdf) | **The research record behind it** — 13 colour-coded sections + endpoint appendix: census rules, 12 engine/discovery passes (audits, evidence ledgers, query inventories, access logs), the quarantine register with its safety charter, the 2026 Accomplishment Register → public-link map, listen-link appearance table, seed-index coverage, and every tool/query template used. |

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
| <span style="background-color:#0b6e4f; color:#ffffff;"> 14 </span> | 🧩 Project-Section Pass — Grouping the Census by Project | `#0b6e4f` |
| <span style="background-color:#0b5d8f; color:#ffffff;"> A </span> | 🧰 Appendix — Tools, Endpoints & Query Templates | `#0b5d8f` |

## 🔢 At a glance

| | Figure | What it counts |
|---|---|---|
| <span style="background-color:#0b6e4f; color:#ffffff;"> 727 </span> | catalogued links | every public exact-name appearance (all records, all tiers) |
| <span style="background-color:#1a73e8; color:#ffffff;"> 73 </span> | engine endpoints | discovery/search endpoints, printed in Annex appendix A |
| <span style="background-color:#7b1fa2; color:#ffffff;"> 14 </span> | media types | the colour-coded sections of the Master Directory |
| <span style="background-color:#0b6e4f; color:#ffffff;"> 102 </span> | project sections | PART I — projects carrying more than one catalogued link (398 links) |
| <span style="background-color:#0b6e4f; color:#ffffff;"> 21 </span> | single-link projects | named in the register, one verified public page each |
| <span style="background-color:#8a6d3b; color:#ffffff;"> 325 </span> | links with no project | artist-level profiles, catalogues, community pages and scrapers — deliberately left out of PART I |
| <span style="background-color:#37424e; color:#ffffff;"> 13 + 1 </span> | Annex sections | research sections 1–13 plus the tools/endpoint appendix |
| <span style="background-color:#1a73e8; color:#ffffff;"> 12 </span> | engine passes | engine/discovery passes documented in the Annex |
| <span style="background-color:#039be5; color:#ffffff;"> 60 </span> | listen links | compilation appearances — 31 confirmed · 28 label pages · 1 unresolved |
| <span style="background-color:#e8710a; color:#ffffff;"> 54 </span> | register links | 2026 Accomplishment Register entries mapped to public links (of 203 register records) |
| <span style="background-color:#7b1fa2; color:#ffffff;"> 8 </span> | pass registries | machine passes under `registry/` |
| <span style="background-color:#b06000; color:#ffffff;"> 3 </span> | source files | original inputs under `sources/` |

## 🎨 Reading the colour code

> [!NOTE]
> The hex values below are the **exact palette** of both PDFs — a single colour system defined once in `scripts/build_master_directory_pdf.py` and `scripts/build_research_annex_pdf.py`.
> **Same colour = same meaning** in the PDFs, in the data, and in this README.

### 1 · 🏷️ Media types — the 14 sections of the Master Directory

In PDF order. The bar shows each section's share of the 727 records.

| # | Swatch | Section (PDF order) | Hex | Count | Share of 727 |
|---|---|---|---|---|---|
| 1 | <span style="background-color:#d93025;">&nbsp;&nbsp;&nbsp;</span> | 📰 Press & Editorial | `#d93025` | 95 | ██████ |
| 2 | <span style="background-color:#7b1fa2;">&nbsp;&nbsp;&nbsp;</span> | 🏆 Publications & Recognition | `#7b1fa2` | 24 | ██ |
| 3 | <span style="background-color:#d81b60;">&nbsp;&nbsp;&nbsp;</span> | 🎬 Film, Festivals & Exhibitions | `#d81b60` | 52 | ███ |
| 4 | <span style="background-color:#3949ab;">&nbsp;&nbsp;&nbsp;</span> | 🎙️ Podcasts & Broadcasts | `#3949ab` | 7 | █ |
| 5 | <span style="background-color:#1a73e8;">&nbsp;&nbsp;&nbsp;</span> | 📇 Profiles & Catalogs | `#1a73e8` | 105 | ███████ |
| 6 | <span style="background-color:#c2185b;">&nbsp;&nbsp;&nbsp;</span> | 💿 Music Discography | `#c2185b` | 1 | █ |
| 7 | <span style="background-color:#039be5;">&nbsp;&nbsp;&nbsp;</span> | 🎧 Streaming & Music Platforms | `#039be5` | 55 | ███ |
| 8 | <span style="background-color:#00897b;">&nbsp;&nbsp;&nbsp;</span> | 📖 Lyrics & Music Databases | `#00897b` | 1 | █ |
| 9 | <span style="background-color:#e8710a;">&nbsp;&nbsp;&nbsp;</span> | 📦 Music Compilations | `#e8710a` | 159 | ██████████ |
| 10 | <span style="background-color:#2e7d32;">&nbsp;&nbsp;&nbsp;</span> | 🏛️ Official Properties & Channels | `#2e7d32` | 50 | ███ |
| 11 | <span style="background-color:#188038;">&nbsp;&nbsp;&nbsp;</span> | 👥 Community, Wiki & Fan Indexes | `#188038` | 54 | ███ |
| 12 | <span style="background-color:#0f9d8f;">&nbsp;&nbsp;&nbsp;</span> | 🔍 Search-Engine Index | `#0f9d8f` | 3 | █ |
| 13 | <span style="background-color:#607d8b;">&nbsp;&nbsp;&nbsp;</span> | 🪞 Video Mirror / Backlink Sites | `#607d8b` | 5 | █ |
| 14 | <span style="background-color:#616161;">&nbsp;&nbsp;&nbsp;</span> | ⛔ Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust | `#616161` | 116 | ███████ |

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

### 5 · 🧩 PART I role bands — what a link *is* inside its project

Inside every project section of the Master Directory the rows are grouped by role, printed in this order
(the project's own page first, the scraped copies of it last). Same colours as the PDF and `data/master/project_clusters.json`.

| # | Role group | Swatch | Hex | Links | What it means |
|---|---|---|---|---|---|
| 1 | 🏠 Project page | <span style="background-color:#0b6e4f;">&nbsp;&nbsp;&nbsp;</span> | `#0b6e4f` | 121 | the project's own home: label page, publisher page, broadcaster page, festival page, register entry |
| 2 | ✍️ Artist credit | <span style="background-color:#2e7d32;">&nbsp;&nbsp;&nbsp;</span> | `#2e7d32` | 8 | the artist's own page for the work — a release, track, book, score or tool carrying the credit |
| 3 | 🗃️ Catalogue record | <span style="background-color:#1a73e8;">&nbsp;&nbsp;&nbsp;</span> | `#1a73e8` | 60 | database records of the same project: Discogs, IMDb, RateYourMusic, Beatport, lyrics and metadata DBs |
| 4 | ▶️ Distribution / listen | <span style="background-color:#039be5;">&nbsp;&nbsp;&nbsp;</span> | `#039be5` | 19 | platform mirrors carrying the same project: streaming services, podcast directories, retail listings |
| 5 | 🎬 Media / embed | <span style="background-color:#7b1fa2;">&nbsp;&nbsp;&nbsp;</span> | `#7b1fa2` | 4 | the project itself as audio/video: official uploads, trailers, screeners, embeds |
| 6 | 📰 Press & reviews | <span style="background-color:#d93025;">&nbsp;&nbsp;&nbsp;</span> | `#d93025` | 33 | independent coverage OF this project: features, reviews, interviews, news items |
| 7 | 🎟️ Event / screening | <span style="background-color:#e8710a;">&nbsp;&nbsp;&nbsp;</span> | `#e8710a` | 9 | listings, tickets, screening and performance pages for the project |
| 8 | 📚 Reference / directory | <span style="background-color:#188038;">&nbsp;&nbsp;&nbsp;</span> | `#188038` | 42 | wikis, community pages, profiles and directories that describe the project |
| 9 | 🪞 Mirror / syndication | <span style="background-color:#607d8b;">&nbsp;&nbsp;&nbsp;</span> | `#607d8b` | 19 | legitimate-but-derived copies: netlabel news reposts, archive.org copies, aggregator mirrors |
| 10 | 🗄️ Archive snapshot | <span style="background-color:#8a6d3b;">&nbsp;&nbsp;&nbsp;</span> | `#8a6d3b` | 7 | Wayback / archive captures of a page that also exists live |
| 11 | ⛔ Quarantine — do not cite | <span style="background-color:#616161;">&nbsp;&nbsp;&nbsp;</span> | `#616161` | 71 | scraped clones, SEO doorways and syndication spam carrying the project — evidence of contamination only |

## 🗂️ Repository map

**One-line data flow** — every file sits somewhere on this pipeline:

```
📥 raw inputs ──▶ 📚 per-pass evidence ──▶ ⚙️ build scripts ──▶ 📊 canonical data ──▶ 📕📓 colour-coded PDFs
 (sources/)        (registry/)             (scripts/)           (data/master/)        (repo root — reading editions)
```

```
📦 Comprehensive Backlink Tracker
├── 📕 Zazie_Master_Directory_COLOUR_CODED.pdf      ← READ: the directory (727 links, 14 sections)
├── 📓 Zazie_Research_Annex_COLOUR_CODED.pdf        ← READ: the method (13 sections + appendix)
├── 📥 sources/                                     ← raw original inputs (3 files)
│   ├── Random_Zazie_Productions_links.pdf          raw link dump
│   ├── Zazie_Media_Master.pdf                      133 verified URL-level records (+leads)
│   └── Zazie_2026_Accomplishment_Register_Maximal_Edition.docx
├── 📊 data/master/                                 ← CANONICAL (source of truth)
│   ├── consolidated_directory.json                 727 records + 73 engine endpoints
│   ├── master_index.csv                            canonical index, one row per URL
│   ├── listen_links.csv                            60 compilation appearances
│   ├── register_link_map.csv                       Accomplishment Register → public links
│   ├── project_clusters.json                       🧩 projects + their links, roles and page-ready sections
│   └── project_clusters.csv                        the same, flattened: one row per link with its project + role
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
│   └── project_sections/
│       ├── projects.csv                            🧩 THE PROJECT REGISTER — one row per project + its match rules
│       └── README.md                               how to add a project, an alias or an exclusion
└── ⚙️ scripts/                                     ← rebuild everything
    ├── ingest_all_links.py                         registries → data/master/*
    ├── build_project_sections.py                   clusters → data/master/project_clusters.*  (run by the master build)
    ├── build_master_directory_pdf.py               → Master Directory PDF (PART I uses the clusters)
    └── build_research_annex_pdf.py                 → Research Annex PDF (§14 = the project pass)
```

| Path | Colour | Role in the pipeline |
|---|---|---|
| `sources/` | <span style="background-color:#b06000; color:#ffffff;"> raw </span> | original inputs — never edited downstream |
| `registry/` | <span style="background-color:#7b1fa2; color:#ffffff;"> evidence </span> | per-pass machine registers — the proof trail |
| `scripts/` | <span style="background-color:#e8710a; color:#ffffff;"> build </span> | rebuilds the canonical data and both PDFs |
| `data/master/` | <span style="background-color:#0b6e4f; color:#ffffff;"> canonical </span> | **source of truth** — 727 records + 73 endpoints |
| `data/research/` | <span style="background-color:#0f9d8f; color:#ffffff;"> audit </span> | engine access results for passes 1–8 |
| root PDFs | <span style="background-color:#37424e; color:#ffffff;"> reading </span> | the organised, permanent reading editions |

## ♻️ Regenerate

Requirements: Python 3 + `reportlab` (and `pymupdf`) — a local `.venv/` is git-ignored.

| Step | Run | Result |
|---|---|---|
| <span style="background-color:#e8710a; color:#ffffff;"> 1 </span> | `python scripts/ingest_all_links.py` | rebuilds `data/master/*` from all the registries |
| <span style="background-color:#0b6e4f; color:#ffffff;"> 2 </span> | `python scripts/build_project_sections.py --report` | rebuilds the 🧩 project clusters and prints the curation report (what matched, what is still loose) |
| <span style="background-color:#37424e; color:#ffffff;"> 3 </span> | `python scripts/build_master_directory_pdf.py` | rebuilds the 📕 Master Directory PDF (it runs step 2 itself, so the PDF can never drift from the register) |
| <span style="background-color:#0b5d8f; color:#ffffff;"> 4 </span> | `python scripts/build_research_annex_pdf.py` | rebuilds the 📓 Research Annex PDF (§14 documents the project pass) |

> [!TIP]
> Run steps 1 → 2 → 3 → 4 in order. Page-number caches (`data/master/.pdf_pagemap.json`, `.annex_pagemap.json`) are regenerated on every build and are git-ignored.

## ✅ Ground rules

> [!IMPORTANT]
> **Source of truth:** the CSV/JSON files in `data/` and `registry/` are the source of truth. The two PDFs are their organised, **permanent reading edition** — never edit the PDFs by hand; regenerate them.

> [!NOTE]
> **No narrative Markdown reports are kept** — everything readable lives in the two PDFs. If it isn't in `data/`, `registry/`, `sources/` or `scripts/`, it belongs in one of the PDFs.

> [!IMPORTANT]
> **Projects are curated, never guessed.** A link joins a project only because a rule in `registry/project_sections/projects.csv` says so — an alias found in its URL/title, a documented URL pin, or (for a few hosts whose titles never name the project) a phrase in its evidence note. No fuzzy similarity: every membership is traceable to one register line. Adding a project = one CSV row + a rebuild.

> [!TIP]
> **One palette, everywhere.** Every colour in the PDFs is defined once in `scripts/build_master_directory_pdf.py` / `scripts/build_research_annex_pdf.py`. The legend in this README is that same palette — so if the PDFs change colour, this page changes with them.
