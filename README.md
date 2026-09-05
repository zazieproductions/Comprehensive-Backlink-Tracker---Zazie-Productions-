<div align="center">

# 🔍 ZAZIE PRESENCE CENSUS — Backlink & Mention Tracker

### A week-long, agent-driven sweep to find **every** place **`Zazie Kanwar-Torge`** and **`Zazie Productions`** are indexed, named, credited, embedded, or linked — across mainstream **and** obscure search engines.

</div>

---

## 🎯 What this project is

This is the **mission homepage** for a *comprehensive, reproducible, week-long directory* of every public-web location where the artist and producer **`Zazie Kanwar-Torge`** / **`Zazie Productions`** appears — including places that only surface on **obscure engines** (SearXNG, Yandex, Bing, Brave, Mojeek, Marginalia, SearX, meta-search layers, regional engines, niche music/film databases, wiki mirrors, YouTube aggregators, archive caches, and so on).

The repo already contains a **dump of earlier research**. This directory turns that dump into an **organized, color-coded operating system** for a repeatable census:

- 📖 **Explains the task** to any future agent (scope, inclusion rules, evidence standard).
- 🗺️ **A color-coded document map** so agents know exactly where to look and what to produce.
- 🧠 **Deep-searching methods & copy-paste queries** ready to prompt agents engine-by-engine.
- 🗂️ **A seed registry** auto-extracted from the existing dump (the places found so far).
- ✅ **A verification runbook** for the “double-check that they work later” pass.

> 🚩 **Important framing:** `Zazie Kanwar-Torge` and `Zazie Productions` refer to **one person / one artist project** (composer, film-scorer, experimental/noise musician, filmmaker, writer, and multimedia artist). The census deliberately tracks the *name-as-person/company*, not the unrelated French singer **“Zazie”**, the company **“Zazie Films”**, or other similarly-named entities.

---

## 🎨 COLOR-CODING SYSTEM (use this everywhere)

Colors carry **meaning** in every table below. If a viewer does not render colors, the matching **emoji + bold label** still carries the same meaning, so the files never break.

### Media-type (what kind of place it is)

| Emoji | Label | Color | Meaning |
|---|---|---|---|
| 🔴 | **Press / Editorial** | `#d93025` | Reviews, features, interviews, articles, press releases |
| 🌸 | **Film / Festivals / Exhibitions** | `#d81b60` | Film credits, screenings, festival pages, gallery shows |
| 🟣 | **Publications / Recognition / Academic** | `#7b1fa2` | Awards, anthologies, papers, honor rolls, security/credits pages |
| 🔵 | **Profiles & Catalogs** | `#1a73e8` | Streaming/artist/directory profile pages, platform catalogs |
| 🟠 | **Music & Discography** | `#e8710a` | Releases, compilations, net-labels, track credits |
| 🩵 | **Data-studies / Analytics / Tooling** | `#0f9d8f` | Stats sites, analytics dashboards, AI/research pages about the work |
| 🟢 | **Social & Community** | `#188038` | Native social posts, community pages, UGC, fan-made content |
| 📼 | **Mirrors / Aggregators** | `#607d8b` | YouTube mirrors, video aggr., RSS scrape/index mirrors (secondary) |
| 🖤 | **Spam / SEO parasite** | `#616161` | Auto-scraped/spun pages — *cross-check before counting* |

### Status (used during the verification pass)

| Status | Color | Meaning |
|---|---|---|
| ✅ **LIVE / VERIFIED** | `#188038` | Link works **and** the exact name is visible on the page |
| 🟡 **PARTIAL / RE-CHECK** | `#b06000` | Page loads but evidence is weak, region-gated, or JS-hidden |
| ❌ **BROKEN / NO EVIDENCE** | `#c5221f` | Dead link, 404/403, or no exact-name evidence found |
| ⬜ **UNCHECKED** | `#80868b` | Recorded but not yet double-checked (this is every seed row today) |

### Priority (used when ranking evidence strength)

- 🥇 **Priority A** — independent editorial, institutional, or database-of-record (press-kit lead)
- 🥈 **Priority B** — supporting coverage / secondary context
- 🥉 **Priority C** — self-issued profiles, own storefronts, catalog/discography rows
- 🔎 **Lead** — unverified or unresolved (do **not** count in totals)

> **Two-name rule (from the existing “Strict Exact-Name” master):** only the exact strings **`Zazie Productions`** and **`Zazie Kanwar-Torge`** qualify as *countable* evidence. Handles/URL-slugs without the space (e.g. `zazieproductions`, `zazie-kanwar-torge`) are useful **leads** but not counted by themselves.

---

## 📚 DOCUMENT MAP

### Mission & method (the “why” and the “how-to-think”)

| File | What it is |
|---|---|
| [`docs/01_MISSION_SCOPE_AND_RULES.md`](docs/01_MISSION_SCOPE_AND_RULES.md) | **The master brief.** Full explanation of the task, targets, eligibility & exclusion rules, evidence standard, and output conventions. Hand this to any agent that asks “what am I doing?” |
| [`docs/02_DEEP_SEARCH_PLAYBOOK.md`](docs/02_DEEP_SEARCH_PLAYBOOK.md) | **Deep-searching methods.** Boolean/operator syntax per engine, meta-search strategy, obscure-engine technique, freshness & backlink-chasing, evidence capture. |

### Look-up references (search-time tools)

| File | What it is |
|---|---|
| [`docs/03_ENGINE_DIRECTORY.md`](docs/03_ENGINE_DIRECTORY.md) | **Color-coded engine directory.** Every engine class to run each name against (major, meta, independent, obscure/alt, regional, music, film, academic, social-native, archive) with the exact URL pattern to use. |
| [`docs/04_QUERY_LIBRARY.md`](docs/04_QUERY_LIBRARY.md) | **Copy-paste query library.** Canonical exact-name queries, near-name/handle variants, platform `site:` dorks, noise-filtering exclusions, file-type sweeps — ready to paste. |

### Execution (how a week gets run)

| File | What it is |
|---|---|
| [`docs/05_WEEK_PLAN_AND_CADENCE.md`](docs/05_WEEK_PLAN_AND_CADENCE.md) | **The 7-day plan.** Day-by-day batching, session cadence, dedupe & logging rhythm, day-7 consolidation. |
| [`docs/06_AGENT_PROMPT_TEMPLATES.md`](docs/06_AGENT_PROMPT_TEMPLATES.md) | **Prompt templates.** Ready-to-send agent briefs per phase with required output format & evidence rules. |
| [`docs/07_LINK_CHECK_AND_VERIFICATION.md`](docs/07_LINK_CHECK_AND_VERIFICATION.md) | **The “double-check they work later” runbook.** HTTP-status probing, redirect handling, exact-name grep, LIVE/PARTIAL/BROKEN tagging, rate-limit etiquette, tooling. |

### Data & registry

| Path | What it is |
|---|---|
| [`registry/README.md`](registry/README.md) | How the live registry is structured and how to add rows. |
| [`registry/seed/SEED_INDEX_FROM_DUMP.md`](registry/seed/SEED_INDEX_FROM_DUMP.md) | **260 unique URLs** auto-extracted from the dump, clustered by media type. *(Source for the “found so far” starting set.)* |
| [`registry/seed/seed_unique_urls.csv`](registry/seed/seed_unique_urls.csv) | Machine-readable full list (domain, url, first-seen source file). |
| [`registry/seed/seed_domain_summary.csv`](registry/seed/seed_domain_summary.csv) | Domain → URL-count summary for eyeballing coverage. |
| [`registry/2026-09-05_maxdepth_research/`](registry/2026-09-05_maxdepth_research/REPORT.md) | **2026-09-05 max-depth research pass.** 54 new verified locations (excl. everything already in the repo), full discovery ledger, 40-query inventory, 57-entry source-access log, engine visibility matrix, relationship graph, appendices. Start at its `REPORT.md`. |

### Original source dump (untouched originals at repo root)

| File | Notes |
|---|---|
| `Random Zazie Productions links .pdf` | Raw link dump (the URL-rich source the seed registry was built from). |
| `Zazie_Media_Master (1).pdf` | Reading edition of the **133-record exact-name master** (Press 25 · Film 11 · Publications 6 · Profiles 31 · Compilations 60), researched through **Aug 9, 2026**. Body text stores URLs as `OPEN` tokens, but the PDF's own `/URI` link annotations carry the **133 real URLs** — extracted during the 2026-09-05 pass and used as part of the 437-URL "already in repo" baseline (see `registry/2026-09-05_maxdepth_research/REPORT.md` §2). |
| `Zazie_2026_Accomplishment_Register_Maximal_Edition.docx` | 2026 external-memory register of releases, press, selections, and professional reach (useful as a **known-ground-truth list** to cross-check the census against). |
| `resource1` | Note file (`maxintel.org` — an OSINT tool referenced as useful). |

---

## 📌 Current status & next actions

- [x] **Dump cataloged** — media master read; 260 real URLs extracted into `registry/seed/`.
- [x] **Operating docs written** — mission, playbook, engine dir, query library, week plan, prompts, verification runbook.
- [x] **Pass 1 — CENSUS (deep-research pass, 2026-09-05)** — both names swept through the general-search API, Bandcamp/Discogs/MusicBrainz/iTunes/archive.org/Wikidata/Wikipedia/GitHub/npm/PyPI/HF/OpenLibrary direct indexes, Wayback CDX, and CAPTCHA-gated engines (documented as blocked). **54 new verified locations** (everything already in the repo excluded per instruction; 11 repo URLs re-verified live in the same pass). Results: [`registry/2026-09-05_maxdepth_research/`](registry/2026-09-05_maxdepth_research/REPORT.md).
- [ ] **Pass 2 — VERIFY** (run per `docs/07`): double-check every found link (HTTP status + exact-name evidence) and tag ✅ / 🟡 / ❌. *(Note: the 2026-09-05 pass already re-verified 11 repo URLs live; full-pass tagging of all 260 seed rows remains.)*
- [ ] **Pass 3 — CONSOLIDATE**: fold verified rows into a single registry and reconcile against the known-ground-truth register (accomplishment DOCX) and the 133-record media master.

> **Easy first step for any agent:** open [`docs/01_MISSION_SCOPE_AND_RULES.md`](docs/01_MISSION_SCOPE_AND_RULES.md), then [`docs/05_WEEK_PLAN_AND_CADENCE.md`](docs/05_WEEK_PLAN_AND_CADENCE.md) for Day 1.

---

*Built for Zazie Productions · Last updated 2026-09-05 (max-depth research pass) · Research baseline in dumps dated through 2026-08-09.*
